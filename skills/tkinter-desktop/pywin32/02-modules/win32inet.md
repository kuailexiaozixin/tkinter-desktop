# 模块 win32inet

> 来源：https://mhammond.github.io/pywin32/win32inet.html （及其成员页，已全部内联）

## Module win32inet

 An interface to the Windows internet (wininet) API

#### Methods

- InternetSetCookie

 Creates a cookie associated with the specified URL.

- InternetGetCookie

 Retrieves the cookie for the specified URL

- InternetAttemptConnect

 Attempts to make a connection to the Internet.

- InternetCheckConnection

 Allows an application to check if a connection to the Internet can be established

- InternetGoOnline

 Prompts the user for permission to initiate connection to a URL.

- InternetCloseHandle

- InternetConnect

 Opens an FTP, Gopher, or HTTP session for a given site.

- InternetOpen

 Initializes an application's use of the Microsoft® Win32® Internet functions.

- InternetOpenUrl

 Opens a resource specified by a complete FTP, Gopher, or HTTP URL.

- InternetCanonicalizeUrl

 Canonicalizes a URL, which includes converting unsafe characters and spaces into escape sequences.

- InternetGetLastResponseInfo

 Retrieves the last Win32® Internet function error description or server response on the thread calling this function.

- InternetReadFile

 Reads data from a handle opened by the win32inet::InternetOpenUrl, win32inet::FtpOpenFile, win32inet::GopherOpenFile , or win32inet::HttpOpenRequest function.

- InternetWriteFile

 Writes data to a handle opened by win32inet::FtpOpenFile.

- FtpOpenFile

 Initiates access to a remote file on an FTP server for reading or writing.

- FtpCommand

 Allows an application to send commands directly to an FTP server.

- InternetQueryOption

 Retrieves an option for an internet handle

- InternetSetOption

 Sets an option for an internet handle

- FindFirstUrlCacheEntry

 Initiates an enumeration of the browser cache

- FindNextUrlCacheEntry

 Continues enumeration of cached files

- FindFirstUrlCacheEntryEx

 Initiates an enumeration of the browser cache

- FindNextUrlCacheEntryEx

 Continues enumeration of cached files

- FindCloseUrlCache

 Closes a cache enumeration handle

- FindFirstUrlCacheGroup

 Initiates enumeration of Url cache groups

- FindNextUrlCacheGroup

 Continues enumeration of cache groups

- GetUrlCacheEntryInfo

 Retrieves cache info for a URL

- DeleteUrlCacheGroup

 Deletes a cache group

- CreateUrlCacheGroup

 Creates a new cache group

- CreateUrlCacheEntry

 Creates a cache entry for a URL

- CommitUrlCacheEntry

 Commits a cache entry

- SetUrlCacheEntryGroup

 Associates a cache entry with a group

- GetUrlCacheGroupAttribute

 Retrieves attributes for a cache group

- SetUrlCacheGroupAttribute

 Changes the attributes of a cache group

- DeleteUrlCacheEntry

 Deletes the cache entry for a URL


---

# win32inet 成员详细文档（共 37 项）


---

<!-- page: win32inet__CommitUrlCacheEntry_meth.html -->

## win32inet.CommitUrlCacheEntry

 str = CommitUrlCacheEntry(UrlName, LocalFileName , ExpireTime , LastModifiedTime , CacheEntryType , HeaderInfo , OriginalUrl )

Commits a cache entry

#### Parameters

- UrlName : str

 The Url for which to create an entry

- LocalFileName : str

 Filename returned from win32inet::CreateUrlCacheEntry. Can be None when creating a history entry.

- ExpireTime=None : PyDateTime

 Time at which entry expires

- LastModifiedTime=None : PyDateTime

 Modification time of URL

- CacheEntryType=NORMAL_CACHE_ENTRY : int

 Combination of *_CACHE_ENTRY flags

- HeaderInfo=None : str

 Header data used to request Url

