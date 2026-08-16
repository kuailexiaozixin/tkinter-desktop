# 索引：《Python GUI Programming with Tkinter》（第 2 版，Alan D. Moore，Packt 2021）

> 本地 PDF：`references/Python GUI Programming with Tkinter Design and build functional and user-friendly GUI applications, 2nd ed. (Alan D. Moore) (z-library.sk, 1lib.sk, z-lib.sk).pdf`
> 全文检索：直接用本地 PDF（pdf 本身可搜索；如需纯文本，可用 `pdftotext -layout` 从本 PDF 即时再生，666 页）
> ISBN 978-1-180181-592-5｜正文 16 章 + 附录 A/B + 书末 Index

## 页码换算（重要）
- 书中**印刷页**（章末/页脚阿拉伯数字）与 **PDF 页序号** 差一个固定偏移：
  **PDF 页 = 印刷页 + 25**
- 验证：第 1 章正文起始印刷页 `1` → PDF 第 `26` 页（已直接核对正文首页 "Introduction to Tkinter"）；其余章节抽查均吻合。
- 前 25 个 PDF 页为封面 / 版权 / 贡献者 / 作者简介 / 目录（罗马数字页码，无阿拉伯页码）。
- 本索引每节同时给出 **印刷页** 与 **PDF 页（P）**，直接跳转到本地 PDF 用 P 列。

---

## A. 章节总览（跳转用）

| # | 章节标题 | 印刷页 | PDF 页 |
|---|----------|-------:|-------:|
| 1 | Introduction to Tkinter | 1 | 26 |
| 2 | Designing GUI Applications | 29 | 54 |
| 3 | Creating Basic Forms with Tkinter and Ttk Widgets | 51 | 76 |
| 4 | Organizing Our Code with Classes | 81 | 106 |
| 5 | Reducing User Error with Validation and Automation | 117 | 142 |
| 6 | Planning for the Expansion of Our Application | 163 | 188 |
| 7 | Creating Menus with Menu and Tkinter Dialogs | 193 | 218 |
| 8 | Navigating Records with Treeview and Notebook | 231 | 256 |
| 9 | Improving the Look with Styles and Themes | 272 | 297 |
| 10 | Maintaining Cross-Platform Compatibility | 327 | 352 |
| 11 | Creating Automated Tests with unittest | 367 | 392 |
| 12 | Improving Data Storage with SQL | 403 | 428 |
| 13 | Connecting to the Cloud | 447 | 472 |
| 14 | Asynchronous Programming with Thread and Queue | 493 | 518 |
| 15 | Visualizing Data Using the Canvas Widget | 521 | 546 |
| 16 | Packaging with setuptools and cxFreeze | 558 | 583 |
| A | A Quick Primer on reStructuredText | 591 | 616 |
| B | A Quick SQL Tutorial | 603 | 628 |
| — | Other Books You May Enjoy | 619 | 644 |
| — | Index（书末主题索引） | 625 | 650 |

---

## B. 逐章小节索引（印刷页 → PDF 页 = +25）

### Ch1 · Introduction to Tkinter （P26）
- Introducing Tkinter and Tk — 2 → P27
- Choosing Tkinter — 2 → P27
- Installing Tkinter — 3 → P28
  - Installing Python 3.9 on Windows — 3 → P28
  - Installing Python 3 on macOS — 4 → P29
  - Installing Python 3 and Tkinter on Linux — 4 → P29
- Introducing IDLE — 4 → P29
  - Using the shell mode of IDLE — 5 → P30
  - Using the editor mode of IDLE — 5 → P30
  - IDLE as a Tkinter example — 6 → P31
- Creating a Tkinter Hello World — 7 → P32
- An overview of basic Tkinter — 9 → P34
- Building a GUI with Tkinter widgets — 10 → P35
- Arranging our widgets with geometry managers — 14 → P39
- Making the form actually do something — 19 → P44
- Handling data with Tkinter control variables — 21 → P46
  - Using control variables in a callback function — 26 → P51
  - The importance of control variables — 28 → P53
- Summary — 28 → P53

