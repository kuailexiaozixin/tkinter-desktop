# 官方示例源码 · com/win32comext

> 来源 https://github.com/mhammond/pywin32/tree/main/com/win32comext （共 28 个 .py，全文内联）


---

## com/win32comext/adsi/demos/objectPicker.py

```python
# A demo for the IDsObjectPicker interface.
import pythoncom
import win32clipboard
from win32com.adsi import adsi
from win32com.adsi.adsicon import *

cf_objectpicker = win32clipboard.RegisterClipboardFormat(CFSTR_DSOP_DS_SELECTION_LIST)


def main():
    hwnd = 0

    # Create an instance of the object picker.
    picker = pythoncom.CoCreateInstance(
        adsi.CLSID_DsObjectPicker,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        adsi.IID_IDsObjectPicker,
    )

    # Create our scope init info.
    siis = adsi.DSOP_SCOPE_INIT_INFOs(1)
    sii = siis[0]

    # Combine multiple scope types in a single array entry.

    sii.type = (
        DSOP_SCOPE_TYPE_UPLEVEL_JOINED_DOMAIN | DSOP_SCOPE_TYPE_DOWNLEVEL_JOINED_DOMAIN
    )

    # Set uplevel and downlevel filters to include only computer objects.
    # Uplevel filters apply to both mixed and native modes.
    # Notice that the uplevel and downlevel flags are different.

    sii.filterFlags.uplevel.bothModes = DSOP_FILTER_COMPUTERS
    sii.filterFlags.downlevel = DSOP_DOWNLEVEL_FILTER_COMPUTERS

    # Initialize the interface.
    picker.Initialize(
        None,  # Target is the local computer.
        siis,  # scope infos
        DSOP_FLAG_MULTISELECT,  # options
        ("objectGUID", "displayName"),
    )  # attributes to fetch

    do = picker.InvokeDialog(hwnd)
    # Extract the data from the IDataObject.
    format_etc = (
        cf_objectpicker,
        None,
        pythoncom.DVASPECT_CONTENT,
        -1,
        pythoncom.TYMED_HGLOBAL,
    )
    medium = do.GetData(format_etc)
    data = adsi.StringAsDS_SELECTION_LIST(medium.data)
    for item in data:
        name, klass, adspath, upn, attrs, flags = item
        print("Item", name)
        print(" Class:", klass)
        print(" AdsPath:", adspath)
        print(" UPN:", upn)
        print(" Attrs:", attrs)
        print(" Flags:", flags)


if __name__ == "__main__":
    main()

```


---

## com/win32comext/adsi/demos/scp.py

```python
"""A re-implementation of the MS DirectoryService samples related to services.

* Adds and removes an ActiveDirectory "Service Connection Point",
  including managing the security on the object.
* Creates and registers Service Principal Names.
* Changes the username for a domain user.

Some of these functions are likely to become move to a module - but there
is also a little command-line-interface to try these functions out.

For example:

scp.py --account-name=domain\\user --service-class=PythonScpTest \\
       --keyword=foo --keyword=bar --binding-string=bind_info \\
       ScpCreate SpnCreate SpnRegister

would:
* Attempt to delete a Service Connection Point for the service class
  'PythonScpTest'
* Attempt to create a Service Connection Point for that class, with 2
  keywords and a binding string of 'bind_info'
* Create a Service Principal Name for the service and register it

to undo those changes, you could execute:

scp.py --account-name=domain\\user --service-class=PythonScpTest \\
       SpnCreate SpnUnregister ScpDelete

which will:
* Create a SPN
* Unregister that SPN from the Active Directory.
* Delete the Service Connection Point

Executing with --test will create and remove one of everything.
"""

import optparse
import textwrap
import traceback

import ntsecuritycon as dscon
import win32api
import win32con
import win32security
import winerror
from win32com.adsi import adsi
from win32com.adsi.adsicon import *
from win32com.client import Dispatch

verbose = 1
g_createdSCP = None
g_createdSPNs = []
g_createdSPNLast = None

import logging

logger = logging  # use logging module global methods for now.

# still a bit confused about log(n, ...) vs logger.info/debug()


# Returns distinguished name of SCP.
def ScpCreate(
    service_binding_info,
    service_class_name,  # Service class string to store in SCP.
    account_name=None,  # Logon account that needs access to SCP.
    container_name=None,
    keywords=None,
    object_class="serviceConnectionPoint",
    dns_name_type="A",
    dn=None,
    dns_name=None,
):
    container_name = container_name or service_class_name
    if not dns_name:
        # Get the DNS name of the local computer
        dns_name = win32api.GetComputerNameEx(win32con.ComputerNameDnsFullyQualified)
    # Get the distinguished name of the computer object for the local computer
    if dn is None:
        dn = win32api.GetComputerObjectName(win32con.NameFullyQualifiedDN)

    # Compose the ADSpath and bind to the computer object for the local computer
    comp = adsi.ADsGetObject("LDAP://" + dn, adsi.IID_IDirectoryObject)

    # Publish the SCP as a child of the computer object
    keywords = keywords or []
    # Fill in the attribute values to be stored in the SCP.
    attrs = [
        ("cn", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (container_name,)),
        ("objectClass", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (object_class,)),
        ("keywords", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, keywords),
        ("serviceDnsName", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, (dns_name,)),
        (
            "serviceDnsNameType",
            ADS_ATTR_UPDATE,
            ADSTYPE_CASE_IGNORE_STRING,
            (dns_name_type,),
        ),
        (
            "serviceClassName",
            ADS_ATTR_UPDATE,
            ADSTYPE_CASE_IGNORE_STRING,
            (service_class_name,),
        ),
        (
            "serviceBindingInformation",
            ADS_ATTR_UPDATE,
            ADSTYPE_CASE_IGNORE_STRING,
            (service_binding_info,),
        ),
    ]
    new = comp.CreateDSObject("cn=" + container_name, attrs)
    logger.info("New connection point is at %s", container_name)
    # Wrap in a usable IDispatch object.
    new = Dispatch(new)
    # And allow access to the SCP for the specified account name
    AllowAccessToScpProperties(account_name, new)
    return new


def ScpDelete(container_name, dn=None):
    if dn is None:
        dn = win32api.GetComputerObjectName(win32con.NameFullyQualifiedDN)
    logger.debug("Removing connection point '%s' from %s", container_name, dn)

    # Compose the ADSpath and bind to the computer object for the local computer
    comp = adsi.ADsGetObject("LDAP://" + dn, adsi.IID_IDirectoryObject)
    comp.DeleteDSObject("cn=" + container_name)
    logger.info("Deleted service connection point '%s'", container_name)


# This function is described in detail in the MSDN article titled
# "Enabling Service Account to Access SCP Properties"
# From that article:
# The following sample code sets a pair of ACEs on a service connection point
# (SCP) object. The ACEs grant read/write access to the user or computer account
# under which the service instance will be running. Your service installation
# program calls this code to ensure that the service will be allowed to update
# its properties at run time. If you don't set ACEs like these, your service
# will get access-denied errors if it tries to modify the SCP's properties.
#
# The code uses the IADsSecurityDescriptor, IADsAccessControlList, and
# IADsAccessControlEntry interfaces to do the following:
# * Get the SCP object's security descriptor.
# * Set ACEs in the DACL of the security descriptor.
# * Set the security descriptor back on the SCP object.


def AllowAccessToScpProperties(
    accountSAM,  # Service account to allow access.
    scpObject,  # The IADs SCP object.
    schemaIDGUIDs=(  # Attributes to allow write-access to.
        "{28630eb8-41d5-11d1-a9c1-0000f80367c1}",  # serviceDNSName
        "{b7b1311c-b82e-11d0-afee-0000f80367c1}",  # serviceBindingInformation
    ),
):
    # If no service account is specified, service runs under LocalSystem.
    # So allow access to the computer account of the service's host.
    if accountSAM:
        trustee = accountSAM
    else:
        # Get the SAM account name of the computer object for the server.
        trustee = win32api.GetComputerObjectName(win32con.NameSamCompatible)

    # Get the nTSecurityDescriptor attribute
    attribute = "nTSecurityDescriptor"
    sd = getattr(scpObject, attribute)
    acl = sd.DiscretionaryAcl

    for sguid in schemaIDGUIDs:
        ace = Dispatch(adsi.CLSID_AccessControlEntry)

        # Set the properties of the ACE.
        # Allow read and write access to the property.
        ace.AccessMask = ADS_RIGHT_DS_READ_PROP | ADS_RIGHT_DS_WRITE_PROP

        # Set the trustee, which is either the service account or the
        # host computer account.
        ace.Trustee = trustee

        # Set the ACE type.
        ace.AceType = ADS_ACETYPE_ACCESS_ALLOWED_OBJECT

        # Set AceFlags to zero because ACE is not inheritable.
        ace.AceFlags = 0

        # Set Flags to indicate an ACE that protects a specified object.
        ace.Flags = ADS_FLAG_OBJECT_TYPE_PRESENT

        # Set ObjectType to the schemaIDGUID of the attribute.
        ace.ObjectType = sguid

        # Add the ACEs to the DACL.
        acl.AddAce(ace)

    # Write the modified DACL back to the security descriptor.
    sd.DiscretionaryAcl = acl
    # Write the ntSecurityDescriptor property to the property cache.
    setattr(scpObject, attribute, sd)
    # SetInfo updates the SCP object in the directory.
    scpObject.SetInfo()
    logger.info("Set security on object for account %r", trustee)


# Service Principal Names functions from the same sample.
# The example calls the DsWriteAccountSpn function, which stores the SPNs in
# Microsoft Active Directory under the servicePrincipalName attribute of the
# account object specified by the serviceAcctDN parameter. The account object
# corresponds to the logon account specified in the CreateService call for this
# service instance. If the logon account is a domain user account,
# serviceAcctDN must be the distinguished name of the account object in
# Active Directory for that user account. If the service's logon account is the
# LocalSystem account, serviceAcctDN must be the distinguished name of the
# computer account object for the host computer on which the service is
# installed. win32api.TranslateNames and win32security.DsCrackNames can
# be used to convert a domain\account format name to a distinguished name.
def SpnRegister(
    serviceAcctDN,  # DN of the service's logon account
    spns,  # List of SPNs to register
    operation,  # Add, replace, or delete SPNs
):
    assert not isinstance(spns, str) and hasattr(spns, "__iter__"), (
        "spns must be a sequence of strings (got %r)" % spns
    )
    # Bind to a domain controller.
    # Get the domain for the current user.
    samName = win32api.GetUserNameEx(win32api.NameSamCompatible)
    samName = samName.split("\\", 1)[0]

    if not serviceAcctDN:
        # Get the SAM account name of the computer object for the server.
        serviceAcctDN = win32api.GetComputerObjectName(win32con.NameFullyQualifiedDN)
    logger.debug("SpnRegister using DN '%s'", serviceAcctDN)

    # Get the name of a domain controller in that domain.
    info = win32security.DsGetDcName(
        domainName=samName,
        flags=dscon.DS_IS_FLAT_NAME
        | dscon.DS_RETURN_DNS_NAME
        | dscon.DS_DIRECTORY_SERVICE_REQUIRED,
    )
    # Bind to the domain controller.
    handle = win32security.DsBind(info["DomainControllerName"])

    # Write the SPNs to the service account or computer account.
    logger.debug("DsWriteAccountSpn with spns %s")
    win32security.DsWriteAccountSpn(
        handle,  # handle to the directory
        operation,  # Add or remove SPN from account's existing SPNs
        serviceAcctDN,  # DN of service account or computer account
        spns,
    )  # names

    # Unbind the DS in any case (but Python would do it anyway)
    handle.Close()


def UserChangePassword(username_dn, new_password):
    # set the password on the account.
    # Use the distinguished name to bind to the account object.
    accountPath = "LDAP://" + username_dn
    user = adsi.ADsGetObject(accountPath, adsi.IID_IADsUser)

    # Set the password on the account.
    user.SetPassword(new_password)


# functions related to the command-line interface
def log(level, msg, *args):
    if verbose >= level:
        print(msg % args)


class _NoDefault:
    pass


def _get_option(po, opt_name, default=_NoDefault):
    parser, options = po
    ret = getattr(options, opt_name, default)
    if not ret and default is _NoDefault:
        parser.error("The '%s' option must be specified for this operation" % opt_name)
    if not ret:
        ret = default
    return ret


def _option_error(po, why):
    parser = po[0]
    parser.error(why)


def do_ScpCreate(po):
    """Create a Service Connection Point"""
    global g_createdSCP
    scp = ScpCreate(
        _get_option(po, "binding_string"),
        _get_option(po, "service_class"),
        _get_option(po, "account_name_sam", None),
        keywords=_get_option(po, "keywords", None),
    )
    g_createdSCP = scp
    return scp.distinguishedName


def do_ScpDelete(po):
    """Delete a Service Connection Point"""
    sc = _get_option(po, "service_class")
    try:
        ScpDelete(sc)
    except adsi.error as details:
        if details[0] != winerror.ERROR_DS_OBJ_NOT_FOUND:
            raise
        log(2, "ScpDelete ignoring ERROR_DS_OBJ_NOT_FOUND for service-class '%s'", sc)
    return sc


def do_SpnCreate(po):
    """Create a Service Principal Name"""
    # The 'service name' is the dn of our scp.
    if g_createdSCP is None:
        # Could accept an arg to avoid this?
        _option_error(po, "ScpCreate must have been specified before SpnCreate")
    # Create a Service Principal Name"
    spns = win32security.DsGetSpn(
        dscon.DS_SPN_SERVICE,
        _get_option(po, "service_class"),
        g_createdSCP.distinguishedName,
        _get_option(po, "port", 0),
        None,
        None,
    )
    spn = spns[0]
    log(2, "Created SPN: %s", spn)
    global g_createdSPNLast
    g_createdSPNLast = spn
    g_createdSPNs.append(spn)
    return spn


def do_SpnRegister(po):
    """Register a previously created Service Principal Name"""
    if not g_createdSPNLast:
        _option_error(po, "SpnCreate must appear before SpnRegister")

    SpnRegister(
        _get_option(po, "account_name_dn", None),
        (g_createdSPNLast,),
        dscon.DS_SPN_ADD_SPN_OP,
    )
    return g_createdSPNLast


def do_SpnUnregister(po):
    """Unregister a previously created Service Principal Name"""
    if not g_createdSPNLast:
        _option_error(po, "SpnCreate must appear before SpnUnregister")
    SpnRegister(
        _get_option(po, "account_name_dn", None),
        (g_createdSPNLast,),
        dscon.DS_SPN_DELETE_SPN_OP,
    )
    return g_createdSPNLast


def do_UserChangePassword(po):
    """Change the password for a specified user"""
    UserChangePassword(_get_option(po, "account_name_dn"), _get_option(po, "password"))
    return "Password changed OK"


handlers = (
    ("ScpCreate", do_ScpCreate),
    ("ScpDelete", do_ScpDelete),
    ("SpnCreate", do_SpnCreate),
    ("SpnRegister", do_SpnRegister),
    ("SpnUnregister", do_SpnUnregister),
    ("UserChangePassword", do_UserChangePassword),
)


class HelpFormatter(optparse.IndentedHelpFormatter):
    def format_description(self, description):
        return description


def main():
    global verbose
    _handlers_dict = {}

    arg_descs = []
    for arg, func in handlers:
        this_desc = "\n".join(textwrap.wrap(func.__doc__, subsequent_indent=" " * 8))
        arg_descs.append(f"  {arg}: {this_desc}")
        _handlers_dict[arg.lower()] = func

    description = __doc__ + "\ncommands:\n" + "\n".join(arg_descs) + "\n"

    parser = optparse.OptionParser(
        usage="%prog [options] command ...",
        description=description,
        formatter=HelpFormatter(),
    )

    parser.add_option(
        "-v",
        action="count",
        dest="verbose",
        default=1,
        help="increase the verbosity of status messages",
    )

    parser.add_option(
        "-q", "--quiet", action="store_true", help="Don't print any status messages"
    )

    parser.add_option(
        "-t",
        "--test",
        action="store_true",
        help="Execute a mini-test suite, providing defaults for most options and args",
    )

    parser.add_option(
        "",
        "--show-tracebacks",
        action="store_true",
        help="Show the tracebacks for any exceptions",
    )

    parser.add_option("", "--service-class", help="The service class name to use")

    parser.add_option(
        "", "--port", default=0, help="The port number to associate with the SPN"
    )

    parser.add_option(
        "", "--binding-string", help="The binding string to use for SCP creation"
    )

    parser.add_option(
        "", "--account-name", help="The account name to use (default is LocalSystem)"
    )

    parser.add_option("", "--password", help="The password to set.")

    parser.add_option(
        "",
        "--keyword",
        action="append",
        dest="keywords",
        help="""A keyword to add to the SCP.  May be specified
                              multiple times""",
    )

    parser.add_option(
        "",
        "--log-level",
        help="""The log-level to use - may be a number or a logging
                             module constant""",
        default=str(logging.WARNING),
    )

    options, args = parser.parse_args()
    po = (parser, options)
    # fixup misc
    try:
        options.port = int(options.port)
    except (TypeError, ValueError):
        parser.error("--port must be numeric")
    # fixup log-level
    try:
        log_level = int(options.log_level)
    except (TypeError, ValueError):
        try:
            log_level = int(getattr(logging, options.log_level.upper()))
        except (ValueError, TypeError, AttributeError):
            parser.error("Invalid --log-level value")
    try:
        sl = logger.setLevel
        # logger is a real logger
    except AttributeError:
        # logger is logging module
        sl = logging.getLogger().setLevel
    sl(log_level)
    # Check -q/-v
    if options.quiet and options.verbose:
        parser.error("Can't specify --quiet and --verbose")
    if options.quiet:
        options.verbose -= 1
    verbose = options.verbose
    # --test
    if options.test:
        if args:
            parser.error("Can't specify args with --test")

        args = "ScpDelete ScpCreate SpnCreate SpnRegister SpnUnregister ScpDelete"
        log(1, "--test - pretending args are:\n %s", args)
        args = args.split()
        if not options.service_class:
            options.service_class = "PythonScpTest"
            log(2, "--test: --service-class=%s", options.service_class)
        if not options.keywords:
            options.keywords = "Python Powered".split()
            log(2, "--test: --keyword=%s", options.keywords)
        if not options.binding_string:
            options.binding_string = "test binding string"
            log(2, "--test: --binding-string=%s", options.binding_string)

    # check args
    if not args:
        parser.error("No command specified (use --help for valid commands)")
    for arg in args:
        if arg.lower() not in _handlers_dict:
            parser.error("Invalid command '%s' (use --help for valid commands)" % arg)

    # Patch up account-name.
    if options.account_name:
        log(2, "Translating account name '%s'", options.account_name)
        options.account_name_sam = win32security.TranslateName(
            options.account_name, win32api.NameUnknown, win32api.NameSamCompatible
        )
        log(2, "NameSamCompatible is '%s'", options.account_name_sam)
        options.account_name_dn = win32security.TranslateName(
            options.account_name, win32api.NameUnknown, win32api.NameFullyQualifiedDN
        )
        log(2, "NameFullyQualifiedDNis '%s'", options.account_name_dn)

    # do it.
    for arg in args:
        handler = _handlers_dict[arg.lower()]  # already been validated
        if handler is None:
            parser.error("Invalid command '%s'" % arg)
        err_msg = None
        try:
            try:
                log(2, "Executing '%s'...", arg)
                result = handler(po)
                log(1, "%s: %s", arg, result)
            except:
                if options.show_tracebacks:
                    print("--show-tracebacks specified - dumping exception")
                    traceback.print_exc()
                raise
        except adsi.error as xxx_todo_changeme:
            (hr, desc, exc, argerr) = xxx_todo_changeme.args
            if exc:
                extra_desc = exc[2]
            else:
                extra_desc = ""
            err_msg = desc
            if extra_desc:
                err_msg += "\n\t" + extra_desc
        except win32api.error as xxx_todo_changeme1:
            (hr, func, msg) = xxx_todo_changeme1.args
            err_msg = msg
        if err_msg:
            log(1, "Command '%s' failed: %s", arg, err_msg)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("*** Interrupted")

```


---

## com/win32comext/adsi/demos/search.py

```python
import pythoncom
import pywintypes
from win32com.adsi import adsi, adsicon
from win32com.adsi.adsicon import *

options = None  # set to optparse options object

ADsTypeNameMap = {}


def getADsTypeName(type_val):
    # convert integer type to the 'typename' as known in the headerfiles.
    if not ADsTypeNameMap:
        for n, v in adsicon.__dict__.items():
            if n.startswith("ADSTYPE_"):
                ADsTypeNameMap[v] = n
    return ADsTypeNameMap.get(type_val, hex(type_val))


def _guid_from_buffer(b):
    return pywintypes.IID(b, True)


def _sid_from_buffer(b):
    return str(pywintypes.SID(b))


_null_converter = lambda x: x

converters = {
    "objectGUID": _guid_from_buffer,
    "objectSid": _sid_from_buffer,
    "instanceType": getADsTypeName,
}


def log(level, msg, *args):
    if options.verbose >= level:
        print("log:", msg % args)


def getGC():
    cont = adsi.ADsOpenObject(
        "GC:", options.user, options.password, 0, adsi.IID_IADsContainer
    )
    enum = adsi.ADsBuildEnumerator(cont)
    # Only 1 child of the global catalog.
    for e in enum:
        gc = e.QueryInterface(adsi.IID_IDirectorySearch)
        return gc
    return None


def print_attribute(col_data):
    prop_name, prop_type, values = col_data
    if values is not None:
        log(2, "property '%s' has type '%s'", prop_name, getADsTypeName(prop_type))
        value = [converters.get(prop_name, _null_converter)(v[0]) for v in values]
        if len(value) == 1:
            value = value[0]
        print(f" {prop_name}={value!r}")
    else:
        print(f" {prop_name} is None")


def search():
    gc = getGC()
    if gc is None:
        log(0, "Can't find the global catalog")
        return

    prefs = [(ADS_SEARCHPREF_SEARCH_SCOPE, (ADS_SCOPE_SUBTREE,))]
    hr, statuses = gc.SetSearchPreference(prefs)
    log(3, "SetSearchPreference returned %d/%r", hr, statuses)

    if options.attributes:
        attributes = options.attributes.split(",")
    else:
        attributes = None

    h = gc.ExecuteSearch(options.filter, attributes)
    hr = gc.GetNextRow(h)
    while hr != S_ADS_NOMORE_ROWS:
        print("-- new row --")
        if attributes is None:
            # Loop over all columns returned
            while 1:
                col_name = gc.GetNextColumnName(h)
                if col_name is None:
                    break
                data = gc.GetColumn(h, col_name)
                print_attribute(data)
        else:
            # loop over attributes specified.
            for a in attributes:
                try:
                    data = gc.GetColumn(h, a)
                    print_attribute(data)
                except adsi.error as details:
                    if details[0] != E_ADS_COLUMN_NOT_SET:
                        raise
                    print_attribute((a, None, None))
        hr = gc.GetNextRow(h)
    gc.CloseSearchHandle(h)


def main():
    global options
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option(
        "-f", "--file", dest="filename", help="write report to FILE", metavar="FILE"
    )
    parser.add_option(
        "-v",
        "--verbose",
        action="count",
        default=1,
        help="increase verbosity of output",
    )
    parser.add_option(
        "-q", "--quiet", action="store_true", help="suppress output messages"
    )

    parser.add_option("-U", "--user", help="specify the username used to connect")
    parser.add_option("-P", "--password", help="specify the password used to connect")
    parser.add_option(
        "",
        "--filter",
        default="(&(objectCategory=person)(objectClass=User))",
        help="specify the search filter",
    )
    parser.add_option(
        "", "--attributes", help="comma sep'd list of attribute names to print"
    )

    options, args = parser.parse_args()
    if options.quiet:
        if options.verbose != 1:
            parser.error("Can not use '--verbose' and '--quiet'")
        options.verbose = 0

    if args:
        parser.error("You need not specify args")

    search()


if __name__ == "__main__":
    main()

```


