# 模块 win32gui

> 来源：https://mhammond.github.io/pywin32/win32gui.html （及其成员页，已全部内联）

## Module win32gui

 A module which provides an interface to the native win32 GUI API.

#### Methods

- EnumFontFamilies

 Enumerates the available font families.

- set_logger

 Sets a logger object for exceptions and error information

- LOGFONT

 Creates a LOGFONT object.

- CreateFontIndirect

 function creates a logical font that has the specified characteristics. The font can subsequently be selected as the current font for any device context.

- GetObject

 Returns a struct containing the parameters used to create a GDI object

- GetObjectType

 Returns the type (OBJ_* constant) of a GDI handle

- PyGetMemory

 Returns a buffer object from and address and length

- PyGetString

 Returns a string from an address.

- PySetString

 Copies a string to an address (null terminated). You almost certainly should use win32gui::PySetMemory instead.

- PySetMemory

 Copies bytes to an address.

- PyGetArraySignedLong

 Returns a signed long from an array object at specified index

- PyGetBufferAddressAndLen

 Returns a buffer object address and len

- FlashWindow

 The FlashWindow function flashes the specified window one time. It does not change the active state of the window.

- FlashWindowEx

 The FlashWindowEx function flashes the specified window a specified number of times.

- GetWindowLong

- GetClassLong

- SetWindowLong

 Places a long value at the specified offset into the extra window memory of the given window.

- CallWindowProc

- SendMessage

 Sends a message to the window.

- SendMessageTimeout

 Sends a message to the window.

- PostMessage

- PostThreadMessage

- ReplyMessage

 Used to reply to a message sent through the SendMessage function without returning control to the function that called SendMessage.

- RegisterWindowMessage

 Defines a new window message that is guaranteed to be unique throughout the system. The message value can be used when sending or posting messages.

- DefWindowProc

- EnumWindows

 Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.

- EnumThreadWindows

 Enumerates all top-level windows associated with a thread on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE

- EnumChildWindows

 Enumerates the child windows that belong to the specified parent window by passing the handle to each child window, in turn, to an application-defined callback function. EnumChildWindows continues until the last child window is enumerated or the callback function returns FALSE.

- EnumDesktopWindows

 Enumerates all top-level windows associated with a desktop on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE

- DialogBox

 Creates a modal dialog box.

- DialogBoxParam

 See win32gui::DialogBox

- DialogBoxIndirect

 Creates a modal dialog box from a template, see win32ui::CreateDialogIndirect

- DialogBoxIndirectParam

 See win32gui::DialogBoxIndirect

- CreateDialogIndirect

 Creates a modeless dialog box from a template, see win32ui::CreateDialogIndirect

- DialogBoxIndirectParam

 See win32gui::CreateDialogIndirect

- EndDialog

 Ends a dialog box.

- GetDlgItem

 Retrieves the handle to a control in the specified dialog box.

- GetDlgItemInt

 Returns the integer value of a dialog control

- SetDlgItemInt

 Places an integer value in a dialog control

- GetDlgCtrlID

 Retrieves the identifier of the specified control.

- GetDlgItemText

 Returns the text of a dialog control

- SetDlgItemText

 Sets the text for a window or control

- GetNextDlgTabItem

 Retrieves a handle to the first control that has the WS_TABSTOP style that precedes (or follows) the specified control.

- GetNextDlgGroupItem

 Retrieves a handle to the first control in a group of controls that precedes (or follows) the specified control in a dialog box.

- SetWindowText

 Sets the window text.

- GetWindowText

 Get the window text.

- InitCommonControls

 Initializes the common controls.

- InitCommonControlsEx

 Initializes specific common controls.

- LoadCursor

 Loads a cursor.

- SetCursor

- GetCursor

- GetCursorInfo

 Retrieves information about the global cursor.

- CreateAcceleratorTable

 Creates an accelerator table

- DestroyAccleratorTable

 Destroys an accelerator table

- LoadMenu

 Loads a menu

- DestroyMenu

 Destroys a previously loaded menu.

- SetMenu

 Sets the menu for the specified window.

- GetMenu

 Gets the menu for the specified window.

- LoadIcon

 Loads an icon

- CopyIcon

 Copies an icon

- DrawIcon

 Draws an icon or cursor into the specified device context. To specify additional drawing options, use the win32gui::DrawIconEx function.

- DrawIconEx

 Draws an icon or cursor into the specified device context, performing the specified raster operations, and stretching or compressing the icon or cursor as specified.

- CreateIconIndirect

 Creates an icon or cursor from an ICONINFO structure.

- CreateIconFromResource

 Creates an icon or cursor from resource bits describing the icon.

- LoadImage

 Loads a bitmap, cursor or icon

- DeleteObject

 Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.

- BitBlt

 Performs a bit-block transfer of the color data corresponding to a rectangle of pixels from the specified source device context into a destination device context.

- StretchBlt

 Copies a bitmap from a source rectangle into a destination rectangle, stretching or compressing the bitmap to fit the dimensions of the destination rectangle, if necessary

- PatBlt

 Paints a rectangle by combining the current brush with existing colors

- SetStretchBltMode

 Sets the stretching mode used by win32gui::StretchBlt

- GetStretchBltMode

 Returns the stretching mode used by win32gui::StretchBlt

- TransparentBlt

 Transfers color from one DC to another, with one color treated as transparent

- MaskBlt

 Combines the color data for the source and destination bitmaps using the specified mask and raster operation.

- AlphaBlend

 Transfers color information using alpha blending

- ImageList_Add

 Adds an image or images to an image list.

- ImageList_Create

 Create an image list

- ImageList_Destroy

 Destroy an imagelist

- ImageList_Draw

 Draw an image on an HDC

- ImageList_DrawEx

 Draw an image on an HDC

- ImageList_GetIcon

 Extract an icon from an imagelist

- ImageList_GetImageCount

 Return count of images in imagelist

- ImageList_LoadImage

 Loads bitmaps, cursors or icons, creates imagelist

- ImageList_LoadBitmap

 Creates an image list from the specified bitmap resource.

- ImageList_Remove

 Remove an image from an imagelist

- ImageList_Replace

 Replace an image in an imagelist with a bitmap image

- ImageList_ReplaceIcon

 Replace an image in an imagelist with an icon image

- ImageList_SetBkColor

 Set the background color for the imagelist

- ImageList_SetOverlayImage

 Adds a specified image to the list of images to be used as overlay masks. An image list can have up to four overlay masks in version 4.70 and earlier and up to 15 in version 4.71. The function assigns an overlay mask index to the specified image.

- MessageBox

 Displays a message box

- MessageBeep

 Plays a waveform sound.

- CreateWindow

 Creates a new window.

- DestroyWindow

- EnableWindow

 Enables and disables keyboard and mouse input to a window

- FindWindow

 Retrieves a handle to the top-level window whose class name and window name match the specified strings.

- FindWindowEx

 Retrieves a handle to the top-level window whose class name and window name match the specified strings.

- DragAcceptFiles

 Registers whether a window accepts dropped files.

- DragDetect

 captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point.

- SetDoubleClickTime

- GetDoubleClickTime

- HideCaret

 Hides the caret

- SetCaretPos

 Changes the position of the caret

- GetCaretPos

 Returns the current caret position

- ShowCaret

 Shows the caret at its current position

- CascadeWindows

 Cascade windows

- ShowWindow

 Shows or hides a window and changes its state

- IsWindowVisible

 Indicates if the window has the WS_VISIBLE style.

- IsWindowEnabled

 Indicates if the window is enabled.

- SetFocus

 Sets focus to the specified window.

- GetFocus

 Returns the HWND of the window with focus.

- UpdateWindow

- BringWindowToTop

- SetActiveWindow

- GetActiveWindow

- SetForegroundWindow

- GetForegroundWindow

- GetClientRect

 Returns the rectangle of the client area of a window, in client coordinates

- GetDC

 Gets the device context for the window.

- SaveDC

 Save the state of a device context

- RestoreDC

 Restores a device context state

- DeleteDC

 Deletes a DC

- CreateCompatibleDC

 Creates a memory device context (DC) compatible with the specified device.

- CreateCompatibleBitmap

 Creates a bitmap compatible with the device that is associated with the specified device context.

- CreateBitmap

 Creates a bitmap

- SelectObject

 Selects an object into the specified device context (DC). The new object replaces the previous object of the same type.

- GetCurrentObject

 Retrieves currently selected object from a DC

- GetWindowRect

 Returns the rectangle for a window in screen coordinates

- GetStockObject

 Creates a handle to one of the standard system Gdi objects

- PostQuitMessage

- WaitMessage

 Waits for a message

- SetWindowPos

 Sets the position and size of a window

- GetWindowPlacement

 Returns placement information about the current window.

- SetWindowPlacement

 Sets the windows placement

- RegisterClass

 Registers a window class.

- UnregisterClass

 Unregisters a window class created by win32gui::RegisterClass

- PumpMessages

 Runs a message loop until a WM_QUIT message is received.

- PumpWaitingMessages

 Pumps all waiting messages for the current thread.

- GetMessage

- TranslateMessage

- DispatchMessage

- TranslateAccelerator

- PeekMessage

- Shell_NotifyIcon

 Adds, removes or modifies a taskbar icon.

- GetSystemMenu

- DrawMenuBar

- MoveWindow

- CloseWindow

- DeleteMenu

- RemoveMenu

- CreateMenu

- CreatePopupMenu

- TrackPopupMenu

 Display popup shortcut menu

- CommDlgExtendedError

- ExtractIcon

- ExtractIconEx

- DestroyIcon

- GetIconInfo

 Returns parameters for an icon or cursor

- ScreenToClient

 Convert screen coordinates to client coords

- ClientToScreen

 Convert client coordinates to screen coords

- PaintDesktop

 Fills a DC with the destop background

- RedrawWindow

 Causes a portion of a window to be redrawn

- GetTextExtentPoint32

 Computes the width and height of the specified string of text.

- GetTextMetrics

 Returns info for the font selected into a DC

- GetTextCharacterExtra

 Returns the space between characters

- SetTextCharacterExtra

 Sets the spacing between characters

- GetTextAlign

 Returns horizontal and vertical alignment for text in a device context

- SetTextAlign

 Sets horizontal and vertical alignment for text in a device context

- GetTextFace

 Retrieves the name of the font currently selected in a DC

- GetMapMode

 Returns the method a device context uses to translate logical units to physical units

- SetMapMode

 Sets the method used for translating logical units to device units

- GetGraphicsMode

 Determines if advanced GDI features are enabled for a device context

- SetGraphicsMode

 Enables or disables advanced graphics features for a DC

- GetLayout

 Retrieves the layout mode of a device context

- SetLayout

 Sets the layout for a device context

- GetPolyFillMode

 Returns the polygon filling mode for a device context

- SetPolyFillMode

 Sets the polygon filling mode for a device context

- GetWorldTransform

 Retrieves a device context's coordinate space translation matrix

- SetWorldTransform

 Transforms a device context's coordinate space

- ModifyWorldTransform

 Combines a coordinate tranformation with device context's current transformation

- CombineTransform

 Combines two coordinate space transformations

- GetWindowOrgEx

 Retrievs the window origin for a DC

- SetWindowOrgEx

 Changes the window origin for a DC

- GetViewportOrgEx

 Retrievs the origin for a DC's viewport

- SetViewportOrgEx

 Changes the viewport origin for a DC

- GetWindowExtEx

 Retrieves the window extents for a DC

- SetWindowExtEx

 Changes the window extents for a DC

- GetViewportExtEx

 Retrieves the viewport extents for a DC

- SetViewportExtEx

 Changes the viewport extents for a DC

- GradientFill

 Shades triangles or rectangles by interpolating between vertex colors

- GetOpenFileName

 Creates an Open dialog box that lets the user specify the drive, directory, and the name of a file or set of files to open.

- InsertMenuItem

 Inserts a menu item

- SetMenuItemInfo

 Sets menu information

- GetMenuItemInfo

 Gets menu information

- GetMenuItemCount

- GetMenuItemRect

- GetMenuState

- SetMenuDefaultItem

- GetMenuDefaultItem

- AppendMenu

- InsertMenu

- EnableMenuItem

- CheckMenuItem

- GetSubMenu

- ModifyMenu

 Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item.

- GetMenuItemID

 Retrieves the menu item identifier of a menu item located at the specified position in a menu.

- SetMenuItemBitmaps

 Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item.

- CheckMenuRadioItem

 Checks a specified menu item and makes it a radio item. At the same time, the function clears all other menu items in the associated group and clears the radio-item type flag for those items.

- SetMenuInfo

 Sets information for a specified menu.

- GetMenuInfo

 Gets information about a specified menu.

- DrawFocusRect

 Draws a standard focus outline around a rectangle

- DrawText

 Draws formatted text on a device context

- LineTo

 Draw a line from current position to specified point

- Ellipse

 Draws a filled ellipse on a device context

- Pie

 Draws a section of an ellipse cut by 2 radials

- Arc

 Draws an arc defined by an ellipse and 2 radials

- ArcTo

 Draws an arc defined by an ellipse and 2 radials

- AngleArc

 Draws a line from current pos and a section of a circle's arc

- Chord

 Draws a chord defined by an ellipse and 2 radials

- ExtFloodFill

 Fills an area with current brush

- SetPixel

 Set the color of a single pixel

- GetPixel

 Returns the RGB color of a single pixel

- GetROP2

 Returns the foreground mixing mode of a DC

- SetROP2

 Sets the foreground mixing mode of a DC

- SetPixelV

 Sets the color of a single pixel to an approximation of specified color

- MoveToEx

 Changes the current drawing position

- GetCurrentPositionEx

 Returns a device context's current drawing position

- GetArcDirection

 Returns the direction in which rectangles and arcs are drawn

- SetArcDirection

 Sets the drawing direction for arcs and rectangles

- Polygon

 Draws a closed filled polygon defined by a sequence of points

- Polyline

 Connects a sequence of points using currently selected pen

- PolylineTo

 Draws a series of lines starting from current position. Updates current position with end point.

- PolyBezier

 Draws a series of Bezier curves starting from first point specified.

- PolyBezierTo

 Draws a series of Bezier curves starting from current drawing position.

- PlgBlt

 Copies color from a rectangle into a parallelogram

- CreatePolygonRgn

 Creates a region from a sequence of vertices

- ExtTextOut

 Writes text to a DC.

- GetTextColor

 Returns the text color for a DC

- SetTextColor

 Changes the text color for a device context

- GetBkMode

 Returns the background mode for a device context

- SetBkMode

 Sets the background mode for a device context

- GetBkColor

 Returns the background color for a device context

- SetBkColor

 Sets the background color for a device context

- DrawEdge

 Draws edge(s) of a rectangle

- FillRect

 Fills a rectangular area with specified brush

- FillRgn

 Fills a region with specified brush

- PaintRgn

 Paints a region with current brush

- FrameRgn

 Draws a frame around a region

- InvertRgn

 Inverts the colors in a region

- EqualRgn

 Determines if 2 regions are equal

- PtInRegion

 Determines if a region contains a point

- PtInRect

 Determines if a rectangle contains a point

- RectInRegion

 Determines if a region and rectangle overlap at any point

- SetRectRgn

 Makes an existing region rectangular

- CombineRgn

 Combines two regions

- DrawAnimatedRects

 Animates a rectangle in the manner of minimizing, mazimizing, or opening

- CreateSolidBrush

 Creates a solid brush of specified color

- CreatePatternBrush

 Creates a brush using a bitmap as a pattern

- CreateHatchBrush

 Creates a hatch brush with specified style and color

- CreatePen

 Create a GDI pen

- GetSysColor

 Returns the color of a window element

- GetSysColorBrush

 Creates a handle to a system color brush

- ValidateRect

 Validates the client area within a rectangle by removing the rectangle from the update region of the specified window.

- InvalidateRect

 Invalidates a rectangular area of a window and adds it to the window's update region

- FrameRect

 Draws an outline around a rectangle

- InvertRect

 Inverts the colors in a regtangular region

- WindowFromDC

 Finds the window associated with a device context

- GetUpdateRgn

 Copies the update region of a window into an existing region

- GetWindowRgn

 Copies the window region of a window into an existing region

- SetWindowRgn

 Sets the visible region of a window

- GetWindowRgnBox

 Returns the bounding box for a window's region

- ValidateRgn

 Removes a region from a window's update region

- InvalidateRgn

 Adds a region to a window's update region

- GetRgnBox

 Calculates the bounding box of a region

- OffsetRgn

 Relocates a region

- Rectangle

 Creates a solid rectangle using currently selected pen and brush

- RoundRect

 Draws a rectangle with elliptically rounded corners, filled using using current brush

- BeginPaint

- EndPaint

- BeginPath

 Initializes a path in a DC

- EndPath

 Finalizes a path begun by win32gui::BeginPath

- AbortPath

 Cancels a path begun by win32gui::BeginPath

- CloseFigure

 Closes a section of a path by connecting the beginning pos with the current pos

- FlattenPath

 Flattens any curves in current path into a series of lines

- FillPath

 Fills a path with currently selected brush

- WidenPath

 Widens current path by amount it would increase by if drawn with currently selected pen

- StrokePath

 Draws current path with currently selected pen

- StrokeAndFillPath

 Combines operations of StrokePath and FillPath with no overlap

- GetMiterLimit

 Retrieves the limit of miter joins for a DC

- SetMiterLimit

 Set the limit of miter joins for a DC

- PathToRegion

 Converts a closed path in a DC to a region

- GetPath

 Returns a sequence of points that describe the current path

- CreateRoundRectRgn

 Create a rectangular region with elliptically rounded corners,

- CreateRectRgnIndirect

 Creates a rectangular region,

- CreateEllipticRgnIndirect

 Creates an ellipse region,

- CreateWindowEx

 Creates a new window with Extended Style.

- GetParent

 Retrieves a handle to the specified child window's parent window.

- SetParent

 changes the parent window of the specified child window.

- GetCursorPos

 retrieves the cursor's position, in screen coordinates.

- GetDesktopWindow

 returns the desktop window

- GetWindow

 returns a window that has the specified relationship (Z order or owner) to the specified window.

- GetTopWindow

 Examines the Z order of the child windows associated with the specified parent window and retrieves a handle to the child window at the top of the Z order.

- GetAncestor

 retrieves the handle to the ancestor of the specified window.

- GetWindowDC

 returns the device context (DC) for the entire window, including title bar, menus, and scroll bars.

- IsIconic

 determines whether the specified window is minimized (iconic).

- IsWindow

 determines whether the specified window handle identifies an existing window.

- IsChild

 Tests whether a window is a child window or descendant window of a specified parent window

- ReleaseCapture

 Releases the moust capture for a window.

- GetCapture

 Returns the window with the mouse capture.

- SetCapture

 Captures the mouse for the specified window.

- _TrackMouseEvent

 Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.

- ReleaseDC

 Releases a device context.

- CreateCaret

 Creates a new caret for a window

- DestroyCaret

 Destroys caret for current task

- ScrollWindowEx

 scrolls the content of the specified window's client area.

- SetScrollInfo

 Sets information about a scroll-bar

- GetScrollInfo

 Returns information about a scroll bar

- GetClassName

 Retrieves the name of the class to which the specified window belongs.

- RealGetWindowClass

 Retrieves the name of the class to which the specified window belongs.

- WindowFromPoint

 Retrieves a handle to the window that contains the specified point.

- ChildWindowFromPoint

 Determines which, if any, of the child windows belonging to a parent window contains the specified point.

- ChildWindowFromPoint

 Determines which, if any, of the child windows belonging to a parent window contains the specified point.

- ListView_SortItems

 Uses an application-defined comparison function to sort the items of a list view control.

- ListView_SortItemsEx

 Uses an application-defined comparison function to sort the items of a list view control.

