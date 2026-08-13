# pywin32 (PyPI project page)

> Source: https://pypi.org/project/pywin32/
> Retrieved: 2026-08-02

**pywin32 312**

```
pip install pywin32
```

- **Latest release:** Jun 4, 2026
- **Summary:** Python for Windows Extensions

### Verified details

**Maintainers:** glyph, mhammond, pf_moore

### Unverified details

**Project links**

- Bugs: https://github.com/mhammond/pywin32/issues
- Changes: https://github.com/mhammond/pywin32/blob/main/CHANGES.md
- Docs: https://mhammond.github.io/pywin32/
- Homepage: https://github.com/mhammond/pywin32
- Mailing List: https://mail.python.org/mailman/listinfo/python-win32
- Support Requests: https://github.com/mhammond/pywin32/discussions

**Meta**

- **License:** Python Software Foundation License (PSF)
- **Author:** Mark Hammond (et al)
- **Requires:** Python >=3.9

**Classifiers**

- Development Status :: 5 - Production/Stable
- Environment :: Win32 (MS Windows)
- Intended Audience :: Developers
- License :: OSI Approved :: Python Software Foundation License
- Operating System :: Microsoft :: Windows
- Programming Language :: Python :: 3.9
- Programming Language :: Python :: 3.10
- Programming Language :: Python :: 3.11
- Programming Language :: Python :: 3.12
- Programming Language :: Python :: 3.13
- Programming Language :: Python :: 3.14
- Programming Language :: Python :: 3.15
- Programming Language :: Implementation :: CPython

## Project description

This is the readme for the Python for Win32 (pywin32) extensions, which provides access to many of the Windows APIs from Python, including COM support.

See CHANGES.md for recent notable changes.

adodbapi's documentation can be found in: adodbapi/readme.txt

isapi's documentation can be found in: isapi/README.txt

### Docs

The docs are a long and sad story, but there's now an online version of the PyWin32.chm helpfile. You can get type hints, signatures and annotations from types-pywin32.

### Support

Feel free to open issues for all bugs in pywin32. Pull-requests for all bugs or features are also welcome. Please do not open GitHub issues for general support requests; start a discussion under the Q&A category instead. The python-win32 mailing list is still available for general Python on Windows help requests.

### Installing via PIP

```
python -m pip install --upgrade pywin32
```

```
python -m pywin32_postinstall -install
```

```
pywin32_postinstall -install
```

### Running as a Windows Service

To run as a service, install pywin32 globally from an elevated command prompt. Ensure Python is installed where the service account can load pywintypesXX.dll and pythonXX.dll. The LocalSystem account typically will not have access to your local %USER% directory structure.

### Troubleshooting

```
The specified procedure could not be found
Entry-point not found
```

- Re-run the post-install script: `python -m pywin32_postinstall -install` (or `pywin32_postinstall -install`).
- Otherwise find and remove all other copies of `pywintypesXX.dll` and `pythoncomXX.dll` (where XX is the Python version, e.g. "39").

### Building from source

Install Visual Studio 2019, follow the Build environment instructions, then the Build instructions (including ARM64 cross-compilation).

### Versioning

pywin32 uses a simple incremental version numbering scheme. Any increase in the version number may correspond to a breaking interface change. It is recommended that projects using pywin32 pin the dependency to a specific version.

### Licenses

pywin32 contains a mix of differently licensed code. The license files in the source tree are the source of truth, as are individual Copyright notices at the top of files.