---

## com/win32comext/adsi/demos/test.py

```python
import sys
from collections.abc import Callable

import pythoncom
import win32api
from win32com.adsi import *

verbose_level = 0

server = ""  # Must have trailing /
local_name = win32api.GetComputerName()


def DumpRoot():
    "Dumps the root DSE"
    path = "LDAP://%srootDSE" % server
    rootdse = ADsGetObject(path)

    for item in rootdse.Get("SupportedLDAPVersion"):
        print(f"{path} supports ldap version {item}")

    attributes = ["CurrentTime", "defaultNamingContext"]
    for attr in attributes:
        val = rootdse.Get(attr)
        print(f" {attr}={val}")


###############################################
#
# Code taken from article titled:
# Reading attributeSchema and classSchema Objects
def _DumpClass(child):
    attrs = "Abstract lDAPDisplayName schemaIDGUID schemaNamingContext attributeSyntax oMSyntax"
    _DumpTheseAttributes(child, attrs.split())


def _DumpAttribute(child):
    attrs = "lDAPDisplayName schemaIDGUID adminDescription adminDisplayName rDNAttID defaultHidingValue defaultObjectCategory systemOnly defaultSecurityDescriptor"
    _DumpTheseAttributes(child, attrs.split())


def _DumpTheseAttributes(child, attrs):
    for attr in attrs:
        try:
            val = child.Get(attr)
        except pythoncom.com_error as details:
            continue
            # ###
            (hr, msg, exc, arg) = details
            if exc and exc[2]:
                msg = exc[2]
            val = f"<Error: {msg}>"
        if verbose_level >= 2:
            print(f" {child.Class}: {attr}={val}")


def DumpSchema():
    "Dumps the default DSE schema"
    # Bind to rootDSE to get the schemaNamingContext property.
    path = "LDAP://%srootDSE" % server
    rootdse = ADsGetObject(path)
    name = rootdse.Get("schemaNamingContext")

    # Bind to the actual schema container.
    path = "LDAP://" + server + name
    print("Binding to", path)
    ob = ADsGetObject(path)
    nclasses = nattr = nsub = nunk = 0

    # Enumerate the attribute and class objects in the schema container.
    for child in ob:
        # Find out if this is a class, attribute, or subSchema object.
        class_name = child.Class
        if class_name == "classSchema":
            _DumpClass(child)
            nclasses += 1
        elif class_name == "attributeSchema":
            _DumpAttribute(child)
            nattr += 1
        elif class_name == "subSchema":
            nsub += 1
        else:
            print("Unknown class:", class_name)
            nunk += 1
    if verbose_level:
        print("Processed", nclasses, "classes")
        print("Processed", nattr, "attributes")
        print("Processed", nsub, "sub-schema's")
        print("Processed", nunk, "unknown types")


def _DumpObject(ob, level=0):
    prefix = "  " * level
    print(f"{prefix}{ob.Class} object: {ob.Name}")
    # Do the directory object thing
    try:
        dir_ob = ADsGetObject(ob.ADsPath, IID_IDirectoryObject)
    except pythoncom.com_error:
        dir_ob = None
    if dir_ob is not None:
        info = dir_ob.GetObjectInformation()
        print(f"{prefix} RDN='{info.RDN}', ObjectDN='{info.ObjectDN}'")
        # Create a list of names to fetch
        names = ["distinguishedName"]
        attrs = dir_ob.GetObjectAttributes(names)
        for attr in attrs:
            for val, typ in attr.Values:
                print(f"{prefix} Attribute '{attr.AttrName}' = {val}")

    for child in ob:
        _DumpObject(child, level + 1)


def DumpAllObjects():
    "Recursively dump the entire directory!"
    path = "LDAP://%srootDSE" % server
    rootdse = ADsGetObject(path)
    name = rootdse.Get("defaultNamingContext")

    # Bind to the actual schema container.
    path = "LDAP://" + server + name
    print("Binding to", path)
    ob = ADsGetObject(path)

    # Enumerate the attribute and class objects in the schema container.
    _DumpObject(ob)


##########################################################
#
# Code taken from article:
# Example Code for Enumerating Schema Classes, Attributes, and Syntaxes

# Fill a map with VT_ datatypes, to give us better names:
vt_map = {}
for name, val in pythoncom.__dict__.items():
    if name[:3] == "VT_":
        vt_map[val] = name


def DumpSchema2():
    "Dumps the schema using an alternative technique"
    path = f"LDAP://{server}schema"
    schema = ADsGetObject(path, IID_IADsContainer)
    nclass = nprop = nsyntax = 0
    for item in schema:
        item_class = item.Class.lower()
        if item_class == "class":
            items = []
            if item.Abstract:
                items.append("Abstract")
            if item.Auxiliary:
                items.append("Auxiliary")
            # 			if item.Structural: items.append("Structural")
            desc = ", ".join(items)
            import win32com.util

            iid_name = win32com.util.IIDToInterfaceName(item.PrimaryInterface)
            if verbose_level >= 2:
                print(
                    "Class: Name={}, Flags={}, Primary Interface={}".format(
                        item.Name, desc, iid_name
                    )
                )
            nclass += 1
        elif item_class == "property":
            if item.MultiValued:
                val_type = "Multi-Valued"
            else:
                val_type = "Single-Valued"
            if verbose_level >= 2:
                print(f"Property: Name={item.Name}, {val_type}")
            nprop += 1
        elif item_class == "syntax":
            data_type = vt_map.get(item.OleAutoDataType, "<unknown type>")
            if verbose_level >= 2:
                print(f"Syntax: Name={item.Name}, Datatype = {data_type}")
            nsyntax += 1
    if verbose_level >= 1:
        print("Processed", nclass, "classes")
        print("Processed", nprop, "properties")
        print("Processed", nsyntax, "syntax items")


def DumpGC():
    "Dumps the GC: object (whatever that is!)"
    ob = ADsGetObject("GC:", IID_IADsContainer)
    for sub_ob in ob:
        print(f"GC ob: {sub_ob.Name} ({sub_ob.ADsPath})")


def DumpLocalUsers():
    "Dumps the local machine users"
    path = f"WinNT://{local_name},computer"
    ob = ADsGetObject(path, IID_IADsContainer)
    ob.put_Filter(["User", "Group"])
    for sub_ob in ob:
        print(f"User/Group: {sub_ob.Name} ({sub_ob.ADsPath})")


def DumpLocalGroups():
    "Dumps the local machine groups"
    path = f"WinNT://{local_name},computer"
    ob = ADsGetObject(path, IID_IADsContainer)

    ob.put_Filter(["Group"])
    for sub_ob in ob:
        print(f"Group: {sub_ob.Name} ({sub_ob.ADsPath})")
        # get the members
        members = sub_ob.Members()
        for member in members:
            print(f"  Group member: {member.Name} ({member.ADsPath})")


def usage(tests):
    import os

    print("Usage: %s [-s server ] [-v] [Test ...]" % os.path.basename(sys.argv[0]))
    print("  -v : Verbose - print more information")
    print("  -s : server - execute the tests against the named server")
    print("where Test is one of:")
    for t in tests:
        print(t.__name__, ":", t.__doc__)
    print()
    print("If not tests are specified, all tests are run")
    sys.exit(1)


def main():
    import getopt
    import traceback

    tests = []
    for ob in globals().values():
        if isinstance(ob, Callable) and ob.__doc__:
            tests.append(ob)
    opts, args = getopt.getopt(sys.argv[1:], "s:hv")
    for opt, val in opts:
        if opt == "-s":
            if val[-1] not in "\\/":
                val += "/"
            global server
            server = val
        if opt == "-h":
            usage(tests)
        if opt == "-v":
            global verbose_level
            verbose_level += 1

    if len(args) == 0:
        print("Running all tests - use '-h' to see command-line options...")
        dotests = tests
    else:
        dotests = []
        for arg in args:
            for t in tests:
                if t.__name__ == arg:
                    dotests.append(t)
                    break
            else:
                print("Test '%s' unknown - skipping" % arg)
    if not dotests:
        print("Nothing to do!")
        usage(tests)
    for test in dotests:
        try:
            test()
        except:
            print("Test %s failed" % test.__name__)
            traceback.print_exc()


if __name__ == "__main__":
    main()

```


---

## com/win32comext/authorization/demos/EditSecurity.py

```python
import os

import pythoncom
import win32api
import win32com.server.policy
import win32con
import win32security
from ntsecuritycon import (
    FILE_ALL_ACCESS,
    FILE_APPEND_DATA,
    FILE_GENERIC_EXECUTE,
    FILE_GENERIC_READ,
    FILE_GENERIC_WRITE,
    FILE_WRITE_DATA,
    READ_CONTROL,
    SI_ACCESS_GENERAL,
    SI_ACCESS_SPECIFIC,
    SI_ADVANCED,
    SI_CONTAINER,
    SI_EDIT_ALL,
    SI_PAGE_TITLE,
    SI_RESET,
    WRITE_DAC,
    WRITE_OWNER,
)
from pythoncom import IID_NULL
from win32com.authorization import authorization
from win32security import CONTAINER_INHERIT_ACE, OBJECT_INHERIT_ACE


class SecurityInformation(win32com.server.policy.DesignatedWrapPolicy):
    _com_interfaces_ = [authorization.IID_ISecurityInformation]
    _public_methods_ = [
        "GetObjectInformation",
        "GetSecurity",
        "SetSecurity",
        "GetAccessRights",
        "GetInheritTypes",
        "MapGeneric",
        "PropertySheetPageCallback",
    ]

    def __init__(self, FileName):
        self.FileName = FileName
        self._wrap_(self)

    def GetObjectInformation(self):
        """Identifies object whose security will be modified, and determines options available
        to the end user"""
        flags = SI_ADVANCED | SI_EDIT_ALL | SI_PAGE_TITLE | SI_RESET
        if os.path.isdir(self.FileName):
            flags |= SI_CONTAINER
        hinstance = 0  ## handle to module containing string resources
        servername = ""  ## name of authenticating server if not local machine
        objectname = os.path.split(self.FileName)[1]
        pagetitle = "Python ACL Editor"
        if os.path.isdir(self.FileName):
            pagetitle += " (dir)"
        else:
            pagetitle += " (file)"
        objecttype = IID_NULL
        return flags, hinstance, servername, objectname, pagetitle, objecttype

    def GetSecurity(self, requestedinfo, bdefault):
        """Requests the existing permissions for object"""
        if bdefault:
            ## This is invoked if the 'Default' button is pressed (only present if SI_RESET is passed
            ## with the flags in GetObjectInfo). Passing an empty SD with a NULL Dacl
            ##  should cause inherited ACL from parent dir or default dacl from user's token to be used
            return win32security.SECURITY_DESCRIPTOR()
        else:
            ## GetFileSecurity sometimes fails to return flags indicating that an ACE is inherited
            return win32security.GetNamedSecurityInfo(
                self.FileName, win32security.SE_FILE_OBJECT, requestedinfo
            )

    def SetSecurity(self, requestedinfo, sd):
        """Applies permissions to the object"""
        owner = sd.GetSecurityDescriptorOwner()
        group = sd.GetSecurityDescriptorGroup()
        dacl = sd.GetSecurityDescriptorDacl()
        sacl = sd.GetSecurityDescriptorSacl()
        win32security.SetNamedSecurityInfo(
            self.FileName,
            win32security.SE_FILE_OBJECT,
            requestedinfo,
            owner,
            group,
            dacl,
            sacl,
        )
        ## should also handle recursive operations here

    def GetAccessRights(self, objecttype, flags):
        """Returns a tuple of (AccessRights, DefaultAccess), where AccessRights is a sequence of tuples representing
        SI_ACCESS structs, containing (guid, access mask, Name, flags). DefaultAccess indicates which of the
        AccessRights will be used initially when a new ACE is added (zero based).
        Flags can contain SI_ACCESS_SPECIFIC,SI_ACCESS_GENERAL,SI_ACCESS_CONTAINER,SI_ACCESS_PROPERTY,
              CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,OBJECT_INHERIT_ACE
        """
        ## input flags: SI_ADVANCED,SI_EDIT_AUDITS,SI_EDIT_PROPERTIES indicating which property sheet is requesting the rights
        if (objecttype is not None) and (objecttype != IID_NULL):
            ## Should not be true for file objects.  Usually only used with DS objects that support security for
            ## their properties
            raise NotImplementedError("Object type is not supported")

        if os.path.isdir(self.FileName):
            file_append_data_desc = "Create subfolders"
            file_write_data_desc = "Create Files"
        else:
            file_append_data_desc = "Append data"
            file_write_data_desc = "Write data"

        accessrights = [
            (
                IID_NULL,
                FILE_GENERIC_READ,
                "Generic read",
                SI_ACCESS_GENERAL
                | SI_ACCESS_SPECIFIC
                | OBJECT_INHERIT_ACE
                | CONTAINER_INHERIT_ACE,
            ),
            (
                IID_NULL,
                FILE_GENERIC_WRITE,
                "Generic write",
                SI_ACCESS_GENERAL
                | SI_ACCESS_SPECIFIC
                | OBJECT_INHERIT_ACE
                | CONTAINER_INHERIT_ACE,
            ),
            (
                IID_NULL,
                win32con.DELETE,
                "Delete",
                SI_ACCESS_SPECIFIC | OBJECT_INHERIT_ACE | CONTAINER_INHERIT_ACE,
            ),
            (
                IID_NULL,
                WRITE_OWNER,
                "Change owner",
                SI_ACCESS_SPECIFIC | OBJECT_INHERIT_ACE | CONTAINER_INHERIT_ACE,
            ),
            (
                IID_NULL,
                READ_CONTROL,
                "Read Permissions",
                SI_ACCESS_SPECIFIC | OBJECT_INHERIT_ACE | CONTAINER_INHERIT_ACE,
            ),
            (
                IID_NULL,
                WRITE_DAC,
                "Change permissions",
                SI_ACCESS_SPECIFIC | OBJECT_INHERIT_ACE | CONTAINER_INHERIT_ACE,
            ),
            (
                IID_NULL,
                FILE_APPEND_DATA,
                file_append_data_desc,
                SI_ACCESS_SPECIFIC | OBJECT_INHERIT_ACE | CONTAINER_INHERIT_ACE,
            ),
            (
                IID_NULL,
                FILE_WRITE_DATA,
                file_write_data_desc,
                SI_ACCESS_SPECIFIC | OBJECT_INHERIT_ACE | CONTAINER_INHERIT_ACE,
            ),
        ]
        return (accessrights, 0)

    def MapGeneric(self, guid, aceflags, mask):
        """Converts generic access rights to specific rights.  This implementation uses standard file system rights,
        but you can map them any way that suits your application.
        """
        return win32security.MapGenericMask(
            mask,
            (
                FILE_GENERIC_READ,
                FILE_GENERIC_WRITE,
                FILE_GENERIC_EXECUTE,
                FILE_ALL_ACCESS,
            ),
        )

    def GetInheritTypes(self):
        """Specifies which types of ACE inheritance are supported.
        Returns a sequence of tuples representing SI_INHERIT_TYPE structs, containing
        (object type guid, inheritance flags, display name).  Guid is usually only used with
        Directory Service objects.
        """
        return (
            (IID_NULL, 0, "Only current object"),
            (IID_NULL, OBJECT_INHERIT_ACE, "Files inherit permissions"),
            (IID_NULL, CONTAINER_INHERIT_ACE, "Sub Folders inherit permissions"),
            (
                IID_NULL,
                CONTAINER_INHERIT_ACE | OBJECT_INHERIT_ACE,
                "Files and subfolders",
            ),
        )

    def PropertySheetPageCallback(self, hwnd, msg, pagetype):
        """Invoked each time a property sheet page is created or destroyed."""
        ## page types from SI_PAGE_TYPE enum: SI_PAGE_PERM SI_PAGE_ADVPERM SI_PAGE_AUDIT SI_PAGE_OWNER
        ## msg: PSPCB_CREATE, PSPCB_RELEASE, PSPCB_SI_INITDIALOG
        return None

    def EditSecurity(self, owner_hwnd=0):
        """Creates an ACL editor dialog based on parameters returned by interface methods"""
        isi = pythoncom.WrapObject(
            self, authorization.IID_ISecurityInformation, pythoncom.IID_IUnknown
        )
        authorization.EditSecurity(owner_hwnd, isi)


## folder permissions
temp_dir = win32api.GetTempPath()
dir_name = win32api.GetTempFileName(temp_dir, "isi")[0]
print(dir_name)
os.remove(dir_name)
os.mkdir(dir_name)
si = SecurityInformation(dir_name)
si.EditSecurity()

## file permissions
fname = win32api.GetTempFileName(dir_name, "isi")[0]
si = SecurityInformation(fname)
si.EditSecurity()

```


---

## com/win32comext/authorization/demos/EditServiceSecurity.py

```python
r"""
Implements a permissions editor for services.
Service can be specified as plain name for local machine,
or as a remote service of the form \\machinename\service
"""

import os

import pythoncom
import win32com.server.policy
import win32con
import win32security
import win32service
from win32com.authorization import authorization

SERVICE_GENERIC_EXECUTE = (
    win32service.SERVICE_START
    | win32service.SERVICE_STOP
    | win32service.SERVICE_PAUSE_CONTINUE
    | win32service.SERVICE_USER_DEFINED_CONTROL
)
SERVICE_GENERIC_READ = (
    win32service.SERVICE_QUERY_CONFIG
    | win32service.SERVICE_QUERY_STATUS
    | win32service.SERVICE_INTERROGATE
    | win32service.SERVICE_ENUMERATE_DEPENDENTS
)
SERVICE_GENERIC_WRITE = win32service.SERVICE_CHANGE_CONFIG

from ntsecuritycon import (
    READ_CONTROL,
    SI_ACCESS_GENERAL,
    SI_ACCESS_SPECIFIC,
    SI_ADVANCED,
    SI_EDIT_ALL,
    SI_PAGE_TITLE,
    SI_RESET,
    WRITE_DAC,
    WRITE_OWNER,
)
from pythoncom import IID_NULL


class ServiceSecurity(win32com.server.policy.DesignatedWrapPolicy):
    _com_interfaces_ = [authorization.IID_ISecurityInformation]
    _public_methods_ = [
        "GetObjectInformation",
        "GetSecurity",
        "SetSecurity",
        "GetAccessRights",
        "GetInheritTypes",
        "MapGeneric",
        "PropertySheetPageCallback",
    ]

    def __init__(self, ServiceName):
        self.ServiceName = ServiceName
        self._wrap_(self)

    def GetObjectInformation(self):
        """Identifies object whose security will be modified, and determines options available
        to the end user"""
        flags = SI_ADVANCED | SI_EDIT_ALL | SI_PAGE_TITLE | SI_RESET
        hinstance = 0  ## handle to module containing string resources
        servername = ""  ## name of authenticating server if not local machine

        ## service name can contain remote machine name of the form \\Server\ServiceName
        objectname = os.path.split(self.ServiceName)[1]
        pagetitle = "Service Permissions for " + self.ServiceName
        objecttype = IID_NULL
        return flags, hinstance, servername, objectname, pagetitle, objecttype

    def GetSecurity(self, requestedinfo, bdefault):
        """Requests the existing permissions for object"""
        if bdefault:
            return win32security.SECURITY_DESCRIPTOR()
        else:
            return win32security.GetNamedSecurityInfo(
                self.ServiceName, win32security.SE_SERVICE, requestedinfo
            )

    def SetSecurity(self, requestedinfo, sd):
        """Applies permissions to the object"""
        owner = sd.GetSecurityDescriptorOwner()
        group = sd.GetSecurityDescriptorGroup()
        dacl = sd.GetSecurityDescriptorDacl()
        sacl = sd.GetSecurityDescriptorSacl()
        win32security.SetNamedSecurityInfo(
            self.ServiceName,
            win32security.SE_SERVICE,
            requestedinfo,
            owner,
            group,
            dacl,
            sacl,
        )

    def GetAccessRights(self, objecttype, flags):
        """Returns a tuple of (AccessRights, DefaultAccess), where AccessRights is a sequence of tuples representing
        SI_ACCESS structs, containing (guid, access mask, Name, flags). DefaultAccess indicates which of the
        AccessRights will be used initially when a new ACE is added (zero based).
        Flags can contain SI_ACCESS_SPECIFIC,SI_ACCESS_GENERAL,SI_ACCESS_CONTAINER,SI_ACCESS_PROPERTY,
              CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,OBJECT_INHERIT_ACE
        """
        ## input flags: SI_ADVANCED,SI_EDIT_AUDITS,SI_EDIT_PROPERTIES indicating which property sheet is requesting the rights
        if (objecttype is not None) and (objecttype != IID_NULL):
            ## Not relevent for services
            raise NotImplementedError("Object type is not supported")

        ## ???? for some reason, the DACL for a service will not retain ACCESS_SYSTEM_SECURITY in an ACE ????
        ## (IID_NULL, win32con.ACCESS_SYSTEM_SECURITY, 'View/change audit settings', SI_ACCESS_SPECIFIC),

        accessrights = [
            (
                IID_NULL,
                win32service.SERVICE_ALL_ACCESS,
                "Full control",
                SI_ACCESS_GENERAL,
            ),
            (IID_NULL, SERVICE_GENERIC_READ, "Generic read", SI_ACCESS_GENERAL),
            (IID_NULL, SERVICE_GENERIC_WRITE, "Generic write", SI_ACCESS_GENERAL),
            (
                IID_NULL,
                SERVICE_GENERIC_EXECUTE,
                "Start/Stop/Pause service",
                SI_ACCESS_GENERAL,
            ),
            (IID_NULL, READ_CONTROL, "Read Permissions", SI_ACCESS_GENERAL),
            (IID_NULL, WRITE_DAC, "Change permissions", SI_ACCESS_GENERAL),
            (IID_NULL, WRITE_OWNER, "Change owner", SI_ACCESS_GENERAL),
            (IID_NULL, win32con.DELETE, "Delete service", SI_ACCESS_GENERAL),
            (IID_NULL, win32service.SERVICE_START, "Start service", SI_ACCESS_SPECIFIC),
            (IID_NULL, win32service.SERVICE_STOP, "Stop service", SI_ACCESS_SPECIFIC),
            (
                IID_NULL,
                win32service.SERVICE_PAUSE_CONTINUE,
                "Pause/unpause service",
                SI_ACCESS_SPECIFIC,
            ),
            (
                IID_NULL,
                win32service.SERVICE_USER_DEFINED_CONTROL,
                "Execute user defined operations",
                SI_ACCESS_SPECIFIC,
            ),
            (
                IID_NULL,
                win32service.SERVICE_QUERY_CONFIG,
                "Read configuration",
                SI_ACCESS_SPECIFIC,
            ),
            (
                IID_NULL,
                win32service.SERVICE_CHANGE_CONFIG,
                "Change configuration",
                SI_ACCESS_SPECIFIC,
            ),
            (
                IID_NULL,
                win32service.SERVICE_ENUMERATE_DEPENDENTS,
                "List dependent services",
                SI_ACCESS_SPECIFIC,
            ),
            (
                IID_NULL,
                win32service.SERVICE_QUERY_STATUS,
                "Query status",
                SI_ACCESS_SPECIFIC,
            ),
            (
                IID_NULL,
                win32service.SERVICE_INTERROGATE,
                "Query status (immediate)",
                SI_ACCESS_SPECIFIC,
            ),
        ]
        return (accessrights, 0)

    def MapGeneric(self, guid, aceflags, mask):
        """Converts generic access rights to specific rights."""
        return win32security.MapGenericMask(
            mask,
            (
                SERVICE_GENERIC_READ,
                SERVICE_GENERIC_WRITE,
                SERVICE_GENERIC_EXECUTE,
                win32service.SERVICE_ALL_ACCESS,
            ),
        )

    def GetInheritTypes(self):
        """Specifies which types of ACE inheritance are supported.
        Services don't use any inheritance
        """
        return ((IID_NULL, 0, "Only current object"),)

    def PropertySheetPageCallback(self, hwnd, msg, pagetype):
        """Invoked each time a property sheet page is created or destroyed."""
        ## page types from SI_PAGE_TYPE enum: SI_PAGE_PERM SI_PAGE_ADVPERM SI_PAGE_AUDIT SI_PAGE_OWNER
        ## msg: PSPCB_CREATE, PSPCB_RELEASE, PSPCB_SI_INITDIALOG
        return None

    def EditSecurity(self, owner_hwnd=0):
        """Creates an ACL editor dialog based on parameters returned by interface methods"""
        isi = pythoncom.WrapObject(
            self, authorization.IID_ISecurityInformation, pythoncom.IID_IUnknown
        )
        authorization.EditSecurity(owner_hwnd, isi)


if __name__ == "__main__":
    # Find the first service on local machine and edit its permissions
    scm = win32service.OpenSCManager(
        None, None, win32service.SC_MANAGER_ENUMERATE_SERVICE
    )
    svcs = win32service.EnumServicesStatus(scm)
    win32service.CloseServiceHandle(scm)
    si = ServiceSecurity(svcs[0][0])
    si.EditSecurity()

```