- CreateDC

 Creates a device context for a printer or display device

- ResetDC

 Resets a DC

- GetSaveFileNameW

 Creates a dialog for user to specify location to save a file or files

- GetOpenFileNameW

 Creates a dialog to allow user to select file(s) to open

- SystemParametersInfo

 Queries or sets system-wide parameters. This function can also update the user profile while setting a parameter.

- SetLayeredWindowAttributes

 Sets the opacity and transparency color key of a layered window.

- GetLayeredWindowAttributes

 Retrieves the layering parameters of a window with the WS_EX_LAYERED extended style

- UpdateLayeredWindow

 Updates the position, size, shape, content, and translucency of a layered window.

- AnimateWindow

 Enables you to produce special effects when showing or hiding windows. There are three types of animation: roll, slide, and alpha-blended fade.

- CreateBrushIndirect

 Creates a GDI brush from a LOGBRUSH struct

- ExtCreatePen

 Creates a GDI pen object

- DrawTextW

 Draws Unicode text on a device context.

- EnumPropsEx

 Enumerates properties attached to a window. Each property is passed to a callback function, which receives 4 arguments:
 Handle to the window, name of the property, handle to the property data, and Param object passed to this function

- RegisterDeviceNotification

 Registers the device or type of device for which a window will receive notifications.

- UnregisterDeviceNotification

 Unregisters a Device Notification handle. It is generally not necessary to call this function manually, but in some cases, handle values may be extracted via the struct module and need to be closed explicitly.

- RegisterHotKey

 Registers a hotkey for a window

- UnregisterHotKey

 Unregisters a previously registeredhotkey


---

# win32gui 成员详细文档（共 339 项）


---

<!-- page: win32gui__AbortPath_meth.html -->

## win32gui.AbortPath

 AbortPath(hdc)

Cancels a path begun by win32gui::BeginPath

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__AlphaBlend_meth.html -->

## win32gui.AlphaBlend

 AlphaBlend(Dest, XOriginDest, YOriginDest, WidthDest, HeightDest, Src, XOriginSrc, YOriginSrc, WidthSrc, HeightSrc, blendFunction)

Transfers color information using alpha blending

#### Parameters

- Dest : PyHANDLE

 Destination device context handle

- XOriginDest : int

 X pos of dest rect

- YOriginDest : int

 Y pos of dest rect

- WidthDest : int

 Width of dest rect

- HeightDest : int

 Height of dest rect

- Src : PyHANDLE

 Source DC handle

- XOriginSrc : int

 X pos of src rect

- YOriginSrc : int

 Y pos of src rect

- WidthSrc : int

 Width of src rect

- HeightSrc : int

 Height of src rect

- blendFunction : PyBLENDFUNCTION

 Alpha blending parameters


---

<!-- page: win32gui__AngleArc_meth.html -->

## win32gui.AngleArc

 AngleArc(hdc, Y, Y, Radius, StartAngle, SweepAngle)

Draws a line from current pos and a section of a circle's arc

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Y : int

 x pos of circle

- Y : int

 y pos of circle

- Radius : int

 Radius of circle

- StartAngle : float

 Angle where arc starts, in degrees

- SweepAngle : float

 Angle that arc covers, in degrees


---

<!-- page: win32gui__AnimateWindow_meth.html -->

## win32gui.AnimateWindow

 AnimateWindow(hwnd, Time, Flags)

Enables you to produce special effects when showing or hiding windows. There are three types of animation: roll, slide, and alpha-blended fade.

#### Parameters

- hwnd : PyHANDLE

 handle to window

- Time : int

 Duration of animation in ms

- Flags : int

 Animation type, combination of win32con.AW_* flags

#### Comments

 Accepts keyword args


---

<!-- page: win32gui__AppendMenu_meth.html -->

## win32gui.AppendMenu

 AppendMenu()


---

<!-- page: win32gui__ArcTo_meth.html -->

## win32gui.ArcTo

 ArcTo(hdc, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2)

Draws an arc defined by an ellipse and 2 radials

#### Parameters

- hdc : PyHANDLE

 Device context on which to draw

- LeftRect : int

 Left limit of ellipse

- TopRect : int

 Top limit of ellipse

- RightRect : int

 Right limit of ellipse

- BottomRect : int

 Bottom limit of ellipse

- XRadial1 : int

 Horizontal pos of Radial1 endpoint

- YRadial1 : int

 Vertical pos of Radial1 endpoint

- XRadial2 : int

 Horizontal pos of Radial2 endpoint

- YRadial2 : int

 Vertical pos of Radial2 endpoint

#### Comments

 Draws exactly as win32gui::Arc, but changes current drawing position


---

<!-- page: win32gui__Arc_meth.html -->

## win32gui.Arc

 Arc(hdc, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2)

Draws an arc defined by an ellipse and 2 radials

#### Parameters

- hdc : PyHANDLE

 Device context on which to draw

- LeftRect : int

 Left limit of ellipse

- TopRect : int

 Top limit of ellipse

- RightRect : int

 Right limit of ellipse

- BottomRect : int

 Bottom limit of ellipse

- XRadial1 : int

 Horizontal pos of Radial1 endpoint

- YRadial1 : int

 Vertical pos of Radial1 endpoint

- XRadial2 : int

 Horizontal pos of Radial2 endpoint

- YRadial2 : int

 Vertical pos of Radial2 endpoint


---

<!-- page: win32gui__BeginPaint_meth.html -->

## win32gui.BeginPaint

 hdc, paintstruct = BeginPaint()


---

<!-- page: win32gui__BeginPath_meth.html -->

## win32gui.BeginPath

 BeginPath(hdc)

Initializes a path in a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__BitBlt_meth.html -->

## win32gui.BitBlt

 BitBlt(hdcDest, x, y, width, height, hdcSrc, nXSrc, nYSrc, dwRop)

Performs a bit-block transfer of the color data corresponding to a rectangle of pixels from the specified source device context into a destination device context.

#### Parameters

- hdcDest : int

 handle to destination DC

- x : int

 x-coord of destination upper-left corner

- y : int

 y-coord of destination upper-left corner

- width : int

 width of destination rectangle

- height : int

 height of destination rectangle

- hdcSrc : int

 handle to source DC

- nXSrc : int

 x-coordinate of source upper-left corner

- nYSrc : int

 y-coordinate of source upper-left corner

- dwRop : int

 raster operation code


---

<!-- page: win32gui__BringWindowToTop_meth.html -->

## win32gui.BringWindowToTop

 BringWindowToTop(hwnd)

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__CallWindowProc_meth.html -->

## win32gui.CallWindowProc

 int = CallWindowProc(wndproc, hwnd , msg , wparam , lparam )

#### Parameters

- wndproc : int

 The wndproc to call - this is generally the return value of SetWindowLong(GWL_WNDPROC)

- hwnd : PyHANDLE

 Handle to the window

- msg : int

 A window message

- wparam : int/str

 Type is dependent on the message

- lparam : int/str

 Type is dependent on the message


---

<!-- page: win32gui__CascadeWindows_meth.html -->

## win32gui.CascadeWindows

 WORD = CascadeWindows(hwnd, wHow , rect , children )

Cascade windows

#### Parameters

- hwnd : PyHANDLE

 Window handle

- wHow : int

 Cascade flag (win32con)

- rect : PyHANDLE

 Rectangle area (can be None)

- children : PyHANDLE

 Tuple of child windows (can be None)


---

<!-- page: win32gui__CheckMenuItem_meth.html -->

## win32gui.CheckMenuItem

 int = CheckMenuItem()


---

<!-- page: win32gui__CheckMenuRadioItem_meth.html -->

## win32gui.CheckMenuRadioItem

 CheckMenuRadioItem(hMenu, idFirst, idLast, idCheck, uFlags)

Checks a specified menu item and makes it a radio item. At the same time, the function clears all other menu items in the associated group and clears the radio-item type flag for those items.

#### Parameters

- hMenu : int

 handle to menu

- idFirst : int

 identifier or position of first item

- idLast : int

 identifier or position of last item

- idCheck : int

 identifier or position of item to check

- uFlags : int

 options


---

<!-- page: win32gui__ChildWindowFromPoint_meth.html -->

## win32gui.ChildWindowFromPoint

 int = ChildWindowFromPoint(hwndParent, point )

Determines which, if any, of the child windows belonging to a parent window contains the specified point.

#### Parameters

- hwndParent : int

 The parent.

- point : (int, int)

 The point.


---

<!-- page: win32gui__ChildWindowFromPoint_meth_1.html -->

## win32gui.ChildWindowFromPoint

 int = ChildWindowFromPoint(hwndParent, point , flags )

Determines which, if any, of the child windows belonging to a parent window contains the specified point.

#### Parameters

- hwndParent : int

 The parent.

- point : (int, int)

 The point.

- flags : int

 Specifies which child windows to skip. This parameter can be one or more of the CWP_* constants.


---

<!-- page: win32gui__Chord_meth.html -->

## win32gui.Chord

 Chord(hdc, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2)

Draws a chord defined by an ellipse and 2 radials

#### Parameters

- hdc : PyHANDLE

 Device context on which to draw

- LeftRect : int

 Left limit of ellipse

- TopRect : int

 Top limit of ellipse

- RightRect : int

 Right limit of ellipse

- BottomRect : int

 Bottom limit of ellipse

- XRadial1 : int

 Horizontal pos of Radial1 endpoint

- YRadial1 : int

 Vertical pos of Radial1 endpoint

- XRadial2 : int

 Horizontal pos of Radial2 endpoint

- YRadial2 : int

 Vertical pos of Radial2 endpoint


---

<!-- page: win32gui__ClientToScreen_meth.html -->

## win32gui.ClientToScreen

 (int,int) = ClientToScreen(hWnd, Point )

Convert client coordinates to screen coords

#### Parameters

- hWnd : PyHANDLE

 Handle to a window

- Point : (int,int)

 Client coordinates to be converted


---

<!-- page: win32gui__CloseFigure_meth.html -->

## win32gui.CloseFigure

 CloseFigure(hdc)

Closes a section of a path by connecting the beginning pos with the current pos

#### Parameters

- hdc : PyHANDLE

 Handle to a device context that contains an open path. See win32gui::BeginPath.


---

<!-- page: win32gui__CloseWindow_meth.html -->

## win32gui.CloseWindow

 CloseWindow()


---

<!-- page: win32gui__CombineRgn_meth.html -->

## win32gui.CombineRgn

 int = CombineRgn(Dest, Src1 , Src2 , CombineMode )

Combines two regions

#### Parameters

- Dest : PyGdiHandle

 Handle to existing region that will receive combined region

- Src1 : PyGdiHandle

 Handle to first region

- Src2 : PyGdiHandle

 Handle to second region

- CombineMode : int

 One of RGN_AND,RGN_COPY,RGN_DIFF,RGN_OR,RGN_XOR

#### Return Value

Returns the type of region created, one of NULLREGION, SIMPLEREGION, COMPLEXREGION


---

<!-- page: win32gui__CombineTransform_meth.html -->

## win32gui.CombineTransform

 PyXFORM = CombineTransform(xform1, xform2 )

Combines two coordinate space transformations

#### Parameters

- xform1 : PyXFORM

 First transformation

- xform2 : PyXFORM

 Second transformation


---

<!-- page: win32gui__CommDlgExtendedError_meth.html -->

## win32gui.CommDlgExtendedError

 int = CommDlgExtendedError()


---

<!-- page: win32gui__CopyIcon_meth.html -->

## win32gui.CopyIcon

 HICON = CopyIcon(hicon)

Copies an icon

#### Parameters

- hicon : int

 Existing icon


---

<!-- page: win32gui__CreateAcceleratorTable_meth.html -->

## win32gui.CreateAcceleratorTable

 HACCEL = CreateAcceleratorTable(accels)

Creates an accelerator table

#### Parameters

- accels : ( (int, int, int), ...)

 A sequence of (fVirt, key, cmd), as per the Win32 ACCEL structure.


---

<!-- page: win32gui__CreateBitmap_meth.html -->

## win32gui.CreateBitmap

 PyGdiHANDLE = CreateBitmap(width, height , cPlanes , cBitsPerPixel , bitmap bits )

Creates a bitmap

#### Parameters

- width : int

 bitmap width, in pixels

- height : int

 bitmap height, in pixels

- cPlanes : int

 number of color planes

- cBitsPerPixel : int

 number of bits to identify color

- bitmap bits : None

 Must be None


---

<!-- page: win32gui__CreateBrushIndirect_meth.html -->

## win32gui.CreateBrushIndirect

 PyGdiHANDLE = CreateBrushIndirect(lb)

Creates a GDI brush from a LOGBRUSH struct

#### Parameters

- lb : PyLOGBRUSH

 Dict containing brush creation parameters


---

<!-- page: win32gui__CreateCaret_meth.html -->

## win32gui.CreateCaret

 CreateCaret(hWnd, hBitmap, nWidth, nHeight)

Creates a new caret for a window

#### Parameters

- hWnd : int

 handle to owner window

- hBitmap : PyGdiHANDLE

 handle to bitmap for caret shape

- nWidth : int

 caret width

- nHeight : int

 caret height


---

<!-- page: win32gui__CreateCompatibleBitmap_meth.html -->

## win32gui.CreateCompatibleBitmap

 PyGdiHANDLE = CreateCompatibleBitmap(hdc, width , height )

Creates a bitmap compatible with the device that is associated with the specified device context.

#### Parameters

- hdc : int

 handle to DC

- width : int

 width of bitmap, in pixels

- height : int

 height of bitmap, in pixels


---

<!-- page: win32gui__CreateCompatibleDC_meth.html -->

## win32gui.CreateCompatibleDC

 HDC = CreateCompatibleDC(dc)

Creates a memory device context (DC) compatible with the specified device.

#### Parameters

- dc : int

 handle to DC


---

<!-- page: win32gui__CreateDC_meth.html -->

## win32gui.CreateDC

 int = CreateDC(Driver, Device , InitData )

Creates a device context for a printer or display device

#### Parameters

- Driver : string

 Name of display or print provider, usually DISPLAY or WINSPOOL

- Device : string

 Name of specific device, eg printer name returned from GetDefaultPrinter

- InitData : PyDEVMODE

 A PyDEVMODE that specifies printing parameters, use None for printer defaults


---

<!-- page: win32gui__CreateDialogIndirect_meth.html -->

## win32gui.CreateDialogIndirect

 int = CreateDialogIndirect(hInstance, controlList , hWndParent , DialogFunc , InitParam )

Creates a modeless dialog box from a template, see win32ui::CreateDialogIndirect

#### Parameters

- hInstance : PyHANDLE

 Handle to module creating the dialog box

- controlList : PyDialogTemplate

 Sequence containing a PyDLGTEMPLATE, followed by variable number of PyDLGITEMTEMPLATEs

- hWndParent : PyHANDLE

 Handle to dialog's parent window

- DialogFunc : function

 Dialog box procedure to process messages

- InitParam=0 : int

 Initialization data to be passed to above procedure during WM_INITDIALOG processing


---

<!-- page: win32gui__CreateEllipticRgnIndirect_meth.html -->

## win32gui.CreateEllipticRgnIndirect

 PyGdiHandle = CreateEllipticRgnIndirect(rc)

Creates an ellipse region,

#### Parameters

- rc : PyRECT

 Coordinates of bounding rectangle in logical units


---

<!-- page: win32gui__CreateFontIndirect_meth.html -->

## win32gui.CreateFontIndirect

 PyGdiHandle = CreateFontIndirect(lplf)

function creates a logical font that has the specified characteristics. The font can subsequently be selected as the current font for any device context.

#### Parameters

- lplf : PyLOGFONT

 A LOGFONT object as returned by win32gui::LOGFONT


---

<!-- page: win32gui__CreateHatchBrush_meth.html -->

## win32gui.CreateHatchBrush

 PyGdiHANDLE = CreateHatchBrush(Style, clrref )

Creates a hatch brush with specified style and color

#### Parameters

- Style : int

 Hatch style, one of win32con.HS_* constants

- clrref : int

 Rgb color value. See win32api::RGB.


---

<!-- page: win32gui__CreateIconFromResource_meth.html -->

## win32gui.CreateIconFromResource

 PyHANDLE = CreateIconFromResource(bits, fIcon , ver )

Creates an icon or cursor from resource bits describing the icon.

#### Parameters

- bits : string

 The bits

- fIcon : bool

 True if an icon, False if a cursor.

- ver=0x00030000 : int

 Specifies the version number of the icon or cursor format for the resource bits pointed to by the presbits parameter. This parameter can be 0x00030000.


---

<!-- page: win32gui__CreateIconIndirect_meth.html -->

## win32gui.CreateIconIndirect

 int = CreateIconIndirect(iconinfo)

Creates an icon or cursor from an ICONINFO structure.

#### Parameters

- iconinfo : PyICONINFO

 Tuple defining the icon parameters


---

<!-- page: win32gui__CreateMenu_meth.html -->

## win32gui.CreateMenu

 int = CreateMenu()

#### Return Value

The result is a HMENU to the new menu.


---

<!-- page: win32gui__CreatePatternBrush_meth.html -->

## win32gui.CreatePatternBrush

 PyGdiHANDLE = CreatePatternBrush(hbmp)

Creates a brush using a bitmap as a pattern

#### Parameters

- hbmp : PyGdiHANDLE

 Handle to a bitmap


---

<!-- page: win32gui__CreatePen_meth.html -->

## win32gui.CreatePen

 PyGdiHANDLE = CreatePen(PenStyle, Width , Color )

Create a GDI pen

#### Parameters

- PenStyle : int

 One of win32con.PS_* pen styles

- Width : int

 Drawing width in logical units. Use zero for single pixel.

- Color : int

 RGB color value. See win32api::RGB.


---

<!-- page: win32gui__CreatePolygonRgn_meth.html -->

## win32gui.CreatePolygonRgn

 PyGdiHANDLE = CreatePolygonRgn(Points, PolyFillMode )

Creates a region from a sequence of vertices

#### Parameters

- Points : [(int,int),...]

 Sequence of POINT tuples: ((x,y),...).

- PolyFillMode : int

 Filling mode, one of ALTERNATE, WINDING


---

<!-- page: win32gui__CreatePopupMenu_meth.html -->

## win32gui.CreatePopupMenu

 int = CreatePopupMenu()

#### Return Value

The result is a HMENU to the new menu.


---

<!-- page: win32gui__CreateRectRgnIndirect_meth.html -->

## win32gui.CreateRectRgnIndirect

 PyGdiHandle = CreateRectRgnIndirect(rc)

Creates a rectangular region,

#### Parameters

- rc : PyRECT

 Coordinates of rectangle


---

<!-- page: win32gui__CreateRoundRectRgn_meth.html -->

## win32gui.CreateRoundRectRgn

 PyGdiHandle = CreateRoundRectRgn(LeftRect, TopRect , RightRect , BottomRect , WidthEllipse , HeightEllipse )

Create a rectangular region with elliptically rounded corners,

#### Parameters

- LeftRect : int

 Position of left edge of rectangle

- TopRect : int

 Position of top edge of rectangle

- RightRect : int

 Position of right edge of rectangle

- BottomRect : int

 Position of bottom edge of rectangle

- WidthEllipse : int

 Width of ellipse

- HeightEllipse : int

 Height of ellipse


---

<!-- page: win32gui__CreateSolidBrush_meth.html -->

## win32gui.CreateSolidBrush

 PyGdiHANDLE = CreateSolidBrush(Color)

Creates a solid brush of specified color

#### Parameters

- Color : int

 RGB color value. See win32api::RGB.


---

<!-- page: win32gui__CreateWindowEx_meth.html -->

## win32gui.CreateWindowEx

 int = CreateWindowEx(dwExStyle, className , windowName , style , x , y , width , height , parent , menu , hinstance , reserved )

