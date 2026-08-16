# pywin32 对象文档 · 分卷 W

> 共 3 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: win32timezone.RangeMap -->


<!-- page: win32timezone.RangeMap.html -->

---

## win32timezone.RangeMap Object

 A dictionary-like object that uses the keys as bounds for a range. Inclusion of the value for that range is determined by the key_match_comparator, which defaults to less-than-or-equal. A value is returned for a key if it is the first key that matches in the sorted list of keys.

#### Comments

 One may supply keyword parameters to be passed to the sort function used to sort keys (i.e. key, reverse) as sort_params.

 Create a map that maps 1-3 -> 'a', 4-6 -> 'b'

```
>>> r = RangeMap({3: 'a', 6: 'b'})  # boy, that was easy



>>> r[1], r[2], r[3], r[4], r[5], r[6]



('a', 'a', 'a', 'b', 'b', 'b')






```

 Even float values should work so long as the comparison operator supports it.

```
>>> r[4.5]



'b'






```

 Notice that the way rangemap is defined, it must be open-ended on one side.

```
>>> r[0]



'a'



>>> r[-1]



'a'






```

 One can close the open-end of the RangeMap by using undefined_value

```
>>> r = RangeMap({0: RangeMap.undefined_value, 3: 'a', 6: 'b'})



>>> r[0]



Traceback (most recent call last):



...



KeyError: 0






```

 One can get the first or last elements in the range by using RangeMap.Item

```
>>> last_item = RangeMap.Item(-1)



>>> r[last_item]



'b'






```

 .last_item is a shortcut for Item(-1)

```
>>> r[RangeMap.last_item]



'b'






```

 Sometimes it's useful to find the bounds for a RangeMap

```
>>> r.bounds()



(0, 6)






```

 RangeMap supports .get(key, default)

```
>>> r.get(0, 'not found')



'not found'





>>> r.get(7, 'not found')



'not found'






```

 One often wishes to define the ranges by their left-most values, which requires use of sort params and a key_match_comparator.

```
>>> r = RangeMap({1: 'a', 4: 'b'},



...     sort_params=dict(reverse=True),



...     key_match_comparator=operator.ge)



>>> r[1], r[2], r[3], r[4], r[5], r[6]



('a', 'a', 'a', 'b', 'b', 'b')






```

 That wasn't nearly as easy as before, so an alternate constructor is provided:

```
>>> r = RangeMap.left({1: 'a', 4: 'b', 7: RangeMap.undefined_value})



>>> r[1], r[2], r[3], r[4], r[5], r[6]



('a', 'a', 'a', 'b', 'b', 'b')






```

#### Methods

- get

 Return the value for key if key is in the dictionary, else default.


<!-- page: win32timezone.RangeMap__get_meth.html -->

## win32timezone.RangeMap.get

 get()

Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.


<!-- page: win32timezone.RangeMap__get_meth_1.html -->

## win32timezone.RangeMap.get

 get(self, key, default)

Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

#### Parameters

- self :

 self

- key :

 key

- default=None :

 default


---

<!-- object: win32timezone.TimeZoneDefinition -->


<!-- page: win32timezone.TimeZoneDefinition.html -->

---

## win32timezone.TimeZoneDefinition Object

 A time zone definition class based on the win32 DYNAMIC_TIME_ZONE_INFORMATION structure.

#### Comments

 Describes a bias against UTC (bias), and two dates at which a separate additional bias applies (standard_bias and daylight_bias).

#### Methods

- current

 Windows Platform SDK GetTimeZoneInformation


<!-- page: win32timezone.TimeZoneDefinition__current_meth.html -->

## win32timezone.TimeZoneDefinition.current

 current()

Windows Platform SDK GetTimeZoneInformation


<!-- page: win32timezone.TimeZoneDefinition__current_meth_1.html -->

## win32timezone.TimeZoneDefinition.current

 current(cls)

Windows Platform SDK GetTimeZoneInformation

#### Parameters

- cls :

 cls


---

<!-- object: win32timezone.TimeZoneInfo -->


<!-- page: win32timezone.TimeZoneInfo.html -->

---

## win32timezone.TimeZoneInfo Object

 Main class for handling Windows time zones. Usage: TimeZoneInfo(<Time Zone Standard Name>, [<Fix Standard Time>])

#### Comments

 If <Fix Standard Time> evaluates to True, daylight savings time is calculated in the same way as standard time.

```
>>> tzi = TimeZoneInfo('Pacific Standard Time')



>>> march31 = datetime.datetime(2000,3,31)






```

 We know that time zone definitions haven't changed from 2007 to 2012, so regardless of whether dynamic info is available, there should be consistent results for these years.