---

## com/win32comext/axcontrol/demos/container_ie.py

```python
# An example of hosting an IE app (without using Pythonwin/MFC)
# A nod to the Code Project's article "Embed an HTML control in your own
# window using plain C"
import sys

import pythoncom
import win32api
import win32con
import win32gui
import winerror
from win32com.axcontrol import axcontrol
from win32com.client import Dispatch
from win32com.server.exception import COMException
from win32com.server.util import wrap

# Set to True to see debug output in the 'trace collector' window.
debugging = False

# If you wanted events or better type info, you'd probably do:
# gencache.EnsureModule('{EAB22AC0-30C1-11CF-A7EB-0000C05BAE0B}', 0, 1, 1)
# which is the "Microsoft Internet Controls" typelib defining interfaces
# such as IWebBrowser2 and the associated events.

IOleClientSite_methods = """SaveObject GetMoniker GetContainer ShowObject
                            OnShowWindow RequestNewObjectLayout""".split()

IOleInPlaceSite_methods = """GetWindow ContextSensitiveHelp CanInPlaceActivate
                             OnInPlaceActivate OnUIActivate GetWindowContext
                             Scroll OnUIDeactivate OnInPlaceDeactivate
                             DiscardUndoState DeactivateAndUndo
                             OnPosRectChange""".split()

IOleInPlaceFrame_methods = """GetWindow ContextSensitiveHelp GetBorder
                              RequestBorderSpace SetBorderSpace
                              SetActiveObject InsertMenus SetMenu
                              RemoveMenus SetStatusText EnableModeless
                              TranslateAccelerator""".split()


class SimpleSite:
    _com_interfaces_ = [axcontrol.IID_IOleClientSite, axcontrol.IID_IOleInPlaceSite]
    _public_methods_ = IOleClientSite_methods + IOleInPlaceSite_methods

    def __init__(self, host_window):
        self.hw = host_window

    # IID_IOleClientSite methods
    def SaveObject(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetMoniker(self, dwAssign, which):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetContainer(self):
        raise COMException(hresult=winerror.E_NOINTERFACE)

    def ShowObject(self):
        pass

    def OnShowWindow(self, fShow):
        pass

    def RequestNewObjectLayout(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    # IID_IOleInPlaceSite methods
    def GetWindow(self):
        return self.hw.hwnd

    def ContextSensitiveHelp(self, fEnter):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def CanInPlaceActivate(self):
        pass  # we can

    def OnInPlaceActivate(self):
        pass

    def OnUIActivate(self):
        pass

    def GetWindowContext(self):
        # return IOleInPlaceFrame, IOleInPlaceUIWindow, rect, clip_rect, frame_info
        # where frame_info is (fMDIApp, hwndFrame, hAccel, nAccel)
        return (
            self.hw.ole_frame,
            None,
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (True, self.hw.hwnd, None, 0),
        )

    def Scroll(self, size):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def OnUIDeactivate(self, fUndoable):
        pass

    def OnInPlaceDeactivate(self):
        pass

    def DiscardUndoState(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def DeactivateAndUndo(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def OnPosRectChange(self, rect):
        browser_ob = self.hw.browser.QueryInterface(axcontrol.IID_IOleInPlaceObject)
        browser_ob.SetObjectRects(rect, rect)


class SimpleFrame:
    # _com_interfaces_ = [axcontrol.IID_IOleInPlaceFrame]
    _public_methods_ = IOleInPlaceFrame_methods

    def __init__(self, host_window):
        self.hw = host_window

    def GetWindow(self):
        return self.hw.hwnd

    def ContextSensitiveHelp(self, fEnterMode):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetBorder(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def RequestBorderSpace(self, widths):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def SetBorderSpace(self, widths):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def SetActiveObject(self, ob, name):
        pass

    def InsertMenus(self, hmenuShared, menuWidths):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def SetMenu(self, hmenuShared, holemenu, hwndActiveObject):
        pass

    def RemoveMenus(self, hmenuShared):
        pass

    def SetStatusText(self, statusText):
        pass

    def EnableModeless(self, fEnable):
        pass

    def TranslateAccelerator(self, msg, wID):
        raise COMException(hresult=winerror.E_NOTIMPL)


# A class that manages the top-level window.
class IEHost:
    wnd_class_name = "EmbeddedBrowser"

    def __init__(self):
        self.hwnd = None
        self.ole_frame = None

    def __del__(self):
        try:
            win32gui.UnregisterClass(self.wnd_class_name, None)
        except win32gui.error:
            pass

    def create_window(self):
        message_map = {
            win32con.WM_SIZE: self.OnSize,
            win32con.WM_DESTROY: self.OnDestroy,
        }

        wc = win32gui.WNDCLASS()
        wc.lpszClassName = self.wnd_class_name
        # wc.style =  win32con.CS_GLOBALCLASS|win32con.CS_VREDRAW | win32con.CS_HREDRAW
        # wc.hbrBackground = win32con.COLOR_WINDOW+1
        wc.lpfnWndProc = message_map
        class_atom = win32gui.RegisterClass(wc)
        self.hwnd = win32gui.CreateWindow(
            wc.lpszClassName,
            "Embedded browser",
            win32con.WS_OVERLAPPEDWINDOW | win32con.WS_VISIBLE,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            0,
            None,
        )
        browser = pythoncom.CoCreateInstance(
            "{8856F961-340A-11D0-A96B-00C04FD705A2}",
            None,
            pythoncom.CLSCTX_INPROC_SERVER | pythoncom.CLSCTX_INPROC_HANDLER,
            axcontrol.IID_IOleObject,
        )
        self.browser = browser
        site = wrap(
            SimpleSite(self), axcontrol.IID_IOleClientSite, useDispatcher=debugging
        )

        browser.SetClientSite(site)
        browser.SetHostNames("IE demo", "Hi there")
        axcontrol.OleSetContainedObject(self.browser, True)
        rect = win32gui.GetWindowRect(self.hwnd)
        browser.DoVerb(axcontrol.OLEIVERB_SHOW, None, site, -1, self.hwnd, rect)
        b2 = Dispatch(browser.QueryInterface(pythoncom.IID_IDispatch))
        self.browser2 = b2
        b2.Left = 0
        b2.Top = 0
        b2.Width = rect[2]
        b2.Height = rect[3]

    def OnSize(self, hwnd, msg, wparam, lparam):
        self.browser2.Width = win32api.LOWORD(lparam)
        self.browser2.Height = win32api.HIWORD(lparam)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        self.browser.Close(axcontrol.OLECLOSE_NOSAVE)
        self.browser = None
        self.browser2 = None
        win32gui.PostQuitMessage(0)


if __name__ == "__main__":
    h = IEHost()
    h.create_window()
    if len(sys.argv) < 2:
        h.browser2.Navigate2("about:blank")
        doc = h.browser2.Document
        doc.write(
            'This is an IE page hosted by <a href="https://www.python.org">python</a>'
        )
        doc.write("<br>(you can also specify a URL on the command-line...)")
    else:
        h.browser2.Navigate2(sys.argv[1])

    win32gui.PumpMessages()

```


---

## com/win32comext/ifilter/demos/filterDemo.py

```python
import pythoncom
import pywintypes
from win32com import storagecon
from win32com.ifilter import ifilter
from win32com.ifilter.ifiltercon import *


class FileParser:
    # Property IDs for the Storage Property Set
    PIDS_BODY = 0x00000013

    # property IDs for HTML Storage Property Set
    PIDH_DESCRIPTION = "DESCRIPTION"
    PIDH_HREF = "A.HREF"
    PIDH_IMGSRC = "IMG.SRC"

    # conversion map to convert ifilter properties to more user friendly names
    propertyToName = {
        PSGUID_STORAGE: {PIDS_BODY: "body"},
        PSGUID_SUMMARYINFORMATION: {
            PIDSI_TITLE: "title",
            PIDSI_SUBJECT: "description",
            PIDSI_AUTHOR: "author",
            PIDSI_KEYWORDS: "keywords",
            PIDSI_COMMENTS: "comments",
        },
        PSGUID_HTMLINFORMATION: {PIDH_DESCRIPTION: "description"},
        PSGUID_HTML2_INFORMATION: {PIDH_HREF: "href", PIDH_IMGSRC: "img"},
    }

    def __init__(self, verbose=False):
        self.f = None
        self.stg = None
        self.verbose = verbose

    def Close(self):
        self.f = None
        self.stg = None

    def Parse(self, fileName, maxErrors=10):
        properties = {}

        try:
            self._bind_to_filter(fileName)
            try:
                flags = self.f.Init(
                    IFILTER_INIT_APPLY_INDEX_ATTRIBUTES
                    | IFILTER_INIT_APPLY_OTHER_ATTRIBUTES
                )
                if flags == IFILTER_FLAGS_OLE_PROPERTIES and self.stg is not None:
                    self._trace("filter requires to get properities via ole")
                    self._get_properties(properties)

                errCnt = 0
                while True:
                    try:
                        # each chunk returns a tuple with the following:-
                        # idChunk       = The chunk identifier. each chunk has a unique identifier
                        # breakType     = The type of break that separates the previous chunk from the current chunk. Values are:-
                        #                 CHUNK_NO_BREAK=0,CHUNK_EOW=1,CHUNK_EOS= 2,CHUNK_EOP= 3,CHUNK_EOC= 4
                        # flags         = Flags indicate whether this chunk contains a text-type or a value-type property
                        #                 locale = The language and sublanguage associated with a chunk of text
                        # attr          = A tuple containing the property to be applied to the chunk. Tuple is (propertyset GUID, property ID)
                        #                 Property ID can be a number or string
                        # idChunkSource = The ID of the source of a chunk. The value of the idChunkSource member depends on the nature of the chunk
                        # startSource   = The offset from which the source text for a derived chunk starts in the source chunk
                        # lenSource     = The length in characters of the source text from which the current chunk was derived.
                        #                 A zero value signifies character-by-character correspondence between the source text and the derived text.

                        (
                            idChunk,
                            breakType,
                            flags,
                            locale,
                            attr,
                            idChunkSource,
                            startSource,
                            lenSource,
                        ) = self.f.GetChunk()
                        self._trace(
                            "Chunk details:",
                            idChunk,
                            breakType,
                            flags,
                            locale,
                            attr,
                            idChunkSource,
                            startSource,
                            lenSource,
                        )

                        # attempt to map each property to a more user friendly name. If we don't know what it is just return
                        # the set guid and property id. (note: the id can be a number or a string.
                        propSet = self.propertyToName.get(attr[0])
                        if propSet:
                            propName = propSet.get(attr[1], "{}:{}".format(*attr))
                        else:
                            propName = "{}:{}".format(*attr)

                    except pythoncom.com_error as e:
                        if e[0] == FILTER_E_END_OF_CHUNKS:
                            # we have read all the chunks
                            break
                        elif e[0] in [
                            FILTER_E_EMBEDDING_UNAVAILABLE,
                            FILTER_E_LINK_UNAVAILABLE,
                        ]:
                            # the next chunk can't be read. Also keep track of the number of times we
                            # fail as some filters (ie. the Msoft office ones can get stuck here)
                            errCnt += 1
                            if errCnt > maxErrors:
                                raise
                            else:
                                continue
                        elif e[0] == FILTER_E_ACCESS:
                            self._trace("Access denied")
                            raise
                        elif e[0] == FILTER_E_PASSWORD:
                            self._trace("Password required")
                            raise
                        else:
                            # any other type of error really can't be recovered from
                            raise

                    # reset consecutive errors (some filters may get stuck in a lopp if embedding or link failures occurs
                    errCnt = 0

                    if flags == CHUNK_TEXT:
                        # it's a text segment - get all available text for this chunk.
                        body_chunks = properties.setdefault(propName, [])
                        self._get_text(body_chunks)
                    elif flags == CHUNK_VALUE:
                        # it's a data segment - get the value
                        properties[propName] = self.f.GetValue()
                    else:
                        self._trace("Unknown flag returned by GetChunk:", flags)
            finally:
                self.Close()

        except pythoncom.com_error as e:
            self._trace("ERROR processing file", e)
            raise

        return properties

    def _bind_to_filter(self, fileName):
        """
        See if the file is a structured storage file or a normal file
        and then return an ifilter interface by calling the appropriate bind/load function
        """
        if pythoncom.StgIsStorageFile(fileName):
            self.stg = pythoncom.StgOpenStorage(
                fileName, None, storagecon.STGM_READ | storagecon.STGM_SHARE_DENY_WRITE
            )
            try:
                self.f = ifilter.BindIFilterFromStorage(self.stg)
            except pythoncom.com_error as e:
                if (
                    e[0] == -2147467262
                ):  # 0x80004002: # no interface, try the load interface (this happens for some MSoft files)
                    self.f = ifilter.LoadIFilter(fileName)
                else:
                    raise
        else:
            self.f = ifilter.LoadIFilter(fileName)
            self.stg = None

    def _get_text(self, body_chunks):
        """
        Gets all the text for a particular chunk. We need to keep calling get text till all the
        segments for this chunk are retrieved
        """
        while True:
            try:
                body_chunks.append(self.f.GetText())
            except pythoncom.com_error as e:
                if e[0] in [
                    FILTER_E_NO_MORE_TEXT,
                    FILTER_E_NO_MORE_TEXT,
                    FILTER_E_NO_TEXT,
                ]:
                    break
                else:
                    raise  # not one of the values we were expecting

    def _get_properties(self, properties):
        """
        Use OLE property sets to get base properties
        """
        try:
            pss = self.stg.QueryInterface(pythoncom.IID_IPropertySetStorage)
        except pythoncom.com_error as e:
            self._trace("No Property information could be retrieved", e)
            return

        ps = pss.Open(PSGUID_SUMMARYINFORMATION)

        props = (
            PIDSI_TITLE,
            PIDSI_SUBJECT,
            PIDSI_AUTHOR,
            PIDSI_KEYWORDS,
            PIDSI_COMMENTS,
        )

        title, subject, author, keywords, comments = ps.ReadMultiple(props)
        if title is not None:
            properties["title"] = title
        if subject is not None:
            properties["description"] = subject
        if author is not None:
            properties["author"] = author
        if keywords is not None:
            properties["keywords"] = keywords
        if comments is not None:
            properties["comments"] = comments

    def _trace(self, *args):
        if self.verbose:
            ret = " ".join([str(arg) for arg in args])
            try:
                print(ret)
            except OSError:
                pass


def _usage():
    import os

    print(f"Usage: {os.path.basename(sys.argv[0])} filename [verbose [dumpbody]]")
    print()
    print("Where:-")
    print("filename = name of the file to extract text & properties from")
    print("verbose = 1=debug output, 0=no debug output (default=0)")
    print("dumpbody = 1=print text content, 0=don't print content (default=1)")
    print()
    print("e.g. to dump a word file called spam.doc go:- filterDemo.py spam.doc")
    print()
    print("by default .htm, .txt, .doc, .dot, .xls, .xlt, .ppt are supported")
    print("you can filter .pdf's by downloading adobes ifilter component. ")
    print(
        "(currently found at https://download.adobe.com/pub/adobe/acrobat/win/all/ifilter50.exe)."
    )
    print("ifilters for other filetypes are also available.")
    print()
    print("For more info on the API check out MSDN under ifilters")


if __name__ == "__main__":
    import operator
    import sys

    fName = ""
    verbose = False
    bDumpBody = True

    if len(sys.argv) < 2:
        _usage()
        sys.exit(1)

    try:
        fName = sys.argv[1]
        verbose = sys.argv[2] != "0"
        bDumpBody = sys.argv[3] != "0"
    except:
        pass

    p = FileParser(verbose)
    propMap = p.Parse(fName)

    if bDumpBody:
        print("Body")
        ch = " ".join(propMap.get("body", []))
        try:
            print(ch)
        except UnicodeError:
            print(ch.encode("iso8859-1", "ignore"))

    print("Properties")
    for propName, propValue in propMap.items():
        print(propName, ":", end=" ")
        if propName == "body":
            print(
                "<%s length: %d>"
                % (
                    propName,
                    reduce(operator.add, [len(p) for p in propValue]),
                )
            )
        elif isinstance(propValue, list):
            print()
            for pv in propValue:
                print(pv)
        else:
            print(propValue)
        print()

```


---

## com/win32comext/mapi/demos/mapisend.py

```python
#!/usr/bin/env python

"""module to send mail with Extended MAPI using the pywin32 mapi wrappers..."""

# this was based on Jason Hattingh's C++ code at http://www.codeproject.com/internet/mapadmin.asp (dead link)
# written by David Fraser <davidf at sjsoft.com> and Stephen Emslie <stephene at sjsoft.com>
# you can test this by changing the variables at the bottom and running from the command line

from win32com.mapi import mapi, mapitags


def SendEMAPIMail(
    Subject="", Message="", SendTo=None, SendCC=None, SendBCC=None, MAPIProfile=None
):
    """Sends an email to the recipient using the extended MAPI interface
    Subject and Message are strings
    Send{To,CC,BCC} are comma-separated address lists
    MAPIProfile is the name of the MAPI profile"""

    # initialize and log on
    mapi.MAPIInitialize(None)
    session = mapi.MAPILogonEx(
        0, MAPIProfile, None, mapi.MAPI_EXTENDED | mapi.MAPI_USE_DEFAULT
    )
    messagestorestable = session.GetMsgStoresTable(0)
    messagestorestable.SetColumns(
        (mapitags.PR_ENTRYID, mapitags.PR_DISPLAY_NAME_A, mapitags.PR_DEFAULT_STORE), 0
    )

    while True:
        rows = messagestorestable.QueryRows(1, 0)
        # if this is the last row then stop
        if len(rows) != 1:
            break
        row = rows[0]
        # if this is the default store then stop
        if (mapitags.PR_DEFAULT_STORE, True) in row:
            break

    # unpack the row and open the message store
    (eid_tag, eid), (name_tag, name), (def_store_tag, def_store) = row
    msgstore = session.OpenMsgStore(
        0, eid, None, mapi.MDB_NO_DIALOG | mapi.MAPI_BEST_ACCESS
    )

    # get the outbox
    hr, props = msgstore.GetProps((mapitags.PR_IPM_OUTBOX_ENTRYID), 0)
    (tag, eid) = props[0]
    # check for errors
    if mapitags.PROP_TYPE(tag) == mapitags.PT_ERROR:
        raise TypeError("got PT_ERROR instead of PT_BINARY: %s" % eid)
    outboxfolder = msgstore.OpenEntry(eid, None, mapi.MAPI_BEST_ACCESS)

    # create the message and the addrlist
    message = outboxfolder.CreateMessage(None, 0)
    # note: you can use the resolveaddress functions for this. but you may get headaches
    pal = []

    def makeentry(recipient, recipienttype):
        return (
            (mapitags.PR_RECIPIENT_TYPE, recipienttype),
            (mapitags.PR_SEND_RICH_INFO, False),
            (mapitags.PR_DISPLAY_TYPE, 0),
            (mapitags.PR_OBJECT_TYPE, 6),
            (mapitags.PR_EMAIL_ADDRESS_A, recipient),
            (mapitags.PR_ADDRTYPE_A, "SMTP"),
            (mapitags.PR_DISPLAY_NAME_A, recipient),
        )

    if SendTo:
        pal.extend(
            [makeentry(recipient, mapi.MAPI_TO) for recipient in SendTo.split(",")]
        )
    if SendCC:
        pal.extend(
            [makeentry(recipient, mapi.MAPI_CC) for recipient in SendCC.split(",")]
        )
    if SendBCC:
        pal.extend(
            [makeentry(recipient, mapi.MAPI_BCC) for recipient in SendBCC.split(",")]
        )

    # add the resolved recipients to the message
    message.ModifyRecipients(mapi.MODRECIP_ADD, pal)
    message.SetProps([(mapitags.PR_BODY_A, Message), (mapitags.PR_SUBJECT_A, Subject)])

    # save changes and submit
    outboxfolder.SaveChanges(0)
    message.SubmitMessage(0)


if __name__ == "__main__":
    MAPIProfile = ""
    # Change this to a valid email address to test
    SendTo = "an.invalid at address"
    SendMessage = "testing one two three"
    SendSubject = "Testing Extended MAPI!!"
    SendEMAPIMail(SendSubject, SendMessage, SendTo, MAPIProfile=MAPIProfile)

```