Creates a new window with Extended Style.

#### Parameters

- dwExStyle : int

 extended window style

- className : int/string

- windowName : string

- style : int

 The style for the window.

- x : int

- y : int

- width : int

- height : int

- parent : int

 Handle to the parent window.

- menu : int

 Handle to the menu to use for this window.

- hinstance : int

- reserved : None

 Must be None


---

<!-- page: win32gui__CreateWindow_meth.html -->

## win32gui.CreateWindow

 int = CreateWindow(className, windowName , style , x , y , width , height , parent , menu , hinstance , reserved )

Creates a new window.

#### Parameters

- className : int/string

- windowName : string

- style : int

 The style for the window.

- x : int

- y : int

- width : int

- height : int

- parent : int

 Handle to the parent window.

- menu : int

 Handle to the menu to use for this window.

- hinstance : int

- reserved : None

 Must be None


---

<!-- page: win32gui__DefWindowProc_meth.html -->

## win32gui.DefWindowProc

 int = DefWindowProc(hwnd, message , wparam , lparam )

#### Parameters

- hwnd : int

 The handle to the Window

- message : int

 The ID of the message to send

- wparam : int

 An integer whose value depends on the message

- lparam : int

 An integer whose value depends on the message


---

<!-- page: win32gui__DeleteDC_meth.html -->

## win32gui.DeleteDC

 DeleteDC(hdc)

Deletes a DC

#### Parameters

- hdc : int

 The source DC


---

<!-- page: win32gui__DeleteMenu_meth.html -->

## win32gui.DeleteMenu

 DeleteMenu(hmenu, position, flags)

#### Parameters

- hmenu : int

 The handle to the menu

- position : int

 The position to delete.

- flags : int


---

<!-- page: win32gui__DeleteObject_meth.html -->

## win32gui.DeleteObject

 DeleteObject(handle)

Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.

#### Parameters

- handle : PyGdiHANDLE

 handle to the object to delete.


---

<!-- page: win32gui__DestroyAccleratorTable_meth.html -->

## win32gui.DestroyAccleratorTable

 DestroyAccleratorTable(haccel)

Destroys an accelerator table

#### Parameters

- haccel : int


---

<!-- page: win32gui__DestroyCaret_meth.html -->

## win32gui.DestroyCaret

 DestroyCaret()

Destroys caret for current task


---

<!-- page: win32gui__DestroyIcon_meth.html -->

## win32gui.DestroyIcon

 DestroyIcon(hicon)

#### Parameters

- hicon : int

 The icon to destroy.


---

<!-- page: win32gui__DestroyMenu_meth.html -->

## win32gui.DestroyMenu

 DestroyMenu()

Destroys a previously loaded menu.


---

<!-- page: win32gui__DestroyWindow_meth.html -->

## win32gui.DestroyWindow

 DestroyWindow(hwnd)

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__DialogBoxIndirectParam_meth.html -->

## win32gui.DialogBoxIndirectParam

 int = DialogBoxIndirectParam()

See win32gui::DialogBoxIndirect


---

<!-- page: win32gui__DialogBoxIndirectParam_meth_1.html -->

## win32gui.DialogBoxIndirectParam

 int = DialogBoxIndirectParam()

See win32gui::CreateDialogIndirect


---

<!-- page: win32gui__DialogBoxIndirect_meth.html -->

## win32gui.DialogBoxIndirect

 int = DialogBoxIndirect(hInstance, controlList , hWndParent , DialogFunc , InitParam )

Creates a modal dialog box from a template, see win32ui::CreateDialogIndirect

#### Parameters

- hInstance : PyHANDLE

 Handle to module creating the dialog box

- controlList : PyDialogTemplate

 Sequence of items defining the dialog box and subcontrols

- hWndParent : PyHANDLE

 Handle to dialog's parent window

- DialogFunc : function

 Dialog box procedure to process messages

- InitParam=0 : long

 Initialization data to be passed to above procedure during WM_INITDIALOG processing


---

<!-- page: win32gui__DialogBoxParam_meth.html -->

## win32gui.DialogBoxParam

 int = DialogBoxParam()

See win32gui::DialogBox


---

<!-- page: win32gui__DialogBox_meth.html -->

## win32gui.DialogBox

 int = DialogBox(hInstance, TemplateName , hWndParent , DialogFunc , InitParam )

Creates a modal dialog box.

#### Parameters

- hInstance : PyHANDLE

 Handle to module that contains the dialog template

- TemplateName : PyResourceId

 Name or resource id of the dialog resource

- hWndParent : PyHANDLE

 Handle to dialog's parent window

- DialogFunc : function

 Dialog box procedure to process messages

- InitParam=0 : int

 Initialization data to be passed to above procedure during WM_INITDIALOG processing


---

<!-- page: win32gui__DispatchMessage_meth.html -->

## win32gui.DispatchMessage

 int = DispatchMessage(msg)

#### Parameters

- msg : MSG


---

<!-- page: win32gui__DragAcceptFiles_meth.html -->

## win32gui.DragAcceptFiles

 DragAcceptFiles(hwnd, fAccept)

Registers whether a window accepts dropped files.

#### Parameters

- hwnd : int

 Handle to the Window

- fAccept : int

 Value that indicates if the window identified by the hWnd parameter accepts dropped files. This value is True to accept dropped files or False to discontinue accepting dropped files.


---

<!-- page: win32gui__DragDetect_meth.html -->

## win32gui.DragDetect

 DragDetect(hwnd, point)

captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point.

#### Parameters

- hwnd : int

 Handle to the Window

- point : (int, int)

 Initial position of the mouse, in screen coordinates. The function determines the coordinates of the drag rectangle by using this point.

#### Return Value

If the user moved the mouse outside of the drag rectangle while holding down the left button , the return value is nonzero.
If the user did not move the mouse outside of the drag rectangle while holding down the left button , the return value is zero.


---

<!-- page: win32gui__DrawAnimatedRects_meth.html -->

## win32gui.DrawAnimatedRects

 DrawAnimatedRects(hwnd, idAni, minCoords, restCoords)

Animates a rectangle in the manner of minimizing, mazimizing, or opening

#### Parameters

- hwnd : int

 handle to clipping window

- idAni : int

 type of animation, win32con.IDANI_*

- minCoords : PyRECT

 rectangle coordinates (minimized)

- restCoords : PyRECT

 rectangle coordinates (restored)


---

<!-- page: win32gui__DrawEdge_meth.html -->

## win32gui.DrawEdge

 PyRECT = DrawEdge(hdc, rc , edge , Flags )

Draws edge(s) of a rectangle

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- rc : PyRECT

 Rectangle whose edge(s) will be drawn

- edge : int

 Combination of win32con.BDR_* flags, or one of win32con.EDGE_* flags

- Flags : int

 Combination of win32con.BF_* flags

#### Return Value

BF_ADJUST flag causes input rectange to be shrunk by size of border.. Rectangle is always returned.


---

<!-- page: win32gui__DrawFocusRect_meth.html -->

## win32gui.DrawFocusRect

 DrawFocusRect(hDC, rc)

Draws a standard focus outline around a rectangle

#### Parameters

- hDC : PyHANDLE

 Handle to a device context

- rc : (int, int, int,int)

 Tuple of (left,top,right,bottom) defining the rectangle


---

<!-- page: win32gui__DrawIconEx_meth.html -->

## win32gui.DrawIconEx

 DrawIconEx(hDC, xLeft, yTop, hIcon, cxWidth, cyWidth, istepIfAniCur, hbrFlickerFreeDraw, diFlags)

Draws an icon or cursor into the specified device context, performing the specified raster operations, and stretching or compressing the icon or cursor as specified.

#### Parameters

- hDC : int

 handle to device context

- xLeft : int

 x-coord of upper left corner

- yTop : int

 y-coord of upper left corner

- hIcon : int

 handle to icon

- cxWidth : int

 icon width

- cyWidth : int

 icon height

- istepIfAniCur : int

 frame index, animated cursor

- hbrFlickerFreeDraw : PyGdiHANDLE

 handle to background brush, can be None

- diFlags : int

 icon-drawing flags (win32con.DI_*)


---

<!-- page: win32gui__DrawIcon_meth.html -->

## win32gui.DrawIcon

 DrawIcon(hDC, X, Y, hicon)

Draws an icon or cursor into the specified device context. To specify additional drawing options, use the win32gui::DrawIconEx function.

#### Parameters

- hDC : int

 handle to DC

- X : int

 x-coordinate of upper-left corner

- Y : int

 y-coordinate of upper-left corner

- hicon : int

 handle to icon


---

<!-- page: win32gui__DrawMenuBar_meth.html -->

## win32gui.DrawMenuBar

 DrawMenuBar(hwnd)

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__DrawTextW_meth.html -->

## win32gui.DrawTextW

 int,PyRECT = DrawTextW(hDC, String , Count , Rect , Format )

Draws Unicode text on a device context.

#### Parameters

- hDC : PyHANDLE

 Handle to a device context

- String : string

 Text to be drawn

- Count : int

 Number of characters to draw, use -1 for entire null terminated string

- Rect : PyRECT

 Rectangle in which to draw text

- Format : int

 Formatting flags, combination of win32con.DT_* values

#### Comments

 Accepts keyword args.

#### Return Value

Returns the height of the drawn text, and the rectangle coordinates


---

<!-- page: win32gui__DrawText_meth.html -->

## win32gui.DrawText

 (int, PyRECT) = DrawText(hDC, String , nCount , Rect , Format )

Draws formatted text on a device context

#### Parameters

- hDC : int/PyHANDLE

 The device context on which to draw

- String : str

 The text to be drawn

- nCount : int

 The number of characters, use -1 for simple null-terminated string

- Rect : PyRECT

 Tuple of 4 ints specifying the position (left, top, right, bottom)

- Format : int

 Formatting flags, combination of win32con.DT_* values

#### Return Value

Returns the height of the drawn text, and the rectangle coordinates


---

<!-- page: win32gui__Ellipse_meth.html -->

## win32gui.Ellipse

 Ellipse(hdc, LeftRect, TopRect, RightRect, BottomRect)

Draws a filled ellipse on a device context

#### Parameters

- hdc : PyHANDLE

 Device context on which to draw

- LeftRect : int

 Left limit of ellipse

- TopRect : int

 Top limit of ellipse

- RightRect : int

 Right limit of ellipse

- BottomRect : int

 Bottom limit of ellipse


---

<!-- page: win32gui__EnableMenuItem_meth.html -->

## win32gui.EnableMenuItem

 EnableMenuItem()


---

<!-- page: win32gui__EnableWindow_meth.html -->

## win32gui.EnableWindow

 int = EnableWindow(hWnd, bEnable )

Enables and disables keyboard and mouse input to a window

#### Parameters

- hWnd : PyHANDLE

 Handle to window

- bEnable : boolean

 True to enable input to the window, False to disable input

#### Return Value

Returns True if window was already disabled when call was made, False otherwise


---

<!-- page: win32gui__EndDialog_meth.html -->

## win32gui.EndDialog

 EndDialog(hwnd, result)

Ends a dialog box.

#### Parameters

- hwnd : int

 Handle to the window.

- result : int

 result


---

<!-- page: win32gui__EndPaint_meth.html -->

## win32gui.EndPaint

 EndPaint(hwnd, ps)

#### Parameters

- hwnd : int

- ps : paintstruct

 As returned from win32gui::BeginPaint


---

<!-- page: win32gui__EndPath_meth.html -->

## win32gui.EndPath

 EndPath(hdc)

Finalizes a path begun by win32gui::BeginPath

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__EnumChildWindows_meth.html -->

## win32gui.EnumChildWindows

 EnumChildWindows(hwnd, callback, extra)

Enumerates the child windows that belong to the specified parent window by passing the handle to each child window, in turn, to an application-defined callback function. EnumChildWindows continues until the last child window is enumerated or the callback function returns FALSE.

#### Parameters

- hwnd : PyHANDLE

 The handle to the window to enumerate.

- callback : object

 A Python function to be used as the callback.

- extra : object

 Any python object - this is passed to the callback function as the second param (first is the hwnd).


---

<!-- page: win32gui__EnumDesktopWindows_meth.html -->

## win32gui.EnumDesktopWindows

 EnumDesktopWindows(hDesktop, callback, extra)

Enumerates all top-level windows associated with a desktop on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE

#### Parameters

- hDesktop : PyHANDLE

 The id of the desktop for which the windows need to be enumerated.

- callback : object

 A Python function to be used as the callback.

- extra : object

 Any python object - this is passed to the callback function as the second param (first is the hwnd).


---

<!-- page: win32gui__EnumFontFamilies_meth.html -->

## win32gui.EnumFontFamilies

 int = EnumFontFamilies(hdc, Family , EnumFontFamProc , Param )

Enumerates the available font families.

#### Parameters

- hdc : PyHANDLE

 Handle to a device context for which to enumerate available fonts

- Family : string

 Family of fonts to enumerate. If none, first member of each font family will be returned.

- EnumFontFamProc : function

 The Python function called with each font family. This function is called with 4 arguments.

- Param : object

 An arbitrary object to be passed to the callback function

#### Comments

 The parameters that the callback function will receive are as follows:
 PyLOGFONT - contains the font parameters
 None - Placeholder for a TEXTMETRIC structure, not supported yet
 int - Font type, combination of DEVICE_FONTTYPE, RASTER_FONTTYPE, TRUETYPE_FONTTYPE
 object - The Param originally passed in to EnumFontFamilies


---

<!-- page: win32gui__EnumPropsEx_meth.html -->

## win32gui.EnumPropsEx

 EnumPropsEx(hWnd, EnumFunc, Param)

Enumerates properties attached to a window. Each property is passed to a callback function, which receives 4 arguments:
 Handle to the window, name of the property, handle to the property data, and Param object passed to this function

#### Parameters

- hWnd : PyHANDLE

 Handle to a window

- EnumFunc : function

 Callback function

- Param : object

 Arbitrary object to be passed to callback function


---

<!-- page: win32gui__EnumThreadWindows_meth.html -->

## win32gui.EnumThreadWindows

 EnumThreadWindows(dwThreadId, callback, extra)

Enumerates all top-level windows associated with a thread on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE

#### Parameters

- dwThreadId : int

 The id of the thread for which the windows need to be enumerated.

- callback : object

 A Python function to be used as the callback.

- extra : object

 Any python object - this is passed to the callback function as the second param (first is the hwnd).


---

<!-- page: win32gui__EnumWindows_meth.html -->

## win32gui.EnumWindows

 EnumWindows(callback, extra)

Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.

#### Parameters

- callback : function

 A Python function to be used as the callback. Function can return False to stop enumeration, or raise an exception.

- extra : object

 Any python object - this is passed to the callback function as the second param (first is the hwnd).


---

<!-- page: win32gui__EqualRgn_meth.html -->

## win32gui.EqualRgn

 boolean = EqualRgn(SrcRgn1, SrcRgn2 )

Determines if 2 regions are equal

#### Parameters

- SrcRgn1 : PyGdiHandle

 Handle to a region

- SrcRgn2 : PyGdiHandle

 Handle to a region


---

<!-- page: win32gui__ExtCreatePen_meth.html -->

## win32gui.ExtCreatePen

 PyHANDLE = ExtCreatePen(PenStyle, Width , lb , Style )

Creates a GDI pen object

#### Parameters

- PenStyle : int

 Combination of win32con.PS_*. Must contain either PS_GEOMETRIC or PS_COSMETIC.

- Width : int

 Width of pen in logical units. Must be 1 for PS_COSMETIC.

- lb : PyLOGBRUSH

 Dict containing brush creation parameters

- Style=None : (int, ...)

 Sequence containing lengths of dashes and spaces Used only with PS_USERSTYLE, otherwise must be None.


---

<!-- page: win32gui__ExtFloodFill_meth.html -->

## win32gui.ExtFloodFill

 ExtFloodFill(, XStart, YStart, Color, FillType)

Fills an area with current brush

#### Parameters

- =hdc : PyHANDLE

 Handle to a device context

- XStart : int

 Horizontal starting pos

- YStart : int

 Vertical starting pos

- Color : int

 RGB color value. See win32api::RGB.

- FillType : int

 One of win32con.FLOODFILL* values


---

<!-- page: win32gui__ExtTextOut_meth.html -->

## win32gui.ExtTextOut

 int = ExtTextOut(hdc, int , int , int , rect , string , tuple )

Writes text to a DC.

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- int : x

 The x coordinate to write the text to.

- int : y

 The y coordinate to write the text to.

- int : nOptions

 Specifies the rectangle type. This parameter can be one, both, or neither of ETO_CLIPPED and ETO_OPAQUE

- rect : PyRECT

 Specifies the text's bounding rectangle. (Can be None.)

- string : text

 The text to write.

- tuple : (width1, width2, ...)

 Optional array of values that indicate distance between origins of character cells.

#### Win32 API References

