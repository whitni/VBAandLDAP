from distutils.core import setup
import py2exe, sys, os

manifest = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <noInheritable/>
    <assemblyIdentity
        type="win32"
        name="Microsoft.VC90.CRT"
        version="9.0.21022.8"
        processorArchitecture="*"
        publicKeyToken="1fc8b3b9a1e18e3b"
    />
    <file name="msvcr90.dll" />
</assembly>
"""

setup(
    console = [
        {
            "script": "LDIFtoCSV.py",
            "other_resources": [(24,1,manifest)]
        }
    ],
    options = {'py2exe': {'bundle_files': 1}},
    zipfile = None
)
