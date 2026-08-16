# com/help/adsi.html

> 来源：https://github.com/mhammond/pywin32/blob/main/com/help/adsi.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

| | ADSI, Exchange, and Python

- SUMMARY

- Introduction
- User Account Management

- Adding a user
- Getting/Modifying user info
- Deleting a User
- Distribution List

- Adding to a list
- Recursively listing all unique members
- a href="#Conclusion">In Conclusion
- Further Info
- Author

---

## SUMMARY

 Python's ADSI access works really well with Exchange (late or early binding since you can read microsoft's type library). To get started, you will need to download ADSI from microsoft: [Setting Up Your Development Environment](https://learn.microsoft.com/en-us/windows/win32/adsi/setting-up-your-development-environment). Microsoft has documentation for using languages other than python in the sdk.

---

### Introduction

 Before doing anything else you need to go through the next two steps:
 Acquiring ADSI object
| | Task | Description
| | Create Global Providers Object | adsi = win32com.client.Dispatch('ADsNameSpaces')
| | Create LDAP Provider Object | ldap = adsi.getobject("","LDAP:")
Now you have to decide how you want to access the exchange server.
I have chosen to authenticate, in which case you need to use OpenDSObject()
 Method of access
| | Task | Description
| | Specify Login and Domain | logon_ex='cn=wilma, dc=bedrock'
| | Specify password | password='dino'
| | Login to Server | myDSObject = ldap.OpenDSObject(ex_path,logon_ex,password,0)
 Note -- the fourth argument to OpenDSObject has various options for how to authenticate. For example, if you use 1 instead of zero, it should either use NTLM or Kerberos for authentication. For more information, check out: [OpenDSObject](https://learn.microsoft.com/en-us/windows/win32/api/iads/nf-iads-iadsopendsobject-opendsobject)

 The ex_path in the above example specifies the resource you are trying to access. For example:
 Types of paths
| | Task | Description
| | Specific User | ex_path="LDAP://server/cn=fredflintsone,cn=Recipients,ou=rubble,o=bedrock"
| | Mailing List | ex_path="LDAP://server/cn=bedrock,cn=Recipients,ou=rubble,o=bedrock"
| | All Recipients | ex_path="LDAP://server/cn=Recipients,ou=rubble,o=bedrock"

---

### User Account Management

#### Adding a user to exchange

```
# Adding a new account to exchange is simple except for one thing.
# You need to associate an NT account with an exchange account.
# To do so at this point requires some c++ to produce some hex SID
# and trustee information that adsi can use.
# At this point assume we have C++ magic
#
# Note we are accessing Recipients directly now
ex_path="LDAP://server/cn=Recipients,ou=rubble,o=bedrock"
logon_ex='cn=wilma,dc=bedrock'
password='dino'
myDSObject = ldap.OpenDSObject(ex_path,logon_ex,password,0)
newobj = myDSObject.create("OrganizationalPerson", "cn=betty")
newobj.put('MailPreferenceOption', 0)
# etc . . . add whatever else you want. There are a few required fields.
# Now the part to get exchange associated with NT
# The Magic is here
import win32pipe
assoc_nt=win32pipe.popen('getsid bedrock\\fredflint')
nt_security=win32pipe.popen('gettrustee bedrock\\fredflint')
newobj.put('NT-Security-Descriptor',assoc_nt)
newobj.put('NT-Security-Descriptor',nt_security)
newobj.SetInfo
```

#### Getting/Modify user info

```
ex_path="LDAP://server/cn=fredflint,cn=Recipients,ou=rubble,o=bedrock"
myDSObject = ldap.OpenDSObject(ex_path,logon_ex,password,0)
myDSObject.Getinfo()
# To access a user's data try:
attribute = myDSObject.Get('Extension-Attribute-1')
print(attribute)
# To modify a user try:
myDSObject.Put('Extension-Attribute-1','barney was here')
myDSObject.Setinfo()
```

 Comments Note -- To make any changes permanent setinfo is required.

#### Deleting a user from exchange

```
#Here we connect to Recipients and then
#delete a user
#This is a more complete example.
#data is a dictionary that contains info
#that may be dynamic like the domain,
#admin login, or exchange server
#notice I am using a try/except clause here
#to catch any exceptions
try:
  #ADSI here
  # Create the Global Providers object
  logon_ex='cn='+data['NT_admin']+', dc='+data['NT_domain']+',cn=admin'
  ex_list_path="LDAP://"+data['EX_site_srv']+"/cn=Recipients,ou="\
  +data['ou']+",o="+data['o']
  adsi = win32com.client.Dispatch('ADsNameSpaces')
  #
  # Now get the LDAP Provider object
  ldap = adsi.getobject("","LDAP:")
  dsobj = ldap.OpenDSObject(ex_list_path,logon_ex,data['NT_password'],0);
  dsobj.Getinfo()
  dsobj.Delete("OrganizationalPerson", "cn="+login)
  dsobj.Setinfo()
except:
  print("Error deleting "+login, sys.exc_type , sys.exc_value)
```

---

### Distribution List

```



---






#### Adding to a distribution list





```
# I used putex instead of put because it has more options
# The '3' value means append. The SDK has specific info on it
ex_list_path="LDAP://"+server+"/cn="+list+",cn=Recipients,ou="+ou+",o="+o
dsobj = ldap.OpenDSObject(ex_list_path,logon_ex,password,0);
dsobj.Getinfo()
list_member='cn='+user+',cn=Recipients,ou='+ou+',o='+o
append_list=[list_member]
dsobj.putEx(3,'Member',append_list);
dsobj.SetInfo()
```






#### Recursively listing all unique members of a distribution list





```
#This function looks for all Organizational persons to add to a dictionary
#If it gets a groupOfNames, it needs to parse that and call the function again
#to get the members of the groupOfNames
def getmembers(path=''):
 user_dict={}
 logon_ex='cn=fred, dc=bedrock'
 password='dino'
 server='flintstone'
 ldap = win32com.client.Dispatch('ADsNameSpaces').getobject("","LDAP:")
 dsobj = ldap.OpenDSObject(path,logon_ex,password,0)
 dsobj.Getinfo()
 if dsobj.Class=='organizationalPerson':
 user_dict[dsobj.cn.capitalize()]=dsobj.uid
 elif dsobj.Class=='groupOfNames':
 for i in dsobj.Members():
 if i.Class=='organizationalPerson':
 user_dict[i.cn.capitalize()]=i.uid
 elif type(i.member)==types.TupleType:
 for j in i.member:
 newpath='LDAP://'+server+'/'+j
 getmembers(newpath)
 elif type(i.member)==types.StringType:
 newpath='LDAP://'+server+'/'+i.member
 getmembers(newpath)
 elif dsobj.Class=='Remote-Address':
 User_dict[dsobj.cn.capitalize()]=dsobj.uid
 elif dsobj.Class=='Public-Folder':
 pass
 else:
 print("skipped",dsobj.Class,dsobj.uid)
 return user_dict
```









---




### In Conclusion


Microsoft's ADSI allows one to manage exchange w/out having to resort to the lower-level APIs.
Python has no trouble accessing Microsoft's ADSI to help simplify user management.







---




## Further Info








-
  [Windows Active Directory Service Interfaces documentation](https://learn.microsoft.com/en-us/windows/win32/ADSI)


- Relevant Python libraries: win32com.client




---



## Author


John Nielsen, jn@who.net

-- Have a great time with programming with python!







|
			 |     ADSI, Exchange, and Python
