
# Collections of issues found when building with pyinstaller.



## ImportError: cannot import name 'ImageFont' from 'PIL'
```py

hiddenimports = ["FMD3","PIL.ImageFont","PIL.ImageDraw"]
```

## Exception: Class "tkinterweb.HtmlFrame" not mapped

If using spec file:

```py
from PyInstaller.utils.hooks import collect_all
datas = []
binaries=[]
collects = [collect_all('tkinterweb'), collect_all('pygubu')]
for ret in collects:
    datas += ret[0]
    binaries += ret[1]
    hiddenimports += ret[2]
```


(Will be updated with more info. just wanted to note it as i'm troubleshooting)