---

## com/win32comext/shell/demos/IActiveDesktop.py

```python
import time

import pythoncom
from win32com.shell import shell, shellcon

website = "https://github.com/mhammond/pywin32/"
iad = pythoncom.CoCreateInstance(
    shell.CLSID_ActiveDesktop,
    None,
    pythoncom.CLSCTX_INPROC_SERVER,
    shell.IID_IActiveDesktop,
)
opts = iad.GetDesktopItemOptions()
if not (opts["ActiveDesktop"] and opts["EnableComponents"]):
    print("Warning: Enabling Active Desktop")
    opts["ActiveDesktop"] = True
    opts["EnableComponents"] = True
    iad.SetDesktopItemOptions(opts)
    iad.ApplyChanges(0xFFFF)
    iad = None
    ## apparently takes a short while for it to become active
    time.sleep(2)
    iad = pythoncom.CoCreateInstance(
        shell.CLSID_ActiveDesktop,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IActiveDesktop,
    )

cnt = iad.GetDesktopItemCount()
print("Count:", cnt)
for i in range(cnt):
    print(iad.GetDesktopItem(i))

component = {
    "ID": cnt + 1,
    "ComponentType": shellcon.COMP_TYPE_WEBSITE,
    "CurItemState": shellcon.IS_NORMAL,
    "SubscribedURL": website,
    "Source": website,
    "FriendlyName": "Pywin32 on SF",
    "Checked": True,  ## this controls whether item is currently displayed
    "NoScroll": False,
    "Dirty": False,
    "Pos": {
        "Top": 69,
        "Left": 69,
        "Height": 400,
        "Width": 400,
        "zIndex": 1002,
        "CanResize": True,
        "CanResizeX": True,
        "CanResizeY": True,
        "PreferredLeftPercent": 0,
        "PreferredTopPercent": 0,
    },
    "Original": {
        "Top": 33,
        "Left": 304,
        "Height": 362,
        "Width": 372,
        "ItemState": shellcon.IS_NORMAL,
    },
    "Restored": {
        "Top": 33,
        "Left": 304,
        "Height": 362,
        "Width": 372,
        "ItemState": shellcon.IS_NORMAL,
    },
}


try:
    existing_item = iad.GetDesktopItemBySource(website)
except pythoncom.com_error:
    pass
else:
    iad.RemoveDesktopItem(existing_item)
    iad.ApplyChanges(0xFFFF)

iad.AddDesktopItem(component)
iad.ApplyChanges(0xFFFF)  ## need to check which AD_APPLY constants are actually needed

```


---

## com/win32comext/shell/demos/IFileOperationProgressSink.py

```python
# Sample implementation of IFileOperationProgressSink that just prints
# some basic info

import pythoncom
from win32com.server.policy import DesignatedWrapPolicy
from win32com.shell import shell, shellcon

tsf_flags = [(k, v) for k, v in shellcon.__dict__.items() if k.startswith("TSF_")]


def decode_flags(flags):
    if flags == 0:
        return "TSF_NORMAL"
    flag_txt = ""
    for k, v in tsf_flags:
        if flags & v:
            if flag_txt:
                flag_txt += "|" + k
            else:
                flag_txt = k
    return flag_txt


class FileOperationProgressSink(DesignatedWrapPolicy):
    _com_interfaces_ = [shell.IID_IFileOperationProgressSink]
    _public_methods_ = [
        "StartOperations",
        "FinishOperations",
        "PreRenameItem",
        "PostRenameItem",
        "PreMoveItem",
        "PostMoveItem",
        "PreCopyItem",
        "PostCopyItem",
        "PreDeleteItem",
        "PostDeleteItem",
        "PreNewItem",
        "PostNewItem",
        "UpdateProgress",
        "ResetTimer",
        "PauseTimer",
        "ResumeTimer",
    ]

    def __init__(self):
        self._wrap_(self)

    def StartOperations(self):
        print("StartOperations")

    def FinishOperations(self, Result):
        print("FinishOperations: HRESULT ", Result)

    def PreRenameItem(self, Flags, Item, NewName):
        print(
            "PreRenameItem: Renaming "
            + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + " to "
            + NewName
        )

    def PostRenameItem(self, Flags, Item, NewName, hrRename, NewlyCreated):
        if NewlyCreated is not None:
            newfile = NewlyCreated.GetDisplayName(shellcon.SHGDN_FORPARSING)
        else:
            newfile = "not renamed, HRESULT " + str(hrRename)
        print(
            "PostRenameItem: renamed "
            + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + " to "
            + newfile
        )

    def PreMoveItem(self, Flags, Item, DestinationFolder, NewName):
        print(
            "PreMoveItem: Moving "
            + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + " to "
            + DestinationFolder.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + "\\"
            + str(NewName)
        )

    def PostMoveItem(
        self, Flags, Item, DestinationFolder, NewName, hrMove, NewlyCreated
    ):
        if NewlyCreated is not None:
            newfile = NewlyCreated.GetDisplayName(shellcon.SHGDN_FORPARSING)
        else:
            newfile = "not copied, HRESULT " + str(hrMove)
        print(
            "PostMoveItem: Moved "
            + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + " to "
            + newfile
        )

    def PreCopyItem(self, Flags, Item, DestinationFolder, NewName):
        if not NewName:
            NewName = ""
        print(
            "PreCopyItem: Copying "
            + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + " to "
            + DestinationFolder.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + "\\"
            + NewName
        )
        print("Flags: ", decode_flags(Flags))

    def PostCopyItem(
        self, Flags, Item, DestinationFolder, NewName, hrCopy, NewlyCreated
    ):
        if NewlyCreated is not None:
            newfile = NewlyCreated.GetDisplayName(shellcon.SHGDN_FORPARSING)
        else:
            newfile = "not copied, HRESULT " + str(hrCopy)
        print(
            "PostCopyItem: Copied "
            + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + " to "
            + newfile
        )
        print("Flags: ", decode_flags(Flags))

    def PreDeleteItem(self, Flags, Item):
        print(
            "PreDeleteItem: Deleting " + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
        )

    def PostDeleteItem(self, Flags, Item, hrDelete, NewlyCreated):
        print(
            "PostDeleteItem: Deleted " + Item.GetDisplayName(shellcon.SHGDN_FORPARSING)
        )
        if NewlyCreated:
            print(
                "    Moved to recycle bin - "
                + NewlyCreated.GetDisplayName(shellcon.SHGDN_FORPARSING)
            )

    def PreNewItem(self, Flags, DestinationFolder, NewName):
        print(
            "PreNewItem: Creating "
            + DestinationFolder.GetDisplayName(shellcon.SHGDN_FORPARSING)
            + "\\"
            + NewName
        )

    def PostNewItem(
        self,
        Flags,
        DestinationFolder,
        NewName,
        TemplateName,
        FileAttributes,
        hrNew,
        NewItem,
    ):
        print(
            "PostNewItem: Created " + NewItem.GetDisplayName(shellcon.SHGDN_FORPARSING)
        )

    def UpdateProgress(self, WorkTotal, WorkSoFar):
        print("UpdateProgress: ", WorkSoFar, WorkTotal)

    def ResetTimer(self):
        print("ResetTimer")

    def PauseTimer(self):
        print("PauseTimer")

    def ResumeTimer(self):
        print("ResumeTimer")


def CreateSink():
    return pythoncom.WrapObject(
        FileOperationProgressSink(), shell.IID_IFileOperationProgressSink
    )

```


---

## com/win32comext/shell/demos/IShellLinkDataList.py

```python
import os
import sys

import pythoncom
import win32api
from win32com.shell import shell, shellcon

temp_dir = win32api.GetTempPath()
linkname = win32api.GetTempFileName(temp_dir, "cmd")[0]
os.remove(linkname)
linkname += ".lnk"
print("Link name:", linkname)
ish = pythoncom.CoCreateInstance(
    shell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink
)
ish.SetPath(os.environ["cOMSPEC"])
ish.SetWorkingDirectory(os.path.split(sys.executable)[0])
ish.SetDescription("shortcut made by python")

console_props = {
    "Signature": shellcon.NT_CONSOLE_PROPS_SIG,
    "InsertMode": True,
    "FullScreen": False,  # True looks like "DOS Mode" from win98!
    "FontFamily": 54,
    "CursorSize": 75,  # pct of character size
    "ScreenBufferSize": (152, 256),
    "AutoPosition": False,
    "FontSize": (4, 5),
    "FaceName": "",
    "HistoryBufferSize": 32,
    "InputBufferSize": 0,
    "QuickEdit": True,
    "Font": 0,  # 0 should always be present, use win32console.GetNumberOfConsoleFonts() to find how many available
    "FillAttribute": 7,
    "PopupFillAttribute": 245,
    "WindowSize": (128, 32),
    "WindowOrigin": (0, 0),
    "FontWeight": 400,
    "HistoryNoDup": False,
    "NumberOfHistoryBuffers": 32,
    # ColorTable copied from a 'normal' console shortcut, with some obvious changes
    # These do not appear to be documented.  From experimentation, [0] is background, [7] is foreground text
    "ColorTable": (
        255,
        8388608,
        32768,
        8421376,
        128,
        8388736,
        32896,
        12582912,
        8421504,
        16711680,
        65280,
        16776960,
        255,
        16711935,
        65535,
        16777215,
    ),
}

ishdl = ish.QueryInterface(shell.IID_IShellLinkDataList)
ishdl.AddDataBlock(console_props)
ipf = ish.QueryInterface(pythoncom.IID_IPersistFile)
ipf.Save(linkname, 1)
os.startfile(linkname)

```


---

## com/win32comext/shell/demos/ITransferAdviseSink.py

```python
# ITransferAdviseSink implementation template

import pythoncom
from win32com.server.policy import DesignatedWrapPolicy
from win32com.shell import shell, shellcon

tsf_flags = []
TRANSFER_ADVISE_STATES = {}

for k, v in shellcon.__dict__.items():
    if k.startswith("TS_"):
        TRANSFER_ADVISE_STATES[v] = k
    elif k.startswith("TSF_"):
        tsf_flags.append((k, v))


def decode_flags(flags):
    if flags == 0:
        return "TSF_NORMAL"
    flag_txt = ""
    for k, v in tsf_flags:
        if flags & v:
            if flag_txt:
                flag_txt += "|" + k
            else:
                flag_txt = k
    return flag_txt


class TransferAdviseSink(DesignatedWrapPolicy):
    _com_interfaces_ = [shell.IID_ITransferAdviseSink]
    _public_methods_ = [
        "UpdateProgress",
        "UpdateTransferState",
        "ConfirmOverwrite",
        "ConfirmEncryptionLoss",
        "FileFailure",
        "SubStreamFailure",
        "PropertyFailure",
    ]

    def __init__(self):
        self._wrap_(self)

    def UpdateProgress(
        self,
        SizeCurrent,
        SizeTotal,
        FilesCurrent,
        FilesTotal,
        FoldersCurrent,
        FoldersTotal,
    ):
        print("UpdateProgress - processed so far:")
        print(f"\t {SizeCurrent} out of {SizeTotal} bytes")
        print(f"\t {FilesCurrent} out of {FilesTotal} files")
        print(f"\t {FoldersCurrent} out of {FoldersTotal} folders")

    def UpdateTransferState(self, State):
        print(
            "Current state: ",
            TRANSFER_ADVISE_STATES.get(State, "??? Unknown state %s ???" % State),
        )

    def ConfirmOverwrite(self, Source, DestParent, Name):
        print(
            "ConfirmOverwrite: ",
            Source.GetDisplayName(shellcon.SHGDN_FORPARSING),
            DestParent.GetDisplayName(shellcon.SHGDN_FORPARSING),
            Name,
        )

    def ConfirmEncryptionLoss(self, Source):
        print(
            "ConfirmEncryptionLoss:", Source.GetDisplayName(shellcon.SHGDN_FORPARSING)
        )

    def FileFailure(self, Item, ItemName, Error):
        print("FileFailure:", Item.GetDisplayName(shellcon.SHGDN_FORPARSING), ItemName)

    def SubStreamFailure(self, Item, StreamName, Error):
        print("SubStreamFailure:\n")

    def PropertyFailure(self, Item, key, Error):
        print("PropertyFailure:\n")


def CreateSink():
    return pythoncom.WrapObject(
        TransferAdviseSink(),
        shell.IID_ITransferAdviseSink,
        shell.IID_ITransferAdviseSink,
    )

```


---

## com/win32comext/shell/demos/IUniformResourceLocator.py

```python
import os

import pythoncom
import win32api
from win32com.shell import shell, shellcon


class InternetShortcut:
    def __init__(self):
        self._base = pythoncom.CoCreateInstance(
            shell.CLSID_InternetShortcut,
            None,
            pythoncom.CLSCTX_INPROC_SERVER,
            shell.IID_IUniformResourceLocator,
        )

    def load(self, filename):
        # Get an IPersist interface
        # which allows save/restore of object to/from files
        self._base.QueryInterface(pythoncom.IID_IPersistFile).Load(filename)

    def save(self, filename):
        self._base.QueryInterface(pythoncom.IID_IPersistFile).Save(filename, 1)

    def __getattr__(self, name):
        if name != "_base":
            return getattr(self._base, name)


temp_dir = win32api.GetTempPath()
linkname = win32api.GetTempFileName(temp_dir, "ish")[0]
print("Link:", linkname)
os.remove(linkname)
linkname += ".url"

ish = InternetShortcut()
ish.SetURL("https://github.com/mhammond/pywin32")
ish.save(linkname)

## IUniformResourceLocator also give access to IPropertySetStorage
pss = ish.QueryInterface(pythoncom.IID_IPropertySetStorage)
ps = pss.Open(shell.FMTID_InternetSite)
property_ids = [
    (k, v) for k, v in shellcon.__dict__.items() if k.startswith("PID_INTSITE_")
]
for pname, pval in property_ids:
    print(pname, ps.ReadMultiple((pval,))[0])

ps = pss.Open(shell.FMTID_Intshcut)
property_ids = [(k, v) for k, v in shellcon.__dict__.items() if k.startswith("PID_IS_")]
for pname, pval in property_ids:
    print(pname, ps.ReadMultiple((pval,))[0])

new_sh = InternetShortcut()
new_sh.load(linkname)
new_sh.InvokeCommand("Open")

```


---

## com/win32comext/shell/demos/browse_for_folder.py

```python
# A couple of samples using SHBrowseForFolder

import os

import win32gui
from win32com.shell import shell, shellcon


# A callback procedure - called by SHBrowseForFolder
def BrowseCallbackProc(hwnd, msg, lp, data):
    if msg == shellcon.BFFM_INITIALIZED:
        win32gui.SendMessage(hwnd, shellcon.BFFM_SETSELECTION, 1, data)
    elif msg == shellcon.BFFM_SELCHANGED:
        # Set the status text of the
        # For this message, 'lp' is the address of the PIDL.
        pidl = shell.AddressAsPIDL(lp)
        try:
            path = shell.SHGetPathFromIDList(pidl)
            win32gui.SendMessage(hwnd, shellcon.BFFM_SETSTATUSTEXT, 0, path)
        except shell.error:
            # No path for this PIDL
            pass


if __name__ == "__main__":
    # Demonstrate a dialog with the cwd selected as the default - this
    # must be done via a callback function.
    flags = shellcon.BIF_STATUSTEXT
    shell.SHBrowseForFolder(
        0,  # parent HWND
        None,  # root PIDL.
        "Default of %s" % os.getcwd(),  # title
        flags,  # flags
        BrowseCallbackProc,  # callback function
        os.getcwd(),  # 'data' param for the callback
    )
    # Browse from this directory down only.
    # Get the PIDL for the cwd.
    desktop = shell.SHGetDesktopFolder()
    cb, pidl, extra = desktop.ParseDisplayName(0, None, os.getcwd())
    shell.SHBrowseForFolder(
        0,  # parent HWND
        pidl,  # root PIDL.
        "From %s down only" % os.getcwd(),  # title
    )

```


---

## com/win32comext/shell/demos/create_link.py

```python
# link.py
# From a demo by Mark Hammond, corrupted by Mike Fletcher
# (and re-corrupted by Mark Hammond :-)
import os
from itertools import zip_longest

import pythoncom
from win32com.shell import shell


class PyShortcut:
    def __init__(self):
        self._base = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink,
            None,
            pythoncom.CLSCTX_INPROC_SERVER,
            shell.IID_IShellLink,
        )

    def load(self, filename):
        # Get an IPersist interface
        # which allows save/restore of object to/from files
        self._base.QueryInterface(pythoncom.IID_IPersistFile).Load(filename)

    def save(self, filename):
        self._base.QueryInterface(pythoncom.IID_IPersistFile).Save(filename, 0)

    def __getattr__(self, name):
        if name != "_base":
            return getattr(self._base, name)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(
            "Usage: %s LinkFile [path [, args[, description[, working_dir]]]]\n\nIf LinkFile does not exist, it will be created using the other args"
        )
        sys.exit(1)
    file = sys.argv[1]
    shortcut = PyShortcut()
    if os.path.exists(file):
        # load and dump info from file...
        shortcut.load(file)
        # now print data...
        print(
            "Shortcut in file %s to file:\n\t%s\nArguments:\n\t%s\nDescription:\n\t%s\nWorking Directory:\n\t%s\nItemIDs:\n\t<skipped>"
            % (
                file,
                shortcut.GetPath(shell.SLGP_SHORTPATH)[0],
                shortcut.GetArguments(),
                shortcut.GetDescription(),
                shortcut.GetWorkingDirectory(),
                # shortcut.GetIDList(),
            )
        )
    else:
        if len(sys.argv) < 3:
            print(
                "Link file does not exist\nYou must supply the path, args, description and working_dir as args"
            )
            sys.exit(1)
        # create the shortcut using rest of args...
        data = zip_longest(
            sys.argv[2:],
            ("SetPath", "SetArguments", "SetDescription", "SetWorkingDirectory"),
        )
        for value, function in data:
            if value and function:
                # call function on each non-null value
                getattr(shortcut, function)(value)
        shortcut.save(file)

```


---

## com/win32comext/shell/demos/dump_link.py

```python
# dump_link.py - dumps information about shell shortcuts
#
import glob
import os
import sys

import pythoncom
from win32com.shell import shell, shellcon
from win32com.storagecon import *


def DumpLink(fname):
    shellLink = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink,
    )
    persistFile = shellLink.QueryInterface(pythoncom.IID_IPersistFile)
    persistFile.Load(fname, STGM_READ)
    shellLink.Resolve(0, shell.SLR_ANY_MATCH | shell.SLR_NO_UI)
    fname, findData = shellLink.GetPath(0)
    print("Filename:", fname, ", UNC=", shellLink.GetPath(shell.SLGP_UNCPRIORITY)[0])
    print("Description:", shellLink.GetDescription())
    print("Working Directory:", shellLink.GetWorkingDirectory())
    print("Icon:", shellLink.GetIconLocation())


def FavDumper(nothing, path, names):
    # called by os.walk
    for name in names:
        print(name, end=" ")
        try:
            DumpLink(name)
        except pythoncom.com_error:
            print(" - not a link")


def DumpFavorites():
    favfold = str(shell.SHGetSpecialFolderPath(0, shellcon.CSIDL_FAVORITES))
    print("Your favourites are at", favfold)
    os.walk(favfold, FavDumper, None)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for fspec in sys.argv[1:]:
            files = glob.glob(fspec)
            if files:
                for file in files:
                    print(file)
                    DumpLink(file)
                    print()
            else:
                print("Can not find", fspec)
    else:
        print("Dumping your favorites folder!")
        DumpFavorites()

```


---

## com/win32comext/shell/demos/explorer_browser.py

```python
# A sample of using IExplorerBrowser interfaces...
# Currently doesn't quite work:
# * CPU sits at 100% while running.

import sys

import pythoncom
import win32api
import win32con
import win32gui
from win32com.server.util import unwrap, wrap
from win32com.shell import shell, shellcon

# event handler for the browser.
IExplorerBrowserEvents_Methods = """OnNavigationComplete OnNavigationFailed
                                    OnNavigationPending OnViewCreated""".split()


class EventHandler:
    _com_interfaces_ = [shell.IID_IExplorerBrowserEvents]
    _public_methods_ = IExplorerBrowserEvents_Methods

    def OnNavigationComplete(self, pidl):
        print("OnNavComplete", pidl)

    def OnNavigationFailed(self, pidl):
        print("OnNavigationFailed", pidl)

    def OnNavigationPending(self, pidl):
        print("OnNavigationPending", pidl)

    def OnViewCreated(self, view):
        print("OnViewCreated", view)
        # And if our demo view has been registered, it may well
        # be that view!
        try:
            pyview = unwrap(view)
            print("and look - it's a Python implemented view!", pyview)
        except ValueError:
            pass


class MainWindow:
    def __init__(self):
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
            win32con.WM_COMMAND: self.OnCommand,
            win32con.WM_SIZE: self.OnSize,
        }
        # Register the Window class.
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "test_explorer_browser"
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = win32gui.RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPEDWINDOW | win32con.WS_VISIBLE
        self.hwnd = win32gui.CreateWindow(
            classAtom,
            "Python IExplorerBrowser demo",
            style,
            0,
            0,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            hinst,
            None,
        )
        eb = pythoncom.CoCreateInstance(
            shellcon.CLSID_ExplorerBrowser,
            None,
            pythoncom.CLSCTX_ALL,
            shell.IID_IExplorerBrowser,
        )
        # as per MSDN docs, hook up events early
        self.event_cookie = eb.Advise(wrap(EventHandler()))

        eb.SetOptions(shellcon.EBO_SHOWFRAMES)
        rect = win32gui.GetClientRect(self.hwnd)
        # Set the flags such that the folders autoarrange and non web view is presented
        flags = (shellcon.FVM_LIST, shellcon.FWF_AUTOARRANGE | shellcon.FWF_NOWEBVIEW)
        eb.Initialize(self.hwnd, rect, (0, shellcon.FVM_DETAILS))
        if len(sys.argv) == 2:
            # If an arg was specified, ask the desktop parse it.
            # You can pass anything explorer accepts as its '/e' argument -
            # eg, "::{guid}\::{guid}" etc.
            # "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}" is "My Computer"
            pidl = shell.SHGetDesktopFolder().ParseDisplayName(0, None, sys.argv[1])[1]
        else:
            # And start browsing at the root of the namespace.
            pidl = []
        eb.BrowseToIDList(pidl, shellcon.SBSP_ABSOLUTE)
        # and for some reason the "Folder" view in the navigator pane doesn't
        # magically synchronize itself - so let's do that ourself.
        # Get the tree control.
        sp = eb.QueryInterface(pythoncom.IID_IServiceProvider)
        try:
            tree = sp.QueryService(
                shell.IID_INameSpaceTreeControl, shell.IID_INameSpaceTreeControl
            )
        except pythoncom.com_error as exc:
            # this should really only fail if no "nav" frame exists...
            print(
                "Strange - failed to get the tree control even though "
                "we asked for a EBO_SHOWFRAMES"
            )
            print(exc)
        else:
            # get the IShellItem for the selection.
            si = shell.SHCreateItemFromIDList(pidl, shell.IID_IShellItem)
            # set it to selected.
            tree.SetItemState(si, shellcon.NSTCIS_SELECTED, shellcon.NSTCIS_SELECTED)

        # eb.FillFromObject(None, shellcon.EBF_NODROPTARGET);
        # eb.SetEmptyText("No known folders yet...");
        self.eb = eb

    def OnCommand(self, hwnd, msg, wparam, lparam):
        pass

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        print("tearing down ExplorerBrowser...")
        self.eb.Unadvise(self.event_cookie)
        self.eb.Destroy()
        self.eb = None
        print("shutting down app...")
        win32gui.PostQuitMessage(0)

    def OnSize(self, hwnd, msg, wparam, lparam):
        x = win32api.LOWORD(lparam)
        y = win32api.HIWORD(lparam)
        self.eb.SetRect(None, (0, 0, x, y))


def main():
    w = MainWindow()
    win32gui.PumpMessages()


if __name__ == "__main__":
    main()

```


