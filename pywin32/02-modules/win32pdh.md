# 模块 win32pdh

> 来源：https://mhammond.github.io/pywin32/win32pdh.html （及其成员页，已全部内联）

## Module win32pdh

 A module, encapsulating the Windows Performance Data Helpers API

#### Methods

- AddCounter

 Adds a new counter

- AddEnglishCounter

 Adds a counter to a query by its English name

- RemoveCounter

 Removes an open counter.

- EnumObjectItems

 Enumerates an object's items

- EnumObjects

 Enumerates objects

- OpenQuery

 Opens a new query

- CloseQuery

 Closes an open query.

- MakeCounterPath

 Makes a fully resolved counter path

- GetCounterInfo

 Retrieves information about a counter, such as data size, counter type, path, and user-supplied data values.

- GetFormattedCounterValue

 Retrieves a formatted counter value

- GetFormattedCounterValueArray

 Retrieves an array of formatted counter values

- CollectQueryData

 Collects the current raw data value for all counters in the specified query and updates the status code of each counter.

- ValidatePath

 Validates that the specified counter is present on the machine specified in the counter path.

- ExpandCounterPath

 Examines the specified machine (or local machine if none is specified) for counters and instances of counters that match the wild card strings in the counter path.

- ParseCounterPath

 Parses the elements of the counter path.

- ParseInstanceName

 Parses the elements of the instance name

- SetCounterScaleFactor

 Sets the scale factor that is applied to the calculated value of the specified counter when you request the formatted counter value.

- BrowseCounters

 Displays the counter browsing dialog box so that the user can select the counters to be returned to the caller.

- ConnectMachine

 connects to the specified machine, and creates and initializes a machine entry in the PDH DLL.

- LookupPerfIndexByName

 Returns the counter index corresponding to the specified counter name.

- LookupPerfNameByIndex

 Returns the performance object name corresponding to the specified index.


---

# win32pdh 成员详细文档（共 21 项）


---

<!-- page: win32pdh__AddCounter_meth.html -->

## win32pdh.AddCounter

 int = AddCounter(hQuery, path , userData )

Adds a new counter

#### Parameters

- hQuery : int

 Handle to an open query.

- path : string

 Full path to the performance data

- userData=0 : int

 User data associated with the counter.

#### Comments

 See also win32pdh::RemoveCounter


---

<!-- page: win32pdh__AddEnglishCounter_meth.html -->

## win32pdh.AddEnglishCounter

 int = AddEnglishCounter(hQuery, path , userData )

Adds a counter to a query by its English name

#### Parameters

- hQuery : int

 Handle to an open query.

- path : string

 Full counter path with standard English names.

- userData=0 : int

 User data associated with the counter.

#### Comments

 See also win32pdh::RemoveCounter

#### Return Value

Returns a handle to the counter


---

<!-- page: win32pdh__BrowseCounters_meth.html -->

## win32pdh.BrowseCounters

 string = BrowseCounters(Flags, hWndOwner , CallBack , DefaultDetailLevel , DialogBoxCaption , InitialPath , DataSource , ReturnMultiple , CallBackArg )

Displays the counter browsing dialog box so that the user can select the counters to be returned to the caller.

#### Parameters

- Flags : (boolean, ...)

 Sequence of boolean flags, or None. All default to False. (bIncludeInstanceIndex, bSingleCounterPerAdd, bSingleCounterPerDialog, bLocalCountersOnly, bWildCardInstances, bHideDetailBox, bInitializePath, bDisableMachineSelection, bIncludeCostlyObjects, bShowObjectBrowser)

- hWndOwner : PyHANDLE

 Parent for the dialog.

- CallBack : object

 A callable object to function as the callback.

- DefaultDetailLevel : int

 The default detail level to show on startup in the Detail Level combo box. If the Detail Level combo box is not shown, this is the detail level to use in filtering the displayed performance counters and objects.

- DialogBoxCaption=None : string

 The dialog caption, or None for default.

- InitialPath=None : str

 Counter to be selected initially, or None for default

- DataSource=None : str

 Name of a performance log file, or None for live counters

- ReturnMultiple=False : boolean

 Return all selected counter paths as a sequence of strings. Previously, this function only returned a single path even when multiple counters were selected.

- CallBackArg=None : object

 Extra argument to be passed to callback function. For backward compatibility, the callback will only receive a single argument if this is not given.


---

<!-- page: win32pdh__CloseQuery_meth.html -->

## win32pdh.CloseQuery

 CloseQuery(handle)

Closes a query

#### Parameters

- handle : int

 Handle to an open query.

#### Comments

 See also win32pdh::OpenQuery


---

<!-- page: win32pdh__CollectQueryData_meth.html -->

## win32pdh.CollectQueryData

 CollectQueryData(hQuery)

Collects the current raw data value for all counters in the specified query and updates the status code of each counter.

#### Parameters

- hQuery : int

 Handle to an open query.


---

<!-- page: win32pdh__ConnectMachine_meth.html -->

## win32pdh.ConnectMachine

 string = ConnectMachine(machineName)

connects to the specified machine, and creates and initializes a machine entry in the PDH DLL.

#### Parameters

- machineName : string

 The machine name.


---

<!-- page: win32pdh__EnumObjectItems_meth.html -->

## win32pdh.EnumObjectItems

 tuple = EnumObjectItems(DataSource, machine , object , detailLevel , flags )

Enumerates an object's items

#### Parameters

- DataSource : string

 Path of a performance log file, or None for machine counters

- machine : string

 The machine to use, or None

- object : string

 The type of object

- detailLevel : int

 The level of data required, win32pdh.PERF_DETAIL_*

- flags=0 : int

 Flags - must be zero


