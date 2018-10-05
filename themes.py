import os
import xml.etree.ElementTree as ET

def importColorThemes(colorThemesFolder):

    xmlThemes = os.listdir(colorThemesFolder)
    colorThemes = {}

    for colorTheme in xmlThemes:
        xmlPath = os.path.join(colorThemesFolder, colorTheme)
        tree = ET.parse(xmlPath)
        root = tree.getroot()
        colorThemeName = root.attrib['name']
        colorThemes[colorThemeName] = {}
        for child in root:
            colorThemes[colorThemeName][child.tag] = child.attrib['color']

    return colorThemes

def convertColorTheme(colorThemeEclipse):

    c = colorThemeEclipse

    return {
        'background' : c['background'],
        'highlight'  : c['selectionBackground'],
        'tokens' : {
            'Token'                      : c['foreground'],
            'Token.Name'                 : c['foreground'],
            'Token.Name.Namespace'       : c['foreground'],
            'Token.Text'                 : c['foreground'],
            'Token.Punctuation'          : c['foreground'],
            'Token.Comment'              : c['singleLineComment'],
            'Token.Name.Attribute'       : c['number'],
            'Token.Literal.Number'       : c['number'],
            'Token.Literal.Number.Float' : c['number'],
            'Token.Literal.Number.Oct'   : c['number'],
            'Token.Literal.Number.Hex'   : c['number'],
            'Token.Name.Tag'             : c['localVariable'],
            'Token.Name.Variable'        : c['localVariable'],
            'Token.Name.Constant'        : c['localVariable'],
            'Token.Name.Class'           : c['class'],
            'Token.Name.Decorator'       : c['class'],
            'Token.Name.Builtin.Pseudo'  : c['class'],
            'Token.Name.Builtin'         : c['class'],
            'Token.Name.Function'        : c['class'],
            'Token.Literal.String'       : c['string'],
            'Token.Literal.String.Doc'   : c['string'],
            'Token.Operator.Word'        : c['keyword'],
            'Token.Keyword'              : c['keyword'],
            'Token.Operator'             : c['operator'],
            'Token.Error'                : c['deprecatedMember'],
            'Token.Keyword.Namespace'    : c['deprecatedMember'],
            'Token.Name.Exception'       : c['deprecatedMember'],
        }
    }

def getColorThemes(colorThemesFolder):
    colorThemesEclipse = importColorThemes(colorThemesFolder)
    colorThemesRF = {}
    for colorThemeName in colorThemesEclipse.keys():
        colorThemesRF[colorThemeName] = convertColorTheme(colorThemesEclipse[colorThemeName])
    return colorThemesRF

if __name__ == '__main__':

    colorThemesFolder = os.path.join(os.getcwd(), 'themes')
    themesDict = getColorThemes(colorThemesFolder)
    print(themesDict.keys())