---

## com/win32comext/shell/demos/servers/column_provider.py

```python
# A sample shell column provider
# Mainly ported from MSDN article:
#  Using Shell Column Handlers for Detailed File Information,
#  Raymond Chen, Microsoft Corporation, February 2000
#
# To demonstrate:
# * Execute this script to register the namespace.
# * Open Windows Explorer
# * Right-click an explorer column header - select "More"
# * Locate column 'pyc size' and add it to the view.
# This handler is providing that column data.
import os
import stat

import commctrl
import pythoncom
from pywintypes import IID
from win32com.shell import shell, shellcon

IPersist_Methods = ["GetClassID"]
IColumnProvider_Methods = IPersist_Methods + [
    "Initialize",
    "GetColumnInfo",
    "GetItemData",
]


class ColumnProvider:
    _reg_progid_ = "Python.ShellExtension.ColumnProvider"
    _reg_desc_ = "Python Sample Shell Extension (Column Provider)"
    _reg_clsid_ = IID("{0F14101A-E05E-4070-BD54-83DFA58C3D68}")
    _com_interfaces_ = [
        pythoncom.IID_IPersist,
        shell.IID_IColumnProvider,
    ]
    _public_methods_ = IColumnProvider_Methods

    # IPersist
    def GetClassID(self):
        return self._reg_clsid_

    # IColumnProvider
    def Initialize(self, colInit):
        flags, reserved, name = colInit
        print("ColumnProvider initializing for file", name)

    def GetColumnInfo(self, index):
        # We used to support exactly 2 columns - 'pyc size' and 'pyo size'
        # pyo isn't a thing since Python 3.5: https://peps.python.org/pep-0488/
        if index == 0:
            # As per the MSDN sample, use our CLSID as the fmtid
            title = ".pyc size"
            description = "Size of compiled .pyc file"
            col_id = (self._reg_clsid_, index)  # fmtid  # pid
            col_info = (
                col_id,  # scid
                pythoncom.VT_I4,  # vt
                commctrl.LVCFMT_RIGHT,  # fmt
                20,  # cChars
                shellcon.SHCOLSTATE_TYPE_INT
                | shellcon.SHCOLSTATE_SECONDARYUI,  # csFlags
                title,
                description,
            )
            return col_info
        return None  # Indicate no more columns.

    def GetItemData(self, colid, colData):
        # colid[1] used to be the pid where 0==pyc or 1==pyo.
        # But pyo isn't a thing since Python 3.5: https://peps.python.org/pep-0488/
        flags, attr, reserved, ext, name = colData
        if ext.lower() not in {".py", ".pyw"}:
            return None
        check_file = os.path.splitext(name)[0] + ".pyc"
        try:
            return os.stat(check_file)[stat.ST_SIZE]
        except OSError:
            # No file
            return None


def DllRegisterServer():
    import winreg

    # Special ColumnProvider key
    key = winreg.CreateKey(
        winreg.HKEY_CLASSES_ROOT,
        "Folder\\ShellEx\\ColumnHandlers\\" + str(ColumnProvider._reg_clsid_),
    )
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, ColumnProvider._reg_desc_)
    print(ColumnProvider._reg_desc_, "registration complete.")


def DllUnregisterServer():
    import winreg

    try:
        key = winreg.DeleteKey(
            winreg.HKEY_CLASSES_ROOT,
            "Folder\\ShellEx\\ColumnHandlers\\" + str(ColumnProvider._reg_clsid_),
        )
    except OSError as details:
        import errno

        if details.errno != errno.ENOENT:
            raise
    print(ColumnProvider._reg_desc_, "unregistration complete.")


if __name__ == "__main__":
    from win32com.server import register

    register.UseCommandLine(
        ColumnProvider,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )

```


---

## com/win32comext/shell/demos/servers/context_menu.py

```python
# A sample context menu handler.
# Adds a 'Hello from Python' menu entry to .py files.  When clicked, a
# simple message box is displayed.
#
# To demonstrate:
# * Execute this script to register the context menu.
# * Open Windows Explorer, and browse to a directory with a .py file.
# * Right-Click on a .py file - locate and click on 'Hello from Python' on
#   the context menu.

import pythoncom
import win32con
import win32gui
from win32com.shell import shell, shellcon


class ShellExtension:
    _reg_progid_ = "Python.ShellExtension.ContextMenu"
    _reg_desc_ = "Python Sample Shell Extension (context menu)"
    _reg_clsid_ = "{CED0336C-C9EE-4a7f-8D7F-C660393C381F}"
    _com_interfaces_ = [shell.IID_IShellExtInit, shell.IID_IContextMenu]
    _public_methods_ = shellcon.IContextMenu_Methods + shellcon.IShellExtInit_Methods

    def Initialize(self, folder, dataobj, hkey):
        print("Init", folder, dataobj, hkey)
        self.dataobj = dataobj

    def QueryContextMenu(self, hMenu, indexMenu, idCmdFirst, idCmdLast, uFlags):
        print("QCM", hMenu, indexMenu, idCmdFirst, idCmdLast, uFlags)
        # Query the items clicked on
        format_etc = win32con.CF_HDROP, None, 1, -1, pythoncom.TYMED_HGLOBAL
        sm = self.dataobj.GetData(format_etc)
        num_files = shell.DragQueryFile(sm.data_handle, -1)
        if num_files > 1:
            msg = "&Hello from Python (with %d files selected)" % num_files
        else:
            fname = shell.DragQueryFile(sm.data_handle, 0)
            msg = "&Hello from Python (with '%s' selected)" % fname
        idCmd = idCmdFirst
        items = ["First Python content menu item"]
        if (
            uFlags & 0x000F
        ) == shellcon.CMF_NORMAL:  # Check == here, since CMF_NORMAL=0
            print("CMF_NORMAL...")
            items.append(msg)
        elif uFlags & shellcon.CMF_VERBSONLY:
            print("CMF_VERBSONLY...")
            items.append(msg + " - shortcut")
        elif uFlags & shellcon.CMF_EXPLORE:
            print("CMF_EXPLORE...")
            items.append(msg + " - normal file, right-click in Explorer")
        elif uFlags & shellcon.CMF_DEFAULTONLY:
            print("CMF_DEFAULTONLY...\r\n")
        else:
            print("** unknown flags", uFlags)
        win32gui.InsertMenu(
            hMenu, indexMenu, win32con.MF_SEPARATOR | win32con.MF_BYPOSITION, 0, None
        )
        indexMenu += 1
        for item in items:
            win32gui.InsertMenu(
                hMenu,
                indexMenu,
                win32con.MF_STRING | win32con.MF_BYPOSITION,
                idCmd,
                item,
            )
            indexMenu += 1
            idCmd += 1

        win32gui.InsertMenu(
            hMenu, indexMenu, win32con.MF_SEPARATOR | win32con.MF_BYPOSITION, 0, None
        )
        indexMenu += 1
        return idCmd - idCmdFirst  # Must return number of menu items we added.

    def InvokeCommand(self, ci):
        mask, hwnd, verb, params, dir, nShow, hotkey, hicon = ci
        win32gui.MessageBox(hwnd, "Hello", "Wow", win32con.MB_OK)

    def GetCommandString(self, cmd: int, typ):
        # If GetCommandString returns the same string for all items then
        # the shell seems to ignore all but one.  This is even true if the
        # status bar is turned off (and hence this string seems ignored).
        return f"Hello from Python ({cmd=})!!"


def DllRegisterServer():
    import winreg

    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "Python.File\\shellex")
    subkey = winreg.CreateKey(key, "ContextMenuHandlers")
    subkey2 = winreg.CreateKey(subkey, "PythonSample")
    winreg.SetValueEx(subkey2, None, 0, winreg.REG_SZ, ShellExtension._reg_clsid_)
    print(ShellExtension._reg_desc_, "registration complete.")


def DllUnregisterServer():
    import winreg

    try:
        key = winreg.DeleteKey(
            winreg.HKEY_CLASSES_ROOT,
            "Python.File\\shellex\\ContextMenuHandlers\\PythonSample",
        )
    except OSError as details:
        import errno

        if details.errno != errno.ENOENT:
            raise
    print(ShellExtension._reg_desc_, "unregistration complete.")


if __name__ == "__main__":
    from win32com.server import register

    register.UseCommandLine(
        ShellExtension,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )

```


---

## com/win32comext/shell/demos/servers/copy_hook.py

```python
# A sample shell copy hook.

# To demonstrate:
# * Execute this script to register the context menu.
# * Open Windows Explorer
# * Attempt to move or copy a directory.
# * Note our hook's dialog is displayed.

import pythoncom
import win32con
import win32gui
from win32com.shell import shell


# Our shell extension.
class ShellExtension:
    _reg_progid_ = "Python.ShellExtension.CopyHook"
    _reg_desc_ = "Python Sample Shell Extension (copy hook)"
    _reg_clsid_ = "{1845b6ba-2bbd-4197-b930-46d8651497c1}"
    _com_interfaces_ = [shell.IID_ICopyHook]
    _public_methods_ = ["CopyCallBack"]

    def CopyCallBack(self, hwnd, func, flags, srcName, srcAttr, destName, destAttr):
        # This function should return:
        # IDYES Allows the operation.
        # IDNO Prevents the operation on this folder but continues with any other operations that have been approved (for example, a batch copy operation).
        # IDCANCEL Prevents the current operation and cancels any pending operations.
        print("CopyCallBack", hwnd, func, flags, srcName, srcAttr, destName, destAttr)
        return win32gui.MessageBox(
            hwnd, "Allow operation?", "CopyHook", win32con.MB_YESNO
        )


def DllRegisterServer():
    import winreg

    key = winreg.CreateKey(
        winreg.HKEY_CLASSES_ROOT,
        "directory\\shellex\\CopyHookHandlers\\" + ShellExtension._reg_desc_,
    )
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, ShellExtension._reg_clsid_)
    key = winreg.CreateKey(
        winreg.HKEY_CLASSES_ROOT,
        "*\\shellex\\CopyHookHandlers\\" + ShellExtension._reg_desc_,
    )
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, ShellExtension._reg_clsid_)
    print(ShellExtension._reg_desc_, "registration complete.")


def DllUnregisterServer():
    import winreg

    try:
        key = winreg.DeleteKey(
            winreg.HKEY_CLASSES_ROOT,
            "directory\\shellex\\CopyHookHandlers\\" + ShellExtension._reg_desc_,
        )
    except OSError as details:
        import errno

        if details.errno != errno.ENOENT:
            raise
    try:
        key = winreg.DeleteKey(
            winreg.HKEY_CLASSES_ROOT,
            "*\\shellex\\CopyHookHandlers\\" + ShellExtension._reg_desc_,
        )
    except OSError as details:
        import errno

        if details.errno != errno.ENOENT:
            raise
    print(ShellExtension._reg_desc_, "unregistration complete.")


if __name__ == "__main__":
    from win32com.server import register

    register.UseCommandLine(
        ShellExtension,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )
#!/usr/bin/env python

```


---

## com/win32comext/shell/demos/servers/empty_volume_cache.py

```python
# A sample implementation of IEmptyVolumeCache - see
# https://learn.microsoft.com/en-ca/windows/win32/lwef/disk-cleanup for an overview.
#
# * Execute this script to register the handler
# * Start the "disk cleanup" tool - look for "pywin32 compiled files"
import os
import stat
import sys

import pythoncom
import win32gui
import winerror
from win32com.server.exception import COMException
from win32com.shell import shell, shellcon

# Our shell extension.
IEmptyVolumeCache_Methods = (
    "Initialize GetSpaceUsed Purge ShowProperties Deactivate".split()
)
IEmptyVolumeCache2_Methods = "InitializeEx".split()

ico = os.path.join(sys.prefix, "py.ico")
if not os.path.isfile(ico):
    ico = os.path.join(sys.prefix, "PC", "py.ico")
if not os.path.isfile(ico):
    ico = None
    print("Can't find python.ico - no icon will be installed")


class EmptyVolumeCache:
    _reg_progid_ = "Python.ShellExtension.EmptyVolumeCache"
    _reg_desc_ = "Python Sample Shell Extension (disk cleanup)"
    _reg_clsid_ = "{EADD0777-2968-4c72-A999-2BF5F756259C}"
    _reg_icon_ = ico
    _com_interfaces_ = [shell.IID_IEmptyVolumeCache, shell.IID_IEmptyVolumeCache2]
    _public_methods_ = IEmptyVolumeCache_Methods + IEmptyVolumeCache2_Methods

    def Initialize(self, hkey, volume, flags):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def InitializeEx(self, hkey, volume, key_name, flags):
        # Must return a tuple of:
        # (display_name, description, button_name, flags)
        print("InitializeEx called with", hkey, volume, key_name, flags)
        self.volume = volume
        if flags & shellcon.EVCF_SETTINGSMODE:
            print("We are being run on a schedule")
            # In this case, "because there is no opportunity for user
            # feedback, only those files that are extremely safe to clean up
            # should be touched. You should ignore the initialization
            # method's pcwszVolume parameter and clean unneeded files
            # regardless of what drive they are on."
            self.volume = None  # flag as 'any disk will do'
        elif flags & shellcon.EVCF_OUTOFDISKSPACE:
            # In this case, "the handler should be aggressive about deleting
            # files, even if it results in a performance loss. However, the
            # handler obviously should not delete files that would cause an
            # application to fail or the user to lose data."
            print("We are being run as we are out of disk-space")
        else:
            # This case is not documented - we are guessing :)
            print("We are being run because the user asked")

        # For the sake of demo etc, we tell the shell to only show us when
        # there are > 0 bytes available.  Our GetSpaceUsed will check the
        # volume, so will return 0 when we are on a different disk
        flags = shellcon.EVCF_DONTSHOWIFZERO | shellcon.EVCF_ENABLEBYDEFAULT

        return (
            "pywin32 compiled files",
            "Removes all .pyc files in the pywin32 directories",
            "click me!",
            flags,
        )

    def _GetDirectories(self):
        root_dir = os.path.abspath(os.path.dirname(os.path.dirname(win32gui.__file__)))
        if self.volume is not None and not root_dir.lower().startswith(
            self.volume.lower()
        ):
            return []
        return [
            os.path.join(root_dir, p)
            for p in ("win32", "win32com", "win32comext", "isapi")
        ]

    def _WalkCallback(self, arg, directory, files):
        # callback function for os.walk - no need to be member, but it's
        # close to the callers :)
        callback, total_list = arg
        for file in files:
            fqn = os.path.join(directory, file).lower()
            if file.endswith(".pyc"):
                # See below - total_list is None means delete files,
                # otherwise it is a list where the result is stored. It's a
                # list simply due to the way os.walk works - only [0] is
                # referenced
                if total_list is None:
                    print("Deleting file", fqn)
                    # Should do callback.PurgeProcess - left as an exercise :)
                    os.remove(fqn)
                else:
                    total_list[0] += os.stat(fqn)[stat.ST_SIZE]
                    # and callback to the tool
                    if callback:
                        # for the sake of seeing the progress bar do its thing,
                        # we take longer than we need to...
                        # ACK - for some bizarre reason this screws up the XP
                        # cleanup manager - clues welcome!! :)
                        # # print("Looking in", directory, ", but waiting a while...")
                        # # time.sleep(3)
                        # now do it
                        used = total_list[0]
                        callback.ScanProgress(used, 0, "Looking at " + fqn)

    def GetSpaceUsed(self, callback):
        total = [0]  # See _WalkCallback above
        try:
            for d in self._GetDirectories():
                os.walk(d, self._WalkCallback, (callback, total))
                print("After looking in", d, "we have", total[0], "bytes")
        except pythoncom.error as exc:
            # This will be raised by the callback when the user selects 'cancel'.
            if exc.hresult != winerror.E_ABORT:
                raise  # that's the documented error code!
            print("User cancelled the operation")
        return total[0]

    def Purge(self, amt_to_free, callback):
        print("Purging", amt_to_free, "bytes...")
        # we ignore amt_to_free - it is generally what we returned for
        # GetSpaceUsed
        try:
            for d in self._GetDirectories():
                os.walk(d, self._WalkCallback, (callback, None))
        except pythoncom.error as exc:
            # This will be raised by the callback when the user selects 'cancel'.
            if exc.hresult != winerror.E_ABORT:
                raise  # that's the documented error code!
            print("User cancelled the operation")

    def ShowProperties(self, hwnd):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def Deactivate(self):
        print("Deactivate called")
        return 0


def DllRegisterServer():
    # Also need to register specially in:
    # HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches
    # See link at top of file.
    import winreg

    kn = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\{}".format(
        EmptyVolumeCache._reg_desc_,
    )
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, kn)
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, EmptyVolumeCache._reg_clsid_)


def DllUnregisterServer():
    import winreg

    kn = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\{}".format(
        EmptyVolumeCache._reg_desc_,
    )
    try:
        key = winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, kn)
    except OSError as details:
        import errno

        if details.errno != errno.ENOENT:
            raise
    print(EmptyVolumeCache._reg_desc_, "unregistration complete.")


if __name__ == "__main__":
    from win32com.server import register

    register.UseCommandLine(
        EmptyVolumeCache,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )

```


---

## com/win32comext/shell/demos/servers/folder_view.py