### Ch2 · Designing GUI Applications （P54）
- Analyzing a problem at ABQ AgriLabs — 29 → P54
- Assessing the problem — 30 → P55
- Gathering information about the problem — 30 → P55
  - Interviewing the interested parties — 31 → P56
  - Analyzing what we've found out — 33 → P58
  - Information from the data originators — 34 → P59
  - Information from the users of the application — 35 → P60
  - Information from technical support — 36 → P61
  - Information from the data consumer — 36 → P61
- Documenting specification requirements — 37 → P62
  - Contents of a simple specification — 38 → P63
  - Writing the ABQ data entry program specification — 39 → P64
- Designing the application — 42 → P67
  - Deciding on input widgets — 42 → P67
  - Grouping our fields — 44 → P69
  - Laying out the form — 45 → P70
  - Laying out the application — 47 → P72
  - Evaluating technology options — 49 → P74
- Summary — 50 → P75

### Ch3 · Creating Basic Forms with Tkinter and Ttk Widgets （P76）
- The Ttk widget set — 51 → P76
- The Label widget — 52 → P77
- The Entry widget — 53 → P78
- The Spinbox widget — 54 → P79
- The Checkbutton widget — 56 → P81
- The Radiobutton widget — 57 → P82
- The Combobox widget — 58 → P83
- The Text widget — 59 → P84
  - Text widget indices — 60 → P85
- The Button widget — 62 → P87
- The LabelFrame widget — 62 → P87
- Implementing the application — 64 → P89
  - First steps — 65 → P90
  - Building the data record form — 66 → P91
  - The Record Information section — 67 → P92
  - The Environment Data section — 69 → P94
  - The Plant Data section — 70 → P95
  - Finishing the GUI — 72 → P97
  - Writing the callback functions — 73 → P98
    - The Reset function — 73 → P98
    - The Save callback — 74 → P99
  - Finishing up and testing — 78 → P103
- Summary — 79 → P104

### Ch4 · Organizing Our Code with Classes （P106）
- A primer on Python classes — 81 → P106
  - The advantages of using classes — 82 → P107
  - Classes are an integral part of Python — 82 → P107
  - Classes make relationships between data and functions explicit — 82 → P107
  - Classes help create reusable code — 83 → P108
  - Syntax of class creation — 83 → P108
  - Attributes and methods — 83 → P108
  - Magic attributes and methods — 86 → P111
  - Public, private, and protected members — 88 → P113
  - Inheritance and subclasses — 90 → P115
- Using classes with Tkinter — 91 → P116
  - Improving Tkinter classes — 91 → P116
  - Creating compound widgets — 93 → P118
  - Building encapsulated components — 95 → P120
  - Subclassing Tk — 97 → P122
  - Rewriting our application using classes — 100 → P125
    - Adding a StringVar to the Text widget — 100 → P125
    - Passing in a variable — 101 → P126
    - Synchronizing the widget to the variable — 101 → P126
    - Synchronizing the variable to the widget — 102 → P127
  - Creating a more advanced LabelInput() — 103 → P128
  - Creating a form class — 106 → P131
  - Creating an application class — 112 → P137
- Summary — 114 → P139

### Ch5 · Reducing User Error with Validation and Automation （P142）
- Validating user input — 117 → P142
  - Strategies to prevent data errors — 118 → P143
  - Validation in Tkinter — 119 → P144
    - The validate argument — 120 → P145
    - The validatecommand argument — 120 → P145
    - The invalidcommand argument — 122 → P147
  - Creating validated widget classes — 123 → P148
  - Creating a Date field — 125 → P150
  - Implementing validated widgets in our GUI — 129 → P154
    - Introducing the power of multiple inheritance — 129 → P154
    - Building a validating mixin class — 132 → P157
    - Building validating input widgets with ValidatedMixin — 136 → P161
    - Requiring data — 136 → P161
    - Creating a Date widget — 137 → P162
    - A better Combobox widget — 138 → P163
    - A range-limited Spinbox widget — 140 → P165
    - Validating Radiobutton widgets — 144 → P169
  - Updating our form with validated widgets — 146 → P171
  - Implementing validation interaction between form widgets — 149 → P174
    - Dynamically updating the Spinbox range — 149 → P174
    - Dynamic disabling of fields — 154 → P179
  - Displaying errors — 156 → P181
  - Preventing form submission on error — 157 → P182
- Automating input — 159 → P184
  - Date automation — 160 → P185
  - Automating Plot, Lab, Time, and Technician — 161 → P186
