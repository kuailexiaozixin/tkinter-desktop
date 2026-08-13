# Translating pygubu-designer to your language

First of all, prepare a development environment in your computer following the instructions [[here|Development-Environment]].

Download and install [[poedit|https://poedit.net]]. This app will help you to translate the strings and generate the required files.

Determine your language and region tags. For example, for Spanish/Argentina the tags are: "es" and "AR".
With this info, create a new folder in pygubudesigner/locale directory:

    mkdir -p pygubudesigner/locale/es_AR/LC_MESSAGES

Open poedit. Navigate to "File > New from POT". Select the file pygubudesigner/locale/pygubu.pot as the template.
Poedit will ask for the target language, in this example Spanish/Argentina.

![poedit-001](https://user-images.githubusercontent.com/8467919/158715762-8e6a233c-9010-4ee9-80dc-23e83c6f8665.png)

Start translating the strings to your language. Then save the file in the folder created before (pygubudesigner/locale/es_AR/LC_MESSAGES) with the name pygubu.po (this will also generate a pygubu.mo in the same directory)

To test the translation just start pygubudesigner in the development environment.

    python -m pygubudesigner

If you do not see the strings translated, try to configure the LANG environment variable:

    # for example in GNU/Linux run:
    LANG=es_AR;  python -m pygubudesigner

Finally, create a pull request with the new pygubu.po generated.