- OriginalUrl=None : str

 If redirected, original site requested

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for CommitUrlCacheEntry at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CommitUrlCacheEntry), [google](https://www.google.com/search?q=CommitUrlCacheEntry) or [google groups](https://groups.google.com/groups?q=CommitUrlCacheEntry).


---

<!-- page: win32inet__CreateUrlCacheEntry_meth.html -->

## win32inet.CreateUrlCacheEntry

 str = CreateUrlCacheEntry(UrlName, ExpectedFileSize , FileExtension )

Creates a cache entry for a URL

#### Parameters

- UrlName : str

 The Url for which to create an entry

- ExpectedFileSize : int

 Size of content, use 0 if unknown

- FileExtension : str

 Extension to use for filename

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for CreateUrlCacheEntry at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateUrlCacheEntry), [google](https://www.google.com/search?q=CreateUrlCacheEntry) or [google groups](https://groups.google.com/groups?q=CreateUrlCacheEntry).

#### Return Value

Returns the filename to which content should be written


---

<!-- page: win32inet__CreateUrlCacheGroup_meth.html -->

## win32inet.CreateUrlCacheGroup

 long = CreateUrlCacheGroup(Flags)

Creates a new cache group

#### Parameters

- Flags=0 : int

 Combination of CACHEGROUP_FLAG_* flags

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for CreateUrlCacheGroup at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateUrlCacheGroup), [google](https://www.google.com/search?q=CreateUrlCacheGroup) or [google groups](https://groups.google.com/groups?q=CreateUrlCacheGroup).


---

<!-- page: win32inet__DeleteUrlCacheEntry_meth.html -->

## win32inet.DeleteUrlCacheEntry

 DeleteUrlCacheEntry(UrlName)

Deletes the cache entry for a URL

#### Parameters

- UrlName : str

 Cached url to be deleted


---

<!-- page: win32inet__DeleteUrlCacheGroup_meth.html -->

## win32inet.DeleteUrlCacheGroup

 DeleteUrlCacheGroup(GroupId, Attributes)

Deletes a cache group

#### Parameters

- GroupId : int

 Group id

- Attributes=CACHEGROUP_FLAG_FLUSHURL_ONDELETE : int

 Combination of CACHEGROUP_FLAG_* flags

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for DeleteUrlCacheGroup at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DeleteUrlCacheGroup), [google](https://www.google.com/search?q=DeleteUrlCacheGroup) or [google groups](https://groups.google.com/groups?q=DeleteUrlCacheGroup).


---

<!-- page: win32inet__FindCloseUrlCache_meth.html -->

## win32inet.FindCloseUrlCache

 FindCloseUrlCache(EnumHandle)

Closes a cache enumeration handle

#### Parameters

- EnumHandle : PyUrlCacheHANDLE

 Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntry

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for FindCloseUrlCache at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindCloseUrlCache), [google](https://www.google.com/search?q=FindCloseUrlCache) or [google groups](https://groups.google.com/groups?q=FindCloseUrlCache).


---

<!-- page: win32inet__FindFirstUrlCacheEntryEx_meth.html -->

## win32inet.FindFirstUrlCacheEntryEx

 (PyUrlCacheHANDLE, dict) = FindFirstUrlCacheEntryEx(SearchPattern, Flags , Filter , GroupId )

Initiates an enumeration of the browser cache

#### Parameters

- SearchPattern=None : str

 Type of entry to find, can be 'visited:', 'cookie:', or None

- Flags=0 : int

 None currently defined

- Filter=0 : int

 Types of entries to return, combination of *_CACHE_ENTRY values

- GroupId=0 : int

 Cache group to enumerate, use 0 for all

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for FindFirstUrlCacheEntryEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindFirstUrlCacheEntryEx), [google](https://www.google.com/search?q=FindFirstUrlCacheEntryEx) or [google groups](https://groups.google.com/groups?q=FindFirstUrlCacheEntryEx).

#### Return Value

Returns a handle that can be passed to win32inet::FindNextUrlCacheEntry, and a dict containing information for the first entry found. Throws error code ERROR_NO_MORE_ITEMS if no items are found.


---

<!-- page: win32inet__FindFirstUrlCacheEntry_meth.html -->

## win32inet.FindFirstUrlCacheEntry

 (PyUrlCacheHANDLE, dict) = FindFirstUrlCacheEntry(SearchPattern)

Initiates an enumeration of the browser cache

#### Parameters

- SearchPattern=None : str

 Type of entry to find, can be 'visited:', 'cookie:', or None

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for FindFirstUrlCacheEntry at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindFirstUrlCacheEntry), [google](https://www.google.com/search?q=FindFirstUrlCacheEntry) or [google groups](https://groups.google.com/groups?q=FindFirstUrlCacheEntry).

#### Return Value

Returns a handle that can be passed to win32inet::FindNextUrlCacheEntry, and a dict containing information for the first entry found. Throws error code ERROR_NO_MORE_ITEMS if no items are found.


---

<!-- page: win32inet__FindFirstUrlCacheGroup_meth.html -->

## win32inet.FindFirstUrlCacheGroup

 (PyUrlCacheHANDLE, int) = FindFirstUrlCacheGroup(Filter)

Initiates enumeration of Url cache groups

#### Parameters

- Filter=CACHEGROUP_SEARCH_ALL : int

 CACHEGROUP_SEARCH_*

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for FindFirstUrlCacheGroup at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindFirstUrlCacheGroup), [google](https://www.google.com/search?q=FindFirstUrlCacheGroup) or [google groups](https://groups.google.com/groups?q=FindFirstUrlCacheGroup).

#### Return Value

Returns a handle that can be passed to win32inet::FindNextUrlCacheGroup, and the id of the first group found.


---

<!-- page: win32inet__FindNextUrlCacheEntryEx_meth.html -->

## win32inet.FindNextUrlCacheEntryEx

 dict = FindNextUrlCacheEntryEx(EnumHandle)

Continues enumeration of cached files

#### Parameters

- EnumHandle : PyUrlCacheHANDLE

 Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntryEx

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for FindNextUrlCacheEntryEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindNextUrlCacheEntryEx), [google](https://www.google.com/search?q=FindNextUrlCacheEntryEx) or [google groups](https://groups.google.com/groups?q=FindNextUrlCacheEntryEx).

#### Return Value

Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct


---

<!-- page: win32inet__FindNextUrlCacheEntry_meth.html -->

## win32inet.FindNextUrlCacheEntry

 dict = FindNextUrlCacheEntry(EnumHandle)

Continues enumeration of cached files

#### Parameters

- EnumHandle : PyUrlCacheHANDLE

 Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntry

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for FindNextUrlCacheEntry at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindNextUrlCacheEntry), [google](https://www.google.com/search?q=FindNextUrlCacheEntry) or [google groups](https://groups.google.com/groups?q=FindNextUrlCacheEntry).

#### Return Value

Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct


---

<!-- page: win32inet__FindNextUrlCacheGroup_meth.html -->

## win32inet.FindNextUrlCacheGroup

 int = FindNextUrlCacheGroup(Find)

Continues enumeration of cache groups

#### Parameters

- Find : PyHANDLE

 Group enumeration handle as returned by win32inet::FindFirstUrlCacheGroup

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for FindNextUrlCacheGroup at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindNextUrlCacheGroup), [google](https://www.google.com/search?q=FindNextUrlCacheGroup) or [google groups](https://groups.google.com/groups?q=FindNextUrlCacheGroup).


---

<!-- page: win32inet__FtpCommand_meth.html -->

## win32inet.FtpCommand

 PyHINTERNET = FtpCommand(Connect, ExpectResponse , Flags , Command , Context )

Allows an application to send commands directly to an FTP server.

#### Parameters

- Connect : PyHINTERNET

 Valid HINTERNET handle to an FTP session.

- ExpectResponse : bool

 Boolean value that indicates whether or not the application expects a response from the FTP server. This must be set to True if a response is expected, or False otherwise.

- Flags : int

 Unsigned long integer value that contains the flags that control this function. This can be set to either FTP_TRANSFER_TYPE_ASCII or FTP_TRANSFER_TYPE_BINARY

- Command : string

 The command to send to the FTP server.

- Context=None : object

 Arbitrary object to be passed to callback

#### Comments

 This function may cause a crash on 32-bit due to an internal error in win32inet.dll. (last checked on Vista)

 Accepts keyword args


---

<!-- page: win32inet__FtpOpenFile_meth.html -->

## win32inet.FtpOpenFile

 PyHINTERNET = FtpOpenFile(hConnect, FileName , Access , Flags , Context )

Initiates access to a remote file on an FTP server for reading or writing.

#### Parameters

- hConnect : PyHINTERNET

 Valid HINTERNET handle to an FTP session.

- FileName : string

 The name of the file to access on the remote system.

- Access : int

 Integer value that determines how the file will be accessed. This can be GENERIC_READ or GENERIC_WRITE, but not both.

- Flags : int

 Integer value that contains the conditions under which the transfers occur. The application should select one transfer type and any of the flags that indicate how the caching of the file will be controlled. The transfer type can be one of the FTP_TRANSFER_TYPE* values

- Context=None : object

 Arbitrary object that will be passed to handle's callback function

#### Comments

 Accepts keyword args


---

<!-- page: win32inet__GetUrlCacheEntryInfo_meth.html -->

## win32inet.GetUrlCacheEntryInfo

 dict = GetUrlCacheEntryInfo(UrlName)

Retrieves cache info for a URL

#### Parameters

- UrlName : str

 Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntry

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for GetUrlCacheEntryInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetUrlCacheEntryInfo), [google](https://www.google.com/search?q=GetUrlCacheEntryInfo) or [google groups](https://groups.google.com/groups?q=GetUrlCacheEntryInfo).

#### Return Value

Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct


---

<!-- page: win32inet__GetUrlCacheGroupAttribute_meth.html -->

## win32inet.GetUrlCacheGroupAttribute

 dict = GetUrlCacheGroupAttribute(GroupId, Attributes )

Retrieves attributes for a cache group

#### Parameters

- GroupId : int

 Group id

- Attributes=CACHEGROUP_ATTRIBUTE_GET_ALL : int

 Attributes to retrieve, CACHEGROUP_ATTRIBUTE_*

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for GetUrlCacheGroupAttribute at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetUrlCacheGroupAttribute), [google](https://www.google.com/search?q=GetUrlCacheGroupAttribute) or [google groups](https://groups.google.com/groups?q=GetUrlCacheGroupAttribute).

#### Return Value

Returns a dict representing a INTERNET_CACHE_GROUP_INFO struct


---

<!-- page: win32inet__InternetAttemptConnect_meth.html -->

## win32inet.InternetAttemptConnect

 InternetAttemptConnect(Reserved)

Attempts to make a connection to the Internet.

#### Parameters

- Reserved=0 : int

 Use only 0.


---

<!-- page: win32inet__InternetCanonicalizeUrl_meth.html -->

## win32inet.InternetCanonicalizeUrl

 string = InternetCanonicalizeUrl(url, flags )

Canonicalizes a URL, which includes converting unsafe characters and spaces into escape sequences.

#### Parameters

- url : string

 The URL to canonicalize.

- flags=0 : int

 integer value that contains the flags that control canonicalization. This can be one of the following values:

| | ICU_BROWSER_MODE | Does not encode or decode characters after "#" or "?", and does not remove trailing white space after "?". If this value is not specified, the entire URL is encoded and trailing white space is removed.
| | ICU_DECODE | Converts all %XX sequences to characters, including escape sequences, before the URL is parsed.
| | ICU_ENCODE_PERCENT | Encodes any percent signs encountered. By default, percent signs are not encoded.
| | ICU_ENCODE_SPACES_ONLY | Encodes spaces only.
| | ICU_NO_ENCODE | Does not convert unsafe characters to escape sequences.
| | ICU_NO_META | Does not remove meta sequences (such as "." and "..") from the URL. If no flags are specified (dwFlags = 0), the function converts all unsafe characters and meta sequences (such as .,\\ .., and ...) to escape sequences.


---

<!-- page: win32inet__InternetCheckConnection_meth.html -->

## win32inet.InternetCheckConnection

 InternetCheckConnection(Url, Flags, Reserved)

Allows an application to check if a connection to the Internet can be established

#### Parameters

- Url : string

 Url to attempt to connect to, can be None

- Flags=0 : int

 FLAG_ICC_FORCE_CONNECTION is only defined flag

- Reserved=0 : int

 Use only 0.


---

<!-- page: win32inet__InternetCloseHandle_meth.html -->

## win32inet.InternetCloseHandle

 InternetCloseHandle(handle)

#### Parameters

- handle : PyHINTERNET

#### Comments

 It should not be necessary to call this function - all handles are PyHINTERNET objects, so can have their Close method called, and will otherwise be automatically closed.


---

<!-- page: win32inet__InternetConnect_meth.html -->

## win32inet.InternetConnect

 InternetConnect(Internet, ServerName, ServerPort, Username, Password, Service, Flags, Context)

Opens an FTP, Gopher, or HTTP session for a given site.

#### Parameters

- Internet : PyHINTERNET

 Valid HINTERNET handle returned by a previous call to win32inet::InternetOpen.

- ServerName : string

 A string that contains the host name of an Internet server. Alternately, the string can contain the IP number of the site, in ASCII dotted-decimal format (for example, 11.0.1.45).

- ServerPort : int

 Number of the TCP/IP port on the server to connect to. These flags set only the port that will be used. The service is set by the value of dwService. This can be one of the INTERNET_DEFAULT_*_PORT constants or INTERNET_INVALID_PORT_NUMBER, which uses the default port for the service specified by dwService.

- Username : string

 A string that contains the name of the user to log on. If this parameter is None, the function uses an appropriate default, except for HTTP; a NULL parameter in HTTP causes the server to return an error. For the FTP protocol, the default is "anonymous".

- Password : string

 Address of a null-terminated string that contains the password to use to log on. If both Password and Username are None, the function uses the default "anonymous" password. In the case of FTP, the default password is the user's e-mail name. If lpszPassword is None, but lpszUsername is not None, the function uses a blank password.

- Service : int

 Iinteger value that contains the type of service to access. This can be one of INTERNET_SERVICE_FTP, INTERNET_SERVICE_GOPHER, or INTERNET_SERVICE_HTTP.

- Flags : int

 Integer value that contains the flags specific to the service used. When the value of dwService is INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE causes the application to use passive FTP semantics.

- Context=None : object

 Arbitrary object to be passed to callback function

#### Comments

 Accepts keyword args


---

<!-- page: win32inet__InternetGetCookie_meth.html -->

## win32inet.InternetGetCookie

 string = InternetGetCookie(Url, CookieName )

Retrieves the cookie for the specified URL

#### Parameters

- Url : string

 Site for which to retrieve cookie

- CookieName : string

 Name of cookie (documented on MSDN as not implemented)


---

<!-- page: win32inet__InternetGetLastResponseInfo_meth.html -->

## win32inet.InternetGetLastResponseInfo

 int, string = InternetGetLastResponseInfo()

Retrieves the last Win32® Internet function error description or server response on the thread calling this function.


---

<!-- page: win32inet__InternetGoOnline_meth.html -->

## win32inet.InternetGoOnline

 InternetGoOnline(Url, Parent, Flags)

Prompts the user for permission to initiate connection to a URL.

#### Parameters

- Url : string

 Web site to connect to

- Parent=None : int

 Handle to parent window

- Flags=0 : int

 INTERNET_GOONLINE_REFRESH is only available flag


---

<!-- page: win32inet__InternetOpenUrl_meth.html -->

## win32inet.InternetOpenUrl

 PyHINTERNET = InternetOpenUrl(Internet, Url , Headers , Flags , Context )

Opens a resource specified by a complete FTP, Gopher, or HTTP URL.

#### Parameters

- Internet : PyHINTERNET

 Internet handle as returned by win32inet::InternetOpen

- Url : string

 A string that contains the URL to begin reading. Only URLs beginning with ftp:, gopher:, http:, or https: are supported.

- Headers=None : string

 a string variable that contains the headers to be sent to the HTTP server.

- Flags=0 : int

 INTERNET_FLAG_*

- Context=None : object

 An arbitrary object to be passed to the status callback function

#### Comments

 Accepts keyword args.

#### Return Value

Returns None in async mode (Internet handle created with INTERNET_FLAG_ASYNC). When handle is created, it will be passed to callback function of parent handle.


---

<!-- page: win32inet__InternetOpen_meth.html -->

## win32inet.InternetOpen

 InternetOpen(agent, proxyName, proxyBypass, flags)

Initializes an application's use of the Microsoft® Win32® Internet functions.

#### Parameters

- agent : string

 A string that contains the name of the application or entity calling the Internet functions. This name is used as the user agent in the HTTP protocol.

- proxyName : string

- proxyBypass : string

- flags : int

 Combination of INTERNET_FLAG_ASYNC,INTERNET_FLAG_FROM_CACHE, or INTERNET_FLAG_OFFLINE


---

<!-- page: win32inet__InternetQueryOption_meth.html -->

## win32inet.InternetQueryOption

 object = InternetQueryOption(hInternet, Option )

Retrieves an option for an internet handle

#### Parameters

- hInternet : PyHINTERNET

 Internet handle, or None for global defaults

- Option : int

 INTERNET_OPTION_* value

| | Option | Returned type
| |

---

 |

---

| | INTERNET_OPTION_CALLBACK | Python callback function
| | INTERNET_OPTION_CONTEXT_VALUE | Context object
| | INTERNET_OPTION_SEND_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_CONTROL_SEND_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_RECEIVE_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_CONTROL_RECEIVE_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_CODEPAGE | Int - Codepage of host part of URL
| | INTERNET_OPTION_CODEPAGE_PATH | Int - Codepage for URL
| | INTERNET_OPTION_CODEPAGE_EXTRA | Int - Codepage for path part of URL
| | INTERNET_OPTION_CONNECT_RETRIES | Int - Number of time to try to reconnect to host
| | INTERNET_OPTION_CONNECT_TIMEOUT | Int - Connection timeout in milliseconds
| | INTERNET_OPTION_CONNECTED_STATE | Int - Connection state, INTERNET_STATE_*
| | INTERNET_OPTION_HANDLE_TYPE | Int, INTERNET_HANDLE_TYPE_*
| | INTERNET_OPTION_ERROR_MASK | Int, combination of INTERNET_ERROR_MASK_*
| | INTERNET_OPTION_EXTENDED_ERROR | Int, ERROR_INTERNET_*
| | INTERNET_OPTION_FROM_CACHE_TIMEOUT | Int - Timeout in ms before cached copy is used
| | INTERNET_OPTION_IDN | Int, INTERNET_FLAG_IDN_*
| | INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVER | Int
| | INTERNET_OPTION_MAX_CONNS_PER_SERVER | Int
| | INTERNET_OPTION_READ_BUFFER_SIZE | Int
| | INTERNET_OPTION_WRITE_BUFFER_SIZE | Int
| | INTERNET_OPTION_REQUEST_FLAGS | Int, combination of INTERNET_REQFLAG_*
| | INTERNET_OPTION_REQUEST_PRIORITY | Int
| | INTERNET_OPTION_SECURITY_FLAGS | Int, SECURITY_FLAG_*
| | INTERNET_OPTION_SECURITY_KEY_BITNESS | Int
| | INTERNET_OPTION_BYPASS_EDITED_ENTRY | Boolean
| | INTERNET_OPTION_HTTP_DECODING | Boolean
| | INTERNET_OPTION_IGNORE_OFFLINE | Boolean
| | INTERNET_OPTION_DATAFILE_NAME | String - Name of internet cache file
| | INTERNET_OPTION_USERNAME | String - Username passed to InternetConnect
| | INTERNET_OPTION_PASSWORD | String - Password passed to InternetConnect
| | INTERNET_OPTION_PROXY_PASSWORD | String
| | INTERNET_OPTION_PROXY_USERNAME | String
| | INTERNET_OPTION_SECONDARY_CACHE_KEY | String
| | INTERNET_OPTION_SECURITY_CERTIFICATE | String
| | INTERNET_OPTION_URL | String
| | INTERNET_OPTION_USER_AGENT | String
| | INTERNET_OPTION_CACHE_TIMESTAMPS | dict - Expiration and last modified times
| | INTERNET_OPTION_HTTP_VERSION | dict - HTTP_VERSION_INFO
| | INTERNET_OPTION_VERSION | dict - INTERNET_VERSION_INFO
| | INTERNET_OPTION_PARENT_HANDLE | PyHINTERNET
| | INTERNET_OPTION_PROXY | dict - INTERNET_PROXY_INFO
| | INTERNET_OPTION_DIAGNOSTIC_SOCKET_INFO | Not yet supported (INTERNET_DIAGNOSTIC_SOCKET_INFO)
| | INTERNET_OPTION_PER_CONNECTION_OPTION | Not yet supported (INTERNET_PER_CONN_OPTION_LIST)
| | INTERNET_OPTION_SECURITY_CERTIFICATE_STRUCT | Not yet supported (INTERNET_CERTIFICATE_INFO)
| | INTERNET_OPTION_ALTER_IDENTITY | Not supported
| | INTERNET_OPTION_ASYNC | Not supported
| | INTERNET_OPTION_ASYNC_ID | Not supported
| | INTERNET_OPTION_ASYNC_PRIORITY | Not supported
| | INTERNET_OPTION_CACHE_STREAM_HANDLE | Not supported
| | INTERNET_OPTION_CALLBACK_FILTER | Not supported
| | INTERNET_OPTION_CLIENT_CERT_CONTEXT | Not supported
| | INTERNET_OPTION_DATA_RECEIVE_TIMEOUT | Not supported
| | INTERNET_OPTION_DATA_SEND_TIMEOUT | Not supported
| | INTERNET_OPTION_CONNECT_BACKOFF | Not supported
| | INTERNET_OPTION_CONNECT_TIME | Not supported
| | INTERNET_OPTION_DISABLE_AUTODIAL | Not supported
| | INTERNET_OPTION_DISCONNECTED_TIMEOUT | Not supported
| | INTERNET_OPTION_IDENTITY | Not supported
| | INTERNET_OPTION_IDLE_STATE | Not supported
| | INTERNET_OPTION_KEEP_CONNECTION | Not supported
| | INTERNET_OPTION_LISTEN_TIMEOUT | Not supported
| | INTERNET_OPTION_OFFLINE_MODE | Not supported
| | INTERNET_OPTION_OFFLINE_SEMANTICS | Not supported
| | INTERNET_OPTION_POLICY | Not supported
| | INTERNET_OPTION_RECEIVE_THROUGHPUT | Not supported
| | INTERNET_OPTION_REMOVE_IDENTITY | Not supported
| | INTERNET_OPTION_SEND_THROUGHPUT | Not supported
| | INTERNET_OPTION_DATAFILE_EXT | Only valid for InternetSetOption
| | INTERNET_OPTION_DIGEST_AUTH_UNLOAD | Only valid for InternetSetOption
| | INTERNET_OPTION_END_BROWSER_SESSION | Only valid for InternetSetOption
| | INTERNET_OPTION_REFRESH | Only valid for InternetSetOption
| | INTERNET_OPTION_RESET_URLCACHE_SESSION | Only valid for InternetSetOption
| | INTERNET_OPTION_SETTINGS_CHANGED | Only valid for InternetSetOption

#### Win32 API References

- Search for InternetQueryOption at [msdn](https://learn.microsoft.com/en-ca/search/?terms=InternetQueryOption), [google](https://www.google.com/search?q=InternetQueryOption) or [google groups](https://groups.google.com/groups?q=InternetQueryOption).

#### Return Value

The type of object returned is dependent on the option requested


---

<!-- page: win32inet__InternetReadFile_meth.html -->

## win32inet.InternetReadFile

 string = InternetReadFile(hInternet, size )

Reads data from a handle opened by the win32inet::InternetOpenUrl, win32inet::FtpOpenFile, win32inet::GopherOpenFile , or win32inet::HttpOpenRequest function.

#### Parameters

- hInternet : PyHINTERNET

- size : int

 Number of bytes to read.

#### Return Value

The result will be a string of zero bytes when the end is reached.


---

<!-- page: win32inet__InternetSetCookie_meth.html -->

## win32inet.InternetSetCookie

 InternetSetCookie(url, lpszCookieName, data)

Creates a cookie associated with the specified URL.

#### Parameters

- url : string

- lpszCookieName : string

- data : string


---

<!-- page: win32inet__InternetSetOption_meth.html -->

## win32inet.InternetSetOption

 InternetSetOption(hInternet, Option, Buffer)

Sets an option for an internet handle

#### Parameters

- hInternet : PyHINTERNET

 Internet handle, or None for global defaults

- Option : int

 The option to set, INTERNET_OPTION_*

- Buffer : object

 Type is dependent on Option

| | Option | Type of input object
| |

---

 |

---

| | INTERNET_OPTION_CALLBACK | Python function called on status change
| | INTERNET_OPTION_CONTEXT_VALUE | Any Python object to be passed to callback function
| | INTERNET_OPTION_SEND_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_CONTROL_SEND_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_RECEIVE_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_CONTROL_RECEIVE_TIMEOUT | Int - timeout in millseconds
| | INTERNET_OPTION_CODEPAGE | Int - Codepage of host part of URL
| | INTERNET_OPTION_CODEPAGE_PATH | Codepage for URL
| | INTERNET_OPTION_CODEPAGE_EXTRA | Int - Codepage for path part of URL
| | INTERNET_OPTION_CONNECT_RETRIES | Int - Number of time to try to reconnect to host
| | INTERNET_OPTION_CONNECT_TIMEOUT | Int - Connection timeout in milliseconds
| | INTERNET_OPTION_CONNECTED_STATE | Int - Connection state, INTERNET_STATE_*
| | INTERNET_OPTION_ERROR_MASK | Int, combination of INTERNET_ERROR_MASK_*
| | INTERNET_OPTION_FROM_CACHE_TIMEOUT | Int - Timeout in ms before cached copy is used
| | INTERNET_OPTION_IDN | Int, INTERNET_FLAG_IDN_*
| | INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVER | Int
| | INTERNET_OPTION_MAX_CONNS_PER_SERVER | Int
| | INTERNET_OPTION_READ_BUFFER_SIZE | Int
| | INTERNET_OPTION_WRITE_BUFFER_SIZE | Int
| | INTERNET_OPTION_REQUEST_PRIORITY | Int
| | INTERNET_OPTION_DIGEST_AUTH_UNLOAD | None
| | INTERNET_OPTION_END_BROWSER_SESSION | None
| | INTERNET_OPTION_REFRESH | None
| | INTERNET_OPTION_RESET_URLCACHE_SESSION | None
| | INTERNET_OPTION_SETTINGS_CHANGED | None
| | INTERNET_OPTION_BYPASS_EDITED_ENTRY | Boolean
| | INTERNET_OPTION_HTTP_DECODING | Boolean
| | INTERNET_OPTION_IGNORE_OFFLINE | Boolean
| | INTERNET_OPTION_USERNAME | String - Username passed to InternetConnect
| | INTERNET_OPTION_PASSWORD | String - Password passed to InternetConnect
| | INTERNET_OPTION_PROXY_PASSWORD | String
| | INTERNET_OPTION_PROXY_USERNAME | String
| | INTERNET_OPTION_SECONDARY_CACHE_KEY | String
| | INTERNET_OPTION_USER_AGENT | String
| | INTERNET_OPTION_DATAFILE_EXT | String - Extension to use for download cache file
| | INTERNET_OPTION_PROXY | Dict representing INTERNET_PROXY_INFO struct
| | INTERNET_OPTION_HTTP_VERSION | Not yet supported - HTTP_VERSION_INFO
| | INTERNET_OPTION_PER_CONNECTION_OPTION | Not yet supported (INTERNET_PER_CONN_OPTION_LIST)
| | INTERNET_OPTION_ALTER_IDENTITY | Not supported
| | INTERNET_OPTION_ASYNC | Not supported
| | INTERNET_OPTION_ASYNC_ID | Not supported
| | INTERNET_OPTION_ASYNC_PRIORITY | Not supported
| | INTERNET_OPTION_CACHE_STREAM_HANDLE | Not supported
| | INTERNET_OPTION_CALLBACK_FILTER | Not supported
| | INTERNET_OPTION_CLIENT_CERT_CONTEXT | Not supported
| | INTERNET_OPTION_DATA_RECEIVE_TIMEOUT | Not supported
| | INTERNET_OPTION_DATA_SEND_TIMEOUT | Not supported
| | INTERNET_OPTION_CONNECT_BACKOFF | Not supported
| | INTERNET_OPTION_CONNECT_TIME | Not supported
| | INTERNET_OPTION_DISABLE_AUTODIAL | Not supported
| | INTERNET_OPTION_DISCONNECTED_TIMEOUT | Not supported
| | INTERNET_OPTION_IDENTITY | Not supported
| | INTERNET_OPTION_IDLE_STATE | Not supported
| | INTERNET_OPTION_KEEP_CONNECTION | Not supported
| | INTERNET_OPTION_LISTEN_TIMEOUT | Not supported
| | INTERNET_OPTION_OFFLINE_MODE | Not supported
| | INTERNET_OPTION_OFFLINE_SEMANTICS | Not supported
| | INTERNET_OPTION_POLICY | Not supported
| | INTERNET_OPTION_RECEIVE_THROUGHPUT | Not supported
| | INTERNET_OPTION_REMOVE_IDENTITY | Not supported
| | INTERNET_OPTION_SEND_THROUGHPUT | Not supported
| | INTERNET_OPTION_CACHE_TIMESTAMPS | Only valid for InternetQueryOption
| | INTERNET_OPTION_HANDLE_TYPE | Only valid for InternetQueryOption
| | INTERNET_OPTION_DATAFILE_NAME | Only valid for InternetQueryOption
| | INTERNET_OPTION_PARENT_HANDLE | Only valid for InternetQueryOption
| | INTERNET_OPTION_SECURITY_CERTIFICATE | Only valid for InternetQueryOption
| | INTERNET_OPTION_SECURITY_CERTIFICATE_STRUCT | Only valid for InternetQueryOption
| | INTERNET_OPTION_SECURITY_FLAGS | Only valid for InternetQueryOption
| | INTERNET_OPTION_SECURITY_KEY_BITNESS | Only valid for InternetQueryOption
| | INTERNET_OPTION_DIAGNOSTIC_SOCKET_INFO | Only valid for InternetQueryOption
| | INTERNET_OPTION_VERSION | Only valid for InternetQueryOption
| | INTERNET_OPTION_EXTENDED_ERROR | Only valid for InternetQueryOption
| | INTERNET_OPTION_REQUEST_FLAGS | Only valid for InternetQueryOption
| | INTERNET_OPTION_URL | Only valid for InternetQueryOption

#### Win32 API References

- Search for InternetSetOption at [msdn](https://learn.microsoft.com/en-ca/search/?terms=InternetSetOption), [google](https://www.google.com/search?q=InternetSetOption) or [google groups](https://groups.google.com/groups?q=InternetSetOption).


---

<!-- page: win32inet__InternetWriteFile_meth.html -->

## win32inet.InternetWriteFile

 int = InternetWriteFile(File, Buffer )

Writes data to a handle opened by win32inet::FtpOpenFile.

#### Parameters

- File : PyHINTERNET

 Writeable internet handle

- Buffer : string

 String or buffer containing data to be written


---

<!-- page: win32inet__SetUrlCacheEntryGroup_meth.html -->

## win32inet.SetUrlCacheEntryGroup

 SetUrlCacheEntryGroup(UrlName, Flags, GroupId)

Associates a cache entry with a group

#### Parameters

- UrlName : str

 Url whose cache is to be added to the group

- Flags : int

 INTERNET_CACHE_GROUP_ADD or INTERNET_CACHE_GROUP_REMOVE

- GroupId : int

 Id of a cache group

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for SetUrlCacheEntryGroup at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetUrlCacheEntryGroup), [google](https://www.google.com/search?q=SetUrlCacheEntryGroup) or [google groups](https://groups.google.com/groups?q=SetUrlCacheEntryGroup).


---

<!-- page: win32inet__SetUrlCacheGroupAttribute_meth.html -->

## win32inet.SetUrlCacheGroupAttribute

 SetUrlCacheGroupAttribute(GroupId, Attributes, GroupInfo, Flags)

Changes the attributes of a cache group

#### Parameters

- GroupId : int

 Id of a cache group

- Attributes : int

 Bitmask of CACHEGROUP_ATTRIBUTE_* flags indicating which attributes to set

- GroupInfo : dict

 INTERNET_CACHE_GROUP_INFO dict as returned by win32inet::GetUrlCacheGroupAttribute

- Flags=0 : int

 Reserved, use 0

#### Comments

 Accepts keyword args

#### Win32 API References

- Search for SetUrlCacheGroupAttribute at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetUrlCacheGroupAttribute), [google](https://www.google.com/search?q=SetUrlCacheGroupAttribute) or [google groups](https://groups.google.com/groups?q=SetUrlCacheGroupAttribute).


---

<!-- page: win32inet__WinHttpGetDefaultProxyConfiguration_meth.html -->

## win32inet.WinHttpGetDefaultProxyConfiguration

 PyWINHTTP_PROXY_INFO = WinHttpGetDefaultProxyConfiguration()

Retrieves the default WinHTTP proxy configuration from the registry.


---

<!-- page: win32inet__WinHttpGetIEProxyConfigForCurrentUser_meth.html -->

## win32inet.WinHttpGetIEProxyConfigForCurrentUser

 tuple = WinHttpGetIEProxyConfigForCurrentUser()

Obtains the Internet Explorer proxy configuration for the current user.

#### Win32 API References

- Search for WinHttpGetIEProxyConfigForCurrentUser at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WinHttpGetIEProxyConfigForCurrentUser), [google](https://www.google.com/search?q=WinHttpGetIEProxyConfigForCurrentUser) or [google groups](https://groups.google.com/groups?q=WinHttpGetIEProxyConfigForCurrentUser).

- Search for WINHTTP_CURRENT_USER_IE_PROXY_CONFIG at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WINHTTP_CURRENT_USER_IE_PROXY_CONFIG), [google](https://www.google.com/search?q=WINHTTP_CURRENT_USER_IE_PROXY_CONFIG) or [google groups](https://groups.google.com/groups?q=WINHTTP_CURRENT_USER_IE_PROXY_CONFIG).

#### Return Value

The result is a windows WINHTTP_CURRENT_USER_IE_PROXY_CONFIG structure; a tuple of an int (bool) and 3 unicode strings (fAutoDetect, lpszAutoConfigUrl, lpszProxy, lpszProxyBypass).


---

<!-- page: win32inet__WinHttpGetProxyForUrl_meth.html -->

## win32inet.WinHttpGetProxyForUrl

 PyWINHTTP_PROXY_INFO = WinHttpGetProxyForUrl(handle, url , options )

Obtains the Internet Explorer proxy configuration for the specified URL.

#### Parameters

- handle : HANDLE /int

- url : unicode/string

- options : PyWINHTTP_AUTOPROXY_OPTIONS


---

<!-- page: win32inet__WinHttpOpen_meth.html -->

## win32inet.WinHttpOpen

 PyHINTERNET = WinHttpOpen(lpszUserAgent, dwAccessType , lpszProxyName , lpszProxyBypass , dwFlags )

Opens a winhttp session.

#### Parameters

- lpszUserAgent : string

- dwAccessType : int

- lpszProxyName : string

- lpszProxyBypass : string

- dwFlags : int

#### Win32 API References

- Search for WinHttpOpen at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WinHttpOpen), [google](https://www.google.com/search?q=WinHttpOpen) or [google groups](https://groups.google.com/groups?q=WinHttpOpen).
