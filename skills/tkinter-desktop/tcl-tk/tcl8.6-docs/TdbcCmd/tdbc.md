### NAME

tdbc — Tcl Database Connectivity

### SYNOPSIS

package require **tdbc 1.0**  
package require **tdbc::***driver version*  
  
**tdbc::***driver***::connection create** *db* ?*-option value*...?  

### DESCRIPTION

Tcl Database Connectivity (TDBC) is a common interface for Tcl programs to
access SQL databases. It is implemented by a series of database *drivers* :
separate modules, each of which adapts Tcl to the interface of one particular
database system. All of the drivers implement a common series of commands for
manipulating the database. These commands are all named dynamically, since they
all represent objects in the database system. They include **connections,**
which represent connections to a database; **statements,** which represent SQL
statements, and **result sets,** which represent the sets of rows that result
from executing statements. All of these have manual pages of their own, listed
under **SEE ALSO**.

In addition, TDBC itself has a few service procedures that are chiefly of
interest to driver writers. **SEE ALSO** also enumerates them.

### SEE ALSO

**[Tdbc_Init](../TdbcLib/Tdbc_Init.md)** ,
**[tdbc::connection](../TdbcCmd/tdbc_connection.md)** , **tdbc::mapSqlState**
, **[tdbc::resultset](../TdbcCmd/tdbc_resultset.md)** ,
**[tdbc::statement](../TdbcCmd/tdbc_statement.md)** ,
**[tdbc::tokenize](../TdbcCmd/tdbc_tokenize.md)** ,
**[tdbc::mysql](../TdbcmysqlCmd/tdbc_mysql.md)** ,
**[tdbc::odbc](../TdbcodbcCmd/tdbc_odbc.md)** ,
**[tdbc::postgres](../TdbcpostgresCmd/tdbc_postgres.md)** ,
**[tdbc::sqlite3](../TdbcsqliteCmd/tdbc_sqlite3.md)**

### KEYWORDS

[TDBC](../Keywords/T.htm#TDBC), [SQL](../Keywords/S.htm#SQL),
[database](../Keywords/D.htm#database),
[connectivity](../Keywords/C.htm#connectivity),
[connection](../Keywords/C.htm#connection),
[resultset](../Keywords/R.htm#resultset),
[statement](../Keywords/S.htm#statement)

### COPYRIGHT

Copyright (c) 2008 by Kevin B. Kenny.

Copyright © 2008 by Kevin B. Kenny.