- Summary — 162 → P187

### Ch6 · Planning for the Expansion of Our Application （P188）
- Separating concerns — 164 → P189
  - The MVC pattern — 164 → P189
    - What is a model? — 165 → P190
    - What is a view? — 165 → P190
    - What is a controller? — 166 → P191
    - Why complicate our design? — 166 → P191
  - Structuring our application directory — 167 → P192
    - Basic directory structure — 167 → P192
    - The abq_data_entry.py file — 168 → P193
    - The README.rst file — 169 → P194
    - Populating the docs folder — 170 → P195
    - Making a Python package — 170 → P195
  - Splitting our application into multiple files — 172 → P197
    - Creating the models module — 172 → P197
    - Moving the widgets — 179 → P204
    - Moving the views — 180 → P205
    - Removing redundancy in our view logic — 181 → P206
    - Using custom events to remove tight coupling — 185 → P210
    - Creating the application file — 186 → P211
    - Running the application — 188 → P213
- Using version control software — 189 → P214
  - A super-quick guide to using Git — 189 → P214
    - Initializing and configuring a Git repository — 190 → P215
    - Adding and committing code — 190 → P215
    - Viewing and using our commits — 191 → P216
- Summary — 192 → P217

### Ch7 · Creating Menus with Menu and Tkinter Dialogs （P218）
- Solving problems in our application — 194 → P219
  - Planning solutions to the issues — 194 → P219
- Implementing Tkinter dialogs — 196 → P221
  - Error dialogs with the Tkinter messagebox — 196 → P221
  - Showing error dialogs in ABQ Data Entry — 199 → P224
  - Using filedialog — 201 → P226
  - Using simpledialog and creating a custom dialog — 204 → P229
    - Creating a Login dialog using simpledialog — 205 → P230
    - Incorporating the LoginDialog in our class — 208 → P233
- Designing the application menu — 211 → P236
  - The Tkinter Menu widget — 211 → P236
  - Using Checkbutton and Radiobutton items — 213 → P238
  - Implementing the ABQ application menu — 215 → P240
    - Adding a Help menu — 216 → P241
    - Adding a File menu — 217 → P242
    - Adding a settings menu — 220 → P245
    - Finishing the menu — 222 → P247
  - Persisting settings — 223 → P248
    - Building a model for settings persistence — 224 → P249
    - Using the settings model in our application — 228 → P253
- Summary — 230 → P255

### Ch8 · Navigating Records with Treeview and Notebook （P256）
- Implementing read and update in the model — 231 → P256
  - Adding read and update to the CSVModel class — 232 → P257
  - Implementing get_all_records() — 233 → P258
  - Implementing get_record() — 235 → P260
  - Adding update capability to save_record() — 236 → P261
- The Ttk Treeview — 237 → P262
  - Anatomy of a Treeview — 238 → P263
  - Building a file browser — 239 → P264
  - Creating and configuring a Treeview — 240 → P265
  - Populating a Treeview with data — 242 → P267
  - Sorting Treeview records — 244 → P269
  - Using Treeview virtual events — 247 → P272
  - Implementing a record list with Treeview — 248 → P273
    - Creating the RecordList class — 249 → P274
    - Configuring a Treeview widget — 250 → P275
    - Adding a scrollbar for the Treeview — 252 → P277
    - Populating the Treeview — 253 → P278
    - Adding the record list to the application — 254 → P279
  - Modifying the record form for read and update — 255 → P280
    - Adding a current record property — 255 → P280
    - Adding a label to show what is being edited — 255 → P280
    - Adding a load_record() method — 256 → P281
  - Updating the application layout — 257 → P282
- The Ttk Notebook widget — 259 → P284
  - Adding a notebook to our application — 261 → P286
  - Adding and updating application callbacks — 262 → P287
    - The _show_recordlist() method — 263 → P288
    - The _populate_recordlist() method — 264 → P289
    - The _new_record() method — 265 → P290
    - The _open_record() method — 266 → P291
    - The _on_save() method — 267 → P292
  - Main menu changes — 267 → P292
  - Testing our program — 268 → P293
- Summary — 269 → P294