- Search for ExtTextOut at [msdn](https://learn.microsoft.com/en-ca/search/?terms=ExtTextOut), [google](https://www.google.com/search?q=ExtTextOut) or [google groups](https://groups.google.com/groups?q=ExtTextOut).

#### Return Value

Always none. If the function fails, an exception is raised.


---

<!-- page: win32gui__ExtractIconEx_meth.html -->

## win32gui.ExtractIconEx

 int = ExtractIconEx(moduleName, index , numIcons )

#### Parameters

- moduleName : string

- index : int

- numIcons=1 : int

#### Comments

 You must destroy each icon handle returned by calling the win32gui::DestroyIcon function.

#### Return Value

If index==-1, the result is an integer with the number of icons in the file, otherwise it is 2 arrays of icon handles.


---

<!-- page: win32gui__ExtractIcon_meth.html -->

## win32gui.ExtractIcon

 int = ExtractIcon(hinstance, moduleName , index )

#### Parameters

- hinstance : int

- moduleName : string

- index : int

#### Comments

 You must destroy the icon handle returned by calling the win32gui::DestroyIcon function.

#### Return Value

The result is a HICON.


---

<!-- page: win32gui__FillPath_meth.html -->

## win32gui.FillPath

 FillPath(hdc)

Fills a path with currently selected brush

#### Parameters

- hdc : PyHANDLE

 Handle to a device context that contains a finalized path. See win32gui::EndPath.

#### Comments

 Any open figures are closed and path is deselected from the DC.


---

<!-- page: win32gui__FillRect_meth.html -->

## win32gui.FillRect

 FillRect(hDC, rc, hbr)

Fills a rectangular area with specified brush

#### Parameters

- hDC : PyHANDLE

 Handle to a device context

- rc : PyRECT

 Rectangle to be filled

- hbr : PyGdiHANDLE

 Handle to brush to be used to fill area


---

<!-- page: win32gui__FillRgn_meth.html -->

## win32gui.FillRgn

 FillRgn(hdc, hrgn, hbr)

Fills a region with specified brush

#### Parameters

- hdc : PyHANDLE

 Handle to the device context

- hrgn : PyGdiHANDLE

 Handle to the region

- hbr : PyGdiHANDLE

 Brush to be used


---

<!-- page: win32gui__FindWindowEx_meth.html -->

## win32gui.FindWindowEx

 PyHANDLE = FindWindowEx(Parent, ChildAfter , ClassName , WindowName )

Retrieves a handle to the top-level window whose class name and window name match the specified strings.

#### Parameters

- Parent : PyHANDLE

 Window whose child windows will be searched. If 0, desktop window is assumed.

- ChildAfter : PyHANDLE

 Child window after which to search in Z-order, can be 0 to search all

- ClassName : PyResourceId

 Name or atom of window class to find, can be None

- WindowName : string

 Title of window to find, can be None


---

<!-- page: win32gui__FindWindow_meth.html -->

## win32gui.FindWindow

 PyHANDLE = FindWindow(ClassName, WindowName )

Retrieves a handle to the top-level window whose class name and window name match the specified strings.

#### Parameters

- ClassName : PyResourceId

 Name or atom of window class to find, can be None

- WindowName : string

 Title of window to find, can be None


---

<!-- page: win32gui__FlashWindowEx_meth.html -->

## win32gui.FlashWindowEx

 int = FlashWindowEx(hwnd, dwFlags , uCount , dwTimeout )

The FlashWindowEx function flashes the specified window a specified number of times.

#### Parameters

- hwnd : PyHANDLE

 Handle to a window

- dwFlags : int

 Combination of win32con.FLASHW_* flags

- uCount : int

 Nbr of times to flash

- dwTimeout : int

 Elapsed time between flashes, in milliseconds


---

<!-- page: win32gui__FlashWindow_meth.html -->

## win32gui.FlashWindow

 int = FlashWindow(hwnd, bInvert )

The FlashWindow function flashes the specified window one time. It does not change the active state of the window.

#### Parameters

- hwnd : PyHANDLE

 Handle to a window

- bInvert : int

 Indicates if window should toggle between active and inactive


---

<!-- page: win32gui__FlattenPath_meth.html -->

## win32gui.FlattenPath

 FlattenPath(hdc)

Flattens any curves in current path into a series of lines

#### Parameters

- hdc : PyHANDLE

 Handle to a device context that contains a closed path. See win32gui::EndPath.


---

<!-- page: win32gui__FrameRect_meth.html -->

## win32gui.FrameRect

 FrameRect(hDC, rc, hbr)

Draws an outline around a rectangle

#### Parameters

- hDC : PyHANDLE

 Handle to a device context

- rc : PyRECT

 Rectangle around which to draw

- hbr : PyGdiHANDLE

 Handle to brush created using CreateHatchBrush, CreatePatternBrush, CreateSolidBrush, or GetStockObject


---

<!-- page: win32gui__FrameRgn_meth.html -->

## win32gui.FrameRgn

 FrameRgn(hdc, hrgn, hbr, Width, Height)

Draws a frame around a region

#### Parameters

- hdc : PyHANDLE

 Handle to the device context

- hrgn : PyGdiHandle

 Handle to the region

- hbr : PyGdiHandle

 Handle to brush to be used

- Width : int

 Frame width

- Height : int

 Frame height


---

<!-- page: win32gui__GetActiveWindow_meth.html -->

## win32gui.GetActiveWindow

 HWND = GetActiveWindow()


---

<!-- page: win32gui__GetAncestor_meth.html -->

## win32gui.GetAncestor

 int = GetAncestor(hWnd, gaFlags )

retrieves the handle to the ancestor of the specified window.

#### Parameters

- hWnd : int

 handle to original window

- gaFlags : int

 ancestor to be retrieved


---

<!-- page: win32gui__GetArcDirection_meth.html -->

## win32gui.GetArcDirection

 int = GetArcDirection(hdc)

Returns the direction in which rectangles and arcs are drawn

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Recturns one of win32con.AD_* values


---

<!-- page: win32gui__GetBkColor_meth.html -->

## win32gui.GetBkColor

 int = GetBkColor(hdc)

Returns the background color for a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns an RGB color value. On error, returns CLR_INVALID.


---

<!-- page: win32gui__GetBkMode_meth.html -->

## win32gui.GetBkMode

 int = GetBkMode(hdc)

Returns the background mode for a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns OPAQUE, TRANSPARENT, or 0 on failure


---

<!-- page: win32gui__GetCapture_meth.html -->

## win32gui.GetCapture

 int = GetCapture()

Returns the window with the mouse capture.


---

<!-- page: win32gui__GetCaretPos_meth.html -->

## win32gui.GetCaretPos

 int,int = GetCaretPos()

Returns the current caret position


---

<!-- page: win32gui__GetClassLong_meth.html -->

## win32gui.GetClassLong

 int = GetClassLong(hwnd, index )

#### Parameters

- hwnd : int

- index : int


---

<!-- page: win32gui__GetClassName_meth.html -->

## win32gui.GetClassName

 string = GetClassName(hwnd)

Retrieves the name of the class to which the specified window belongs.

#### Parameters

- hwnd : PyHANDLE

 The handle to the window


---

<!-- page: win32gui__GetClientRect_meth.html -->

## win32gui.GetClientRect

 (left, top, right, bottom) = GetClientRect(hwnd)

Returns the rectangle of the client area of a window, in client coordinates

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__GetCurrentObject_meth.html -->

## win32gui.GetCurrentObject

 PyHANDLE = GetCurrentObject(hdc, ObjectType )

Retrieves currently selected object from a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- ObjectType : int

 Type of object to retrieve, one of win32con.OBJ_*;


---

<!-- page: win32gui__GetCurrentPositionEx_meth.html -->

## win32gui.GetCurrentPositionEx

 (int,int) = GetCurrentPositionEx(hdc)

Returns a device context's current drawing position

#### Parameters

- hdc : PyHANDLE

 Device context


---

<!-- page: win32gui__GetCursorInfo_meth.html -->

## win32gui.GetCursorInfo

 flags, hcursor, (x,y) = GetCursorInfo()

Retrieves information about the global cursor.


---

<!-- page: win32gui__GetCursorPos_meth.html -->

## win32gui.GetCursorPos

 (int, int) = GetCursorPos()

retrieves the cursor's position, in screen coordinates.


---

<!-- page: win32gui__GetCursor_meth.html -->

## win32gui.GetCursor

 HCURSOR = GetCursor()


---

<!-- page: win32gui__GetDC_meth.html -->

## win32gui.GetDC

 HDC = GetDC(hwnd)

Gets the device context for the window.

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__GetDesktopWindow_meth.html -->

## win32gui.GetDesktopWindow

 int = GetDesktopWindow()

returns the desktop window


---

<!-- page: win32gui__GetDlgCtrlID_meth.html -->

## win32gui.GetDlgCtrlID

 int = GetDlgCtrlID(hwnd)

Retrieves the identifier of the specified control.

#### Parameters

- hwnd : int

 The handle to the control


---

<!-- page: win32gui__GetDlgItemInt_meth.html -->

## win32gui.GetDlgItemInt

 GetDlgItemInt(hDlg, IDDlgItem, Signed)

Returns the integer value of a dialog control

#### Parameters

- hDlg : PyHANDLE

 Handle to a dialog window

- IDDlgItem : int

 Identifier of one of the dialog's controls

- Signed : boolean

 Indicates whether control value should be interpreted as signed


---

<!-- page: win32gui__GetDlgItemText_meth.html -->

## win32gui.GetDlgItemText

 string = GetDlgItemText(hDlg, IDDlgItem )

Returns the text of a dialog control

#### Parameters

- hDlg : PyHANDLE

 Handle to a dialog window

- IDDlgItem : int

 The Id of a control within the dialog


---

<!-- page: win32gui__GetDlgItem_meth.html -->

## win32gui.GetDlgItem

 HWND = GetDlgItem(hDlg, IDDlgItem )

Retrieves the handle to a control in the specified dialog box.

#### Parameters

- hDlg : PyHANDLE

 Handle to a dialog window

- IDDlgItem : int

 Identifier of one of the dialog's controls


---

<!-- page: win32gui__GetDoubleClickTime_meth.html -->

## win32gui.GetDoubleClickTime

 int = GetDoubleClickTime()


---

<!-- page: win32gui__GetFocus_meth.html -->

## win32gui.GetFocus

 GetFocus()

Returns the HWND of the window with focus.


---

<!-- page: win32gui__GetForegroundWindow_meth.html -->

## win32gui.GetForegroundWindow

 HWND = GetForegroundWindow()


---

<!-- page: win32gui__GetGraphicsMode_meth.html -->

## win32gui.GetGraphicsMode

 int = GetGraphicsMode(hdc)

Determines if advanced GDI features are enabled for a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns GM_COMPATIBLE or GM_ADVANCED


---

<!-- page: win32gui__GetIconInfo_meth.html -->

## win32gui.GetIconInfo

 PyICONINFO = GetIconInfo(hicon)

Returns parameters for an icon or cursor

#### Parameters

- hicon : PyHANDLE

 The icon to query

#### Return Value

The result is a tuple of (fIcon, xHotspot, yHotspot, hbmMask, hbmColor) The hbmMask and hbmColor items are bitmaps created for the caller, so must be freed.


---

<!-- page: win32gui__GetLayeredWindowAttributes_meth.html -->

## win32gui.GetLayeredWindowAttributes

 (int,int,int) = GetLayeredWindowAttributes(hwnd)

Retrieves the layering parameters of a window with the WS_EX_LAYERED extended style

#### Parameters

- hwnd : PyHANDLE

 Handle to a layered window

#### Comments

 Accepts keyword arguments.

#### Return Value

Returns a tuple of (color key, alpha, flags)


---

<!-- page: win32gui__GetLayout_meth.html -->

## win32gui.GetLayout

 int = GetLayout(hdc)

Retrieves the layout mode of a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns one of win32con.LAYOUT_*


---

<!-- page: win32gui__GetMapMode_meth.html -->

## win32gui.GetMapMode

 int = GetMapMode(hdc)

Returns the method a device context uses to translate logical units to physical units

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns one of win32con.MM_* values


---

<!-- page: win32gui__GetMenuDefaultItem_meth.html -->

## win32gui.GetMenuDefaultItem

 int = GetMenuDefaultItem(hMenu, fByPos , flags )

#### Parameters

- hMenu : int

 Handle to the menu

- fByPos : int

- flags : int


---

<!-- page: win32gui__GetMenuInfo_meth.html -->

## win32gui.GetMenuInfo

 GetMenuInfo(hmenu, info)

Gets information about a specified menu.

#### Parameters

- hmenu : int

 handle to menu

- info : buffer

 A buffer to fill with the information.

#### Comments

 See win32gui_struct for helper functions.

 This function will raise NotImplementedError on early platforms (eg, Windows NT.)


---

<!-- page: win32gui__GetMenuItemCount_meth.html -->

## win32gui.GetMenuItemCount

 int = GetMenuItemCount(hMenu)

#### Parameters

- hMenu : int

 Handle to the menu


---

<!-- page: win32gui__GetMenuItemID_meth.html -->

## win32gui.GetMenuItemID

 int = GetMenuItemID(hMenu, nPos )

Retrieves the menu item identifier of a menu item located at the specified position in a menu.

#### Parameters

- hMenu : int

 handle to menu

- nPos : int

 position of menu item


---

<!-- page: win32gui__GetMenuItemInfo_meth.html -->

## win32gui.GetMenuItemInfo

 GetMenuItemInfo(hMenu, uItem, fByPosition, menuItem)

Gets menu information

#### Parameters

- hMenu : int

 Handle to the menu

- uItem : int

 The menu item identifier or the menu item position.

- fByPosition : int

 Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.

- menuItem : buffer

 A string or buffer that will receive the information in the format of a MENUITEMINFO structure.


---

<!-- page: win32gui__GetMenuItemRect_meth.html -->

## win32gui.GetMenuItemRect

 (int, int, int, int) = GetMenuItemRect(hWnd, hMenu , uItem )

#### Parameters

- hWnd : int

- hMenu : int

 Handle to the menu

- uItem : int


---

<!-- page: win32gui__GetMenuState_meth.html -->

## win32gui.GetMenuState

 int = GetMenuState(hMenu, uID , flags )

#### Parameters

- hMenu : int

 Handle to the menu

- uID : int

- flags : int


---

<!-- page: win32gui__GetMenu_meth.html -->

## win32gui.GetMenu

 GetMenu()

Gets the menu for the specified window.


---

<!-- page: win32gui__GetMessage_meth.html -->

## win32gui.GetMessage

 MSG = GetMessage(hwnd, min , max )

#### Parameters

- hwnd : int

- min : int

- max : int


---

<!-- page: win32gui__GetMiterLimit_meth.html -->

## win32gui.GetMiterLimit

 float = GetMiterLimit(hdc)

Retrieves the limit of miter joins for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__GetNextDlgGroupItem_meth.html -->

## win32gui.GetNextDlgGroupItem

 HWND = GetNextDlgGroupItem(hDlg, hCtl , bPrevious )

Retrieves a handle to the first control in a group of controls that precedes (or follows) the specified control in a dialog box.

#### Parameters

- hDlg : int

 handle to dialog box

- hCtl : int

 handle to known control

- bPrevious : int

 direction flag


---

<!-- page: win32gui__GetNextDlgTabItem_meth.html -->

## win32gui.GetNextDlgTabItem

 HWND = GetNextDlgTabItem(hDlg, hCtl , bPrevious )

Retrieves a handle to the first control that has the WS_TABSTOP style that precedes (or follows) the specified control.

#### Parameters

- hDlg : int

 handle to dialog box

- hCtl : int

 handle to known control

- bPrevious : int

 direction flag


---

<!-- page: win32gui__GetObjectType_meth.html -->

## win32gui.GetObjectType

 int = GetObjectType(h)

Returns the type (OBJ_* constant) of a GDI handle

#### Parameters

- h : PyHANDLE

 A handle to a GDI object


---

<!-- page: win32gui__GetObject_meth.html -->

## win32gui.GetObject

 object = GetObject(handle)

Returns a struct containing the parameters used to create a GDI object

#### Parameters

- handle : PyHANDLE

 Handle to the object.

#### Comments

 The result depends on the type of the handle.

| | Object type as determined by win32gui::GetObjectType | Returned object
| |

---

 |

---

| | OBJ_FONT | PyLOGFONT
| | OBJ_BITMAP | PyBITMAP
| | OBJ_PEN | Dict representing a LOGPEN struct


---

<!-- page: win32gui__GetOpenFileNameW_meth.html -->

## win32gui.GetOpenFileNameW

 (string,string, int) = GetOpenFileNameW(hwndOwner, hInstance , Filter , CustomFilter , FilterIndex , File , MaxFile , InitialDir , Title , Flags , DefExt , TemplateName )

Creates a dialog to allow user to select file(s) to open

#### Parameters

- hwndOwner=None : PyHANDLE

 Handle to window that owns dialog

- hInstance=None : PyHANDLE

 Handle to module that contains dialog template

- Filter=None : string

 Contains pairs of descriptions and filespecs separated by NULLS, with a final trailing NULL. Example: 'Python Scripts\\0*.py;*.pyw;*.pys\\0Text files\\0*.txt\\0'

- CustomFilter=None : string

 Description to be used for filter that user selected or typed, can also contain a filespec as above

- FilterIndex=0 : int

 Specifies which of the filters is initially selected, use 0 for CustomFilter

- File=None : string

 The file name initially displayed

- MaxFile=1024 : int

 Number of characters to allocate for selected filename, override if large number of files expected

- InitialDir=None : string

 The starting directory

- Title=None : string

 The title of the dialog box

- Flags=0 : int

 Combination of win32con.OFN_* constants

- DefExt=None : string

 The default extension to use

- TemplateName=None : PyResourceId

 Name or resource id of dialog box template

#### Comments

 Accepts keyword arguments, all arguments optional Input parameters and return values are identical to win32gui::GetSaveFileNameW


---

<!-- page: win32gui__GetOpenFileName_meth.html -->

## win32gui.GetOpenFileName

 int = GetOpenFileName(OPENFILENAME)

Creates an Open dialog box that lets the user specify the drive, directory, and the name of a file or set of files to open.

#### Parameters

- OPENFILENAME : string/bytes

 A string packed into an OPENFILENAME structure, probably via the struct module.

#### Comments

 The win32gui::GetOpenFileNameW function is far more convenient to use.

#### Return Value

If the user presses OK, the function returns TRUE. Otherwise, use CommDlgExtendedError for error details (ie, a win32gui.error is raised). If the user cancels the dialog, the winerror attribute of the exception will be zero.


---

<!-- page: win32gui__GetParent_meth.html -->

## win32gui.GetParent

 int = GetParent(child)

Retrieves a handle to the specified child window's parent window.

#### Parameters

- child : int

 handle to child window


---

<!-- page: win32gui__GetPath_meth.html -->

## win32gui.GetPath

 tuple,tuple = GetPath(hdc)

Returns a sequence of points that describe the current path

#### Parameters

- hdc : PyHANDLE

 Handle to a device context containing a finalized path. See win32gui::EndPath

#### Return Value

Returns a sequence of POINT tuples, and a sequence of ints designating each point's function (combination of win32con.PT_* values)


---

<!-- page: win32gui__GetPixel_meth.html -->

## win32gui.GetPixel

 int = GetPixel(hdc, XPos , YPos )

Returns the RGB color of a single pixel

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- XPos : int

 Horizontal pos

- YPos : int

 Vertical pos


---

<!-- page: win32gui__GetPolyFillMode_meth.html -->

## win32gui.GetPolyFillMode

 int = GetPolyFillMode(hdc)

Returns the polygon filling mode for a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns win32con.ALTERNATE or win32con.WINDING


---

<!-- page: win32gui__GetROP2_meth.html -->

## win32gui.GetROP2

 int = GetROP2(hdc)

Returns the foreground mixing mode of a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns one of win32con.R2_* values


---

<!-- page: win32gui__GetRgnBox_meth.html -->

## win32gui.GetRgnBox

 int, PyRECT = GetRgnBox(hrgn)

Calculates the bounding box of a region

#### Parameters

- hrgn : PyGdiHANDLE

 Handle to a region

#### Return Value

Returns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION) and rectangle in logical units


---

<!-- page: win32gui__GetSaveFileNameW_meth.html -->

## win32gui.GetSaveFileNameW

 (string, string,int) = GetSaveFileNameW(hwndOwner, hInstance , Filter , CustomFilter , FilterIndex , File , MaxFile , InitialDir , Title , Flags , DefExt , TemplateName )

Creates a dialog for user to specify location to save a file or files

#### Parameters

- hwndOwner=None : PyHANDLE

 Handle to window that owns dialog

- hInstance=None : PyHANDLE

 Handle to module that contains dialog template

- Filter=None : string

 Contains pairs of descriptions and filespecs separated by NULLS, with a final trailing NULL. Example: 'Python Scripts\\0*.py;*.pyw;*.pys\\0Text files\\0*.txt\\0'

- CustomFilter=None : string

 Description to be used for filter that user selected or typed, can also contain a filespec as above

- FilterIndex=0 : int

 Specifies which of the filters is initially selected, use 0 for CustomFilter

- File=None : string

 The file name initially displayed

- MaxFile=1024 : int

 Number of characters to allocate for selected filename(s), override if large number of files expected

- InitialDir=None : string

 The starting directory

- Title=None : string

 The title of the dialog box

- Flags=0 : int

 Combination of win32con.OFN_* constants

- DefExt=None : string

 The default extension to use

- TemplateName=None : PyResourceId

 Name or resource id of dialog box template

#### Comments

 Accepts keyword arguments, all arguments optional

#### Return Value

Returns a tuple of 3 values (string, string, int):
 First is the selected file(s). If multiple files are selected, returned string will be the directory followed by files names separated by nulls, otherwise it will be the full path. In other words, if you use the OFN_ALLOWMULTISELECT flag you should split this value on \\0 characters and if the length of the result list is 1, it will be the full path, otherwise element 0 will be the directory and the rest of the elements will be filenames in this directory.
 Second is a unicode string containing user-selected filter, will be None if CustomFilter was not specified
 Third item contains flags pertaining to users input, such as OFN_READONLY and OFN_EXTENSIONDIFFERENT
If the user presses cancel or an error occurs, a win32gui.error is raised. If the user pressed cancel, the error number (ie, the winerror attribute of the exception) will be zero.


---

<!-- page: win32gui__GetScrollInfo_meth.html -->

