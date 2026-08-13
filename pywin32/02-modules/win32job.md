# 模块 win32job

> 来源：https://mhammond.github.io/pywin32/win32job.html （及其成员页，已全部内联）

## Module win32job

 An interface to the win32 Process and Thread API's,

#### Methods

- AssignProcessToJobObject

 Associates a process with an existing job object.

- CreateJobObject

 Creates or opens a job object.

- OpenJobObject

 Opens an existing job object.

- TerminateJobObject

 Terminates all processes currently associated with the job.

- UserHandleGrantAccess

 Grants or denies access to a handle to a User object to a job that has a user-interface restriction.

- IsProcessInJob

 Determines if the process is running in the specified job.

- QueryInformationJobObject

 Retrieves limit and job state information from the job object.

- SetInformationJobObject

 Sets quotas and limits for a job


---

# win32job 成员详细文档（共 8 项）


---

<!-- page: win32job__AssignProcessToJobObject_meth.html -->

## win32job.AssignProcessToJobObject

 AssignProcessToJobObject(hJob, hProcess)

Associates a process with an existing job object.

#### Parameters

- hJob : PyHANDLE

- hProcess : PyHANDLE


---

<!-- page: win32job__CreateJobObject_meth.html -->

## win32job.CreateJobObject

 CreateJobObject(jobAttributes, name)

Creates or opens a job object.

#### Parameters

- jobAttributes : PySECURITY_ATTRIBUTES

- name : unicode


---

<!-- page: win32job__IsProcessInJob_meth.html -->

## win32job.IsProcessInJob

 boolean = IsProcessInJob(hProcess, hJob )

Determines if the process is running in the specified job.

#### Parameters

- hProcess : PyHANDLE

 Handle to a process

- hJob : PyHANDLE

 Handle to a job, use None to check if process is part of any job


---

<!-- page: win32job__OpenJobObject_meth.html -->

## win32job.OpenJobObject

 OpenJobObject(desiredAccess, inheritHandles, name)

Opens an existing job object.

#### Parameters

- desiredAccess : int

- inheritHandles : bool

- name : unicode


---

<!-- page: win32job__QueryInformationJobObject_meth.html -->

## win32job.QueryInformationJobObject

 dict = QueryInformationJobObject(Job, JobObjectInfoClass )

Retrieves limit and job state information from the job object.

#### Parameters

- Job : PyHANDLE

 Handle to a job, use None for job that calling process is part of

- JobObjectInfoClass : int

 The type of data required, one of JobObject* values

| | JobObjectInfoClass | Type of information returned
| |

---

 |

---

| | JobObjectBasicAccountingInformation | Returns a dict representing a JOBOBJECT_BASIC_ACCOUNTING_INFORMATION struct
| | JobObjectBasicAndIoAccountingInformation | Returns a dict representing a JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION struct
| | JobObjectBasicLimitInformation | Returns a dict representing a JOBOBJECT_BASIC_LIMIT_INFORMATION struct
| | JobObjectExtendedLimitInformation | Returns a dict representing a JOBOBJECT_EXTENDED_LIMIT_INFORMATION struct
| | JobObjectEndOfJobTimeInformation | Returns a dict representing a JOBOBJECT_END_OF_JOB_TIME_INFORMATION struct
| | JobObjectBasicUIRestrictions | Returns a dict representing a JOBOBJECT_BASIC_UI_RESTRICTIONS struct
| | JobObjectBasicProcessIdList | Returns a sequence of pids of processes assigned to the job
| | JobObjectJobSetInformation | Returns a dict representing a JOBOBJECT_JOBSET_INFORMATION struct (not documented on MSDN)
| | JobObjectSecurityLimitInformation | JOBOBJECT_SECURITY_LIMIT_INFORMATION Not implemented
| | JobObjectAssociateCompletionPortInformation | JOBOBJECT_ASSOCIATE_COMPLETION_PORT Not implemented

#### Return Value

The type of the returned information is dependent on the class requested


---

<!-- page: win32job__SetInformationJobObject_meth.html -->

## win32job.SetInformationJobObject

 SetInformationJobObject(Job, JobObjectInfoClass, JobObjectInfo)

Sets quotas and limits for a job

#### Parameters

- Job : PyHANDLE

 Handle to a job

- JobObjectInfoClass : int

 The type of data required, one of JobObject* values

- JobObjectInfo : dict

 Dictionary containing info to be set, as returned by win32job::QueryInformationJobObject

| | JobObjectInfoClass | Type of information to be set
| |

---

 |

---

| | JobObjectBasicLimitInformation | A JOBOBJECT_BASIC_LIMIT_INFORMATION dict
| | JobObjectExtendedLimitInformation | dict representing a JOBOBJECT_EXTENDED_LIMIT_INFORMATION struct
| | JobObjectEndOfJobTimeInformation | dict representing a JOBOBJECT_END_OF_JOB_TIME_INFORMATION struct
| | JobObjectBasicUIRestrictions | dict representing a JOBOBJECT_BASIC_UI_RESTRICTIONS struct
| | JobObjectJobSetInformation | Input is a JOBOBJECT_JOBSET_INFORMATION dict - Not implemented
| | JobObjectSecurityLimitInformation | Input is a JOBOBJECT_SECURITY_LIMIT_INFORMATION dict - Not implemented
| | JobObjectAssociateCompletionPortInformation | Input is a JOBOBJECT_ASSOCIATE_COMPLETION_PORT dict - Not implemented


---

<!-- page: win32job__TerminateJobObject_meth.html -->

## win32job.TerminateJobObject

 TerminateJobObject(hJob, exitCode)

Terminates all processes currently associated with the job.

#### Parameters

- hJob : PyHANDLE

- exitCode : int


---

<!-- page: win32job__UserHandleGrantAccess_meth.html -->

## win32job.UserHandleGrantAccess

 UserHandleGrantAccess(hUserHandle, hJob, grant)

Grants or denies access to a handle to a User object to a job that has a user-interface restriction.

#### Parameters

- hUserHandle : PyHANDLE

- hJob : PyHANDLE

- grant : bool