### Ch9 · Improving the Look with Styles and Themes （P297）
- Working with images in Tkinter — 272 → P297
  - Tkinter PhotoImage — 273 → P298
    - PhotoImage and variable scope — 274 → P299
  - Using Pillow for extended image support — 277 → P302
  - Adding the company logo to ABQ Data Entry — 278 → P303
    - Dealing with the image path problem — 281 → P306
  - Setting a window icon — 282 → P307
  - Adding icons to buttons and menus — 286 → P311
    - Using BitmapImage — 287 → P312
- Styling Tkinter widgets — 287 → P312
  - Widget color properties — 288 → P313
    - Using widget properties on the MainMenu — 291 → P316
  - Styling widget content with tags — 294 → P319
    - Styling our record list with tags — 297 → P322
- Working with fonts in Tkinter — 297 → P322
  - Configuring Tkinter fonts — 298 → P323
    - Configuring fonts with strings and tuples — 299 → P324
    - The font module — 302 → P327
  - Giving users font options in ABQ Data Entry — 305 → P330
- Styling Ttk widgets — 306 → P331
  - TTK styling breakdown — 307 → P332
    - Exploring a Ttk widget — 312 → P337
    - Using themes — 313 → P338
  - Adding some color to ABQ Data Entry — 316 → P341
    - Adding styles to individual form widgets — 319 → P344
    - Fixing the error colors — 321 → P346
    - Styling input widgets on error — 321 → P346
  - Setting themes — 321 → P346
    - Building a theme selector — 325 → P350
- Summary — 327 → P352

### Ch10 · Maintaining Cross-Platform Compatibility （P352）
- Writing cross-platform Python — 328 → P353
  - Filenames and file paths across platforms — 328 → P353
    - Path separators and drives — 331 → P356
    - Case sensitivity — 332 → P357
    - Symbolic links — 333 → P358
    - Path variables — 334 → P359
  - Inconsistent library and feature support — 334 → P359
    - Python's platform-limited libraries — 335 → P360
    - Checking low-level function compatibility — 336 → P361
    - The dangers of the subprocess module — 336 → P361
  - Text file encodings and formats — 337 → P362
  - Graphical and console modes — 337 → P362
- Writing code that changes according to the platform — 338 → P363
- Writing cross-platform Tkinter — 341 → P366
  - Tkinter version differences across platforms — 341 → P366
  - Application menus across platforms — 342 → P367
    - Menu widget capabilities — 342 → P367
    - Menu guidelines and standards — 346 → P371
    - Menus and accelerator keys — 347 → P372
  - Cross-platform fonts — 347 → P372
  - Cross-platform theme support — 348 → P373
  - Window zoomed state — 348 → P373
- Improving our application's cross-platform compatibility — 349 → P374
  - Storing preferences correctly — 349 → P374
  - Specifying an encoding for our CSV file — 351 → P376
  - Making platform-appropriate menus — 351 → P376
    - Preparing our MainMenu class — 351 → P376
    - Adding accelerators — 355 → P380
    - Building the Windows menu — 357 → P382
    - Building the Linux menu — 359 → P384
    - Building the macOS menu — 360 → P385
    - Creating and using our selector function — 363 → P388
- Summary — 365 → P390

### Ch11 · Creating Automated Tests with unittest （P392）
- Automated testing basics — 367 → P392
  - A simple unit test — 368 → P393
  - The unittest module — 370 → P395
  - Writing a test case — 371 → P396
  - TestCase assertion methods — 373 → P398
  - Fixtures — 374 → P399
  - Using Mock and patch — 375 → P400
  - Running multiple unit tests — 377 → P402
- Testing Tkinter code — 377 → P402
  - Managing asynchronous code — 378 → P403
  - Simulating user actions — 378 → P403
  - Specifying an event sequence — 379 → P404
  - Managing focus and grab — 380 → P405
  - Getting widget information — 381 → P406
- Writing tests for our application — 381 → P406
  - Testing the data model — 381 → P406
    - Testing file reading in get_all_records() — 383 → P408
    - Testing file saving in save_record() — 385 → P410
  - More tests on the models — 387 → P412
  - Testing our Application object — 387 → P412
  - Testing our widgets — 392 → P417
    - Unit testing the ValidatedSpinbox widget — 393 → P418
    - Integration testing the ValidatedSpinbox widget — 395 → P420
  - Testing our mixin class — 400 → P425
