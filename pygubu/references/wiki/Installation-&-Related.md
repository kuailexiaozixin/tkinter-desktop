# Installation with pip
At the command-line, terminal or shell, run the following command.

`pip install pygubu-designer`


### Upgrade
From time to time, we release a new version with bug fixes and new features. Run the following command to upgrade.

`pip install pygubu-designer -U`

### Removal
Run the following, should you ever want to remove the program.

`pip uninstall pygubu-designer`

### What is pip, you say?
[Pip](https://pypi.org/project/pip/) is the package installer for [Python](https://www.python.org).

### Notes for Windows Users:

If your Python installation directory contains spaces (e.g., `C:\Program Files\Python312`), you may encounter errors. Use one of the following solutions:

1. Use quotation marks when running commands:

```

"C:\Program Files\Python312\Scripts\pygubu-designer.exe"
```

2. Add Python to your system's PATH:
- Open **System Properties** > **Environment Variables**.
- Under **System Variables**, select `Path` > **Edit**.
- Add the path to your Python installation (e.g., `C:\Program Files\Python312`).

3. Use the short pathname format for directories with spaces:


```

C:\PROGRA~1\Python312\Scripts\pygubu-designer.exe
```


# Installation on Arch Linux ([AUR](https://aur.archlinux.org/packages/pygubu-designer))

```
yay pygubu-designer
```


# Installation with pipx

If you are using debian 12 or above, pip can't be used without a virtual environment.  As an alternative you can use pipx.

`sudo apt install pipx`

### Install

`pipx install pygubu-designer`

### Upgrade

`pipx upgrade pygubu-designer`

### Removal

`pipx uninstall pygubu-designer`

# Installing from github

If you want to try the latest development version, install from github using the following commands:

    # Create a virtual environment (use your preferred tool here)
    python3 -m venv test-venv
    source test-venv/bin/activate
    # Install development versions
    pip install git+https://github.com/alejandroautalan/pygubu.git
    pip install git+https://github.com/alejandroautalan/pygubu-designer.git


# Installing older versions

If you need to run an older version, prepare a virtual environment and run the pip command. 
Note that an older version may require an older python version also.

2025-05-31 version 0.41.2

    pip install pygubu-designer==0.41.2 pygubu==0.38

2025-02-14 version 0.40.2

    pip install pygubu-designer==0.40.2 pygubu==0.36.3

2024-02-22 version 0.39.3

    pip install pygubu-designer==0.39.3 pygubu==0.35.6

2024-02-11 version 0.38

    pip install pygubu-designer==0.38 pygubu==0.35.1

2024-01-06 version 0.37

    pip install pygubu-designer==0.37 pygubu==0.32

2023-05-28 version 0.36

    pip install pygubu-designer==0.36 pygubu==0.31

2023-03-02 version 0.35

    pip install pygubu-designer==0.35 pygubu==0.30

2023-01-17 version 0.34

    pip install pygubu-designer==0.34 pygubu==0.29

2022-12-12 version 0.33

    pip install pygubu-designer==0.33 pygubu==0.29

2022-11-19 version 0.32

    pip install pygubu-designer==0.32 pygubu==0.27

2022-11-01 version 0.31.3

    pip install pygubu-designer==0.31.3 pygubu==0.26.2

2022-09-04 version 0.30

    pip install pygubu-designer==0.30 pygubu==0.25.1

2022-08-28 version 0.29.1

    pip install pygubu-designer==0.28 pygubu==0.24.2

2022-07-16 version 0.28

    pip install pygubu-designer==0.28 pygubu==0.23.1

2022-06-14 version 0.27

    pip install pygubu-designer==0.27 pygubu==0.22

2022-05-12 version 0.26.1

    pip install pygubu-designer==0.26.1 pygubu==0.21

2022-04-15 version 0.25.1

    pip install pygubu-designer==0.25.1 pygubu==0.20.1

2022-02-06 version 0.24

    pip install pygubu-designer==0.22 pygubu==0.20

2022-01-09 version 0.23

    pip install pygubu-designer==0.22 pygubu==0.19

2021-10-26 version 0.22

    pip install pygubu-designer==0.22 pygubu==0.18.1

2021-09-25 version 0.21

    pip install pygubu-designer==0.21 pygubu==0.16

2021-09-19 version 0.20

    pip install pygubu-designer==0.20 pygubu==0.15

2021-09-05 version 0.19

    pip install pygubu-designer==0.19 pygubu==0.14

2021-08-22 version 0.18

    pip install pygubu-designer==0.18 pygubu==0.13
 
2021-05-23 version 0.17

    pip install pygubu-designer==0.17 pygubu==0.11

2021-03-25 version 0.16

    pip install pygubu-designer==0.16 pygubu==0.10.9

2021-03-15 version 0.15

    pip install pygubu-designer==0.15 pygubu==0.10.9

2021-03-15 version 0.14

    pip install pygubu-designer==0.14 pygubu==0.10.8

version 0.12

    pip install pygubu-designer==0.12 pygubu==0.10.7

version 0.11

    pip install pygubu-designer==0.11 pygubu==0.10.3

version 0.10.1

    pip install pygubu-designer==0.10.1 pygubu===0.10.3

