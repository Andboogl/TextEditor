from setuptools import setup


APP_NAME = 'TextEditor'
APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'packages': ['PyQt6-Qt6', 'PyQt6-sip'],
    'iconfile': 'ic.icns',
    'argv_emulation': True,
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