```python
# This is a port of the Vista SDK "FolderView" sample, and associated
# notes at https://web.archive.org/web/20081225011615/http://shellrevealed.com/blogs/shellblog/archive/2007/03/15/Shell-Namespace-Extension_3A00_-Creating-and-Using-the-System-Folder-View-Object.aspx
# A key difference to shell_view.py is that this version uses the default
# IShellView provided by the shell (via SHCreateShellFolderView) rather
# than our own.
# XXX - sadly, it doesn't work quite like the original sample.  Oh well,
# another day...
import os
import pickle
import random
import struct
import winreg

import commctrl
import pythoncom
import win32api
import win32con
import win32gui
import winerror
from win32com.axcontrol import axcontrol  # IObjectWithSite
from win32com.propsys import propsys
from win32com.server.exception import COMException
from win32com.server.util import NewEnum as _NewEnum, wrap as _wrap
from win32com.shell import shell, shellcon

GUID = pythoncom.MakeIID

# If set, output spews to the win32traceutil collector...
debug = 0


# wrap a python object in a COM pointer
def wrap(ob, iid=None):
    return _wrap(ob, iid, useDispatcher=(debug > 0))


def NewEnum(seq, iid):
    return _NewEnum(seq, iid=iid, useDispatcher=(debug > 0))


# The sample makes heavy use of "string ids" (ie, integer IDs defined in .h
# files, loaded at runtime from a (presumably localized) DLL.  We cheat.
_sids = {}  # strings, indexed bystring_id,


def LoadString(sid):
    return _sids[sid]


# fn to create a unique string ID
_last_ids = 0


def _make_ids(s):
    global _last_ids
    _last_ids += 1
    _sids[_last_ids] = s
    return _last_ids


# These strings are what the user sees and would be localized.
# XXX - it's possible that the shell might persist these values, so
# this scheme wouldn't really be suitable in a real ap.
IDS_UNSPECIFIED = _make_ids("unspecified")
IDS_SMALL = _make_ids("small")
IDS_MEDIUM = _make_ids("medium")
IDS_LARGE = _make_ids("large")
IDS_CIRCLE = _make_ids("circle")
IDS_TRIANGLE = _make_ids("triangle")
IDS_RECTANGLE = _make_ids("rectangle")
IDS_POLYGON = _make_ids("polygon")
IDS_DISPLAY = _make_ids("Display")
IDS_DISPLAY_TT = _make_ids("Display the item.")
IDS_SETTINGS = _make_ids("Settings")
IDS_SETTING1 = _make_ids("Setting 1")
IDS_SETTING2 = _make_ids("Setting 2")
IDS_SETTING3 = _make_ids("Setting 3")
IDS_SETTINGS_TT = _make_ids("Modify settings.")
IDS_SETTING1_TT = _make_ids("Modify setting 1.")
IDS_SETTING2_TT = _make_ids("Modify setting 2.")
IDS_SETTING3_TT = _make_ids("Modify setting 3.")
IDS_LESSTHAN5 = _make_ids("Less Than 5")
IDS_5ORGREATER = _make_ids("Five or Greater")
del _make_ids, _last_ids

# Other misc resource stuff
IDI_ICON1 = 100
IDI_SETTINGS = 101

# The sample defines a number of "category ids".  Each one gets
# its own GUID.
CAT_GUID_NAME = GUID("{de094c9d-c65a-11dc-ba21-005056c00008}")
CAT_GUID_SIZE = GUID("{de094c9e-c65a-11dc-ba21-005056c00008}")
CAT_GUID_SIDES = GUID("{de094c9f-c65a-11dc-ba21-005056c00008}")
CAT_GUID_LEVEL = GUID("{de094ca0-c65a-11dc-ba21-005056c00008}")
# The next category guid is NOT based on a column (see
# ViewCategoryProvider::EnumCategories()...)
CAT_GUID_VALUE = "{de094ca1-c65a-11dc-ba21-005056c00008}"

GUID_Display = GUID("{4d6c2fdd-c689-11dc-ba21-005056c00008}")
GUID_Settings = GUID("{4d6c2fde-c689-11dc-ba21-005056c00008}")
GUID_Setting1 = GUID("{4d6c2fdf-c689-11dc-ba21-005056c00008}")
GUID_Setting2 = GUID("{4d6c2fe0-c689-11dc-ba21-005056c00008}")
GUID_Setting3 = GUID("{4d6c2fe1-c689-11dc-ba21-005056c00008}")

# Hrm - not sure what to do about the std keys.
# Probably need a simple parser for propkey.h
PKEY_ItemNameDisplay = ("{B725F130-47EF-101A-A5F1-02608C9EEBAC}", 10)
PKEY_PropList_PreviewDetails = ("{C9944A21-A406-48FE-8225-AEC7E24C211B}", 8)

# Not sure what the "3" here refers to - docs say PID_FIRST_USABLE (2) be
# used.  Presumably it is the 'propID' value in the .propdesc file!
# note that the following GUIDs are also references in the .propdesc file
PID_SOMETHING = 3
# These are our 'private' PKEYs
# Col 2, name="Sample.AreaSize"
PKEY_Sample_AreaSize = ("{d6f5e341-c65c-11dc-ba21-005056c00008}", PID_SOMETHING)
# Col 3, name="Sample.NumberOfSides"
PKEY_Sample_NumberOfSides = ("{d6f5e342-c65c-11dc-ba21-005056c00008}", PID_SOMETHING)
# Col 4, name="Sample.DirectoryLevel"
PKEY_Sample_DirectoryLevel = ("{d6f5e343-c65c-11dc-ba21-005056c00008}", PID_SOMETHING)


# We construct a PIDL from a pickle of a dict - turn it back into a
# dict (we should *never* be called with a PIDL that the last elt is not
# ours, so it is safe to assume we created it (assume->"ass" = "u" + "me" :)
def pidl_to_item(pidl):
    # Note that only the *last* elt in the PIDL is certainly ours,
    # but it contains everything we need encoded as a dict.
    return pickle.loads(pidl[-1])


# Start of msdn sample port...
# make_item_enum replaces the sample's entire EnumIDList.cpp :)
def make_item_enum(level, flags):
    pidls = []
    nums = """zero one two three four five size seven eight nine ten""".split()
    for i, name in enumerate(nums):
        size = random.randint(0, 255)
        sides = 1
        while sides in [1, 2]:
            sides = random.randint(0, 5)
        is_folder = (i % 2) != 0
        # check the flags say to include it.
        # (This seems strange; if you ask the same folder for, but appear
        skip = False
        if not (flags & shellcon.SHCONTF_STORAGE):
            if is_folder:
                skip = not (flags & shellcon.SHCONTF_FOLDERS)
            else:
                skip = not (flags & shellcon.SHCONTF_NONFOLDERS)
        if not skip:
            data = {
                "name": name,
                "size": size,
                "sides": sides,
                "level": level,
                "is_folder": is_folder,
            }
            pidls.append([pickle.dumps(data)])
    return NewEnum(pidls, shell.IID_IEnumIDList)


# start of Utils.cpp port
def DisplayItem(shell_item_array, hwnd_parent=0):
    # Get the first ShellItem and display its name
    if shell_item_array is None:
        msg = "You must select something!"
    else:
        si = shell_item_array.GetItemAt(0)
        name = si.GetDisplayName(shellcon.SIGDN_NORMALDISPLAY)
        msg = "%d items selected, first is %r" % (shell_item_array.GetCount(), name)
    win32gui.MessageBox(hwnd_parent, msg, "Hello", win32con.MB_OK)


# end of Utils.cpp port


# start of sample's FVCommands.cpp port
class Command:
    def __init__(self, guid, ids, ids_tt, idi, flags, callback, children):
        self.guid = guid
        self.ids = ids
        self.ids_tt = ids_tt
        self.idi = idi
        self.flags = flags
        self.callback = callback
        self.children = children
        assert not children or isinstance(children[0], Command)

    def tuple(self):
        return (
            self.guid,
            self.ids,
            self.ids_tt,
            self.idi,
            self.flags,
            self.callback,
            self.children,
        )


# command callbacks - called back directly by us - see ExplorerCommand.Invoke
def onDisplay(items, bindctx):
    DisplayItem(items)


def onSetting1(items, bindctx):
    win32gui.MessageBox(0, LoadString(IDS_SETTING1), "Hello", win32con.MB_OK)


def onSetting2(items, bindctx):
    win32gui.MessageBox(0, LoadString(IDS_SETTING2), "Hello", win32con.MB_OK)


def onSetting3(items, bindctx):
    win32gui.MessageBox(0, LoadString(IDS_SETTING3), "Hello", win32con.MB_OK)


taskSettings = [
    Command(
        GUID_Setting1, IDS_SETTING1, IDS_SETTING1_TT, IDI_SETTINGS, 0, onSetting1, None
    ),
    Command(
        GUID_Setting2, IDS_SETTING2, IDS_SETTING2_TT, IDI_SETTINGS, 0, onSetting2, None
    ),
    Command(
        GUID_Setting3, IDS_SETTING3, IDS_SETTING3_TT, IDI_SETTINGS, 0, onSetting3, None
    ),
]

tasks = [
    Command(GUID_Display, IDS_DISPLAY, IDS_DISPLAY_TT, IDI_ICON1, 0, onDisplay, None),
    Command(
        GUID_Settings,
        IDS_SETTINGS,
        IDS_SETTINGS_TT,
        IDI_SETTINGS,
        shellcon.ECF_HASSUBCOMMANDS,
        None,
        taskSettings,
    ),
]


class ExplorerCommandProvider:
    _com_interfaces_ = [shell.IID_IExplorerCommandProvider]
    _public_methods_ = shellcon.IExplorerCommandProvider_Methods

    def GetCommands(self, site, iid):
        items = [wrap(ExplorerCommand(t)) for t in tasks]
        return NewEnum(items, shell.IID_IEnumExplorerCommand)


class ExplorerCommand:
    _com_interfaces_ = [shell.IID_IExplorerCommand]
    _public_methods_ = shellcon.IExplorerCommand_Methods

    def __init__(self, cmd):
        self.cmd = cmd

    # The sample also appears to ignore the pidl args!?
    def GetTitle(self, pidl):
        return LoadString(self.cmd.ids)

    def GetToolTip(self, pidl):
        return LoadString(self.cmd.ids_tt)

    def GetIcon(self, pidl):
        # Return a string of the usual "dll,resource_id" format
        # todo - just return any ".ico that comes with python" + ",0" :)
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetState(self, shell_items, slow_ok):
        return shellcon.ECS_ENABLED

    def GetFlags(self):
        return self.cmd.flags

    def GetCanonicalName(self):
        return self.cmd.guid

    def Invoke(self, items, bind_ctx):
        # If no function defined - just return S_OK
        if self.cmd.callback:
            self.cmd.callback(items, bind_ctx)
        else:
            print("No callback for command ", LoadString(self.cmd.ids))

    def EnumSubCommands(self):
        if not self.cmd.children:
            return None
        items = [wrap(ExplorerCommand(c)) for c in self.cmd.children]
        return NewEnum(items, shell.IID_IEnumExplorerCommand)


# end of sample's FVCommands.cpp port


# start of sample's Category.cpp port
class FolderViewCategorizer:
    _com_interfaces_ = [shell.IID_ICategorizer]
    _public_methods_ = shellcon.ICategorizer_Methods

    description = None  # subclasses should set their own

    def __init__(self, shell_folder):
        self.sf = shell_folder

    #  Determines the relative order of two items in their item identifier lists.
    def CompareCategory(self, flags, cat1, cat2):
        return cat1 - cat2

    #  Retrieves the name of a categorizer, such as "Group By Device
    #  Type", that can be displayed in the user interface.
    def GetDescription(self, cch):
        return self.description

    # Retrieves information about a category, such as the default
    # display and the text to display in the user interface.
    def GetCategoryInfo(self, catid):
        # Note: this isn't always appropriate!  See overrides below
        return 0, str(catid)  # ????


class FolderViewCategorizer_Name(FolderViewCategorizer):
    description = "Alphabetical"

    def GetCategory(self, pidls):
        ret = []
        for pidl in pidls:
            val = self.sf.GetDetailsEx(pidl, PKEY_ItemNameDisplay)
            ret.append(val)
        return ret


class FolderViewCategorizer_Size(FolderViewCategorizer):
    description = "Group By Size"

    def GetCategory(self, pidls):
        ret = []
        for pidl in pidls:
            # Why don't we just get the size of the PIDL?
            val = self.sf.GetDetailsEx(pidl, PKEY_Sample_AreaSize)
            val = int(val)  # it probably came in a VT_BSTR variant
            if val < 255 // 3:
                cid = IDS_SMALL
            elif val < 2 * 255 // 3:
                cid = IDS_MEDIUM
            else:
                cid = IDS_LARGE
            ret.append(cid)
        return ret

    def GetCategoryInfo(self, catid):
        return 0, LoadString(catid)


class FolderViewCategorizer_Sides(FolderViewCategorizer):
    description = "Group By Sides"

    def GetCategory(self, pidls):
        ret = []
        for pidl in pidls:
            val = self.sf.GetDetailsEx(pidl, PKEY_ItemNameDisplay)
            if val == 0:
                cid = IDS_CIRCLE
            elif val == 3:
                cid = IDS_TRIANGLE
            elif val == 4:
                cid = IDS_RECTANGLE
            elif val == 5:
                cid = IDS_POLYGON
            else:
                cid = IDS_UNSPECIFIED
            ret.append(cid)
        return ret

    def GetCategoryInfo(self, catid):
        return 0, LoadString(catid)


class FolderViewCategorizer_Value(FolderViewCategorizer):
    description = "Group By Value"

    def GetCategory(self, pidls):
        ret = []
        for pidl in pidls:
            val = self.sf.GetDetailsEx(pidl, PKEY_ItemNameDisplay)
            if val in "one two three four".split():
                ret.append(IDS_LESSTHAN5)
            else:
                ret.append(IDS_5ORGREATER)
        return ret

    def GetCategoryInfo(self, catid):
        return 0, LoadString(catid)


class FolderViewCategorizer_Level(FolderViewCategorizer):
    description = "Group By Value"

    def GetCategory(self, pidls):
        return [
            self.sf.GetDetailsEx(pidl, PKEY_Sample_DirectoryLevel) for pidl in pidls
        ]


class ViewCategoryProvider:
    _com_interfaces_ = [shell.IID_ICategoryProvider]
    _public_methods_ = shellcon.ICategoryProvider_Methods

    def __init__(self, shell_folder):
        self.shell_folder = shell_folder

    def CanCategorizeOnSCID(self, pkey):
        return pkey in [
            PKEY_ItemNameDisplay,
            PKEY_Sample_AreaSize,
            PKEY_Sample_NumberOfSides,
            PKEY_Sample_DirectoryLevel,
        ]

    #  Creates a category object.
    def CreateCategory(self, guid, iid):
        if iid == shell.IID_ICategorizer:
            if guid == CAT_GUID_NAME:
                klass = FolderViewCategorizer_Name
            elif guid == CAT_GUID_SIDES:
                klass = FolderViewCategorizer_Sides
            elif guid == CAT_GUID_SIZE:
                klass = FolderViewCategorizer_Size
            elif guid == CAT_GUID_VALUE:
                klass = FolderViewCategorizer_Value
            elif guid == CAT_GUID_LEVEL:
                klass = FolderViewCategorizer_Level
            else:
                raise COMException(hresult=winerror.E_INVALIDARG)
            return wrap(klass(self.shell_folder))
        raise COMException(hresult=winerror.E_NOINTERFACE)

    #  Retrieves the enumerator for the categories.
    def EnumCategories(self):
        # These are additional categories beyond the columns
        seq = [CAT_GUID_VALUE]
        return NewEnum(seq, pythoncom.IID_IEnumGUID)

    #  Retrieves a globally unique identifier (GUID) that represents
    #  the categorizer to use for the specified Shell column.
    def GetCategoryForSCID(self, scid):
        if scid == PKEY_ItemNameDisplay:
            guid = CAT_GUID_NAME
        elif scid == PKEY_Sample_AreaSize:
            guid = CAT_GUID_SIZE
        elif scid == PKEY_Sample_NumberOfSides:
            guid = CAT_GUID_SIDES
        elif scid == PKEY_Sample_DirectoryLevel:
            guid = CAT_GUID_LEVEL
        elif scid == pythoncom.IID_NULL:
            # This can be called with a NULL
            # format ID. This will happen if you have a category,
            # not based on a column, that gets stored in the
            # property bag. When a return is made to this item,
            # it will call this function with a NULL format id.
            guid = CAT_GUID_VALUE
        else:
            raise COMException(hresult=winerror.E_INVALIDARG)
        return guid

    #  Retrieves the name of the specified category. This is where
    #  additional categories that appear under the column
    #  related categories in the UI, get their display names.
    def GetCategoryName(self, guid, cch):
        if guid == CAT_GUID_VALUE:
            return "Value"
        raise COMException(hresult=winerror.E_FAIL)

    #  Enables the folder to override the default grouping.
    def GetDefaultCategory(self):
        return CAT_GUID_LEVEL, (pythoncom.IID_NULL, 0)


# end of sample's Category.cpp port

# start of sample's ContextMenu.cpp port
MENUVERB_DISPLAY = 0

folderViewImplContextMenuIDs = [
    (
        "display",
        MENUVERB_DISPLAY,
        0,
    ),
]


class ContextMenu:
    _reg_progid_ = "Python.ShellFolderSample.ContextMenu"
    _reg_desc_ = "Python FolderView Context Menu"
    _reg_clsid_ = "{fed40039-021f-4011-87c5-6188b9979764}"
    _com_interfaces_ = [
        shell.IID_IShellExtInit,
        shell.IID_IContextMenu,
        axcontrol.IID_IObjectWithSite,
    ]
    _public_methods_ = (
        shellcon.IContextMenu_Methods
        + shellcon.IShellExtInit_Methods
        + ["GetSite", "SetSite"]
    )
    _context_menu_type_ = "PythonFolderViewSampleType"

    def __init__(self):
        self.site = None
        self.dataobj = None

    def Initialize(self, folder, dataobj, hkey):
        self.dataobj = dataobj

    def QueryContextMenu(self, hMenu, indexMenu, idCmdFirst, idCmdLast, uFlags):
        s = LoadString(IDS_DISPLAY)
        win32gui.InsertMenu(
            hMenu, indexMenu, win32con.MF_BYPOSITION, idCmdFirst + MENUVERB_DISPLAY, s
        )
        indexMenu += 1
        # other verbs could go here...

        # indicate that we added one verb.
        return 1

    def InvokeCommand(self, ci):
        mask, hwnd, verb, params, dir, nShow, hotkey, hicon = ci
        # this seems very convoluted, but it's what the sample does :)
        for verb_name, verb_id, flag in folderViewImplContextMenuIDs:
            if isinstance(verb, int):
                matches = verb == verb_id
            else:
                matches = verb == verb_name
            if matches:
                break
        else:
            raise AssertionError(ci, "failed to find our ID")
        if verb_id == MENUVERB_DISPLAY:
            sia = shell.SHCreateShellItemArrayFromDataObject(self.dataobj)
            DisplayItem(hwnd, sia)
        else:
            raise AssertionError(ci, "Got some verb we weren't expecting?")

    def GetCommandString(self, cmd, typ):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def SetSite(self, site):
        self.site = site

    def GetSite(self, iid):
        return self.site


# end of sample's ContextMenu.cpp port


# start of sample's ShellFolder.cpp port
class ShellFolder:
    _com_interfaces_ = [
        shell.IID_IBrowserFrameOptions,
        pythoncom.IID_IPersist,
        shell.IID_IPersistFolder,
        shell.IID_IPersistFolder2,
        shell.IID_IShellFolder,
        shell.IID_IShellFolder2,
    ]

    _public_methods_ = (
        shellcon.IBrowserFrame_Methods
        + shellcon.IPersistFolder2_Methods
        + shellcon.IShellFolder2_Methods
    )

    _reg_progid_ = "Python.ShellFolderSample.Folder2"
    _reg_desc_ = "Python FolderView sample"
    _reg_clsid_ = "{bb8c24ad-6aaa-4cec-ac5e-c429d5f57627}"

    max_levels = 5

    def __init__(self, level=0):
        self.current_level = level
        self.pidl = None  # set when Initialize is called

    def ParseDisplayName(self, hwnd, reserved, displayName, attr):
        # print("ParseDisplayName", displayName)
        raise COMException(hresult=winerror.E_NOTIMPL)

    def EnumObjects(self, hwndOwner, flags):
        if self.current_level >= self.max_levels:
            return None
        return make_item_enum(self.current_level + 1, flags)

    def BindToObject(self, pidl, bc, iid):
        tail = pidl_to_item(pidl)
        # assert tail['is_folder'], "BindToObject should only be called on folders?"
        # *sob*
        # No point creating object just to have QI fail.
        if iid not in ShellFolder._com_interfaces_:
            raise COMException(hresult=winerror.E_NOTIMPL)
        child = ShellFolder(self.current_level + 1)
        # hrmph - not sure what multiple PIDLs here mean?
        #        assert len(pidl)==1, pidl # expecting just relative child PIDL
        child.Initialize(self.pidl + pidl)
        return wrap(child, iid)

    def BindToStorage(self, pidl, bc, iid):
        return self.BindToObject(pidl, bc, iid)

    def CompareIDs(self, param, id1, id2):
        return 0  # XXX - todo - implement this!

    def CreateViewObject(self, hwnd, iid):
        if iid == shell.IID_IShellView:
            com_folder = wrap(self)
            return shell.SHCreateShellFolderView(com_folder)
        elif iid == shell.IID_ICategoryProvider:
            return wrap(ViewCategoryProvider(self))
        elif iid == shell.IID_IContextMenu:
            ws = wrap(self)
            dcm = (hwnd, None, self.pidl, ws, None)
            return shell.SHCreateDefaultContextMenu(dcm, iid)
        elif iid == shell.IID_IExplorerCommandProvider:
            return wrap(ExplorerCommandProvider())
        else:
            raise COMException(hresult=winerror.E_NOINTERFACE)

    def GetAttributesOf(self, pidls, attrFlags):
        assert len(pidls) == 1, "sample only expects 1 too!"
        assert len(pidls[0]) == 1, "expect relative pidls!"
        item = pidl_to_item(pidls[0])
        flags = 0
        if item["is_folder"]:
            flags |= shellcon.SFGAO_FOLDER
        if item["level"] < self.max_levels:
            flags |= shellcon.SFGAO_HASSUBFOLDER
        return flags

    #  Retrieves an OLE interface that can be used to carry out
    #  actions on the specified file objects or folders.
    def GetUIObjectOf(self, hwndOwner, pidls, iid, inout):
        assert len(pidls) == 1, "oops - aren't expecting more than one!"
        assert len(pidls[0]) == 1, "assuming relative pidls!"
        item = pidl_to_item(pidls[0])
        if iid == shell.IID_IContextMenu:
            ws = wrap(self)
            dcm = (hwndOwner, None, self.pidl, ws, pidls)
            return shell.SHCreateDefaultContextMenu(dcm, iid)
        elif iid == shell.IID_IExtractIconW:
            dxi = shell.SHCreateDefaultExtractIcon()
            # dxi is IDefaultExtractIconInit
            if item["is_folder"]:
                dxi.SetNormalIcon("shell32.dll", 4)
            else:
                dxi.SetNormalIcon("shell32.dll", 1)
            # just return the dxi - let Python QI for IID_IExtractIconW
            return dxi

        elif iid == pythoncom.IID_IDataObject:
            return shell.SHCreateDataObject(self.pidl, pidls, None, iid)

        elif iid == shell.IID_IQueryAssociations:
            elts = []
            if item["is_folder"]:
                elts.append((shellcon.ASSOCCLASS_FOLDER, None, None))
            elts.append(
                (shellcon.ASSOCCLASS_PROGID_STR, None, ContextMenu._context_menu_type_)
            )
            return shell.AssocCreateForClasses(elts, iid)

        raise COMException(hresult=winerror.E_NOINTERFACE)

    #  Retrieves the display name for the specified file object or subfolder.
    def GetDisplayNameOf(self, pidl, flags):
        item = pidl_to_item(pidl)
        if flags & shellcon.SHGDN_FORPARSING:
            if flags & shellcon.SHGDN_INFOLDER:
                return item["name"]
            else:
                if flags & shellcon.SHGDN_FORADDRESSBAR:
                    sigdn = shellcon.SIGDN_DESKTOPABSOLUTEEDITING
                else:
                    sigdn = shellcon.SIGDN_DESKTOPABSOLUTEPARSING
                parent = shell.SHGetNameFromIDList(self.pidl, sigdn)
                return parent + "\\" + item["name"]
        else:
            return item["name"]

    def SetNameOf(self, hwndOwner, pidl, new_name, flags):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetClassID(self):
        return self._reg_clsid_

    #  IPersistFolder method
    def Initialize(self, pidl):
        self.pidl = pidl

    #  IShellFolder2 methods
    def EnumSearches(self):
        raise COMException(hresult=winerror.E_NOINTERFACE)

    #  Retrieves the default sorting and display columns.
    def GetDefaultColumn(self, dwres):
        # result is (sort, display)
        return 0, 0

    #  Retrieves the default state for a specified column.
    def GetDefaultColumnState(self, iCol):
        if iCol < 3:
            return shellcon.SHCOLSTATE_ONBYDEFAULT | shellcon.SHCOLSTATE_TYPE_STR
        raise COMException(hresult=winerror.E_INVALIDARG)

    #  Requests the GUID of the default search object for the folder.
    def GetDefaultSearchGUID(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    #  Helper function for getting the display name for a column.
    def _GetColumnDisplayName(self, pidl, pkey):
        item = pidl_to_item(pidl)
        is_folder = item["is_folder"]
        if pkey == PKEY_ItemNameDisplay:
            val = item["name"]
        elif pkey == PKEY_Sample_AreaSize and not is_folder:
            val = "%d Sq. Ft." % item["size"]
        elif pkey == PKEY_Sample_NumberOfSides and not is_folder:
            val = str(item["sides"])  # not sure why str()
        elif pkey == PKEY_Sample_DirectoryLevel:
            val = str(item["level"])
        else:
            val = ""
        return val

    #  Retrieves detailed information, identified by a
    #  property set ID (FMTID) and property ID (PID),
    #  on an item in a Shell folder.
    def GetDetailsEx(self, pidl, pkey):
        item = pidl_to_item(pidl)
        is_folder = item["is_folder"]
        if not is_folder and pkey == PKEY_PropList_PreviewDetails:
            return "prop:Sample.AreaSize;Sample.NumberOfSides;Sample.DirectoryLevel"
        return self._GetColumnDisplayName(pidl, pkey)

    #  Retrieves detailed information, identified by a
    #  column index, on an item in a Shell folder.
    def GetDetailsOf(self, pidl, iCol):
        key = self.MapColumnToSCID(iCol)
        if pidl is None:
            data = [
                (commctrl.LVCFMT_LEFT, "Name"),
                (commctrl.LVCFMT_CENTER, "Size"),
                (commctrl.LVCFMT_CENTER, "Sides"),
                (commctrl.LVCFMT_CENTER, "Level"),
            ]
            if iCol >= len(data):
                raise COMException(hresult=winerror.E_FAIL)
            fmt, val = data[iCol]
        else:
            fmt = 0  # ?
            val = self._GetColumnDisplayName(pidl, key)
        cxChar = 24
        return fmt, cxChar, val

    #  Converts a column name to the appropriate
    #  property set ID (FMTID) and property ID (PID).
    def MapColumnToSCID(self, iCol):
        data = [
            PKEY_ItemNameDisplay,
            PKEY_Sample_AreaSize,
            PKEY_Sample_NumberOfSides,
            PKEY_Sample_DirectoryLevel,
        ]
        if iCol >= len(data):
            raise COMException(hresult=winerror.E_FAIL)
        return data[iCol]

    #  IPersistFolder2 methods
    #  Retrieves the PIDLIST_ABSOLUTE for the folder object.
    def GetCurFolder(self):
        # The docs say this is OK, but I suspect it's a problem in this case :)
        # assert self.pidl, "haven't been initialized?"
        return self.pidl


# end of sample's ShellFolder.cpp port


def get_schema_fname():
    me = win32api.GetFullPathName(__file__)
    sc = os.path.splitext(me)[0] + ".propdesc"
    assert os.path.isfile(sc), sc
    return sc


def DllRegisterServer():
    key = winreg.CreateKey(
        winreg.HKEY_LOCAL_MACHINE,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\"
        "Explorer\\Desktop\\Namespace\\" + ShellFolder._reg_clsid_,
    )
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, ShellFolder._reg_desc_)
    # And special shell keys under our CLSID
    key = winreg.CreateKey(
        winreg.HKEY_CLASSES_ROOT, "CLSID\\" + ShellFolder._reg_clsid_ + "\\ShellFolder"
    )
    # 'Attributes' is an int stored as a binary! use struct
    attr = (
        shellcon.SFGAO_FOLDER | shellcon.SFGAO_HASSUBFOLDER | shellcon.SFGAO_BROWSABLE
    )

    s = struct.pack("i", attr)
    winreg.SetValueEx(key, "Attributes", 0, winreg.REG_BINARY, s)
    # register the context menu handler under the FolderViewSampleType type.
    keypath = "{}\\shellex\\ContextMenuHandlers\\{}".format(
        ContextMenu._context_menu_type_,
        ContextMenu._reg_desc_,
    )
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, keypath)
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, ContextMenu._reg_clsid_)
    propsys.PSRegisterPropertySchema(get_schema_fname())
    print(ShellFolder._reg_desc_, "registration complete.")


def DllUnregisterServer():
    paths = [
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\Namespace\\"
        + ShellFolder._reg_clsid_,
        "{}\\shellex\\ContextMenuHandlers\\{}".format(
            ContextMenu._context_menu_type_, ContextMenu._reg_desc_
        ),
    ]
    for path in paths:
        try:
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, path)
        except OSError as details:
            import errno

            if details.errno != errno.ENOENT:
                print(f"FAILED to remove {path}: {details}")

    propsys.PSUnregisterPropertySchema(get_schema_fname())
    print(ShellFolder._reg_desc_, "unregistration complete.")


if __name__ == "__main__":
    from win32com.server import register

    register.UseCommandLine(
        ShellFolder,
        ContextMenu,
        debug=debug,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )

```