## win32gui.GetScrollInfo

 PySCROLLINFO = GetScrollInfo(hwnd, nBar , mask )

Returns information about a scroll bar

#### Parameters

- hwnd : int

 The handle to the window.

- nBar : int

 The scroll bar to examine. Can be one of win32con.SB_CTL, win32con.SB_VERT or win32con.SB_HORZ

- mask=SIF_ALL : int

 The mask for attributes to retrieve.


---

<!-- page: win32gui__GetStockObject_meth.html -->

## win32gui.GetStockObject

 PyHANDLE = GetStockObject(Object)

Creates a handle to one of the standard system Gdi objects

#### Parameters

- Object : int

 One of *_BRUSH, *_PEN, *_FONT, or *_PALLETTE constants


---

<!-- page: win32gui__GetStretchBltMode_meth.html -->

## win32gui.GetStretchBltMode

 int = GetStretchBltMode(hdc)

Returns the stretching mode used by win32gui::StretchBlt

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns one of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS,WHITEONBLACK, or 0 on error.


---

<!-- page: win32gui__GetSubMenu_meth.html -->

## win32gui.GetSubMenu

 HMENU = GetSubMenu(hMenu, nPos )

#### Parameters

- hMenu : int

 Handle to the menu

- nPos : int


---

<!-- page: win32gui__GetSysColorBrush_meth.html -->

## win32gui.GetSysColorBrush

 PyGdiHANDLE = GetSysColorBrush(Index)

Creates a handle to a system color brush

#### Parameters

- Index : int

 Index of a window element color (win32con.COLOR_*)


---

<!-- page: win32gui__GetSysColor_meth.html -->

## win32gui.GetSysColor

 int = GetSysColor(Index)

Returns the color of a window element

#### Parameters

- Index : int

 One of win32con.COLOR_* values


---

<!-- page: win32gui__GetSystemMenu_meth.html -->

## win32gui.GetSystemMenu

 int = GetSystemMenu(hwnd, bRevert )

#### Parameters

- hwnd : int

 The handle to the window

- bRevert : int

#### Return Value

The result is a HMENU to the menu.


---

<!-- page: win32gui__GetTextAlign_meth.html -->

## win32gui.GetTextAlign

 int = GetTextAlign(hdc)

Returns horizontal and vertical alignment for text in a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns combination of win32con.TA_* flags


---

<!-- page: win32gui__GetTextCharacterExtra_meth.html -->

## win32gui.GetTextCharacterExtra

 int = GetTextCharacterExtra(hdc)

Returns the space between characters

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__GetTextColor_meth.html -->

## win32gui.GetTextColor

 int = GetTextColor(hdc)

Returns the text color for a DC

#### Parameters

- hdc : int

 Handle to a device context

#### Return Value

Returns an RGB color. On error, returns CLR_INVALID


---

<!-- page: win32gui__GetTextExtentPoint32_meth.html -->

## win32gui.GetTextExtentPoint32

 cx, cy = GetTextExtentPoint32(hdc, str )

Computes the width and height of the specified string of text.

#### Parameters

- hdc : PyHANDLE

 The device context

- str : string

 The string to measure.


---

<!-- page: win32gui__GetTextFace_meth.html -->

## win32gui.GetTextFace

 string = GetTextFace(hdc)

Retrieves the name of the font currently selected in a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Comments

 Calls unicode api function (GetTextFaceW)


---

<!-- page: win32gui__GetTextMetrics_meth.html -->

## win32gui.GetTextMetrics

 dict = GetTextMetrics()

Returns info for the font selected into a DC


---

<!-- page: win32gui__GetTopWindow_meth.html -->

## win32gui.GetTopWindow

 int = GetTopWindow(hWnd)

Examines the Z order of the child windows associated with the specified parent window and retrieves a handle to the child window at the top of the Z order.

#### Parameters

- hWnd : int

 handle to parent window


---

<!-- page: win32gui__GetUpdateRgn_meth.html -->

## win32gui.GetUpdateRgn

 int = GetUpdateRgn(hWnd, hRgn , Erase )

Copies the update region of a window into an existing region

#### Parameters

- hWnd : PyHANDLE

 Handle to a window

- hRgn : PyGdiHANDLE

 Handle to an existing region to receive update area

- Erase : boolean

 Indicates if window background is to be erased

#### Return Value

Returns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION


---

<!-- page: win32gui__GetViewportExtEx_meth.html -->

## win32gui.GetViewportExtEx

 (int,int) = GetViewportExtEx(hdc)

Retrieves the viewport extents for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns the extents as (x,y) in logical units


---

<!-- page: win32gui__GetViewportOrgEx_meth.html -->

## win32gui.GetViewportOrgEx

 (int,int) = GetViewportOrgEx(hdc)

Retrievs the origin for a DC's viewport

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__GetWindowDC_meth.html -->

## win32gui.GetWindowDC

 int = GetWindowDC(hWnd)

returns the device context (DC) for the entire window, including title bar, menus, and scroll bars.

#### Parameters

- hWnd : int

 handle of window


---

<!-- page: win32gui__GetWindowExtEx_meth.html -->

## win32gui.GetWindowExtEx

 (int,int) = GetWindowExtEx(hdc)

Retrieves the window extents for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Return Value

Returns the extents as (x,y) in logical units


---

<!-- page: win32gui__GetWindowLong_meth.html -->

## win32gui.GetWindowLong

 int = GetWindowLong(hwnd, index )

#### Parameters

- hwnd : int

- index : int


---

<!-- page: win32gui__GetWindowOrgEx_meth.html -->

## win32gui.GetWindowOrgEx

 (int,int) = GetWindowOrgEx(hdc)

Retrievs the window origin for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__GetWindowPlacement_meth.html -->

## win32gui.GetWindowPlacement

 tuple = GetWindowPlacement()

Returns placement information about the current window.

#### Return Value

The result is a tuple of (flags, showCmd, (minposX, minposY), (maxposX, maxposY), (normalposX, normalposY))

| | Item | Description
| |

---

 |

---

| | flags | One of the WPF_* constants
| | showCmd | Current state - one of the SW_* constants.
| | minpos | Specifies the coordinates of the window's upper-left corner when the window is minimized.
| | maxpos | Specifies the coordinates of the window's upper-left corner when the window is maximized.
| | normalpos | Specifies the window's coordinates when the window is in the restored position.


---

<!-- page: win32gui__GetWindowRect_meth.html -->

## win32gui.GetWindowRect

 (left, top, right, bottom) = GetWindowRect(hwnd)

Returns the rectangle for a window in screen coordinates

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__GetWindowRgnBox_meth.html -->

## win32gui.GetWindowRgnBox

 int, PyRECT = GetWindowRgnBox(hWnd)

Returns the bounding box for a window's region

#### Parameters

- hWnd : PyHANDLE

 Handle to a window that has a window region. (see win32gui::SetWindowRgn)

#### Return Value

Returns type of region and rectangle coordinates in device units


---

<!-- page: win32gui__GetWindowRgn_meth.html -->

## win32gui.GetWindowRgn

 int = GetWindowRgn(hWnd, hRgn )

Copies the window region of a window into an existing region

#### Parameters

- hWnd : PyHANDLE

 Handle to a window

- hRgn : PyGdiHANDLE

 Handle to an existing region that receives window region

#### Return Value

Returns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION


---

<!-- page: win32gui__GetWindowText_meth.html -->

## win32gui.GetWindowText

 string = GetWindowText(hwnd)

Get the window text.

#### Parameters

- hwnd : PyHANDLE

 The handle to the window


---

<!-- page: win32gui__GetWindow_meth.html -->

## win32gui.GetWindow

 int = GetWindow(hWnd, uCmd )

returns a window that has the specified relationship (Z order or owner) to the specified window.

#### Parameters

- hWnd : int

 handle to original window

- uCmd : int

 relationship flag


---

<!-- page: win32gui__GetWorldTransform_meth.html -->

## win32gui.GetWorldTransform

 PyXFORM = GetWorldTransform(hdc)

Retrieves a device context's coordinate space translation matrix

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

#### Comments

 DC's mode must be set to GM_ADVANCED. See win32gui::SetGraphicsMode.


---

<!-- page: win32gui__GradientFill_meth.html -->

## win32gui.GradientFill

 GradientFill(hdc, Vertex, Mesh, Mode)

Shades triangles or rectangles by interpolating between vertex colors

#### Parameters

- hdc : int

 Handle to device context

- Vertex : (PyTRIVERTEX,...)

 Sequence of TRIVERTEX dicts defining color info

- Mesh : tuple

 Sequence of tuples containing either 2 or 3 ints that index into the trivertex array to define either triangles or rectangles

- Mode : int

 win32con.GRADIENT_FILL_* value defining whether to fill by triangle or by rectangle


---

<!-- page: win32gui__HideCaret_meth.html -->

## win32gui.HideCaret

 HideCaret(hWnd)

Hides the caret

#### Parameters

- hWnd : PyHANDLE

 Window that owns the caret, can be 0.


---

<!-- page: win32gui__ImageList_Add_meth.html -->

## win32gui.ImageList_Add

 int = ImageList_Add(himl, hbmImage , hbmMask )

Adds an image or images to an image list.

#### Parameters

- himl : int

 Handle to the image list.

- hbmImage : PyGdiHANDLE

 Handle to the bitmap that contains the image or images. The number of images is inferred from the width of the bitmap.

- hbmMask : PyGdiHANDLE

 Handle to the bitmap that contains the mask. If no mask is used with the image list, this parameter is ignored

#### Return Value

Returns the index of the first new image if successful, or -1 otherwise.


---

<!-- page: win32gui__ImageList_Create_meth.html -->

## win32gui.ImageList_Create

 HIMAGELIST = ImageList_Create()

Create an image list


---

<!-- page: win32gui__ImageList_Destroy_meth.html -->

## win32gui.ImageList_Destroy

 BOOL = ImageList_Destroy()

Destroy an imagelist


---

<!-- page: win32gui__ImageList_DrawEx_meth.html -->

## win32gui.ImageList_DrawEx

 BOOL = ImageList_DrawEx()

Draw an image on an HDC


---

<!-- page: win32gui__ImageList_Draw_meth.html -->

## win32gui.ImageList_Draw

 BOOL = ImageList_Draw()

Draw an image on an HDC


---

<!-- page: win32gui__ImageList_GetIcon_meth.html -->

## win32gui.ImageList_GetIcon

 HICON = ImageList_GetIcon()

Extract an icon from an imagelist


---

<!-- page: win32gui__ImageList_GetImageCount_meth.html -->

## win32gui.ImageList_GetImageCount

 int = ImageList_GetImageCount()

Return count of images in imagelist


---

<!-- page: win32gui__ImageList_LoadBitmap_meth.html -->

## win32gui.ImageList_LoadBitmap

 HANDLE = ImageList_LoadBitmap()

Creates an image list from the specified bitmap resource.


---

<!-- page: win32gui__ImageList_LoadImage_meth.html -->

## win32gui.ImageList_LoadImage

 HANDLE = ImageList_LoadImage()

Loads bitmaps, cursors or icons, creates imagelist


---

<!-- page: win32gui__ImageList_Remove_meth.html -->

## win32gui.ImageList_Remove

 BOOL = ImageList_Remove()

Remove an image from an imagelist


---

<!-- page: win32gui__ImageList_ReplaceIcon_meth.html -->

## win32gui.ImageList_ReplaceIcon

 BOOL = ImageList_ReplaceIcon()

Replace an image in an imagelist with an icon image


---

<!-- page: win32gui__ImageList_Replace_meth.html -->

## win32gui.ImageList_Replace

 BOOL = ImageList_Replace()

Replace an image in an imagelist with a bitmap image


---

<!-- page: win32gui__ImageList_SetBkColor_meth.html -->

## win32gui.ImageList_SetBkColor

 COLORREF = ImageList_SetBkColor()

Set the background color for the imagelist


---

<!-- page: win32gui__ImageList_SetOverlayImage_meth.html -->

## win32gui.ImageList_SetOverlayImage

 ImageList_SetOverlayImage(hImageList, iImage, iOverlay)

Adds a specified image to the list of images to be used as overlay masks. An image list can have up to four overlay masks in version 4.70 and earlier and up to 15 in version 4.71. The function assigns an overlay mask index to the specified image.

#### Parameters

- hImageList : int

- iImage : int

- iOverlay : int


---

<!-- page: win32gui__InitCommonControlsEx_meth.html -->

## win32gui.InitCommonControlsEx

 InitCommonControlsEx(flag)

Initializes specific common controls.

#### Parameters

- flag : int

 One of the ICC_ constants


---

<!-- page: win32gui__InitCommonControls_meth.html -->

## win32gui.InitCommonControls

 InitCommonControls()

Initializes the common controls.


---

<!-- page: win32gui__InsertMenuItem_meth.html -->

## win32gui.InsertMenuItem

 InsertMenuItem(hMenu, uItem, fByPosition, menuItem)

Inserts a menu item

#### Parameters

- hMenu : int

 Handle to the menu

- uItem : int

 The menu item identifier or the menu item position.

- fByPosition : int

 Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.

- menuItem : buffer

 A string or buffer in the format of a MENUITEMINFO structure.


---

<!-- page: win32gui__InsertMenu_meth.html -->

## win32gui.InsertMenu

 InsertMenu()


---

<!-- page: win32gui__InvalidateRect_meth.html -->

## win32gui.InvalidateRect

 InvalidateRect(hWnd, Rect, Erase)

Invalidates a rectangular area of a window and adds it to the window's update region

#### Parameters

- hWnd : PyHANDLE

 Handle to the window

- Rect : PyRECT

 Client coordinates defining area to be redrawn. Use None for entire client area.

- Erase : boolean

 Indicates if background should be erased


---

<!-- page: win32gui__InvalidateRgn_meth.html -->

## win32gui.InvalidateRgn

 InvalidateRgn(hWnd, hRgn, Erase)

Adds a region to a window's update region

#### Parameters

- hWnd : PyHANDLE

 Handle to the window

- hRgn : PyGdiHANDLE

 Region to be redrawn

- Erase : boolean

 Indidates if background should be erased


---

<!-- page: win32gui__InvertRect_meth.html -->

## win32gui.InvertRect

 InvertRect(hDC, rc)

Inverts the colors in a regtangular region

#### Parameters

- hDC : PyHANDLE

 Handle to a device context

- rc : PyRECT

 Coordinates of rectangle to invert


---

<!-- page: win32gui__InvertRgn_meth.html -->

## win32gui.InvertRgn

 InvertRgn(hdc, hrgn)

Inverts the colors in a region

#### Parameters

- hdc : PyHANDLE

 Handle to the device context

- hrgn : PyGdiHandle

 Handle to the region


---

<!-- page: win32gui__IsChild_meth.html -->

## win32gui.IsChild

 IsChild(hWndParent, hWnd)

Tests whether a window is a child window or descendant window of a specified parent window

#### Parameters

- hWndParent : int

 handle to parent window

- hWnd : int

 handle to window to test


---

<!-- page: win32gui__IsIconic_meth.html -->

## win32gui.IsIconic

 IsIconic(hWnd)

determines whether the specified window is minimized (iconic).

#### Parameters

- hWnd : int

 handle to window


---

<!-- page: win32gui__IsWindowEnabled_meth.html -->

## win32gui.IsWindowEnabled

 int = IsWindowEnabled(hwnd)

Indicates if the window is enabled.

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__IsWindowVisible_meth.html -->

## win32gui.IsWindowVisible

 int = IsWindowVisible(hwnd)

Indicates if the window has the WS_VISIBLE style.

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__IsWindow_meth.html -->

## win32gui.IsWindow

 IsWindow(hWnd)

determines whether the specified window handle identifies an existing window.

#### Parameters

- hWnd : int

 handle to window


---

<!-- page: win32gui__LOGFONT_meth.html -->

## win32gui.LOGFONT

 PyLOGFONT = LOGFONT()

Creates a LOGFONT object.


---

<!-- page: win32gui__LineTo_meth.html -->

## win32gui.LineTo

 LineTo(hdc, XEnd, YEnd)

Draw a line from current position to specified point

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- XEnd : int

 Horizontal position in logical units

- YEnd : int

 Vertical position in logical units


---

<!-- page: win32gui__ListView_SortItemsEx_meth.html -->

## win32gui.ListView_SortItemsEx

 ListView_SortItemsEx(hwnd, callback, param)

Uses an application-defined comparison function to sort the items of a list view control.

#### Parameters

- hwnd : int

 The handle to the window

- callback : object

 A callback object, taking 3 params.

- param=None : object

 The third param to the callback function.


---

<!-- page: win32gui__ListView_SortItems_meth.html -->

## win32gui.ListView_SortItems

 ListView_SortItems(hwnd, callback, param)

Uses an application-defined comparison function to sort the items of a list view control.

#### Parameters

- hwnd : int

 The handle to the window

- callback : object

 A callback object, taking 3 params.

- param=None : object

 The third param to the callback function.


---

<!-- page: win32gui__LoadCursor_meth.html -->

## win32gui.LoadCursor

 HCURSOR = LoadCursor(hinstance, resid )

Loads a cursor.

#### Parameters

- hinstance : int

 The module to load from

- resid : int

 The resource ID


---

<!-- page: win32gui__LoadIcon_meth.html -->

## win32gui.LoadIcon

 HCURSOR = LoadIcon(hinstance, resource_id )

Loads an icon

#### Parameters

- hinstance : int

- resource_id : int/string


---

<!-- page: win32gui__LoadImage_meth.html -->

## win32gui.LoadImage

 HANDLE = LoadImage(hinst, name , type , cxDesired , cyDesired , fuLoad )

Loads a bitmap, cursor or icon

#### Parameters

- hinst : int

 Handle to an instance of the module that contains the image to be loaded. To load an OEM image, set this parameter to zero.

- name : int/string

 Specifies the image to load. If the hInst parameter is non-zero and the fuLoad parameter omits LR_LOADFROMFILE, name specifies the image resource in the hInst module. If the image resource is to be loaded by name, the name parameter is a string that contains the name of the image resource.

- type : int

 Specifies the type of image to be loaded.

- cxDesired : int

 Specifies the width, in pixels, of the icon or cursor. If this parameter is zero and the fuLoad parameter is LR_DEFAULTSIZE, the function uses the SM_CXICON or SM_CXCURSOR system metric value to set the width. If this parameter is zero and LR_DEFAULTSIZE is not used, the function uses the actual resource width.

- cyDesired : int

 Specifies the height, in pixels, of the icon or cursor. If this parameter is zero and the fuLoad parameter is LR_DEFAULTSIZE, the function uses the SM_CYICON or SM_CYCURSOR system metric value to set the height. If this parameter is zero and LR_DEFAULTSIZE is not used, the function uses the actual resource height.

- fuLoad : int


---

<!-- page: win32gui__LoadMenu_meth.html -->

## win32gui.LoadMenu

 HMENU = LoadMenu(hinstance, resource_id )

Loads a menu

#### Parameters

- hinstance : int

- resource_id : int/string


---

<!-- page: win32gui__MaskBlt_meth.html -->

## win32gui.MaskBlt

 MaskBlt(Dest, XDest, YDest, Width, Height, Src, XSrc, YSrc, Mask, xMask, yMask, Rop)

Combines the color data for the source and destination bitmaps using the specified mask and raster operation.

#### Parameters

- Dest : PyHANDLE

 Destination device context handle

- XDest : int

 X pos of dest rect

- YDest : int

 Y pos of dest rect

- Width : int

 Width of rect to be copied

- Height : int

 Height of rect to be copied

- Src : PyHANDLE

 Source DC handle

- XSrc : int

 X pos of src rect

- YSrc : int

 Y pos of src rect

- Mask : PyGdiHANDLE

 Handle to monochrome bitmap used to mask color

