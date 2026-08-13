# 模块 odbc

> 来源：https://mhammond.github.io/pywin32/odbc.html （及其成员页，已全部内联）

## Module odbc

 A Python wrapper around the ODBC API.

#### Methods

- odbc

 Creates an connection object.

- SQLDataSources

 Enumerates ODBC data sources.


---

# odbc 成员详细文档（共 2 项）


---

<!-- page: odbc__SQLDataSources_meth.html -->

## odbc.SQLDataSources

 (name, desc)/None = SQLDataSources(direction)

Enumerates ODBC data sources

#### Parameters

- direction : int

 One of SQL_FETCH_* flags indicating how to retrieve data sources

#### Return Value

The result is None when SQL_NO_DATA is returned from ODBC.


---

<!-- page: odbc__odbc_meth.html -->

## odbc.odbc

 connection = odbc(connectionString)

Creates an ODBC connection

#### Parameters

- connectionString : string

 An ODBC connection string. For backwards-compatibility, this parameter can be of the form DSN[/username[/password]] (e.g. "myDSN/myUserName/myPassword"). Alternatively, a full ODBC connection string can be used (e.g., "Driver={SQL Server};Server=(local);Database=myDatabase").