- Summary — 402 → P427

### Ch12 · Improving Data Storage with SQL （P428）
- PostgreSQL — 404 → P429
  - Installing and configuring PostgreSQL — 404 → P429
    - Configuring PostgreSQL using the GUI utility — 405 → P430
    - Configuring PostgreSQL using the command line — 405 → P430
  - Modeling relational data — 406 → P431
    - Primary keys — 406 → P431
    - Using surrogate primary keys — 407 → P432
    - Normalization — 408 → P433
      - First normal form — 409 → P434
      - Second normal form — 410 → P435
      - Third normal form — 411 → P436
      - More normalization forms — 411 → P436
    - Entity-relationship diagrams — 412 → P437
    - Assigning data types — 414 → P439
  - Creating the ABQ database — 415 → P440
    - Creating our tables — 415 → P440
    - Creating the lookup tables — 415 → P440
    - The lab_checks table — 417 → P442
    - The plot_checks table — 417 → P442
  - Creating a view — 419 → P444
  - Populating the lookup tables — 420 → P445
  - Connecting to PostgreSQL with psycopg2 — 420 → P445
    - psycopg2 basics — 421 → P446
    - Parameterized queries — 423 → P448
    - Special cursor classes — 425 → P450
  - Integrating SQL into our application — 426 → P451
    - Creating a new model — 426 → P451
    - Saving data — 431 → P456
    - Getting the current seed sample for the plot — 434 → P459
    - Adjusting the Application class for the SQL backend — 435 → P460
    - Implementing SQL logins — 435 → P460
    - Updating the Application._on_save() method — 437 → P462
    - Removing file-based code — 438 → P463
    - Adjusting the DataRecordForm for SQL data — 438 → P463
    - Reordering fields — 438 → P463
    - Fixing the load_record() method — 439 → P464
    - Improving auto-fill — 440 → P465
    - Updating the RecordList for the SQLModel — 441 → P466
- We're done! — 444 → P469
- Summary — 444 → P469

### Ch13 · Connecting to the Cloud （P472）
- HTTP using urllib — 447 → P472
  - HTTP transaction fundamentals — 448 → P473
  - HTTP status codes — 448 → P473
  - Basic downloading with urllib.request — 449 → P474
  - Generating POST requests — 450 → P475
  - Downloading weather data to ABQ Data Entry — 451 → P476
    - Creating a weather data model — 451 → P476
    - Parsing the XML weather data — 453 → P478
    - Implementing weather data storage — 456 → P481
    - Adding the GUI elements for weather download — 458 → P483
- RESTful HTTP using requests — 461 → P486
  - Understanding RESTful web services — 461 → P486
  - The Python requests library — 462 → P487
    - Installing and using requests — 462 → P487
    - Interacting with authenticated sites using Session — 463 → P488
    - The requests.Response object — 465 → P490
  - Implementing a REST backend — 466 → P491
    - The authenticate() method — 468 → P493
    - The upload_file() method — 470 → P495
    - The check_file() method — 470 → P495
    - The get_file() method — 471 → P496
  - Integrating REST upload into the application — 471 → P496
    - Creating a CSV extract — 472 → P497
    - Creating the upload callback — 473 → P498
    - Finishing up — 476 → P501
- SFTP using paramiko — 478 → P503
  - Setting up SSH services for testing — 478 → P503
  - Installing and using paramiko — 479 → P504
  - Using paramiko — 479 → P504
  - Inspecting our connection — 481 → P506
  - Using SFTP — 481 → P506
  - Implementing an SFTP model — 482 → P507
    - Uploading files — 485 → P510
    - Checking a file's existence — 486 → P511
  - Using SFTPModel in our application — 487 → P512
  - Finishing up — 490 → P515
- Summary — 491 → P516

### Ch14 · Asynchronous Programming with Thread and Queue （P518）
- Tkinter's event queue — 494 → P519
  - Event queue control — 494 → P519
  - The update() methods — 494 → P519
  - The after() methods — 495 → P520
  - Common uses of event queue control — 496 → P521
    - Smoothing out display changes — 496 → P521
    - Mitigating GUI freezes — 497 → P522
- Running code in the background with threads — 500 → P525
  - The threading module — 500 → P525
  - Tkinter and thread safety — 502 → P527
  - Converting our network functions to threaded execution — 503 → P528
  - Using the threaded uploader — 505 → P530
