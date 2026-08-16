# 模块 perfmon

> 来源：https://mhammond.github.io/pywin32/perfmon.html （及其成员页，已全部内联）

## Module perfmon

 A module which wraps Performance Monitor functions.

#### Methods

- LoadPerfCounterTextStrings

- UnloadPerfCounterTextStrings

- CounterDefinition

 Creates a new PyPERF_COUNTER_DEFINITION object

- ObjectType

 Creates a new PyPERF_OBJECT_TYPE object

- PerfMonManager

 Creates a new PyPerfMonManager objects>


---

# perfmon 成员详细文档（共 5 项）


---

<!-- page: perfmon__CounterDefinition_meth.html -->

## perfmon.CounterDefinition

 PyPERF_COUNTER_DEFINITION = CounterDefinition()

Creates a new PyPERF_COUNTER_DEFINITION object


---

<!-- page: perfmon__LoadPerfCounterTextStrings_meth.html -->

## perfmon.LoadPerfCounterTextStrings

 LoadPerfCounterTextStrings()


---

<!-- page: perfmon__ObjectType_meth.html -->

## perfmon.ObjectType

 PyPERF_OBJECT_TYPE = ObjectType()

Creates a new PERF_OBJECT_TYPE object


---

<!-- page: perfmon__PerfMonManager_meth.html -->

## perfmon.PerfMonManager

 PyPerfMonManager = PerfMonManager(serviceName, seqPerfObTypes , mappingName , eventSourceName )

Creates a new PERF_OBJECT_TYPE object

#### Parameters

- serviceName : PyUnicode

 The name of the service for which data is being provided.

- seqPerfObTypes : [PyPERF_OBJECT_TYPE, ...]

 A sequence of objects to use in the performance monitor. At this stage, len(seqPerfObTypes) must == 1.

- mappingName=None : PyUnicode

 The name of the mapping to open. This must be the same as the DLL name providing the information. If None, the serviceName is used.

- eventSourceName=None : PyUnicode

 The name used by the DLL for error messages in the registry. If None, the serviceName is used.

#### Comments

 The application need not be a service, but it must have an entry in the Services section of the registry. This limits the performance monitor to being able to provide only one 'counter type', but still many counters within that type. See the documentation for the Performance Monitor API for more details.


---

<!-- page: perfmon__UnloadPerfCounterTextStrings_meth.html -->

## perfmon.UnloadPerfCounterTextStrings

 UnloadPerfCounterTextStrings()
