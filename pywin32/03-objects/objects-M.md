# pywin32 对象文档 · 分卷 M

> 共 1 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: MAPIINIT_0 -->


<!-- page: MAPIINIT_0.html -->

---

## MAPIINIT_0 Object

 A MAPIINIT_0 is represented as a tuple of:

#### Items

- [0] int : version

 This must be MAPI_INIT_VERSION.

- [1] int : flags

 MAPI initlization flags.

| | Value | Meaning
| |

---

 |

---

| | MAPI_MULTITHREAD_NOTIFICATIONS | MAPI should generate notifications using a thread dedicated to notification handling rather than the first thread used to call mapi::MAPIInitialize.
| | MAPI_NT_SERVICE | The caller is running as a NT service. Callers that are not running in a Windows NT service should not set this flag; callers that are running as a service must set this flag.

#### Comments

 Multithreaded clients should set MAPI_MULTITHREAD_NOTIFICATIONS flag so that they can receive notifications on threads other than the first thread to call mapi::MAPIInitialize.