- Passing messages using a queue — 506 → P531
  - The Queue object — 506 → P531
  - Using queues to communicate between threads — 508 → P533
  - Adding a communication queue to our threaded uploader — 510 → P535
  - Creating a communications protocol — 511 → P536
    - Sending messages from the uploader — 513 → P538
    - Handling queue messages — 514 → P539
  - Using locks to protect shared resources — 516 → P541
    - Understanding the Lock object — 516 → P541
    - Using a Lock object to prevent concurrent uploads — 518 → P543
  - Threading and the GIL — 518 → P543
- Summary — 519 → P544

### Ch15 · Visualizing Data Using the Canvas Widget （P546）
- Drawing and animation with Tkinter's Canvas — 521 → P546
  - Drawing on the Canvas — 522 → P547
    - Rectangles and squares — 522 → P547
    - Ovals, circles, and arcs — 524 → P549
    - Lines — 525 → P550
    - Polygons — 526 → P551
    - Text — 526 → P551
    - Images — 527 → P552
    - Tkinter widgets — 527 → P552
  - Canvas items and state — 528 → P553
  - Canvas object methods — 528 → P553
  - Scrolling the Canvas — 530 → P555
  - Animating Canvas objects — 533 → P558
    - Setting up the playing field — 533 → P558
    - Setting our players — 534 → P559
    - Animating the racers — 535 → P560
    - Running the game loop and detecting a win condition — 539 → P564
  - Creating simple graphs using Canvas — 542 → P567
    - Creating the model method — 543 → P568
    - Creating the chart view — 544 → P569
    - Updating the application — 549 → P574
  - Advanced graphs using Matplotlib — 551 → P576
    - Data model method — 551 → P576
    - Creating the bubble chart view — 552 → P577
    - Updating the Application class — 555 → P580
- Summary — 555 → P580

### Ch16 · Packaging with setuptools and cxFreeze （P583）
- Creating distributable packages with setuptools — 559 → P584
  - Preparing our package for distribution — 559 → P584
    - Creating a requirements.txt file — 560 → P585
    - Creating a pyproject.toml file — 560 → P585
    - Adding a license file — 560 → P585
    - Making our package executable — 562 → P587
  - Configuring a setup.py script — 564 → P589
    - Basic metadata arguments — 565 → P590
    - Packages and dependencies — 566 → P591
    - Adding extra files — 566 → P591
    - Defining commands — 567 → P592
    - Testing the configuration — 569 → P594
  - Creating and using source distributions — 571 → P596
    - Testing our source distribution — 571 → P596
  - Building a wheel distribution — 572 → P597
- Creating executables with cx_Freeze — 573 → P598
  - First steps with cx_Freeze — 575 → P600
  - The build_exe options — 575 → P600
  - Including external files — 577 → P602
  - Building executables — 578 → P603
    - Cleaning up the build — 580 → P605
  - Building Windows executables with cx_Freeze — 580 → P605
    - Building a Windows installer file — 582 → P607
  - Building macOS executables with cx_Freeze — 582 → P607
    - Building macOS application bundles — 586 → P611
    - Building macOS .dmg files — 586 → P611
- Summary — 588 → P613

### 附录
- Appendix A · A Quick Primer on reStructuredText — 591 → P616
- Appendix B · A Quick SQL Tutorial — 603 → P628
- Other Books You May Enjoy — 619 → P644
- Index（书末主题索引）— 625 → P650

---

## C. 主题速查（概念 → 章节 / PDF 页）