---

## com/win32comext/shell/demos/servers/icon_handler.py

```python
# A sample icon handler.  Sets the icon for Python files to a random
# ICO file.  ICO files are found in the Python directory - generally there will
# be 3 icons found.
#
# To demonstrate:
# * Execute this script to register the context menu.
# * Open Windows Explorer, and browse to a directory with a .py file.
# * Note the pretty, random selection of icons!
# Use glob to locate ico files, and random.choice to pick one.
import glob
import os
import random
import sys

import pythoncom
import winerror
from win32com.shell import shell

ico_files = glob.glob(os.path.join(sys.prefix, "*.ico"))
if not ico_files:
    ico_files = glob.glob(os.path.join(sys.prefix, "PC", "*.ico"))
if not ico_files:
    print("WARNING: Can't find any icon files")

# Our shell extension.
IExtractIcon_Methods = "Extract GetIconLocation".split()
IPersistFile_Methods = "IsDirty Load Save SaveCompleted GetCurFile".split()


class ShellExtension:
    _reg_progid_ = "Python.ShellExtension.IconHandler"
    _reg_desc_ = "Python Sample Shell Extension (icon handler)"
    _reg_clsid_ = "{a97e32d7-3b78-448c-b341-418120ea9227}"
    _com_interfaces_ = [shell.IID_IExtractIcon, pythoncom.IID_IPersistFile]
    _public_methods_ = IExtractIcon_Methods + IPersistFile_Methods

    def Load(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def GetIconLocation(self, flags):
        # note - returning a single int will set the HRESULT (eg, S_FALSE,
        # E_PENDING - see MS docs for details.
        return random.choice(ico_files), 0, 0

    def Extract(self, fname, index, size):
        return winerror.S_FALSE


def DllRegisterServer():
    import winreg

    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "Python.File\\shellex")
    subkey = winreg.CreateKey(key, "IconHandler")
    winreg.SetValueEx(subkey, None, 0, winreg.REG_SZ, ShellExtension._reg_clsid_)
    print(ShellExtension._reg_desc_, "registration complete.")


def DllUnregisterServer():
    import winreg

    try:
        key = winreg.DeleteKey(
            winreg.HKEY_CLASSES_ROOT, "Python.File\\shellex\\IconHandler"
        )
    except OSError as details:
        import errno

        if details.errno != errno.ENOENT:
            raise
    print(ShellExtension._reg_desc_, "unregistration complete.")


if __name__ == "__main__":
    from win32com.server import register

    register.UseCommandLine(
        ShellExtension,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )

```


---

## com/win32comext/shell/demos/servers/shell_view.py

