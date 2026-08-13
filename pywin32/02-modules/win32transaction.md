# 模块 win32transaction

> 来源：https://mhammond.github.io/pywin32/win32transaction.html （及其成员页，已全部内联）

## Module win32transaction

 Module wrapping Kernal Transaction Manager functions, as used with transacted NTFS and transacted registry functions.

#### Comments

 All functions accept keyword arguments.

#### Methods

- CreateTransaction

 Creates a transaction

- RollbackTransaction

 Rolls back a transaction

- RollbackTransactionAsync

 Rolls back a transaction asynchronously

- CommitTransaction

 Commits a transaction

- CommitTransactionAsync

 Commits a transaction asynchronously

- GetTransactionId

 Returns the transaction's GUID

- OpenTransaction

 Creates a handle to an existing transaction


---

# win32transaction 成员详细文档（共 7 项）


---

<!-- page: win32transaction__CommitTransactionAsync_meth.html -->

## win32transaction.CommitTransactionAsync

 CommitTransactionAsync(TransactionHandle)

Commits a transaction asynchronously

#### Parameters

- TransactionHandle : PyHANDLE

 Handle to a transaction

#### Win32 API References

- Search for CommitTransactionAsync at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CommitTransactionAsync), [google](https://www.google.com/search?q=CommitTransactionAsync) or [google groups](https://groups.google.com/groups?q=CommitTransactionAsync).


---

<!-- page: win32transaction__CommitTransaction_meth.html -->

## win32transaction.CommitTransaction

 CommitTransaction(TransactionHandle)

Commits a transaction

#### Parameters

- TransactionHandle : PyHANDLE

 Handle to a transaction

#### Win32 API References

- Search for CommitTransaction at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CommitTransaction), [google](https://www.google.com/search?q=CommitTransaction) or [google groups](https://groups.google.com/groups?q=CommitTransaction).


---

<!-- page: win32transaction__CreateTransaction_meth.html -->

## win32transaction.CreateTransaction

 PyHANDLE = CreateTransaction(TransactionAttributes, UOW , CreateOptions , IsolationLevel , IsolationFlags , Timeout , Description )

Creates a transaction

#### Parameters

- TransactionAttributes=None : PySECURITY_ATTRIBUTES

 Security and inheritance for the transaction, can be None

- UOW=None : PyIID

 Reserved, use only None

- CreateOptions=0 : int

 TRANSACTION_DO_NOT_PROMOTE is only defined flag

- IsolationLevel=0 : int

 Reserved, use only 0

- IsolationFlags=0 : int

 Reserved, use only 0

- Timeout=0 : int

 Abort timeout in milliseconds

- Description=None : PyUnicode

 Text description of transaction, can be None

#### Win32 API References

- Search for CreateTransaction at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateTransaction), [google](https://www.google.com/search?q=CreateTransaction) or [google groups](https://groups.google.com/groups?q=CreateTransaction).


---

<!-- page: win32transaction__GetTransactionId_meth.html -->

## win32transaction.GetTransactionId

 PyIID = GetTransactionId(TransactionHandle)

Returns the transaction's GUID

#### Parameters

- TransactionHandle : PyHANDLE

 Handle to a transaction


---

<!-- page: win32transaction__OpenTransaction_meth.html -->

## win32transaction.OpenTransaction

 PyHANDLE = OpenTransaction(DesiredAccess, TransactionId )

Creates a handle to an existing transaction

#### Parameters

- DesiredAccess : int

 Combination of TRANSACTION_* access rights

- TransactionId : PyIID

 GUID identifying the transaction


---

<!-- page: win32transaction__RollbackTransactionAsync_meth.html -->

## win32transaction.RollbackTransactionAsync

 RollbackTransactionAsync(TransactionHandle)

Rolls back a transaction asynchronously

#### Parameters

- TransactionHandle : PyHANDLE

 Handle to a transaction

#### Win32 API References

- Search for RollbackTransactionAsync at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RollbackTransactionAsync), [google](https://www.google.com/search?q=RollbackTransactionAsync) or [google groups](https://groups.google.com/groups?q=RollbackTransactionAsync).


---

<!-- page: win32transaction__RollbackTransaction_meth.html -->

## win32transaction.RollbackTransaction

 RollbackTransaction(TransactionHandle)

Rolls back a transaction

#### Parameters

- TransactionHandle : PyHANDLE

 Handle to a transaction

#### Win32 API References

- Search for RollbackTransaction at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RollbackTransaction), [google](https://www.google.com/search?q=RollbackTransaction) or [google groups](https://groups.google.com/groups?q=RollbackTransaction).