| 主题 | 章节 | 关键节（PDF 页） |
|------|------|------------------|
| 几何管理器 pack/grid/place | Ch1 | Arranging widgets · P39 |
| 控件变量 StringVar/IntVar/BoolVar/DoubleVar | Ch1 | Control variables · P46 |
| IDLE 作为 Tkinter 范例 | Ch1 | IDLE · P29 |
| Ttk 控件集（Label/Entry/Spinbox/Checkbutton/Radiobutton/Combobox/Text/Button/LabelFrame） | Ch3 | Ttk widget set · P76–P87 |
| Text 控件索引体系 | Ch3 | Text widget indices · P85 |
| 复合控件 / 封装组件 | Ch4 | Compound widgets · P118 |
| 继承 Tk（Subclassing Tk） | Ch4 | P122 |
| 输入校验 validate / validatecommand / invalidcommand | Ch5 | Validation in Tkinter · P144–P147 |
| ValidatedMixin 与多重继承校验 | Ch5 | P157–P165 |
| MVC 架构模式 | Ch6 | The MVC pattern · P189 |
| 自定义事件解耦（custom events） | Ch6 | P210 |
| Git 版本控制 | Ch6 | P214–P216 |
| Menu 菜单控件 | Ch7 | Tkinter Menu widget · P236 |
| 对话框 messagebox / filedialog / simpledialog / 自定义 LoginDialog | Ch7 | P221–P233 |
| 设置持久化（settings persistence） | Ch7 | P248–P253 |
| Treeview（表格/文件浏览器/虚拟事件/排序） | Ch8 | P262–P273 |
| Notebook 选项卡 | Ch8 | P284 |
| 图像 PhotoImage / BitmapImage / 变量作用域 | Ch9 | P298 / P312 |
| Pillow 扩展图像支持 | Ch9 | P302 |
| 窗口图标 setting window icon | Ch9 | P307 |
| 字体 font 模块 / 字符串与元组配置 | Ch9 | P323–P327 |
| Text 内容样式 tags | Ch9 | P319 |
| Ttk 样式与主题 themes / 样式引擎 | Ch9 | P331–P350 |
| 跨平台（路径/编码/菜单/字体/主题/zoomed） | Ch10 | P353–P390 |
| 平台专属菜单（Windows/Linux/macOS）+ 快捷键 | Ch10 | P376–P388 |
| unittest / Mock / patch 单元测试 | Ch11 | P395–P400 |
| 测试 Tkinter（模拟事件/焦点/grab） | Ch11 | P402–P406 |
| SQL / 关系建模 / 范式 / ERD / PostgreSQL / psycopg2 | Ch12 | P428–P450 |
| 参数化查询 / 特殊游标类 | Ch12 | P448–P450 |
| HTTP urllib（请求/POST/状态码/XML 解析） | Ch13 | P472–P483 |
| requests 库 / REST / Session 认证 | Ch13 | P486–P496 |
| paramiko / SFTP / SSH 上传 | Ch13 | P503–P512 |
| 事件队列 / after() / update() 防冻结 | Ch14 | P519–P522 |
| 多线程 threading / 线程安全 | Ch14 | P525–P527 |
| Queue / Lock / GIL 线程通信 | Ch14 | P531–P543 |
| Canvas 绘图（矩形/椭圆/弧/线/多边形/文本/图像） | Ch15 | P547–P552 |
| Canvas 滚动 / 动画 / 游戏循环 | Ch15 | P555–P564 |
| 用 Canvas 画图表 | Ch15 | P567–P574 |
| Matplotlib 气泡图 | Ch15 | P576–P580 |
| setuptools / pyproject.toml / wheel 打包 | Ch16 | P584–P597 |
| cx_Freeze 生成 exe / 安装包 / .app / .dmg | Ch16 | P598–P611 |
| reStructuredText 速成 | App A | P616 |
| SQL 速成教程 | App B | P628 |

---

## D. 与本技能（tkinter-desktop）的衔接建议
- 本书是「从脚本到完整桌面应用」的实战教程，与技能已有的 `03-ui-design.md`/`04-widgets-and-patterns.md` 形成「原理 → 工程化」互补。
- 技能尚未覆盖、本书强覆盖的主题（可日后按 DRY 补进 03/04 或新建参考）：**MVC 分层、校验 Mixin、Treeview/Notebook 实战、Ttk 主题引擎、跨平台菜单、unittest 测 Tkinter、SQL 后端、urllib/requests/paramiko 联网、threading+Queue 异步、Canvas 图表、cx_Freeze 打包**。
- 注意：本书第 2 版打包用 **cx_Freeze**（非 PyInstaller）；打包章节结论需结合运行期 Tk 8.6 / Python 3.13 实测复核（技能铁律：论断须本机验证）。
- 同类本地参考：Tcl/Tk 8.6 官方文档（`tcl-tk/tcl8.6-docs/`，底层命令权威源）。本书偏「工程组织与最佳实践」，二者互补。