- xMask : int

 X pos in mask

- yMask : int

 Y pos in mask

- Rop : int

 Foreground and background raster operations. See MSDN docs for how to construct this value.

#### Win32 API References

- Search for MaskBlt at [msdn](https://learn.microsoft.com/en-ca/search/?terms=MaskBlt), [google](https://www.google.com/search?q=MaskBlt) or [google groups](https://groups.google.com/groups?q=MaskBlt).


---

<!-- page: win32gui__MessageBeep_meth.html -->

## win32gui.MessageBeep

 MessageBeep(type)

Plays a waveform sound.

#### Parameters

- type : int

 The type of the beep


---

<!-- page: win32gui__MessageBox_meth.html -->

## win32gui.MessageBox

 int = MessageBox(parent, text , caption , flags )

Displays a message box

#### Parameters

- parent : int

 The parent window

- text : string

 The text for the message box

- caption : string

 The caption for the message box

- flags : int


---

<!-- page: win32gui__ModifyMenu_meth.html -->

## win32gui.ModifyMenu

 ModifyMenu(hMnu, uPosition, uFlags, uIDNewItem, newItem)

Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item.

#### Parameters

- hMnu : int

 handle to menu

- uPosition : int

 menu item to modify

- uFlags : int

 options

- uIDNewItem : int

 identifier, menu, or submenu

- newItem : string

 menu item content


---

<!-- page: win32gui__ModifyWorldTransform_meth.html -->

## win32gui.ModifyWorldTransform

 ModifyWorldTransform(hdc, Xform, Mode)

Combines a coordinate tranformation with device context's current transformation

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Xform : PyXFORM

 Transformation to be applied. Ignored if Mode is MWT_IDENTITY.

- Mode : int

 One of win32con.MWT_* values specifying how transformations will be combined

#### Comments

 DC's mode must be set to GM_ADVANCED. See win32gui::SetGraphicsMode.


---

<!-- page: win32gui__MoveToEx_meth.html -->

## win32gui.MoveToEx

 (int, int) = MoveToEx(hdc, X , Y )

Changes the current drawing position

#### Parameters

- hdc : PyHANDLE

 Device context handle

- X : int

 Horizontal pos in logical units

- Y : int

 Vertical pos in logical units

#### Return Value

Returns the previous position as (X, Y)


---

<!-- page: win32gui__MoveWindow_meth.html -->

## win32gui.MoveWindow

 MoveWindow(hwnd, x, y, width, height, bRepaint)

#### Parameters

- hwnd : int

 The handle to the window

- x : int

- y : int

- width : int

- height : int

- bRepaint : int


---

<!-- page: win32gui__OffsetRgn_meth.html -->

## win32gui.OffsetRgn

 int = OffsetRgn(hrgn, XOffset , YOffset )

Relocates a region

#### Parameters

- hrgn : PyGdiHANDLE

 Handle to a region

- XOffset : int

 Horizontal offset

- YOffset : int

 Vertical offset

#### Return Value

Returns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION)


---

<!-- page: win32gui__PaintDesktop_meth.html -->

## win32gui.PaintDesktop

 PaintDesktop(hdc)

Fills a DC with the destop background

#### Parameters

- hdc : PyHANDLE

 Handle to a device context


---

<!-- page: win32gui__PaintRgn_meth.html -->

## win32gui.PaintRgn

 PaintRgn(hdc, hrgn)

Paints a region with current brush

#### Parameters

- hdc : PyHANDLE

 Handle to the device context

- hrgn : PyGdiHANDLE

 Handle to the region


---

<!-- page: win32gui__PatBlt_meth.html -->

## win32gui.PatBlt

 PatBlt(hdc, XLeft, YLeft, Width, Height, Rop)

Paints a rectangle by combining the current brush with existing colors

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- XLeft : int

 Horizontal pos

- YLeft : int

 Vertical pos

- Width : int

 Width of rectangular area

- Height : int

 Height of rectangular area

- Rop : int

 Raster operation, one of PATCOPY,PATINVERT,DSTINVERT,BLACKNESS,WHITENESS


---

<!-- page: win32gui__PathToRegion_meth.html -->

## win32gui.PathToRegion

 PyGdiHANDLE = PathToRegion(hdc)

Converts a closed path in a DC to a region

#### Parameters

- hdc : PyHANDLE

 Handle to a device context that contains a closed path. See win32gui::EndPath.

#### Comments

 On success, the path is deselected from the DC


---

<!-- page: win32gui__PeekMessage_meth.html -->

## win32gui.PeekMessage

 MSG = PeekMessage(hwnd, filterMin , filterMax , removalOptions )

#### Parameters

- hwnd : int

- filterMin : int

- filterMax : int

- removalOptions : int


---

<!-- page: win32gui__Pie_meth.html -->

## win32gui.Pie

 Pie(hdc, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2)

Draws a section of an ellipse cut by 2 radials

#### Parameters

- hdc : PyHANDLE

 Device context on which to draw

- LeftRect : int

 Left limit of ellipse

- TopRect : int

 Top limit of ellipse

- RightRect : int

 Right limit of ellipse

- BottomRect : int

 Bottom limit of ellipse

- XRadial1 : int

 Horizontal pos of Radial1 endpoint

- YRadial1 : int

 Vertical pos of Radial1 endpoint

- XRadial2 : int

 Horizontal pos of Radial2 endpoint

- YRadial2 : int

 Vertical pos of Radial2 endpoint


---

<!-- page: win32gui__PlgBlt_meth.html -->

## win32gui.PlgBlt

 PlgBlt(Dest, Point, Src, XSrc, YSrc, Width, Height, Mask, xMask, yMask)

Copies color from a rectangle into a parallelogram

#### Parameters

- Dest : PyHANDLE

 Destination DC

- Point : tuple

 Sequence of 3 POINT tuples (x,y) describing a paralellogram

- Src : PyHANDLE

 Source device context

- XSrc : int

 Left edge of source rectangle

- YSrc : int

 Top of source rectangle

- Width : int

 Width of source rectangle

- Height : int

 Height of source rectangle

- Mask=None : PyGdiHANDLE

 Handle to monochrome bitmap to mask source, can be None

- xMask=0 : int

 x pos in mask

- yMask=0 : int

 y pos in mask


---

<!-- page: win32gui__PolyBezierTo_meth.html -->

## win32gui.PolyBezierTo

 PolyBezierTo(hdc, Points)

Draws a series of Bezier curves starting from current drawing position.

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Points : [(int,int),...]

 Sequence of POINT tuples: ((x,y),...).

#### Comments

 Points must contain 3 points for each curve. Current position is updated with last endpoint.


---

<!-- page: win32gui__PolyBezier_meth.html -->

## win32gui.PolyBezier

 PolyBezier(hdc, Points)

Draws a series of Bezier curves starting from first point specified.

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Points : [(int,int),...]

 Sequence of POINT tuples: ((x,y),...).

#### Comments

 Number of points must be a multiple of 3 plus 1.


---

<!-- page: win32gui__Polygon_meth.html -->

## win32gui.Polygon

 Polygon(hdc, Points)

Draws a closed filled polygon defined by a sequence of points

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Points : [(int,int),...]

 Sequence of POINT tuples: ((x,y),...)


---

<!-- page: win32gui__PolylineTo_meth.html -->

## win32gui.PolylineTo

 PolylineTo(hdc, Points)

Draws a series of lines starting from current position. Updates current position with end point.

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Points : [(int,int),...]

 Sequence of POINT tuples: ((x,y),...)


---

<!-- page: win32gui__Polyline_meth.html -->

## win32gui.Polyline

 Polyline(hdc, Points)

Connects a sequence of points using currently selected pen

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Points : [(int,int),...]

 Sequence of POINT tuples: ((x,y),...)


---

<!-- page: win32gui__PostMessage_meth.html -->

## win32gui.PostMessage

 PostMessage(hwnd, message, wparam, lparam)

#### Parameters

- hwnd : int

 The handle to the Window

- message : int

 The ID of the message to post

- wparam=0 : int

 An integer whose value depends on the message

- lparam=0 : int

 An integer whose value depends on the message


---

<!-- page: win32gui__PostQuitMessage_meth.html -->

## win32gui.PostQuitMessage

 PostQuitMessage(rc)

#### Parameters

- rc : int


---

<!-- page: win32gui__PostThreadMessage_meth.html -->

## win32gui.PostThreadMessage

 PostThreadMessage(threadId, message, wparam, lparam)

#### Parameters

- threadId : int

 The ID of the thread to post the message to.

- message : int

 The ID of the message to post

- wparam : int

 An integer whose value depends on the message

- lparam : int

 An integer whose value depends on the message


---

<!-- page: win32gui__PtInRect_meth.html -->

## win32gui.PtInRect

 boolean = PtInRect(rect, point )

Determines if a rectangle contains a point

#### Parameters

- rect : (int, int, int, int)

 The rect to check

- point : (int,int)

 The point


---

<!-- page: win32gui__PtInRegion_meth.html -->

## win32gui.PtInRegion

 boolean = PtInRegion(hrgn, X , Y )

Determines if a region contains a point

#### Parameters

- hrgn : PyGdiHandle

 Handle to a region

- X : int

 X coord

- Y : int

 Y coord


---

<!-- page: win32gui__PumpMessages_meth.html -->

## win32gui.PumpMessages

 PumpMessages()

Runs a message loop until a WM_QUIT message is received.

#### See Also

- win32gui::PumpWaitingMessages

#### Return Value

Returns exit code from PostQuitMessage when a WM_QUIT message is received


---

<!-- page: win32gui__PumpWaitingMessages_meth.html -->

## win32gui.PumpWaitingMessages

 int = PumpWaitingMessages()

Pumps all waiting messages for the current thread.

#### See Also

- win32gui::PumpMessages

#### Win32 API References