```
>>> subsequent_years = [march31.replace(year=year)



...     for year in range(2007, 2013)]



>>> offsets = set(tzi.utcoffset(year) for year in subsequent_years)



>>> len(offsets)



1






```

 Cannot create a `TimeZoneInfo` with an invalid name.

```
>>> TimeZoneInfo('Does not exist')



Traceback (most recent call last):



...



ValueError: Timezone Name 'Does not exist' not found



>>> TimeZoneInfo(None)



Traceback (most recent call last):



...



ValueError: subkey name cannot be empty



>>> TimeZoneInfo("")



Traceback (most recent call last):



...



ValueError: subkey name cannot be empty






```

#### Methods

- tzname

 >>> MST = TimeZoneInfo('Mountain Standard Time')

- getWinInfo

 Return the most relevant "info" for this time zone

- utcoffset

 Calculates the utcoffset according to the datetime.tzinfo spec

- dst

 Calculate the daylight savings offset according to the

- GetDSTStartTime

 Given a year, determines the time when daylight savings time starts

- GetDSTEndTime

 Given a year, determines the time when daylight savings ends.

- local

 Returns the local time zone as defined by the operating system in the

- utc

 Returns a time-zone representing UTC.

- get_sorted_time_zone_names

 Return a list of time zone names that can

- get_sorted_time_zones

 Return the time zones sorted by some key.


<!-- page: win32timezone.TimeZoneInfo__GetDSTEndTime_meth.html -->

## win32timezone.TimeZoneInfo.GetDSTEndTime

 GetDSTEndTime()

Given a year, determines the time when daylight savings ends.


<!-- page: win32timezone.TimeZoneInfo__GetDSTEndTime_meth_1.html -->

## win32timezone.TimeZoneInfo.GetDSTEndTime

 GetDSTEndTime(self, year)

Given a year, determines the time when daylight savings ends.

#### Parameters

- self :

 self

- year :

 year


<!-- page: win32timezone.TimeZoneInfo__GetDSTStartTime_meth.html -->

## win32timezone.TimeZoneInfo.GetDSTStartTime

 GetDSTStartTime()

Given a year, determines the time when daylight savings time starts


<!-- page: win32timezone.TimeZoneInfo__GetDSTStartTime_meth_1.html -->

## win32timezone.TimeZoneInfo.GetDSTStartTime

 GetDSTStartTime(self, year)

Given a year, determines the time when daylight savings time starts

#### Parameters

- self :

 self

- year :

 year


<!-- page: win32timezone.TimeZoneInfo__dst_meth.html -->

## win32timezone.TimeZoneInfo.dst

 dst()

Calculate the daylight savings offset according to the datetime.tzinfo spec.


<!-- page: win32timezone.TimeZoneInfo__dst_meth_1.html -->

## win32timezone.TimeZoneInfo.dst

 dst(self, dt)

Calculate the daylight savings offset according to the datetime.tzinfo spec.

#### Parameters

- self :

 self

- dt :

 dt


<!-- page: win32timezone.TimeZoneInfo__getWinInfo_meth.html -->

## win32timezone.TimeZoneInfo.getWinInfo

 getWinInfo()

Return the most relevant "info" for this time zone in the target year.


<!-- page: win32timezone.TimeZoneInfo__getWinInfo_meth_1.html -->

## win32timezone.TimeZoneInfo.getWinInfo

 getWinInfo(self, targetYear)

Return the most relevant "info" for this time zone in the target year.

#### Parameters

- self :

 self

- targetYear :

 targetYear


<!-- page: win32timezone.TimeZoneInfo__get_sorted_time_zone_names_meth.html -->

## win32timezone.TimeZoneInfo.get_sorted_time_zone_names

 get_sorted_time_zone_names()

Return a list of time zone names that can be used to initialize TimeZoneInfo instances.


<!-- page: win32timezone.TimeZoneInfo__get_sorted_time_zone_names_meth_1.html -->

## win32timezone.TimeZoneInfo.get_sorted_time_zone_names

 get_sorted_time_zone_names()

Return a list of time zone names that can be used to initialize TimeZoneInfo instances.


<!-- page: win32timezone.TimeZoneInfo__get_sorted_time_zones_meth.html -->

## win32timezone.TimeZoneInfo.get_sorted_time_zones

 get_sorted_time_zones()

