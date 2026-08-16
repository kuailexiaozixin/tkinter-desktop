# 官方示例源码 · adodbapi/examples

> 来源 https://github.com/mhammond/pywin32/tree/main/adodbapi/examples （共 4 个 .py，全文内联）


---

## adodbapi/examples/db_print.py

```python
"""db_print.py -- a simple demo for ADO database reads."""

import sys

import adodbapi.ado_consts as adc

cmd_args = ("filename", "table_name")
if "help" in sys.argv:
    print("possible settings keywords are:", cmd_args)
    sys.exit()

kw_args = {}  # pick up filename and proxy address from command line (optionally)
for arg in sys.argv:
    s = arg.split("=")
    if len(s) > 1:
        if s[0] in cmd_args:
            kw_args[s[0]] = s[1]

kw_args.setdefault(
    "filename", "test.mdb"
)  # assumes server is running from examples folder
kw_args.setdefault("table_name", "Products")  # the name of the demo table

# the server needs to select the provider based on his Python installation
provider_switch = ["provider", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]

# ------------------------ START HERE -------------------------------------
# create the connection
constr = "Provider=%(provider)s;Data Source=%(filename)s"
import adodbapi as db

con = db.connect(constr, kw_args, macro_is64bit=provider_switch)

if kw_args["table_name"] == "?":
    print("The tables in your database are:")
    for name in con.get_table_names():
        print(name)
else:
    # make a cursor on the connection
    with con.cursor() as c:
        # run an SQL statement on the cursor
        sql = "select * from %s" % kw_args["table_name"]
        print('performing query="%s"' % sql)
        c.execute(sql)

        # check the results
        print(
            'result rowcount shows as= %d. (Note: -1 means "not known")' % (c.rowcount,)
        )
        print("")
        print("result data description is:")
        print("            NAME Type         DispSize IntrnlSz Prec Scale Null?")
        for d in c.description:
            print(
                ("%16s %-12s %8s %8d %4d %5d %s")
                % (d[0], adc.adTypeNames[d[1]], d[2], d[3], d[4], d[5], bool(d[6]))
            )
        print("")
        print("str() of first five records are...")

        # get the results
        db = c.fetchmany(5)

        # print them
        for rec in db:
            print(rec)

        print("")
        print("repr() of next row is...")
        print(repr(c.fetchone()))
        print("")
con.close()

```


---

## adodbapi/examples/db_table_names.py

```python
"""db_table_names.py -- a simple demo for ADO database table listing."""

import sys

import adodbapi

try:
    databasename = sys.argv[1]
except IndexError:
    databasename = "test.mdb"

provider = ["prv", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]
constr = "Provider=%(prv)s;Data Source=%(db)s"

# create the connection
con = adodbapi.connect(constr, db=databasename, macro_is64bit=provider)

print("Table names in= %s" % databasename)

for table in con.get_table_names():
    print(table)

```


---

## adodbapi/examples/xls_read.py

```python
import sys

import adodbapi

try:
    import adodbapi.is64bit as is64bit

    is64 = is64bit.Python()
except ImportError:
    is64 = False

if is64:
    driver = "Microsoft.ACE.OLEDB.12.0"
else:
    driver = "Microsoft.Jet.OLEDB.4.0"
extended = 'Extended Properties="Excel 8.0;HDR=Yes;IMEX=1;"'

try:  # first command line argument will be xls file name -- default to the one written by xls_write.py
    filename = sys.argv[1]
except IndexError:
    filename = "xx.xls"

constr = "Provider=%s;Data Source=%s;%s" % (driver, filename, extended)

conn = adodbapi.connect(constr)

try:  # second command line argument will be worksheet name -- default to first worksheet
    sheet = sys.argv[2]
except IndexError:
    # use ADO feature to get the name of the first worksheet
    sheet = conn.get_table_names()[0]

print("Shreadsheet=%s  Worksheet=%s" % (filename, sheet))
print("------------------------------------------------------------")
crsr = conn.cursor()
sql = "SELECT * from [%s]" % sheet
crsr.execute(sql)
for row in crsr.fetchmany(10):
    print(repr(row))
crsr.close()
conn.close()

```


---

## adodbapi/examples/xls_write.py

```python
import datetime

import adodbapi

try:
    import adodbapi.is64bit as is64bit

    is64 = is64bit.Python()
except ImportError:
    is64 = False  # in case the user has an old version of adodbapi
if is64:
    driver = "Microsoft.ACE.OLEDB.12.0"
else:
    driver = "Microsoft.Jet.OLEDB.4.0"
filename = "xx.xls"  # file will be created if it does not exist
extended = 'Extended Properties="Excel 8.0;Readonly=False;"'

constr = "Provider=%s;Data Source=%s;%s" % (driver, filename, extended)

conn = adodbapi.connect(constr)
with conn:  # will auto commit if no errors
    with conn.cursor() as crsr:
        try:
            crsr.execute("drop table SheetOne")
        except:
            pass  # just is case there is one already there

        # create the sheet and the header row and set the types for the columns
        crsr.execute(
            "create table SheetOne (Name varchar, Rank varchar, SrvcNum integer, Weight float,  Birth date)"
        )

        sql = "INSERT INTO SheetOne (name, rank , srvcnum, weight, birth) values (?,?,?,?,?)"

        data = ("Mike Murphy", "SSG", 123456789, 167.8, datetime.date(1922, 12, 27))
        crsr.execute(sql, data)  # write the first row of data
        crsr.execute(
            sql, ["John Jones", "Pvt", 987654321, 140.0, datetime.date(1921, 7, 4)]
        )  # another row of data
conn.close()
print("Created spreadsheet=%s worksheet=%s" % (filename, "SheetOne"))

```