- Search for PeekMessage and DispatchMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PeekMessage and DispatchMessage), [google](https://www.google.com/search?q=PeekMessage and DispatchMessage) or [google groups](https://groups.google.com/groups?q=PeekMessage and DispatchMessage).

#### Return Value

Returns non-zero (exit code from PostQuitMessage) if a WM_QUIT message was received, else 0


---

<!-- page: win32gui__PyGetArraySignedLong_meth.html -->

## win32gui.PyGetArraySignedLong

 object = PyGetArraySignedLong(array, index )

Returns a signed long from an array object at specified index

#### Parameters

- array : array

 array object to use

- index : int

 index of offset


---

<!-- page: win32gui__PyGetBufferAddressAndLen_meth.html -->

## win32gui.PyGetBufferAddressAndLen

 object = PyGetBufferAddressAndLen(obj)

Returns a buffer object address and len

#### Parameters

- obj : buffer

 the buffer object


---

<!-- page: win32gui__PyGetMemory_meth.html -->

## win32gui.PyGetMemory

 object = PyGetMemory(addr, len )

Returns a buffer object from and address and length

#### Parameters

- addr : int

 Address of the memory to reference.

- len : int

 Number of bytes to return.

#### Comments

 If zero is passed a ValueError will be raised.


---

<!-- page: win32gui__PyGetString_meth.html -->

## win32gui.PyGetString

 string = PyGetString(addr, len )

Returns a string from an address.

#### Parameters

- addr : int

 Address of the memory to reference

- len : int

 Number of characters to read. If not specified, the string must be NULL terminated.


---

<!-- page: win32gui__PySetMemory_meth.html -->

## win32gui.PySetMemory

 object = PySetMemory(addr, String )

Copies bytes to an address.

#### Parameters

- addr : int

 Address of the memory to reference

- String : string or buffer

 The string to copy


---

<!-- page: win32gui__PySetString_meth.html -->

## win32gui.PySetString

 object = PySetString(addr, String , maxLen )

Copies a string to an address (null terminated). You almost certainly should use win32gui::PySetMemory instead.

#### Parameters

- addr : int

 Address of the memory to reference

- String : str

 The string to copy

- maxLen : int

 Maximum number of chars to copy (optional)


---

<!-- page: win32gui__RealGetWindowClass_meth.html -->

## win32gui.RealGetWindowClass

 string = RealGetWindowClass(hwnd)

Retrieves the name of the class to which the specified window belongs.

#### Parameters

- hwnd : PyHANDLE

 The handle to the window


---

<!-- page: win32gui__RectInRegion_meth.html -->

## win32gui.RectInRegion

 boolean = RectInRegion(hrgn, rc )

Determines if a region and rectangle overlap at any point

#### Parameters

- hrgn : PyGdiHandle

 Handle to a region

- rc : PyRECT

 Rectangle coordinates in logical units


---

<!-- page: win32gui__Rectangle_meth.html -->

## win32gui.Rectangle

 Rectangle(hdc, LeftRect, TopRect, RightRect, BottomRect)

Creates a solid rectangle using currently selected pen and brush

#### Parameters

- hdc : PyHANDLE

 Handle to device context

- LeftRect : int

 Position of left edge of rectangle

- TopRect : int

 Position of top edge of rectangle

- RightRect : int

 Position of right edge of rectangle

- BottomRect : int

 Position of bottom edge of rectangle


---

<!-- page: win32gui__RedrawWindow_meth.html -->

## win32gui.RedrawWindow

 RedrawWindow(hWnd, rcUpdate, hrgnUpdate, flags)

Causes a portion of a window to be redrawn

#### Parameters

- hWnd : PyHANDLE

 Handle to window to be redrawn

- rcUpdate : (int,int,int,int)

 Rectangle (left, top, right, bottom) identifying part of window to be redrawn, can be None

- hrgnUpdate : PyGdiHANDLE

 Handle to region to be redrawn, can be None to indicate entire client area

- flags : int

 Combination of win32con.RDW_* flags


---

<!-- page: win32gui__RegisterClass_meth.html -->

## win32gui.RegisterClass

 int = RegisterClass(wndClass)

Registers a window class.

#### Parameters

- wndClass : PyWNDCLASS

 An object describing the window class.


---

<!-- page: win32gui__RegisterDeviceNotification_meth.html -->

## win32gui.RegisterDeviceNotification

 PyHDEVNOTIFY = RegisterDeviceNotification(handle, filter , flags )

Registers the device or type of device for which a window will receive notifications.

#### Parameters

- handle : PyHANDLE

 The handle to a window or a service

- filter : buffer

 A buffer laid out like one of the DEV_BROADCAST_* structures, generally built by one of the win32gui_struct helpers.

- flags : int

#### Win32 API References

- Search for RegisterDeviceNotification at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegisterDeviceNotification), [google](https://www.google.com/search?q=RegisterDeviceNotification) or [google groups](https://groups.google.com/groups?q=RegisterDeviceNotification).


---

<!-- page: win32gui__RegisterHotKey_meth.html -->

## win32gui.RegisterHotKey

 RegisterHotKey(hWnd, id, Modifiers, vk)

Registers a hotkey for a window

#### Parameters

- hWnd : PyHANDLE

 Handle to window that will receive WM_HOTKEY messages

- id : int

 Unique id to be used for the hot key

- Modifiers : int

 Control keys, combination of win32con.MOD_*

- vk : int

 Virtual key code

#### Win32 API References

- Search for RegisterHotKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegisterHotKey), [google](https://www.google.com/search?q=RegisterHotKey) or [google groups](https://groups.google.com/groups?q=RegisterHotKey).


---

<!-- page: win32gui__RegisterWindowMessage_meth.html -->

## win32gui.RegisterWindowMessage

 int = RegisterWindowMessage(name)

Defines a new window message that is guaranteed to be unique throughout the system. The message value can be used when sending or posting messages.

#### Parameters

- name : unicode

 The string


---

<!-- page: win32gui__ReleaseCapture_meth.html -->

## win32gui.ReleaseCapture

 ReleaseCapture()

Releases the moust capture for a window.


---

<!-- page: win32gui__ReleaseDC_meth.html -->

## win32gui.ReleaseDC

 int = ReleaseDC(hWnd, hDC )

Releases a device context.

#### Parameters

- hWnd : int

 handle to window

- hDC : int

 handle to device context


---

<!-- page: win32gui__RemoveMenu_meth.html -->

## win32gui.RemoveMenu

 RemoveMenu(hmenu, position, flags)

#### Parameters

- hmenu : int

 The handle to the menu

- position : int

 The position to delete.

- flags : int


---

<!-- page: win32gui__ReplyMessage_meth.html -->

## win32gui.ReplyMessage

 int = ReplyMessage(result)

Used to reply to a message sent through the SendMessage function without returning control to the function that called SendMessage.

#### Parameters

- result : int

 Specifies the result of the message processing. The possible values are based on the message sent.


---

<!-- page: win32gui__ResetDC_meth.html -->

## win32gui.ResetDC

 int = ResetDC(hdc)

Resets a DC

#### Parameters

- hdc : int

 The source DC


---

<!-- page: win32gui__RestoreDC_meth.html -->

## win32gui.RestoreDC

 RestoreDC(hdc, SavedDC)

Restores a device context state

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- SavedDC : int

 Identifier of state to be restored, as returned by win32gui::SaveDC.


---

<!-- page: win32gui__RoundRect_meth.html -->

## win32gui.RoundRect

 RoundRect(hdc, LeftRect, TopRect, RightRect, BottomRect, Width, Height)

Draws a rectangle with elliptically rounded corners, filled using using current brush

#### Parameters

- hdc : PyHANDLE

 Handle to device context

- LeftRect : int

 Position of left edge of rectangle

- TopRect : int

 Position of top edge of rectangle

- RightRect : int

 Position of right edge of rectangle

- BottomRect : int

 Position of bottom edge of rectangle

- Width : int

 Width of ellipse

- Height : int

 Height of ellipse


---

<!-- page: win32gui__SaveDC_meth.html -->

## win32gui.SaveDC

 int = SaveDC(hdc)

Save the state of a device context

#### Parameters

- hdc : PyHANDLE

 Handle to device context

#### Return Value

Returns a value identifying the state that can be passed to win32gui::RestoreDC. On error, returns 0.


---

<!-- page: win32gui__ScreenToClient_meth.html -->

## win32gui.ScreenToClient

 (int,int) = ScreenToClient(hWnd, Point )

Convert screen coordinates to client coords

#### Parameters

- hWnd : PyHANDLE

 Handle to a window

- Point : (int,int)

 Screen coordinates to be converted


---

<!-- page: win32gui__ScrollWindowEx_meth.html -->

## win32gui.ScrollWindowEx

 int,PyRECT = ScrollWindowEx(hWnd, dx , dy , rcScroll , rcClip , hrgnUpdate , flags )

scrolls the content of the specified window's client area.

#### Parameters

- hWnd : int

 handle to window to scroll

- dx : int

 Amount of horizontal scrolling, in device units

- dy : int

 Amount of vertical scrolling, in device units

- rcScroll : PyRECT

 Scroll rectangle, can be None for entire client area

- rcClip : PyRECT

 Clipping rectangle, can be None

- hrgnUpdate : PyGdiHandle

 Handle to region which will be updated with area invalidated by scroll operation, can be None

- flags : int

 Scrolling flags, combination of SW_ERASE,SW_INVALIDATE,SW_SCROLLCHILDREN,SW_SMOOTHSCROLL. If SW_SMOOTHSCROLL is specified, use upper 16 bits to specify time in milliseconds.

#### Return Value

Returns the type of region invalidated by scrolling, and a rectangle defining the affected area.


---

<!-- page: win32gui__SelectObject_meth.html -->

## win32gui.SelectObject

 HGDIOBJ = SelectObject(hdc, object )

Selects an object into the specified device context (DC). The new object replaces the previous object of the same type.

#### Parameters

- hdc : int

 handle to DC

- object : int

 The GDI object


---

<!-- page: win32gui__SendMessageTimeout_meth.html -->

## win32gui.SendMessageTimeout

 int,int = SendMessageTimeout(hwnd, message , wparam , lparam , flags , timeout )

Sends a message to the window.

#### Parameters

- hwnd : int

 The handle to the Window

- message : int

 The ID of the message to post

- wparam : int

 An integer whose value depends on the message

- lparam : int

 An integer whose value depends on the message

- flags : int

 Send options

- timeout : int

 Timeout duration in milliseconds.

#### Return Value

The result is the result of the SendMessageTimeout call, plus the last 'result' param. If the timeout period expires, a pywintypes.error exception will be thrown, with zero as the error code. See the Microsoft documentation for more information.


---

<!-- page: win32gui__SendMessage_meth.html -->

## win32gui.SendMessage

 int = SendMessage(hwnd, message , wparam , lparam )

Sends a message to the window.

#### Parameters

- hwnd : int

 The handle to the Window

- message : int

 The ID of the message to post

- wparam=None : int/str

 Type depends on the message

- lparam=None : int/str

 Type depends on the message


---

<!-- page: win32gui__SetActiveWindow_meth.html -->

## win32gui.SetActiveWindow

 HWND = SetActiveWindow(hwnd)

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__SetArcDirection_meth.html -->

## win32gui.SetArcDirection

 int = SetArcDirection(hdc, ArcDirection )

Sets the drawing direction for arcs and rectangles

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- ArcDirection : int

 One of win32con.AD_* constants

#### Return Value

Returns the previous direction, or 0 on error.


---

<!-- page: win32gui__SetBkColor_meth.html -->

## win32gui.SetBkColor

 int = SetBkColor(hdc, color )

Sets the background color for a device context

#### Parameters

- hdc : int/PyHANDLE

 Handle to a device context

- color : int

#### Return Value

Returns the previous color, or CLR_INVALID on failure


---

<!-- page: win32gui__SetBkMode_meth.html -->

## win32gui.SetBkMode

 int = SetBkMode(hdc, BkMode )

Sets the background mode for a device context

#### Parameters

- hdc : int/PyHANDLE

 Handle to a device context

- BkMode : int

 OPAQUE or TRANSPARENT

#### Return Value

Returns the previous mode, or 0 on failure


---

<!-- page: win32gui__SetCapture_meth.html -->

## win32gui.SetCapture

 SetCapture()

Captures the mouse for the specified window.


---

<!-- page: win32gui__SetCaretPos_meth.html -->

## win32gui.SetCaretPos

 SetCaretPos(x, y)

Changes the position of the caret

#### Parameters

- x : int

 horizontal position

- y : int

 vertical position


---

<!-- page: win32gui__SetCursor_meth.html -->

## win32gui.SetCursor

 HCURSOR = SetCursor(hcursor)

#### Parameters

- hcursor : int


---

<!-- page: win32gui__SetDlgItemInt_meth.html -->

## win32gui.SetDlgItemInt

 SetDlgItemInt(hDlg, IDDlgItem, Value, Signed)

Places an integer value in a dialog control

#### Parameters

- hDlg : PyHANDLE

 Handle to a dialog window

- IDDlgItem : int

 Identifier of one of the dialog's controls

- Value : int

 Value to placed in the control

- Signed : boolean

 Indicates if the input value is signed


---

<!-- page: win32gui__SetDlgItemText_meth.html -->

## win32gui.SetDlgItemText

 SetDlgItemText(hDlg, IDDlgItem, text)

Sets the text for a window or control

#### Parameters

- hDlg : PyHANDLE

 Handle to a dialog window

- IDDlgItem : int

 The Id of a control within the dialog

- text : string

 The text to put in the control


---

<!-- page: win32gui__SetDoubleClickTime_meth.html -->

## win32gui.SetDoubleClickTime

 SetDoubleClickTime(newVal)

#### Parameters

- newVal : int


---

<!-- page: win32gui__SetFocus_meth.html -->

## win32gui.SetFocus

 SetFocus(hwnd)

Sets focus to the specified window.

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__SetForegroundWindow_meth.html -->

## win32gui.SetForegroundWindow

 HWND = SetForegroundWindow(hwnd)

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__SetGraphicsMode_meth.html -->

## win32gui.SetGraphicsMode

 int = SetGraphicsMode(hdc, Mode )

Enables or disables advanced graphics features for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Mode : int

 GM_COMPATIBLE or GM_ADVANCED (from win32con)

#### Return Value

Returns the previous mode, one of win32con.GM_COMPATIBLE or win32con.GM_ADVANCED


---

<!-- page: win32gui__SetLayeredWindowAttributes_meth.html -->

## win32gui.SetLayeredWindowAttributes

 SetLayeredWindowAttributes(hwnd, Key, Alpha, Flags)

Sets the opacity and transparency color key of a layered window.

#### Parameters

- hwnd : PyHANDLE

 handle to the layered window

- Key : int

 Specifies the color key. Use win32api::RGB to generate value.

- Alpha : int

 Opacity, in the range 0-255

- Flags : int

 Combination of win32con.LWA_* values

#### Comments

 Accepts keyword arguments


---

<!-- page: win32gui__SetLayout_meth.html -->

## win32gui.SetLayout

 int = SetLayout(hdc, Layout )

Sets the layout for a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Layout : int

 One of win32con.LAYOUT_* constants

#### Return Value

Returns the previous layout mode


---

<!-- page: win32gui__SetMapMode_meth.html -->

## win32gui.SetMapMode

 int = SetMapMode(hdc, MapMode )

Sets the method used for translating logical units to device units

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- MapMode : int

 The new mapping mode (win32con.MM_*)

#### Return Value

Returns the previous mapping mode, one of win32con.MM_* constants


---

<!-- page: win32gui__SetMenuDefaultItem_meth.html -->

## win32gui.SetMenuDefaultItem

 SetMenuDefaultItem(hMenu, uItem, fByPos)

#### Parameters

- hMenu : int

 Handle to the menu

- uItem : int

- fByPos : int


---

<!-- page: win32gui__SetMenuInfo_meth.html -->

## win32gui.SetMenuInfo

 SetMenuInfo(hmenu, info)

Sets information for a specified menu.

#### Parameters

- hmenu : int

 handle to menu

- info : MENUINFO

 menu information in the format of a buffer.

#### Comments

 See win32gui_struct for helper functions.

 This function will raise NotImplementedError on early platforms (eg, Windows NT.)


---

<!-- page: win32gui__SetMenuItemBitmaps_meth.html -->

## win32gui.SetMenuItemBitmaps

 SetMenuItemBitmaps(hMenu, uPosition, uFlags, hBitmapUnchecked, hBitmapChecked)

Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item.

#### Parameters

- hMenu : int

 handle to menu

- uPosition : int

 menu item

- uFlags : int

 options

- hBitmapUnchecked : PyGdiHANDLE

 handle to unchecked bitmap, can be None

- hBitmapChecked : PyGdiHANDLE

 handle to checked bitmap, can be None


---

<!-- page: win32gui__SetMenuItemInfo_meth.html -->

## win32gui.SetMenuItemInfo

 SetMenuItemInfo(hMenu, uItem, fByPosition, menuItem)

Sets menu information

#### Parameters

- hMenu : int

 Handle to the menu

- uItem : int

 The menu item identifier or the menu item position.

- fByPosition : int

 Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.

- menuItem : buffer

 A string or buffer in the format of a MENUITEMINFO structure.


---

<!-- page: win32gui__SetMenu_meth.html -->

## win32gui.SetMenu

 SetMenu(hwnd, hmenu)

Sets the menu for the specified window.

#### Parameters

- hwnd : int

- hmenu : int


---

<!-- page: win32gui__SetMiterLimit_meth.html -->

## win32gui.SetMiterLimit

 float = SetMiterLimit(hdc, NewLimit )

Set the limit of miter joins for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- NewLimit : float

 New limit to be set

#### Return Value

Returns the previous limit


---

<!-- page: win32gui__SetParent_meth.html -->

## win32gui.SetParent

 int = SetParent(child, child )

changes the parent window of the specified child window.

#### Parameters

- child : int

 handle to window whose parent is changing

- child : int

 handle to new parent window


---

<!-- page: win32gui__SetPixelV_meth.html -->

## win32gui.SetPixelV

 SetPixelV(hdc, X, Y, Color)

Sets the color of a single pixel to an approximation of specified color

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- X : int

 Horizontal pos

- Y : int

 Vertical pos

- Color : int

 RGB color to be set.


---

<!-- page: win32gui__SetPixel_meth.html -->

## win32gui.SetPixel

 int = SetPixel(hdc, X , Y , Color )

Set the color of a single pixel

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- X : int

 Horizontal pos

- Y : int

 Vertical pos

- Color : int

 RGB color to be set.

#### Return Value

Returns the RGB color actually set, which may be different from the one passed in


---

<!-- page: win32gui__SetPolyFillMode_meth.html -->

## win32gui.SetPolyFillMode

 int = SetPolyFillMode(hdc, PolyFillMode )

Sets the polygon filling mode for a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- PolyFillMode : int

 One of ALTERNATE or WINDING

#### Return Value

Returns the previous mode, one of win32con.ALTERNATE or win32con.WINDING


---

<!-- page: win32gui__SetROP2_meth.html -->

## win32gui.SetROP2

 int = SetROP2(hdc, DrawMode )

Sets the foreground mixing mode of a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- DrawMode : int

 Mixing mode, one of win32con.R2_*.

#### Return Value

Returns previous mode


---

<!-- page: win32gui__SetRectRgn_meth.html -->

## win32gui.SetRectRgn

 SetRectRgn(hrgn, LeftRect, TopRect, RightRect, BottomRect)

Makes an existing region rectangular

#### Parameters

- hrgn : PyGdiHandle

 Handle to a region

- LeftRect : int

 Left edge in logical units

- TopRect : int

 Top edge in logical units

- RightRect : int

 Right edge in logical units

- BottomRect : int

 Bottom edge in logical units


---

<!-- page: win32gui__SetScrollInfo_meth.html -->

## win32gui.SetScrollInfo

 SetScrollInfo(hwnd, nBar, scollInfo, bRedraw)

Sets information about a scroll-bar

#### Parameters

- hwnd : int

 The handle to the window.

- nBar : int

 Identifies the bar.

- scollInfo : PySCROLLINFO

 Scollbar info.

- bRedraw=1 : int

 Should the bar be redrawn?

#### Return Value

Returns an int with the current position of the scroll box.


---

<!-- page: win32gui__SetStretchBltMode_meth.html -->

## win32gui.SetStretchBltMode

 int = SetStretchBltMode(hdc, StretchMode )

Sets the stretching mode used by win32gui::StretchBlt

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- StretchMode : int

 One of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS, or WHITEONBLACK (from win32con)

#### Return Value

If the function succeeds, the return value is the previous stretching mode.
If the function fails, the return value is zero.


---

<!-- page: win32gui__SetTextAlign_meth.html -->

## win32gui.SetTextAlign

 int = SetTextAlign(hdc, Mode )

Sets horizontal and vertical alignment for text in a device context

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Mode : int

 Combination of win32con.TA_* constants

#### Return Value

Returns the previous alignment flags


---

<!-- page: win32gui__SetTextCharacterExtra_meth.html -->

## win32gui.SetTextCharacterExtra

 int = SetTextCharacterExtra(hdc, CharExtra )

Sets the spacing between characters

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- CharExtra : int

 Space between adjacent chars, in logical units

#### Return Value

Returns the previous spacing


---

<!-- page: win32gui__SetTextColor_meth.html -->

## win32gui.SetTextColor

 int = SetTextColor(hdc, color )

Changes the text color for a device context

#### Parameters

- hdc : int

 Handle to a device context

- color : int

 The RGB color value - see win32api::RGB

#### Return Value

Returns the previous color, or CLR_INVALID on failure


---

<!-- page: win32gui__SetViewportExtEx_meth.html -->

## win32gui.SetViewportExtEx

 (int,int) = SetViewportExtEx(hdc, XExtent , YExtent )

Changes the viewport extents for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- XExtent : int

 New X extent in logical units

- YExtent : int

 New Y extent in logical units

#### Return Value

Returns the previous extents as (x,y) in logical units


---

<!-- page: win32gui__SetViewportOrgEx_meth.html -->

## win32gui.SetViewportOrgEx

 (int,int) = SetViewportOrgEx(hdc, X , Y )

Changes the viewport origin for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- X : int

 New X coord in logical units

- Y : int

 New Y coord in logical units

#### Return Value

Returns the previous origin as (x,y)


---

<!-- page: win32gui__SetWindowExtEx_meth.html -->

## win32gui.SetWindowExtEx

 (int,int) = SetWindowExtEx(hdc, XExtent , YExtent )

Changes the window extents for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- XExtent : int

 New X extent in logical units

- YExtent : int

 New Y extent in logical units

#### Return Value

Returns the previous extents


---

<!-- page: win32gui__SetWindowLong_meth.html -->

## win32gui.SetWindowLong

 int = SetWindowLong(hwnd, index , value )

Places a long value at the specified offset into the extra window memory of the given window.

#### Parameters

- hwnd : PyHANDLE

 The handle to the window

- index : int

 The index of the item to set.

- value : object

 The value to set.

#### Comments

 This function calls the SetWindowLongPtr Api function

 If index is GWLP_WNDPROC, then the value parameter must be a callable object (or a dictionary) to use as the new window procedure.


---

<!-- page: win32gui__SetWindowOrgEx_meth.html -->

## win32gui.SetWindowOrgEx

 (int,int) = SetWindowOrgEx(hdc, X , Y )

Changes the window origin for a DC

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- X : int

 New X coord in logical units

- Y : int

 New Y coord in logical units

#### Return Value

Returns the previous origin


---

<!-- page: win32gui__SetWindowPlacement_meth.html -->

## win32gui.SetWindowPlacement

 SetWindowPlacement(hWnd, placement)

Sets the windows placement

#### Parameters

- hWnd : PyHANDLE

 Handle to a window

- placement : (tuple)

 A tuple representing the WINDOWPLACEMENT structure.


---

<!-- page: win32gui__SetWindowPos_meth.html -->

## win32gui.SetWindowPos

 SetWindowPos(hWnd, InsertAfter, X, Y, cx, cy, Flags)

Sets the position and size of a window

#### Parameters

- hWnd : PyHANDLE

 Handle to the window

- InsertAfter : PyHANDLE

 Window that hWnd will be placed below. Can be a window handle or one of HWND_BOTTOM,HWND_NOTOPMOST,HWND_TOP, or HWND_TOPMOST

- X : int

 New X coord

- Y : int

 New Y coord

- cx : int

 New width of window

- cy : int

 New height of window

- Flags : int

 Combination of win32con.SWP_* flags


---

<!-- page: win32gui__SetWindowRgn_meth.html -->

## win32gui.SetWindowRgn

 SetWindowRgn(hWnd, hRgn, Redraw)

Sets the visible region of a window

#### Parameters

- hWnd : PyHANDLE

 Handle to a window

- hRgn : PyGdiHANDLE

 Handle to region to be set, can be None

- Redraw : boolean

 Indicates if window should be completely redrawn

#### Comments

 On success, the system assumes ownership of the region so you should call the handle's Detach() method to prevent it from being automatically closed.


---

<!-- page: win32gui__SetWindowText_meth.html -->

## win32gui.SetWindowText

 SetWindowText()

Sets the window text.


---

<!-- page: win32gui__SetWorldTransform_meth.html -->

## win32gui.SetWorldTransform

 SetWorldTransform(hdc, Xform)

Transforms a device context's coordinate space

#### Parameters

- hdc : PyHANDLE

 Handle to a device context

- Xform : PyXFORM

 Matrix defining the transformation

#### Comments

 DC's mode must be set to GM_ADVANCED. See win32gui::SetGraphicsMode.


---

<!-- page: win32gui__Shell_NotifyIcon_meth.html -->

## win32gui.Shell_NotifyIcon

 Shell_NotifyIcon(Message, nid)

Adds, removes or modifies a taskbar icon.

#### Parameters

- Message : int

 One of win32gui.NIM_* flags

- nid : PyNOTIFYICONDATA

 Tuple containing NOTIFYICONDATA info


---

<!-- page: win32gui__ShowCaret_meth.html -->

## win32gui.ShowCaret

 ShowCaret(hWnd)

Shows the caret at its current position

#### Parameters

- hWnd : PyHANDLE

 Window that owns the caret, can be 0.


---

<!-- page: win32gui__ShowWindow_meth.html -->

## win32gui.ShowWindow

 boolean = ShowWindow(hWnd, cmdShow )

Shows or hides a window and changes its state

#### Parameters

- hWnd : int

 The handle to the window

- cmdShow : int

 Combination of win32con.SW_* flags


---

<!-- page: win32gui__StretchBlt_meth.html -->

## win32gui.StretchBlt

 StretchBlt(hdcDest, x, y, width, height, hdcSrc, nXSrc, nYSrc, nWidthSrc, nHeightSrc, dwRop)

Copies a bitmap from a source rectangle into a destination rectangle, stretching or compressing the bitmap to fit the dimensions of the destination rectangle, if necessary

#### Parameters

- hdcDest : int

 handle to destination DC

- x : int

 x-coord of destination upper-left corner

- y : int

 y-coord of destination upper-left corner

- width : int

 width of destination rectangle

- height : int

 height of destination rectangle

- hdcSrc : int

 handle to source DC

- nXSrc : int

 x-coord of source upper-left corner

- nYSrc : int

 y-coord of source upper-left corner

- nWidthSrc : int

 width of source rectangle

- nHeightSrc : int

 height of source rectangle

- dwRop : int

 raster operation code


---

<!-- page: win32gui__StrokeAndFillPath_meth.html -->

## win32gui.StrokeAndFillPath

 StrokeAndFillPath(hdc)

Combines operations of StrokePath and FillPath with no overlap

#### Parameters

- hdc : PyHANDLE

 Handle to a device context that contains a closed path. See win32gui::EndPath.


---

<!-- page: win32gui__StrokePath_meth.html -->

## win32gui.StrokePath

 StrokePath(hdc)

Draws current path with currently selected pen

#### Parameters

- hdc : PyHANDLE

 Handle to a device context that contains a closed path. See win32gui::EndPath.


---

<!-- page: win32gui__SystemParametersInfo_meth.html -->

## win32gui.SystemParametersInfo

 SystemParametersInfo(Action, Param, WinIni)

Queries or sets system-wide parameters. This function can also update the user profile while setting a parameter.

#### Parameters

- Action : int

 System parameter to query or set, one of the SPI_GET* or SPI_SET* constants

- Param=None : object

 depends on action to be taken

- WinIni=0 : int

 Flags specifying whether change should be permanent, and if all windows should be notified of change. Combination of SPIF_UPDATEINIFILE, SPIF_SENDCHANGE, SPIF_SENDWININICHANGE

| | Action | Input/return type
| |

---

 |

---

| | SPI_GETDESKWALLPAPER | Returns the path to the bmp used as wallpaper
| | SPI_SETDESKWALLPAPER | Param should be a string specifying a .bmp file
| | SPI_GETDROPSHADOW | Returns a boolean
| | SPI_GETFLATMENU | Returns a boolean
| | SPI_GETFONTSMOOTHING | Returns a boolean
| | SPI_GETICONTITLEWRAP | Returns a boolean
| | SPI_GETSNAPTODEFBUTTON | Returns a boolean
| | SPI_GETBEEP | Returns a boolean
| | SPI_GETBLOCKSENDINPUTRESETS | Returns a boolean
| | SPI_GETMENUUNDERLINES | Returns a boolean
| | SPI_GETKEYBOARDCUES | Returns a boolean
| | SPI_GETKEYBOARDPREF | Returns a boolean
| | SPI_GETSCREENSAVEACTIVE | Returns a boolean
| | SPI_GETSCREENSAVERRUNNING | Returns a boolean
| | SPI_GETMENUDROPALIGNMENT | Returns a boolean (True indicates left aligned, False right aligned)
| | SPI_GETMENUFADE | Returns a boolean
| | SPI_GETLOWPOWERACTIVE | Returns a boolean
| | SPI_GETPOWEROFFACTIVE | Returns a boolean
| | SPI_GETCOMBOBOXANIMATION | Returns a boolean
| | SPI_GETCURSORSHADOW | Returns a boolean
| | SPI_GETGRADIENTCAPTIONS | Returns a boolean
| | SPI_GETHOTTRACKING | Returns a boolean
| | SPI_GETLISTBOXSMOOTHSCROLLING | Returns a boolean
| | SPI_GETMENUANIMATION | Returns a boolean
| | SPI_GETSELECTIONFADE | Returns a boolean
| | SPI_GETTOOLTIPANIMATION | Returns a boolean
| | SPI_GETTOOLTIPFADE | Returns a boolean (TRUE=fade, False=slide)
| | SPI_GETUIEFFECTS | Returns a boolean
| | SPI_GETACTIVEWINDOWTRACKING | Returns a boolean
| | SPI_GETACTIVEWNDTRKZORDER | Returns a boolean
| | SPI_GETDRAGFULLWINDOWS | Returns a boolean
| | SPI_GETSHOWIMEUI | Returns a boolean
| | SPI_GETMOUSECLICKLOCK | Returns a boolean
| | SPI_GETMOUSESONAR | Returns a boolean
| | SPI_GETMOUSEVANISH | Returns a boolean
| | SPI_GETSCREENREADER | Returns a boolean
| | SPI_GETSHOWSOUNDS | Returns a boolean
| | SPI_SETDROPSHADOW | Param must be a boolean
| | SPI_SETDROPSHADOW | Param must be a boolean
| | SPI_SETMENUUNDERLINES | Param must be a boolean
| | SPI_SETKEYBOARDCUES | Param must be a boolean
| | SPI_SETMENUFADE | Param must be a boolean
| | SPI_SETCOMBOBOXANIMATION | Param must be a boolean
| | SPI_SETCURSORSHADOW | Param must be a boolean
| | SPI_SETGRADIENTCAPTIONS | Param must be a boolean
| | SPI_SETHOTTRACKING | Param must be a boolean
| | SPI_SETLISTBOXSMOOTHSCROLLING | Param must be a boolean
| | SPI_SETMENUANIMATION | Param must be a boolean
| | SPI_SETSELECTIONFADE | Param must be a boolean
| | SPI_SETTOOLTIPANIMATION | Param must be a boolean
| | SPI_SETTOOLTIPFADE | Param must be a boolean
| | SPI_SETUIEFFECTS | Param must be a boolean
| | SPI_SETACTIVEWINDOWTRACKING | Param must be a boolean
| | SPI_SETACTIVEWNDTRKZORDER | Param must be a boolean
| | SPI_SETMOUSESONAR | Param must be a boolean
| | SPI_SETMOUSEVANISH | Param must be a boolean
| | SPI_SETMOUSECLICKLOCK | Param must be a boolean
| | SPI_SETFONTSMOOTHING | Param should specify a boolean
| | SPI_SETICONTITLEWRAP | Param should specify a boolean
| | SPI_SETSNAPTODEFBUTTON | Param is a boolean
| | SPI_SETBEEP | Param is a boolean
| | SPI_SETBLOCKSENDINPUTRESETS | Param is a boolean
| | SPI_SETKEYBOARDPREF | Param is a boolean
| | SPI_SETMOUSEBUTTONSWAP | Param is a boolean
| | SPI_SETSCREENSAVEACTIVE | Param is a boolean
| | SPI_SETMENUDROPALIGNMENT | Param is a boolean (True=left aligned, False=right aligned)
| | SPI_SETLOWPOWERACTIVE | Param is a boolean
| | SPI_SETPOWEROFFACTIVE | Param is a boolean
| | SPI_SETDRAGFULLWINDOWS | Param is a boolean
| | SPI_SETSHOWIMEUI | Param is a boolean
| | SPI_SETSCREENREADER | Param is a boolean
| | SPI_SETSHOWSOUNDS | Param is a boolean
| | SPI_SETMOUSETRAILS | Param should be an int specifying the nbr of cursors in the trail (0 or 1 means disabled)
| | SPI_SETWHEELSCROLLLINES | Param is an int specifying nbr of lines
| | SPI_SETKEYBOARDDELAY | Param is an int in the range 0 - 3
| | SPI_SETKEYBOARDSPEED | Param is an int in the range 0 - 31
| | SPI_SETDOUBLECLICKTIME | Param is an int (in milliseconds), Use win32gui::GetDoubleClickTime to retrieve the value.
| | SPI_SETDOUBLECLKWIDTH | Param is an int. Use win32api.GetSystemMetrics(SM_CXDOUBLECLK) to retrieve the value.
| | SPI_SETDOUBLECLKHEIGHT | Param is an int, Use win32api.GetSystemMetrics(SM_CYDOUBLECLK) to retrieve the value.
| | SPI_SETMOUSEHOVERHEIGHT | Param is an int
| | SPI_SETMOUSEHOVERWIDTH | Param is an int
| | SPI_SETMOUSEHOVERTIME | Param is an int
| | SPI_SETSCREENSAVETIMEOUT | Param is an int specifying the timeout in seconds
| | SPI_SETMENUSHOWDELAY | Param is an int specifying the shortcut menu delay in milliseconds
| | SPI_SETLOWPOWERTIMEOUT | Param is an int (in seconds)
| | SPI_SETPOWEROFFTIMEOUT | Param is an int (in seconds)
| | SPI_SETDRAGHEIGHT | Param is an int. Use win32api.GetSystemMetrics(SM_CYDRAG) to retrieve the value.
| | SPI_SETDRAGWIDTH | Param is an int. Use win32api.GetSystemMetrics(SM_CXDRAG) to retrieve the value.
| | SPI_SETBORDER | Param is an int
| | SPI_GETFONTSMOOTHINGCONTRAST | Returns an int
| | SPI_GETFONTSMOOTHINGTYPE | Returns an int
| | SPI_GETMOUSETRAILS | Returns an int specifying the nbr of cursor images in the trail, 0 or 1 indicates disabled
| | SPI_GETWHEELSCROLLLINES | Returns the nbr of lines to scroll for the mouse wheel
| | SPI_GETKEYBOARDDELAY | Returns an int
| | SPI_GETKEYBOARDSPEED | Returns an int
| | SPI_GETMOUSESPEED | Returns an int
| | SPI_GETMOUSEHOVERHEIGHT | Returns an int
| | SPI_GETMOUSEHOVERWIDTH | Returns an int
| | SPI_GETMOUSEHOVERTIME | Returns an int
| | SPI_GETSCREENSAVETIMEOUT | Returns an int (idle time in seconds)
| | SPI_GETMENUSHOWDELAY | Returns an int (shortcut delay in milliseconds)
| | SPI_GETLOWPOWERTIMEOUT | Returns an int (in seconds)
| | SPI_GETPOWEROFFTIMEOUT | Returns an int (in seconds)
| | SPI_GETACTIVEWNDTRKTIMEOUT | Returns an int (milliseconds)
| | SPI_GETBORDER | Returns an int
| | SPI_GETCARETWIDTH | Returns an int
| | SPI_GETFOREGROUNDFLASHCOUNT | Returns an int
| | SPI_GETFOREGROUNDLOCKTIMEOUT | Returns an int
| | SPI_GETFOCUSBORDERHEIGHT | Returns an int
| | SPI_GETFOCUSBORDERWIDTH | Returns an int
| | SPI_GETMOUSECLICKLOCKTIME | Returns an int (in milliseconds)
| | SPI_SETFONTSMOOTHINGCONTRAST | Param should be an int in the range 1000 to 2200
| | SPI_SETFONTSMOOTHINGTYPE | Param should be one of the FE_FONTSMOOTHING* constants
| | SPI_SETMOUSESPEED | Param should be an int in the range 1 - 20
| | SPI_SETACTIVEWNDTRKTIMEOUT | Param is an int (in milliseconds)
| | SPI_SETCARETWIDTH | Param is an int (in pixels)
| | SPI_SETFOREGROUNDFLASHCOUNT | Param is an int
| | SPI_SETFOREGROUNDLOCKTIMEOUT | Param is an int (in milliseconds)
| | SPI_SETFOCUSBORDERHEIGHT | Returns an int
| | SPI_SETFOCUSBORDERWIDTH | Returns an int
| | SPI_SETMOUSECLICKLOCKTIME | Param is an int (in milliseconds)
| | SPI_GETICONTITLELOGFONT | Returns a PyLOGFONT,
| | SPI_SETICONTITLELOGFONT | Param must be a PyLOGFONT,
| | SPI_SETLANGTOGGLE | Param is ignored. Sets the language toggle hotkey from registry key HKCU\\keyboard layout\\toggle
| | SPI_SETICONS | Reloads the system icons. Param is not used
| | SPI_GETMOUSE | Returns a tuple of 3 ints containing the x and y mouse thresholds and the acceleration factor.
| | SPI_SETMOUSE | Param should be a sequence of 3 ints
| | SPI_GETDEFAULTINPUTLANG | Returns an int (locale id for default language)
| | SPI_SETDEFAULTINPUTLANG | Param is an int containing a locale id
| | SPI_GETANIMATION | Returns an int
| | SPI_SETANIMATION | Param is an int
| | SPI_ICONHORIZONTALSPACING | Functions as both a get and set operation. If Param is None, functions as a get operation, otherwise Param is an int to be set as the new value
| | SPI_ICONVERTICALSPACING | Functions as both a get and set operation. If Param is None, functions as a get operation, otherwise Param is an int to be set as the new value
| | SPI_GETNONCLIENTMETRICS | Param must be None. The result is a dict.
| | SPI_SETNONCLIENTMETRICS | Param is a dict in the form of a NONCLIENTMETRICS struct, as returned by SPI_GETNONCLIENTMETRICS operation
| | SPI_GETMINIMIZEDMETRICS | Returns a dict representing a MINIMIZEDMETRICS struct. Param is not used.
| | SPI_SETMINIMIZEDMETRICS | Param should be a MINIMIZEDMETRICS dict as returned by SPI_GETMINIMIZEDMETRICS action
| | SPI_SETDESKPATTERN | Unsupported (obsolete)
| | SPI_GETFASTTASKSWITCH | Unsupported (obsolete)
| | SPI_SETFASTTASKSWITCH | Unsupported (obsolete)
| | SPI_SETSCREENSAVERRUNNING | Unsupported (documented as internal use only)
| | SPI_SCREENSAVERRUNNING | Same as SPI_SETSCREENSAVERRUNNING
| | SPI_SETPENWINDOWS | Unsupported (only relevant for Win95)
| | SPI_GETWINDOWSEXTENSION | Unsupported (only relevant for Win95)
| | SPI_GETGRIDGRANULARITY | Unsupported (obsolete)
| | SPI_SETGRIDGRANULARITY | Unsupported (obsolete)
| | SPI_LANGDRIVER | Unsupported (use is not documented)
| | SPI_GETFONTSMOOTHINGORIENTATION | Unsupported (use is not documented)
| | SPI_SETFONTSMOOTHINGORIENTATION | Unsupported (use is not documented)
| | SPI_SETHANDHELD | Unsupported (use is not documented)
| | SPI_GETICONMETRICS | Not implemented yet
| | SPI_SETICONMETRICS | Not implemented yet
| | SPI_GETWORKAREA | Not implemented yet
| | SPI_SETWORKAREA | Not implemented yet
| | SPI_GETSERIALKEYS | Not implemented yet
| | SPI_SETSERIALKEYS | Not implemented yet
| | SPI_SETMOUSEKEYS | Not implemented yet
| | SPI_GETMOUSEKEYS | Not implemented yet
| | SPI_GETHIGHCONTRAST | Not implemented yet
| | SPI_SETHIGHCONTRAST | Not implemented yet
| | SPI_GETSOUNDSENTRY | Not implemented yet
| | SPI_SETSOUNDSENTRY | Not implemented yet
| | SPI_GETSTICKYKEYS | Not implemented yet
| | SPI_SETSTICKYKEYS | Not implemented yet
| | SPI_GETTOGGLEKEYS | Not implemented yet
| | SPI_SETTOGGLEKEYS | Not implemented yet
| | SPI_GETACCESSTIMEOUT | Not implemented yet
| | SPI_SETACCESSTIMEOUT | Not implemented yet
| | SPI_GETFILTERKEYS | Not implemented yet
| | SPI_SETFILTERKEYS | Not implemented yet

#### Comments

 Param and WinIni are not used with any of the SPI_GET operations
 Boolean parameters can be any object that can be evaluated as True or False

#### Return Value

SPI_SET functions all return None on success. Types returned by SPI_GET functions are dependent on the operation


---

<!-- page: win32gui__TrackPopupMenu_meth.html -->

## win32gui.TrackPopupMenu

 int = TrackPopupMenu(hmenu, flags , x , y , reserved , hwnd , prcRect )

Display popup shortcut menu

#### Parameters

- hmenu : int

 The handle to the menu

- flags : uint

 flags

- x : int

 x pos

- y : int

 y pos

- reserved : int

 reserved

- hwnd : hwnd

 owner window

- prcRect : PyRECT

 Pointer to rec (can be None)


---

<!-- page: win32gui__TranslateAccelerator_meth.html -->

## win32gui.TranslateAccelerator

 int = TranslateAccelerator(hwnd, haccel , msg )

#### Parameters

- hwnd : int

- haccel : int

- msg : MSG


---

<!-- page: win32gui__TranslateMessage_meth.html -->

## win32gui.TranslateMessage

 int = TranslateMessage(msg)

#### Parameters

- msg : MSG


---

<!-- page: win32gui__TransparentBlt_meth.html -->

## win32gui.TransparentBlt

 TransparentBlt(Dest, XOriginDest, YOriginDest, WidthDest, HeightDest, Src, XOriginSrc, YOriginSrc, WidthSrc, HeightSrc, Transparent)

Transfers color from one DC to another, with one color treated as transparent

#### Parameters

- Dest : PyHANDLE

 Destination device context handle

- XOriginDest : int

 X pos of dest rect

- YOriginDest : int

 Y pos of dest rect

- WidthDest : int

 Width of dest rect

- HeightDest : int

 Height of dest rect

- Src : PyHANDLE

 Source DC handle

- XOriginSrc : int

 X pos of src rect

- YOriginSrc : int

 Y pos of src rect

- WidthSrc : int

 Width of src rect

- HeightSrc : int

 Height of src rect

- Transparent : int

 RGB color value that will be transparent


---

<!-- page: win32gui__UnregisterClass_meth.html -->

## win32gui.UnregisterClass

 UnregisterClass(atom, hinst)

Unregisters a window class created by win32gui::RegisterClass

#### Parameters

- atom : PyResourceId

 The atom or classname identifying the class previously registered.

- hinst : PyHANDLE

 The handle to the instance unregistering the class, can be None


---

<!-- page: win32gui__UnregisterDeviceNotification_meth.html -->

## win32gui.UnregisterDeviceNotification

 UnregisterDeviceNotification()

Unregisters a Device Notification handle. It is generally not necessary to call this function manually, but in some cases, handle values may be extracted via the struct module and need to be closed explicitly.


---

<!-- page: win32gui__UnregisterHotKey_meth.html -->

## win32gui.UnregisterHotKey

 UnregisterHotKey(hWnd, id)

Unregisters a previously registeredhotkey

#### Parameters

- hWnd : PyHANDLE

 A handle to the window associated with the hot key to be freed

- id : int

 The identifier of the hot key

#### Win32 API References

- Search for UnregisterHotKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=UnregisterHotKey), [google](https://www.google.com/search?q=UnregisterHotKey) or [google groups](https://groups.google.com/groups?q=UnregisterHotKey).


---

<!-- page: win32gui__UpdateLayeredWindow_meth.html -->

## win32gui.UpdateLayeredWindow

 UpdateLayeredWindow(hwnd, hdcDst, ptDst, size, hdcSrc, ptSrc, Key, blend, Flags)

Updates the position, size, shape, content, and translucency of a layered window.

#### Parameters

- hwnd : PyHANDLE

 handle to layered window

- hdcDst=None : PyHANDLE

 handle to screen DC, can be None. *Must* be None if hdcSrc is None

- ptDst=None : (x,y)

 New screen position, can be None.

- size=None : (cx, cy)

 New size of the layered window, can be None. *Must* be None if hdcSrc is None.

- hdcSrc=None : int

 handle to surface DC for the window, can be None

- ptSrc=None : (x,y)

 layer position, can be None. *Must* be None if hdcSrc is None.

- Key=0 : int

 Color key, generate using win32api::RGB

- blend=(0,0,255,0) : (int, int, int, int)

 PyBLENDFUNCTION specifying alpha blending parameters

- Flags=0 : int

 One of the win32con.ULW_* values. Use 0 if hdcSrc is None.

#### Comments

 Accepts keyword arguments.


---

<!-- page: win32gui__UpdateWindow_meth.html -->

## win32gui.UpdateWindow

 UpdateWindow(hwnd)

#### Parameters

- hwnd : int

 The handle to the window


---

<!-- page: win32gui__ValidateRect_meth.html -->

## win32gui.ValidateRect

 ValidateRect(hWnd, Rect)

Validates the client area within a rectangle by removing the rectangle from the update region of the specified window.

#### Parameters

- hWnd : PyHANDLE

 Handle to the window

- Rect : PyRECT

 Client coordinates of the rectangle to be removed from the update region. If this parameter is Nonr, the entire client area is removed.


---

<!-- page: win32gui__ValidateRgn_meth.html -->

## win32gui.ValidateRgn

 ValidateRgn(hWnd, hRgn)

Removes a region from a window's update region

#### Parameters

- hWnd : PyHANDLE

 Handle to the window

- hRgn : PyGdiHANDLE

 Region to be validated


---

<!-- page: win32gui__WaitMessage_meth.html -->

## win32gui.WaitMessage

 WaitMessage()

Waits for a message


---

<!-- page: win32gui__WidenPath_meth.html -->

## win32gui.WidenPath

 WidenPath(hdc)

Widens current path by amount it would increase by if drawn with currently selected pen

#### Parameters

- hdc : PyHANDLE

 Handle to a device context that contains a closed path. See win32gui::EndPath.


---

<!-- page: win32gui__WindowFromDC_meth.html -->

## win32gui.WindowFromDC

 PyHANDLE = WindowFromDC(hDC)

Finds the window associated with a device context

#### Parameters

- hDC : PyHANDLE

 Handle to a device context

#### Return Value

Returns a handle to the window, or 0 if the DC is not associated with a window


---

<!-- page: win32gui__WindowFromPoint_meth.html -->

## win32gui.WindowFromPoint

 int = WindowFromPoint(point)

Retrieves a handle to the window that contains the specified point.

#### Parameters

- point : (int, int)

 The point.


---

<!-- page: win32gui___TrackMouseEvent_meth.html -->

## win32gui._TrackMouseEvent

 _TrackMouseEvent(tme)

Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.

#### Parameters

- tme : TRACKMOUSEEVENT


---

<!-- page: win32gui__set_logger_meth.html -->

## win32gui.set_logger

 set_logger(logger)

Sets a logger object for exceptions and error information

#### Parameters

- logger : object

 A logger object, generally from the standard logger package.

#### Comments

 Once a logger has been set for the module, unhandled exceptions, such as from a window's WNDPROC, will be written (via logger.exception()) to the log instead of to stderr.
Note that using this with the Python 2.3 logging package will prevent the traceback from being written to the log. However, it is possible to use the Python 2.4 logging package directly with Python 2.3
