import os
from mojo.extensions import ExtensionBundle

libPath       = os.path.dirname(__file__)
extensionFile = 'codeColors.roboFontExt'
extensionPath = os.path.join(libPath, extensionFile)

print('building extension...', end='')

B = ExtensionBundle()
B.name            = "codeColors"
B.developer       = 'RoboDocs'
B.developerURL    = 'http://github.com/roboDocs/'
B.version         = "0.0.1"
B.mainScript      = ""
B.launchAtStartUp = 0
B.addToMenu       = [{
        'path'          : 'dialog.py',
        'preferredName' : 'CodeColors',
        'shortKey'      : ''
}]
B.requiresVersionMajor = '3'
B.requiresVersionMinor = '0'
B.save(extensionPath, libPath=libPath, resourcesPath=None, pycOnly=False)

print('done!\n')