Return the time zones sorted by some key. key must be a function that takes a TimeZoneInfo object and returns a value suitable for sorting on. The key defaults to the bias (descending), as is done in Windows (see https://web.archive.org/web/20130723075340/http://blogs.msdn.com/b/michkap/archive/2006/12/22/1350684.aspx)


<!-- page: win32timezone.TimeZoneInfo__get_sorted_time_zones_meth_1.html -->

## win32timezone.TimeZoneInfo.get_sorted_time_zones

 get_sorted_time_zones(key)

Return the time zones sorted by some key. key must be a function that takes a TimeZoneInfo object and returns a value suitable for sorting on. The key defaults to the bias (descending), as is done in Windows (see https://web.archive.org/web/20130723075340/http://blogs.msdn.com/b/michkap/archive/2006/12/22/1350684.aspx)

#### Parameters

- key=None :

 key


<!-- page: win32timezone.TimeZoneInfo__local_meth.html -->

## win32timezone.TimeZoneInfo.local

 local()

Returns the local time zone as defined by the operating system in the registry.

#### Comments

 Now one can compare the results of the two offset aware values

```
>>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)



True






```

 Or use the newer `datetime.timezone.utc`

```
>>> now_UTC = datetime.datetime.now(datetime.timezone.utc)



>>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)



True





>>> localTZ = TimeZoneInfo.local()



>>> now_local = datetime.datetime.now(localTZ)



>>> now_UTC = datetime.datetime.utcnow()  # deprecated



>>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)



Traceback (most recent call last):



...



TypeError: can't subtract offset-naive and offset-aware datetimes





>>> now_UTC = now_UTC.replace(tzinfo = TimeZoneInfo('GMT Standard Time', True))






```


<!-- page: win32timezone.TimeZoneInfo__local_meth_1.html -->

## win32timezone.TimeZoneInfo.local

 local(cls)

Returns the local time zone as defined by the operating system in the registry.

#### Parameters

- cls :

 cls

#### Comments

 Now one can compare the results of the two offset aware values

```
>>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)



True






```

 Or use the newer `datetime.timezone.utc`

```
>>> now_UTC = datetime.datetime.now(datetime.timezone.utc)



>>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)



True





>>> localTZ = TimeZoneInfo.local()



>>> now_local = datetime.datetime.now(localTZ)



>>> now_UTC = datetime.datetime.utcnow()  # deprecated



>>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)



Traceback (most recent call last):



...



TypeError: can't subtract offset-naive and offset-aware datetimes





>>> now_UTC = now_UTC.replace(tzinfo = TimeZoneInfo('GMT Standard Time', True))






```


<!-- page: win32timezone.TimeZoneInfo__tzname_meth.html -->

## win32timezone.TimeZoneInfo.tzname

 tzname()

>>> MST = TimeZoneInfo('Mountain Standard Time') >>> MST.tzname(datetime.datetime(2003, 8, 2)) 'Mountain Daylight Time' >>> MST.tzname(datetime.datetime(2003, 11, 25)) 'Mountain Standard Time' >>> MST.tzname(None)


<!-- page: win32timezone.TimeZoneInfo__tzname_meth_1.html -->

## win32timezone.TimeZoneInfo.tzname

 tzname(self, dt)

>>> MST = TimeZoneInfo('Mountain Standard Time') >>> MST.tzname(datetime.datetime(2003, 8, 2)) 'Mountain Daylight Time' >>> MST.tzname(datetime.datetime(2003, 11, 25)) 'Mountain Standard Time' >>> MST.tzname(None)

#### Parameters

- self :

 self

- dt :

 dt


<!-- page: win32timezone.TimeZoneInfo__utc_meth.html -->

## win32timezone.TimeZoneInfo.utc

 utc()

Returns a time-zone representing UTC.

#### Comments

 Same as TimeZoneInfo('GMT Standard Time', True) but caches the result for performance.

```
>>> isinstance(TimeZoneInfo.utc(), TimeZoneInfo)



True






```


<!-- page: win32timezone.TimeZoneInfo__utc_meth_1.html -->

## win32timezone.TimeZoneInfo.utc

 utc(cls)

Returns a time-zone representing UTC.

#### Parameters

- cls :

 cls

#### Comments

 Same as TimeZoneInfo('GMT Standard Time', True) but caches the result for performance.

```
>>> isinstance(TimeZoneInfo.utc(), TimeZoneInfo)



True






```


<!-- page: win32timezone.TimeZoneInfo__utcoffset_meth.html -->

## win32timezone.TimeZoneInfo.utcoffset

 utcoffset()

Calculates the utcoffset according to the datetime.tzinfo spec


<!-- page: win32timezone.TimeZoneInfo__utcoffset_meth_1.html -->

## win32timezone.TimeZoneInfo.utcoffset

 utcoffset(self, dt)

Calculates the utcoffset according to the datetime.tzinfo spec

#### Parameters

- self :

 self

- dt :

 dt