---

<!-- page: win32pdh__EnumObjects_meth.html -->

## win32pdh.EnumObjects

 list = EnumObjects(DataSource, machine , detailLevel , refresh )

Enumerates objects

#### Parameters

- DataSource : string

 Path to a performance log file, or None for machine counters

- machine : string

 The machine to use, or None

- detailLevel : int

 The level of data required.

- refresh=1 : int

 Should the list be refreshed.


---

<!-- page: win32pdh__ExpandCounterPath_meth.html -->

## win32pdh.ExpandCounterPath

 [string,] = ExpandCounterPath(wildCardPath)

Examines the specified machine (or local machine if none is specified) for counters and instances of counters that match the wild card strings in the counter path.

#### Parameters

- wildCardPath : string

 The counter path to expand.

#### Comments

 The counter path format is assumed to be:
\\machine\\object(parent/instance#index)\\countername
and the parent, instance, index, and countername elements may contain either a valid name or a wild card character.

 The API function leaks memory on Windows XP.


---

<!-- page: win32pdh__GetCounterInfo_meth.html -->

## win32pdh.GetCounterInfo

 GetCounterInfo(handle, bRetrieveExplainText)

Retrieves information about a counter, such as data size, counter type, path, and user-supplied data values.

#### Parameters

- handle : int

 The handle of the item to query

- bRetrieveExplainText : int

 Should explain text be retrieved?


---

<!-- page: win32pdh__GetFormattedCounterArray_meth.html -->

## win32pdh.GetFormattedCounterArray

 dictionary = GetFormattedCounterArray(handle, format )

Retrieves an array of formatted counter values

#### Parameters

- handle : int

 Handle to the counter

- format : int

 Format of result. Can be PDH_FMT_DOUBLE, PDH_FMT_LARGE, PDH_FMT_LONG and or'd with PDH_FMT_NOSCALE, PDH_FMT_1000


---

<!-- page: win32pdh__GetFormattedCounterValue_meth.html -->

## win32pdh.GetFormattedCounterValue

 (int,object) = GetFormattedCounterValue(handle, format )

Retrieves a formatted counter value

#### Parameters

- handle : int

 Handle to the counter

- format : int

 Format of result. Can be PDH_FMT_DOUBLE, PDH_FMT_LARGE, PDH_FMT_LONG and or'd with PDH_FMT_NOSCALE, PDH_FMT_1000


---

<!-- page: win32pdh__LookupPerfIndexByName_meth.html -->

## win32pdh.LookupPerfIndexByName

 int = LookupPerfIndexByName(machineName, instanceName )

Returns the counter index corresponding to the specified counter name.

#### Parameters

- machineName : string

 The name of the machine where the specified counter is located. The machine name can be specified by the DNS name or the IP address.

- instanceName : string

 The full name of the counter.


---

<!-- page: win32pdh__LookupPerfNameByIndex_meth.html -->

## win32pdh.LookupPerfNameByIndex

 string = LookupPerfNameByIndex(machineName, index )

Returns the performance object name corresponding to the specified index.

#### Parameters

- machineName : string

 The name of the machine where the specified counter is located. The machine name can be specified by the DNS name or the IP address.

- index : int

 The index of the performance object.


---

<!-- page: win32pdh__MakeCounterPath_meth.html -->

## win32pdh.MakeCounterPath

 MakeCounterPath(elements, flags)

Makes a fully resolved counter path

#### Parameters

- elements : (machineName, objectName, instanceName, parentInstance, instanceIndex, counterName)

 The elements to use to create the path.

- flags=0 : int

 PDH_PATH_WBEM_RESULT, PDH_PATH_WBEM_INPUT, or 0


---

<!-- page: win32pdh__OpenQuery_meth.html -->

## win32pdh.OpenQuery

 int = OpenQuery(DataSource, userData )

Opens a new query

#### Parameters

- DataSource=None : str

 Name of a performaance log file, or None for live data

- userData=0 : int

 User data associated with the query.

#### Comments

 See also win32pdh::CloseQuery


---

<!-- page: win32pdh__ParseCounterPath_meth.html -->

## win32pdh.ParseCounterPath

 (machineName, objectName, instanceName, parentInstance, instanceIndex, counterName) = ParseCounterPath(path, flags )

Parses the elements of the counter path.

#### Parameters

- path : string

 The counter path to parse.

- flags=0 : int

 Reserved - must be zero.


---

<!-- page: win32pdh__ParseInstanceName_meth.html -->

## win32pdh.ParseInstanceName

 (name, parent, instance) = ParseInstanceName(instanceName)

Parses the elements of the instance name

#### Parameters

- instanceName : string

 The instance name to parse.


---

<!-- page: win32pdh__RemoveCounter_meth.html -->

## win32pdh.RemoveCounter

 RemoveCounter(handle)

Removes a previously opened counter

#### Parameters

- handle : int

 Handle to an open counter.

#### Comments

 See also win32pdh::AddCounter


---

<!-- page: win32pdh__SetCounterScaleFactor_meth.html -->

## win32pdh.SetCounterScaleFactor

 SetCounterScaleFactor(hCounter, factor)

Sets the scale factor that is applied to the calculated value of the specified counter when you request the formatted counter value.

#### Parameters

- hCounter : int

 Handle to the counter.

- factor : int

 power of ten used to multiply value.


---

<!-- page: win32pdh__ValidatePath_meth.html -->

## win32pdh.ValidatePath

 int = ValidatePath(path)

Validates that the specified counter is present on the machine specified in the counter path.

#### Parameters

- path : string

 The counter path to validate.

#### Comments

 This method returns an integer result code. No exception is ever thrown. Zero result indicates success.