```python
# A sample shell namespace view

# To demonstrate:
# * Execute this script to register the namespace.
# * Open Windows Explorer, and locate the new "Python Path Shell Browser"
#   folder off "My Computer"
# * Browse this tree - .py files are shown expandable, with classes and
#   methods selectable.  Selecting a Python file, or a class/method, will
#   display the file using Scintilla.
# Known problems:
# * Classes and methods don't have icons - this is a demo, so we keep it small
#   See icon_handler.py for examples of how to work with icons.
#
#
# Notes on PIDLs
# PIDLS are complicated, but fairly well documented in MSDN.  If you need to
# do much with these shell extensions, you must understand their concept.
# Here is a short-course, as it applies to this sample:
# A PIDL identifies an item, much in the same way that a filename does
# (however, the shell is not limited to displaying "files").
# An "ItemID" is a single string, each being an item in the hierarchy.
# A "PIDL" is a list of these strings.
# All shell etc functions work with PIDLs, so even in the case where
# an ItemID is conceptually used, a 1-item list is always used.
# Conceptually, think of:
#    pidl = pathname.split("\\") # pidl is a list of "parent" items.
#    # each item is a string 'item id', but these are ever used directly
# As there is no concept of passing a single item, to open a file using only
# a relative filename, conceptually you would say:
#   open_file([filename]) # Pass a single-itemed relative "PIDL"
# and continuing the analogy, a "listdir" type function would return a list
# of single-itemed lists - each list containing the relative PIDL of the child.
#
# Each PIDL entry is a binary string, and may contain any character.  For
# PIDLs not created by you, they can not be interpreted - they are just
# blobs.  PIDLs created by you (ie, children of your IShellFolder) can
# store and interpret the string however makes most sense for your application.
# (but within PIDL rules - they must be persistable, etc)
# There is no reason that pickled strings, for example, couldn't be used
# as an EntryID.
# This application takes a simple approach - each PIDL is a string of form
# "directory\0directory_name", "file\0file_name" or
# "object\0file_name\0class_name[.method_name"
# The first string in each example is literal (ie, the word 'directory',
# 'file' or 'object', and every other string is variable.  We use '\0' as
# a field sep just 'cos we can (and 'cos it can't possibly conflict with the
# string content)

import os
import pyclbr
import sys

import commctrl
import pythoncom
import win32api
import win32con
import win32gui
import win32gui_struct
import winerror
from pywin.scintilla import scintillacon
from win32com.server.exception import COMException
from win32com.server.util import NewEnum, wrap
from win32com.shell import shell, shellcon
from win32com.util import IIDToInterfaceName

# Set this to 1 to cause debug version to be registered and used.  A debug
# version will spew output to win32traceutil.
debug = 0
if debug:
    import win32traceutil

# markh is toying with an implementation that allows auto reload of a module
# if this attribute exists.
com_auto_reload = True


# Helper function to get a system IShellFolder interface, and the PIDL within
# that folder for an existing file/directory.
def GetFolderAndPIDLForPath(filename):
    desktop = shell.SHGetDesktopFolder()
    info = desktop.ParseDisplayName(0, None, os.path.abspath(filename))
    cchEaten, pidl, attr = info
    # We must walk the ID list, looking for one child at a time.
    folder = desktop
    while len(pidl) > 1:
        this = pidl.pop(0)
        folder = folder.BindToObject([this], None, shell.IID_IShellFolder)
    # We are left with the pidl for the specific item.  Leave it as
    # a list, so it remains a valid PIDL.
    return folder, pidl


# A cache of pyclbr module objects, so we only parse a given filename once.
clbr_modules = {}  # Indexed by path, item is dict as returned from pyclbr


def get_clbr_for_file(path):
    try:
        objects = clbr_modules[path]
    except KeyError:
        dir, filename = os.path.split(path)
        base, ext = os.path.splitext(filename)
        objects = pyclbr.readmodule_ex(base, [dir])
        clbr_modules[path] = objects
    return objects


# Our COM interfaces.


# Base class for a shell folder.
# All child classes use a simple PIDL of the form:
#  "object_type\0object_name[\0extra ...]"
class ShellFolderBase:
    _com_interfaces_ = [
        shell.IID_IBrowserFrameOptions,
        pythoncom.IID_IPersist,
        shell.IID_IPersistFolder,
        shell.IID_IShellFolder,
    ]

    _public_methods_ = (
        shellcon.IBrowserFrame_Methods
        + shellcon.IPersistFolder_Methods
        + shellcon.IShellFolder_Methods
    )

    def GetFrameOptions(self, mask):
        # print("GetFrameOptions", self, mask)
        return 0

    def ParseDisplayName(self, hwnd, reserved, displayName, attr):
        print("ParseDisplayName", displayName)
        # return cchEaten, pidl, attr

    def BindToStorage(self, pidl, bc, iid):
        print("BTS", iid, IIDToInterfaceName(iid))

    def BindToObject(self, pidl, bc, iid):
        # We may be passed a set of relative PIDLs here - ie
        # [pidl_of_dir, pidl_of_child_dir, pidl_of_file, pidl_of_function]
        # But each of our PIDLs keeps the fully qualified name anyway - so
        # just jump directly to the last.
        final_pidl = pidl[-1]
        typ, extra = final_pidl.split("\0", 1)
        if typ == "directory":
            klass = ShellFolderDirectory
        elif typ == "file":
            klass = ShellFolderFile
        elif typ == "object":
            klass = ShellFolderObject
        else:
            raise RuntimeError(f"What is {typ!r}")
        ret = wrap(klass(extra), iid, useDispatcher=(debug > 0))
        return ret


# A ShellFolder for an object with CHILDREN on the file system
# Note that this means our "File" folder is *not* a 'FileSystem' folder,
# as it's children (functions and classes) are not on the file system.
#
class ShellFolderFileSystem(ShellFolderBase):
    def _GetFolderAndPIDLForPIDL(self, my_idl):
        typ, name = my_idl[0].split("\0")
        return GetFolderAndPIDLForPath(name)

    # Interface methods
    def CompareIDs(self, param, id1, id2):
        if id1 < id2:
            return -1
        if id1 == id2:
            return 0
        return 1

    def GetUIObjectOf(self, hwndOwner, pidls, iid, inout):
        # delegate to the shell.
        assert len(pidls) == 1, "oops - aren't expecting more than one!"
        pidl = pidls[0]
        folder, child_pidl = self._GetFolderAndPIDLForPIDL(pidl)
        try:
            inout, ret = folder.GetUIObjectOf(hwndOwner, [child_pidl], iid, inout, iid)
        except pythoncom.com_error as exc:
            raise COMException(hresult=exc.hresult)
        return inout, ret
        # return object of IID

    def GetDisplayNameOf(self, pidl, flags):
        # delegate to the shell.
        folder, child_pidl = self._GetFolderAndPIDLForPIDL(pidl)
        ret = folder.GetDisplayNameOf(child_pidl, flags)
        return ret

    def GetAttributesOf(self, pidls, attrFlags):
        ret_flags = -1
        for pidl in pidls:
            pidl = pidl[0]  # ??
            typ, name = pidl.split("\0")
            flags = shellcon.SHGFI_ATTRIBUTES
            rc, info = shell.SHGetFileInfo(name, 0, flags)
            hIcon, iIcon, dwAttr, name, typeName = info
            # All our items, even files, have sub-items
            extras = (
                shellcon.SFGAO_HASSUBFOLDER
                | shellcon.SFGAO_FOLDER
                | shellcon.SFGAO_FILESYSANCESTOR
                | shellcon.SFGAO_BROWSABLE
            )
            ret_flags &= dwAttr | extras
        return ret_flags


class ShellFolderDirectory(ShellFolderFileSystem):
    def __init__(self, path):
        self.path = os.path.abspath(path)

    def CreateViewObject(self, hwnd, iid):
        # delegate to the shell.
        folder, child_pidl = GetFolderAndPIDLForPath(self.path)
        return folder.CreateViewObject(hwnd, iid)

    def EnumObjects(self, hwndOwner, flags):
        pidls = []
        for fname in os.listdir(self.path):
            fqn = os.path.join(self.path, fname)
            if os.path.isdir(fqn):
                type_name = "directory"
                type_class = ShellFolderDirectory
            else:
                base, ext = os.path.splitext(fname)
                if ext in [".py", ".pyw"]:
                    type_class = ShellFolderFile
                    type_name = "file"
                else:
                    type_class = None
            if type_class is not None:
                pidls.append([type_name + "\0" + fqn])
        return NewEnum(pidls, iid=shell.IID_IEnumIDList, useDispatcher=(debug > 0))

    def GetDisplayNameOf(self, pidl, flags):
        final_pidl = pidl[-1]
        full_fname = final_pidl.split("\0")[-1]
        return os.path.split(full_fname)[-1]

    def GetAttributesOf(self, pidls, attrFlags):
        return (
            shellcon.SFGAO_HASSUBFOLDER
            | shellcon.SFGAO_FOLDER
            | shellcon.SFGAO_FILESYSANCESTOR
            | shellcon.SFGAO_BROWSABLE
        )


# As per comments above, even though this manages a file, it is *not* a
# ShellFolderFileSystem, as the children are not on the file system.
class ShellFolderFile(ShellFolderBase):
    def __init__(self, path):
        self.path = os.path.abspath(path)

    def EnumObjects(self, hwndOwner, flags):
        objects = get_clbr_for_file(self.path)
        pidls = []
        for name in objects:
            pidls.append(["object\0" + self.path + "\0" + name])
        return NewEnum(pidls, iid=shell.IID_IEnumIDList, useDispatcher=(debug > 0))

    def GetAttributesOf(self, pidls, attrFlags):
        ret_flags = -1
        for pidl in pidls:
            assert len(pidl) == 1, "Expecting relative pidls"
            pidl = pidl[0]
            typ, filename, obname = pidl.split("\0")
            obs = get_clbr_for_file(filename)
            ob = obs[obname]
            flags = (
                shellcon.SFGAO_BROWSABLE
                | shellcon.SFGAO_FOLDER
                | shellcon.SFGAO_FILESYSANCESTOR
            )
            if hasattr(ob, "methods"):
                flags |= shellcon.SFGAO_HASSUBFOLDER
            ret_flags &= flags
        return ret_flags

    def GetDisplayNameOf(self, pidl, flags):
        assert len(pidl) == 1, "Expecting relative PIDL"
        typ, fname, obname = pidl[0].split("\0")
        fqname = os.path.splitext(fname)[0] + "." + obname
        if flags & shellcon.SHGDN_INFOLDER:
            ret = obname
        else:  # SHGDN_NORMAL is the default
            ret = fqname
        # No need to look at the SHGDN_FOR* modifiers.
        return ret

    def CreateViewObject(self, hwnd, iid):
        return wrap(ScintillaShellView(hwnd, self.path), iid, useDispatcher=debug > 0)


# A ShellFolder for our Python objects
class ShellFolderObject(ShellFolderBase):
    def __init__(self, details):
        self.path, details = details.split("\0")
        if details.find(".") > 0:
            self.class_name, self.method_name = details.split(".")
        else:
            self.class_name = details
            self.method_name = None

    def CreateViewObject(self, hwnd, iid):
        mod_objects = get_clbr_for_file(self.path)
        object = mod_objects[self.class_name]
        if self.method_name is None:
            lineno = object.lineno
        else:
            lineno = object.methods[self.method_name]
            return wrap(
                ScintillaShellView(hwnd, self.path, lineno),
                iid,
                useDispatcher=debug > 0,
            )

    def EnumObjects(self, hwndOwner, flags):
        assert self.method_name is None, "Should not be enuming methods!"
        mod_objects = get_clbr_for_file(self.path)
        my_objects = mod_objects[self.class_name]
        pidls = []
        for func_name in my_objects.methods:
            pidl = ["object\0" + self.path + "\0" + self.class_name + "." + func_name]
            pidls.append(pidl)
        return NewEnum(pidls, iid=shell.IID_IEnumIDList, useDispatcher=(debug > 0))

    def GetDisplayNameOf(self, pidl, flags):
        assert len(pidl) == 1, "Expecting relative PIDL"
        typ, fname, obname = pidl[0].split("\0")
        class_name, method_name = obname.split(".")
        fqname = os.path.splitext(fname)[0] + "." + obname
        if flags & shellcon.SHGDN_INFOLDER:
            ret = method_name
        else:  # SHGDN_NORMAL is the default
            ret = fqname
        # No need to look at the SHGDN_FOR* modifiers.
        return ret

    def GetAttributesOf(self, pidls, attrFlags):
        ret_flags = -1
        for pidl in pidls:
            assert len(pidl) == 1, "Expecting relative pidls"
            flags = (
                shellcon.SFGAO_BROWSABLE
                | shellcon.SFGAO_FOLDER
                | shellcon.SFGAO_FILESYSANCESTOR
            )
            ret_flags &= flags
        return ret_flags


# The "Root" folder of our namespace.  As all children are directories,
# it is derived from ShellFolderFileSystem
# This is the only COM object actually registered and externally created.
class ShellFolderRoot(ShellFolderFileSystem):
    _reg_progid_ = "Python.ShellExtension.Folder"
    _reg_desc_ = "Python Path Shell Browser"
    _reg_clsid_ = "{f6287035-3074-4cb5-a8a6-d3c80e206944}"

    def GetClassID(self):
        return self._reg_clsid_

    def Initialize(self, pidl):
        # This is the PIDL of us, as created by the shell.  This is our
        # top-level ID.  All other items under us have PIDLs defined
        # by us - see the notes at the top of the file.
        # print("Initialize called with pidl={pidl!r}")
        self.pidl = pidl

    def CreateViewObject(self, hwnd, iid):
        return wrap(FileSystemView(self, hwnd), iid, useDispatcher=debug > 0)

    def EnumObjects(self, hwndOwner, flags):
        items = [["directory\0" + p] for p in sys.path if os.path.isdir(p)]
        return NewEnum(items, iid=shell.IID_IEnumIDList, useDispatcher=(debug > 0))

    def GetDisplayNameOf(self, pidl, flags):
        ## return full path for sys.path dirs, since they don't appear under a parent folder
        final_pidl = pidl[-1]
        display_name = final_pidl.split("\0")[-1]
        return display_name


# Simple shell view implementations


# Uses a builtin listview control to display simple lists of directories
# or filenames.
class FileSystemView:
    _public_methods_ = shellcon.IShellView_Methods
    _com_interfaces_ = [
        pythoncom.IID_IOleWindow,
        shell.IID_IShellView,
    ]

    def __init__(self, folder, hwnd):
        self.hwnd_parent = hwnd  # provided by explorer.
        self.hwnd = None  # intermediate window for catching command notifications.
        self.hwnd_child = None  # our ListView
        self.activate_state = None
        self.hmenu = None
        self.browser = None
        self.folder = folder
        self.children = None

    # IOleWindow
    def GetWindow(self):
        return self.hwnd

    def ContextSensitiveHelp(self, enter_mode):
        raise COMException(hresult=winerror.E_NOTIMPL)

    # IShellView
    def CreateViewWindow(self, prev, settings, browser, rect):
        print("FileSystemView.CreateViewWindow", prev, settings, browser, rect)
        self.cur_foldersettings = settings
        self.browser = browser
        self._CreateMainWindow(prev, settings, browser, rect)
        self._CreateChildWindow(prev)

        # This isn't part of the sample, but the most convenient place to
        # test/demonstrate how you can get an IShellBrowser from a HWND
        # (but ONLY when you are in the same process as the IShellBrowser!)
        # Obviously it is not necessary here - we already have the browser!
        browser_ad = win32gui.SendMessage(self.hwnd_parent, win32con.WM_USER + 7, 0, 0)
        browser_ob = pythoncom.ObjectFromAddress(browser_ad, shell.IID_IShellBrowser)
        assert browser == browser_ob
        # and make a call on the object to prove it doesn't die :)
        assert browser.QueryActiveShellView() == browser_ob.QueryActiveShellView()

    def _CreateMainWindow(self, prev, settings, browser, rect):
        # Creates a parent window that hosts the view window.  This window
        # gets the control notifications etc sent from the child.
        style = win32con.WS_CHILD | win32con.WS_VISIBLE  #
        wclass_name = "ShellViewDemo_DefView"
        # Register the Window class.
        wc = win32gui.WNDCLASS()
        wc.hInstance = win32gui.dllhandle
        wc.lpszClassName = wclass_name
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
        try:
            win32gui.RegisterClass(wc)
        except win32gui.error as details:
            # Should only happen when this module is reloaded
            if details[0] != winerror.ERROR_CLASS_ALREADY_EXISTS:
                raise

        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
            win32con.WM_COMMAND: self.OnCommand,
            win32con.WM_NOTIFY: self.OnNotify,
            win32con.WM_CONTEXTMENU: self.OnContextMenu,
            win32con.WM_SIZE: self.OnSize,
        }

        self.hwnd = win32gui.CreateWindow(
            wclass_name,
            "",
            style,
            rect[0],
            rect[1],
            rect[2] - rect[0],
            rect[3] - rect[1],
            self.hwnd_parent,
            0,
            win32gui.dllhandle,
            None,
        )
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_WNDPROC, message_map)
        print("View 's hwnd is", self.hwnd)
        return self.hwnd

    def _CreateChildWindow(self, prev):
        # Creates the list view window.
        assert self.hwnd_child is None, "already have a window"
        assert self.cur_foldersettings is not None, "no settings"
        style = (
            win32con.WS_CHILD
            | win32con.WS_VISIBLE
            | win32con.WS_BORDER
            | commctrl.LVS_SHAREIMAGELISTS
            | commctrl.LVS_EDITLABELS
        )

        view_mode, view_flags = self.cur_foldersettings
        if view_mode == shellcon.FVM_ICON:
            style |= commctrl.LVS_ICON | commctrl.LVS_AUTOARRANGE
        elif view_mode == shellcon.FVM_SMALLICON:
            style |= commctrl.LVS_SMALLICON | commctrl.LVS_AUTOARRANGE
        elif view_mode == shellcon.FVM_LIST:
            style |= commctrl.LVS_LIST | commctrl.LVS_AUTOARRANGE
        elif view_mode == shellcon.FVM_DETAILS:
            style |= commctrl.LVS_REPORT | commctrl.LVS_AUTOARRANGE
        else:
            # XP 'thumbnails' etc
            view_mode = shellcon.FVM_DETAILS
            # Default to 'report'
            style |= commctrl.LVS_REPORT | commctrl.LVS_AUTOARRANGE

        for f_flag, l_flag in [
            (shellcon.FWF_SINGLESEL, commctrl.LVS_SINGLESEL),
            (shellcon.FWF_ALIGNLEFT, commctrl.LVS_ALIGNLEFT),
            (shellcon.FWF_SHOWSELALWAYS, commctrl.LVS_SHOWSELALWAYS),
        ]:
            if view_flags & f_flag:
                style |= l_flag

        self.hwnd_child = win32gui.CreateWindowEx(
            win32con.WS_EX_CLIENTEDGE,
            "SysListView32",
            None,
            style,
            0,
            0,
            0,
            0,
            self.hwnd,
            1000,
            0,
            None,
        )

        cr = win32gui.GetClientRect(self.hwnd)
        win32gui.MoveWindow(self.hwnd_child, 0, 0, cr[2] - cr[0], cr[3] - cr[1], True)

        # Setup the columns for the view.
        lvc, extras = win32gui_struct.PackLVCOLUMN(
            fmt=commctrl.LVCFMT_LEFT, subItem=1, text="Name", cx=300
        )
        win32gui.SendMessage(self.hwnd_child, commctrl.LVM_INSERTCOLUMN, 0, lvc)

        lvc, extras = win32gui_struct.PackLVCOLUMN(
            fmt=commctrl.LVCFMT_RIGHT, subItem=1, text="Exists", cx=50
        )
        win32gui.SendMessage(self.hwnd_child, commctrl.LVM_INSERTCOLUMN, 1, lvc)
        # and fill it with the content
        self.Refresh()

    def GetCurrentInfo(self):
        return self.cur_foldersettings

    def UIActivate(self, activate_state):
        print("OnActivate")

    def _OnActivate(self, activate_state):
        if self.activate_state == activate_state:
            return
        self._OnDeactivate()  # restore menu's first, if necessary.
        if activate_state != shellcon.SVUIA_DEACTIVATE:
            assert self.hmenu is None, "Should have destroyed it!"
            self.hmenu = win32gui.CreateMenu()
            widths = 0, 0, 0, 0, 0, 0
            # Ask explorer to add its standard items.
            self.browser.InsertMenusSB(self.hmenu, widths)
            # Merge with these standard items
            self._MergeMenus(activate_state)
            self.browser.SetMenuSB(self.hmenu, 0, self.hwnd)
        self.activate_state = activate_state

    def _OnDeactivate(self):
        if self.browser is not None and self.hmenu is not None:
            self.browser.SetMenuSB(0, 0, 0)
            self.browser.RemoveMenusSB(self.hmenu)
            win32gui.DestroyMenu(self.hmenu)
            self.hmenu = None
        self.hsubmenus = None
        self.activate_state = shellcon.SVUIA_DEACTIVATE

    def _MergeMenus(self, activate_state):
        # Merge the operations we support into the top-level menus.
        # NOTE: This function it *not* called each time the selection changes.
        # SVUIA_ACTIVATE_FOCUS really means "have a selection?"
        have_sel = activate_state == shellcon.SVUIA_ACTIVATE_FOCUS
        # only do "file" menu here, and only 1 item on it!
        mid = shellcon.FCIDM_MENU_FILE
        # Get the hmenu for the menu
        buf, extras = win32gui_struct.EmptyMENUITEMINFO(win32con.MIIM_SUBMENU)
        win32gui.GetMenuItemInfo(self.hmenu, mid, False, buf)
        data = win32gui_struct.UnpackMENUITEMINFO(buf)
        submenu = data[3]
        print("Do someting with the file menu!")

    def Refresh(self):
        stateMask = commctrl.LVIS_SELECTED | commctrl.LVIS_DROPHILITED
        state = 0
        self.children = []
        # Enumerate and store the child PIDLs
        for cid in self.folder.EnumObjects(self.hwnd, 0):
            self.children.append(cid)

        for row_index, data in enumerate(self.children):
            assert len(data) == 1, "expecting just a child PIDL"
            typ, path = data[0].split("\0")
            desc = os.path.exists(path) and "Yes" or "No"
            prop_vals = (path, desc)
            # first col
            data, extras = win32gui_struct.PackLVITEM(
                item=row_index,
                subItem=0,
                text=prop_vals[0],
                state=state,
                stateMask=stateMask,
            )
            win32gui.SendMessage(
                self.hwnd_child, commctrl.LVM_INSERTITEM, row_index, data
            )
            # rest of the cols.
            col_index = 1
            for prop_val in prop_vals[1:]:
                data, extras = win32gui_struct.PackLVITEM(
                    item=row_index, subItem=col_index, text=prop_val
                )

                win32gui.SendMessage(self.hwnd_child, commctrl.LVM_SETITEM, 0, data)
                col_index += 1

    def SelectItem(self, pidl, flag):
        # For the sake of brevity, we don't implement this yet.
        # You would need to locate the index of the item in the shell-view
        # with that PIDL, then ask the list-view to select it.
        print("Please implement SelectItem for PIDL", pidl)

    def GetItemObject(self, item_num, iid):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def TranslateAccelerator(self, msg):
        return winerror.S_FALSE

    def DestroyViewWindow(self):
        win32gui.DestroyWindow(self.hwnd)
        self.hwnd = None
        print("Destroyed view window")

    # Message handlers.
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        print("OnDestory")

    def OnCommand(self, hwnd, msg, wparam, lparam):
        print("OnCommand")

    def OnNotify(self, hwnd, msg, wparam, lparam):
        hwndFrom, idFrom, code = win32gui_struct.UnpackWMNOTIFY(lparam)
        # print("OnNotify code=0x%x (0x%x, 0x%x)" % (code, wparam, lparam))
        if code == commctrl.NM_SETFOCUS:
            # Control got focus - Explorer may not know - tell it
            if self.browser is not None:
                self.browser.OnViewWindowActive(None)
            # And do our menu thang
            self._OnActivate(shellcon.SVUIA_ACTIVATE_FOCUS)
        elif code == commctrl.NM_KILLFOCUS:
            self._OnDeactivate()
        elif code == commctrl.NM_DBLCLK:
            # This DblClick implementation leaves a little to be desired :)
            # It demonstrates some useful concepts, such as asking the
            # folder for its context-menu and invoking a command from it.
            # However, as our folder delegates IContextMenu to the shell
            # itself, the end result is that the folder is opened in
            # its "normal" place in Windows explorer rather than inside
            # our shell-extension.
            # Determine the selected items.
            sel = []
            n = -1
            while 1:
                n = win32gui.SendMessage(
                    self.hwnd_child, commctrl.LVM_GETNEXTITEM, n, commctrl.LVNI_SELECTED
                )
                if n == -1:
                    break
                sel.append(self.children[n][-1:])
            print("Selection is", sel)
            hmenu = win32gui.CreateMenu()
            try:
                # Get the IContextMenu for the items.
                inout, cm = self.folder.GetUIObjectOf(
                    self.hwnd_parent, sel, shell.IID_IContextMenu, 0
                )

                # As per 'Q179911', we need to determine if the default operation
                # should be 'open' or 'explore'
                flags = shellcon.CMF_DEFAULTONLY
                try:
                    self.browser.GetControlWindow(shellcon.FCW_TREE)
                    flags |= shellcon.CMF_EXPLORE
                except pythoncom.com_error:
                    pass
                # *sob* - delegating to the shell does work - but lands us
                # in the original location.  Q179911 also shows that
                # ShellExecuteEx should work - but I can't make it work as
                # described (XP: function call succeeds, but another thread
                # shows a dialog with text of E_INVALID_PARAM, and new
                # Explorer window opens with desktop view. Vista: function
                # call succeeds, but no window created at all.
                # On Vista, I'd love to get an IExplorerBrowser interface
                # from the shell, but a QI fails, and although the
                # IShellBrowser does appear to support IServiceProvider, I
                # still can't get it
                if 0:
                    id_cmd_first = 1  # TrackPopupMenu makes it hard to use 0
                    cm.QueryContextMenu(hmenu, 0, id_cmd_first, -1, flags)
                    # Find the default item in the returned menu.
                    cmd = win32gui.GetMenuDefaultItem(hmenu, False, 0)
                    if cmd == -1:
                        print("Oops: _doDefaultActionFor found no default menu")
                    else:
                        ci = (
                            0,
                            self.hwnd_parent,
                            cmd - id_cmd_first,
                            None,
                            None,
                            0,
                            0,
                            0,
                        )
                        cm.InvokeCommand(ci)
                else:
                    rv = shell.ShellExecuteEx(
                        hwnd=self.hwnd_parent,
                        nShow=win32con.SW_NORMAL,
                        lpClass="folder",
                        lpVerb="explore",
                        lpIDList=sel[0],
                    )
                    print("ShellExecuteEx returned", rv)
            finally:
                win32gui.DestroyMenu(hmenu)

    def OnContextMenu(self, hwnd, msg, wparam, lparam):
        # Get the selected items.
        pidls = []
        n = -1
        while 1:
            n = win32gui.SendMessage(
                self.hwnd_child, commctrl.LVM_GETNEXTITEM, n, commctrl.LVNI_SELECTED
            )
            if n == -1:
                break
            pidls.append(self.children[n][-1:])

        spt = win32api.GetCursorPos()
        if not pidls:
            print("Ignoring background click")
            return
        # Get the IContextMenu for the items.
        inout, cm = self.folder.GetUIObjectOf(
            self.hwnd_parent, pidls, shell.IID_IContextMenu, 0
        )
        hmenu = win32gui.CreatePopupMenu()
        sel = None
        # As per 'Q179911', we need to determine if the default operation
        # should be 'open' or 'explore'
        try:
            flags = 0
            try:
                self.browser.GetControlWindow(shellcon.FCW_TREE)
                flags |= shellcon.CMF_EXPLORE
            except pythoncom.com_error:
                pass
            id_cmd_first = 1  # TrackPopupMenu makes it hard to use 0
            cm.QueryContextMenu(hmenu, 0, id_cmd_first, -1, flags)
            tpm_flags = (
                win32con.TPM_LEFTALIGN
                | win32con.TPM_RETURNCMD
                | win32con.TPM_RIGHTBUTTON
            )
            sel = win32gui.TrackPopupMenu(
                hmenu, tpm_flags, spt[0], spt[1], 0, self.hwnd, None
            )
            print("TrackPopupMenu returned", sel)
        finally:
            win32gui.DestroyMenu(hmenu)
        if sel:
            ci = 0, self.hwnd_parent, sel - id_cmd_first, None, None, 0, 0, 0
            cm.InvokeCommand(ci)

    def OnSize(self, hwnd, msg, wparam, lparam):
        # print("OnSize", self.hwnd_child, win32api.LOWORD(lparam), win32api.HIWORD(lparam))
        if self.hwnd_child is not None:
            x = win32api.LOWORD(lparam)
            y = win32api.HIWORD(lparam)
            win32gui.MoveWindow(self.hwnd_child, 0, 0, x, y, False)


# This uses scintilla to display a filename, and optionally jump to a line
# number.
class ScintillaShellView:
    _public_methods_ = shellcon.IShellView_Methods
    _com_interfaces_ = [
        pythoncom.IID_IOleWindow,
        shell.IID_IShellView,
    ]

    def __init__(self, hwnd, filename, lineno=None):
        self.filename = filename
        self.lineno = lineno
        self.hwnd_parent = hwnd
        self.hwnd = None

    def _SendSci(self, msg, wparam=0, lparam=0):
        return win32gui.SendMessage(self.hwnd, msg, wparam, lparam)

    # IShellView
    def CreateViewWindow(self, prev, settings, browser, rect):
        print("ScintillaShellView.CreateViewWindow", prev, settings, browser, rect)
        # Make sure scintilla.dll is loaded.  If not, find it on sys.path
        # (which it generally is for Pythonwin)
        try:
            win32api.GetModuleHandle("Scintilla.dll")
        except win32api.error:
            for p in sys.path:
                fname = os.path.join(p, "Scintilla.dll")
                if not os.path.isfile(fname):
                    fname = os.path.join(p, "Build", "Scintilla.dll")
                if os.path.isfile(fname):
                    win32api.LoadLibrary(fname)
                    break
            else:
                raise RuntimeError("Can't find scintilla!")

        style = (
            win32con.WS_CHILD
            | win32con.WS_VSCROLL
            | win32con.WS_HSCROLL
            | win32con.WS_CLIPCHILDREN
            | win32con.WS_VISIBLE
        )
        self.hwnd = win32gui.CreateWindow(
            "Scintilla",
            "Scintilla",
            style,
            rect[0],
            rect[1],
            rect[2] - rect[0],
            rect[3] - rect[1],
            self.hwnd_parent,
            1000,
            0,
            None,
        )

        message_map = {
            win32con.WM_SIZE: self.OnSize,
        }
        #        win32gui.SetWindowLong(self.hwnd, win32con.GWL_WNDPROC, message_map)

        file_data = open(self.filename, "U").read()

        self._SetupLexer()
        self._SendSci(scintillacon.SCI_ADDTEXT, len(file_data), file_data)
        if self.lineno is not None:
            self._SendSci(scintillacon.SCI_GOTOLINE, self.lineno)
        print("Scintilla's hwnd is", self.hwnd)

    def _SetupLexer(self):
        h = self.hwnd
        styles = [
            ((0, 0, 200, 0, 0x808080), None, scintillacon.SCE_P_DEFAULT),
            ((0, 2, 200, 0, 0x008000), None, scintillacon.SCE_P_COMMENTLINE),
            ((0, 2, 200, 0, 0x808080), None, scintillacon.SCE_P_COMMENTBLOCK),
            ((0, 0, 200, 0, 0x808000), None, scintillacon.SCE_P_NUMBER),
            ((0, 0, 200, 0, 0x008080), None, scintillacon.SCE_P_STRING),
            ((0, 0, 200, 0, 0x008080), None, scintillacon.SCE_P_CHARACTER),
            ((0, 0, 200, 0, 0x008080), None, scintillacon.SCE_P_TRIPLE),
            ((0, 0, 200, 0, 0x008080), None, scintillacon.SCE_P_TRIPLEDOUBLE),
            ((0, 0, 200, 0, 0x000000), 0x008080, scintillacon.SCE_P_STRINGEOL),
            ((0, 1, 200, 0, 0x800000), None, scintillacon.SCE_P_WORD),
            ((0, 1, 200, 0, 0xFF0000), None, scintillacon.SCE_P_CLASSNAME),
            ((0, 1, 200, 0, 0x808000), None, scintillacon.SCE_P_DEFNAME),
            ((0, 0, 200, 0, 0x000000), None, scintillacon.SCE_P_OPERATOR),
            ((0, 0, 200, 0, 0x000000), None, scintillacon.SCE_P_IDENTIFIER),
        ]
        self._SendSci(scintillacon.SCI_SETLEXER, scintillacon.SCLEX_PYTHON, 0)
        self._SendSci(scintillacon.SCI_SETSTYLEBITS, 5)
        baseFormat = (-402653169, 0, 200, 0, 0, 0, 49, "Courier New")
        for f, bg, stylenum in styles:
            self._SendSci(scintillacon.SCI_STYLESETFORE, stylenum, f[4])
            self._SendSci(scintillacon.SCI_STYLESETFONT, stylenum, baseFormat[7])
            if f[1] & 1:
                self._SendSci(scintillacon.SCI_STYLESETBOLD, stylenum, 1)
            else:
                self._SendSci(scintillacon.SCI_STYLESETBOLD, stylenum, 0)
            if f[1] & 2:
                self._SendSci(scintillacon.SCI_STYLESETITALIC, stylenum, 1)
            else:
                self._SendSci(scintillacon.SCI_STYLESETITALIC, stylenum, 0)
            self._SendSci(
                scintillacon.SCI_STYLESETSIZE, stylenum, int(baseFormat[2] / 20)
            )
            if bg is not None:
                self._SendSci(scintillacon.SCI_STYLESETBACK, stylenum, bg)
            self._SendSci(
                scintillacon.SCI_STYLESETEOLFILLED, stylenum, 1
            )  # Only needed for unclosed strings.

    # IOleWindow
    def GetWindow(self):
        return self.hwnd

    def UIActivate(self, activate_state):
        print("OnActivate")

    def DestroyViewWindow(self):
        win32gui.DestroyWindow(self.hwnd)
        self.hwnd = None
        print("Destroyed scintilla window")

    def TranslateAccelerator(self, msg):
        return winerror.S_FALSE

    def OnSize(self, hwnd, msg, wparam, lparam):
        x = win32api.LOWORD(lparam)
        y = win32api.HIWORD(lparam)
        win32gui.MoveWindow(self.hwnd, 0, 0, x, y, False)


def DllRegisterServer():
    import winreg

    key = winreg.CreateKey(
        winreg.HKEY_LOCAL_MACHINE,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\"
        "Explorer\\Desktop\\Namespace\\" + ShellFolderRoot._reg_clsid_,
    )
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, ShellFolderRoot._reg_desc_)
    # And special shell keys under our CLSID
    key = winreg.CreateKey(
        winreg.HKEY_CLASSES_ROOT,
        "CLSID\\" + ShellFolderRoot._reg_clsid_ + "\\ShellFolder",
    )
    # 'Attributes' is an int stored as a binary! use struct
    attr = (
        shellcon.SFGAO_FOLDER | shellcon.SFGAO_HASSUBFOLDER | shellcon.SFGAO_BROWSABLE
    )
    import struct

    s = struct.pack("i", attr)
    winreg.SetValueEx(key, "Attributes", 0, winreg.REG_BINARY, s)
    print(ShellFolderRoot._reg_desc_, "registration complete.")


def DllUnregisterServer():
    import winreg

    try:
        key = winreg.DeleteKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\"
            "Explorer\\Desktop\\Namespace\\" + ShellFolderRoot._reg_clsid_,
        )
    except OSError as details:
        import errno

        if details.errno != errno.ENOENT:
            raise
    print(ShellFolderRoot._reg_desc_, "unregistration complete.")


if __name__ == "__main__":
    from win32com.server import register

    register.UseCommandLine(
        ShellFolderRoot,
        debug=debug,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )

```


---

## com/win32comext/shell/demos/shellexecuteex.py

```python
import win32con
from win32com.shell import shell, shellcon


def ExplorePIDL():
    pidl = shell.SHGetSpecialFolderLocation(0, shellcon.CSIDL_DESKTOP)
    print("The desktop is at", shell.SHGetPathFromIDList(pidl))
    shell.ShellExecuteEx(
        fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
        nShow=win32con.SW_NORMAL,
        lpClass="folder",
        lpVerb="explore",
        lpIDList=pidl,
    )
    print("Done!")


if __name__ == "__main__":
    ExplorePIDL()

```


---

## com/win32comext/shell/demos/viewstate.py

```python
"""
Demonstrates how to propagate a folder's view state to all its subfolders
The format of the ColInfo stream is apparently undocumented, but
it can be read raw from one folder and copied to another's view state.
"""

import os
import sys

import pythoncom
from win32com.shell import shell, shellcon

template_folder = os.path.split(sys.executable)[0]
print("Template folder:", template_folder)
template_pidl = shell.SHILCreateFromPath(template_folder, 0)[0]
template_pb = shell.SHGetViewStatePropertyBag(
    template_pidl,
    "Shell",
    shellcon.SHGVSPB_FOLDERNODEFAULTS,
    pythoncom.IID_IPropertyBag,
)

# Column info has to be read as a stream
# This may blow up if folder has never been opened in Explorer and has no ColInfo yet
template_iunk = template_pb.Read("ColInfo", pythoncom.VT_UNKNOWN)
template_stream = template_iunk.QueryInterface(pythoncom.IID_IStream)
streamsize = template_stream.Stat()[2]
template_colinfo = template_stream.Read(streamsize)


def update_colinfo(not_used, dir_name, fnames):
    for fname in fnames:
        full_fname = os.path.join(dir_name, fname)
        if os.path.isdir(full_fname):
            print(full_fname)
            pidl = shell.SHILCreateFromPath(full_fname, 0)[0]
            pb = shell.SHGetViewStatePropertyBag(
                pidl,
                "Shell",
                shellcon.SHGVSPB_FOLDERNODEFAULTS,
                pythoncom.IID_IPropertyBag,
            )
            ## not all folders already have column info, and we're replacing it anyway
            pb.Write("ColInfo", template_stream)
            iunk = pb.Read("ColInfo", pythoncom.VT_UNKNOWN)
            s = iunk.QueryInterface(pythoncom.IID_IStream)
            s.Write(template_colinfo)
            s = None
            ## attribute names read from registry, can't find any way to enumerate IPropertyBag
            for attr in (
                "Address",
                "Buttons",
                "Col",
                "Vid",
                "WFlags",
                "FFlags",
                "Sort",
                "SortDir",
                "ShowCmd",
                "FolderType",
                "Mode",
                "Rev",
            ):
                pb.Write(attr, template_pb.Read(attr))
            pb = None


os.walk(template_folder, update_colinfo, None)

```


---

## com/win32comext/shell/demos/walk_shell_folders.py

```python
# A little sample that walks from the desktop into child
# items.
from win32com.shell import shell, shellcon


def walk(folder, depth=2, indent=""):
    try:
        pidls = folder.EnumObjects(0, shellcon.SHCONTF_FOLDERS)
    except shell.error:
        # no items
        return
    for pidl in pidls:
        dn = folder.GetDisplayNameOf(pidl, shellcon.SHGDN_NORMAL)
        print(indent, dn)
        if depth:
            try:
                child = folder.BindToObject(pidl, None, shell.IID_IShellFolder)
            except shell.error:
                pass
            else:
                walk(child, depth - 1, indent + " ")


walk(shell.SHGetDesktopFolder())

```
