import os
from AppKit import NSNotificationCenter, NSColor
from vanilla import FloatingWindow, List
from vanilla.vanillaBase import VanillaCallbackWrapper
from lib.tools.defaults import getDefault, getDefaultColor, setDefault, setDefaultColor
from themes import getColorThemes


def rgbToNSColor(rgbColor):
    if rgbColor is None or len(rgbColor) > 4:
        return
    elif len(rgbColor) == 1:
        r = g = b = rgbColor[0]
        a = 1.0
    elif len(rgbColor) == 2:
        grey, a = rgbColor
        r = g = b = grey
    elif len(rgbColor) == 3:
        r, g, b = rgbColor
        a = 1.0
    elif len(rgbColor) == 4:
        r, g, b, a = rgbColor
    return NSColor.colorWithCalibratedRed_green_blue_alpha_(r, g, b, a)


def hexToRGB(value):
    value = value.lstrip('#')
    lv = len(value)
    rgb = tuple()
    for i in range(0, lv, lv//3):
        rgb += (int(value[i:i+lv//3], 16) / 255.0,)
    return rgb


def setColorTheme(colorTheme):
    notification = "PyDEUserDefaultChanged"

    # set token colors
    setDefault("PyDETokenColors", colorTheme['tokens'])

    # set background color
    colorBackground = rgbToNSColor(hexToRGB(colorTheme['background']))
    setDefaultColor("PyDEbackgroundColor", colorBackground)

    # set highlight color
    colorHighlight = rgbToNSColor(hexToRGB(colorTheme['highlight']))
    setDefaultColor("PyDEHightLightColor", colorHighlight)

    # update code editor
    nc = NSNotificationCenter.defaultCenter()
    nc.postNotificationName_object_userInfo_(notification, None, None)


def getColorTheme():

    try:
        tokens = dict(getDefault("PyDETokenColors"))
    except:
        tokens = {}
        print('no custom colors defined.\n')

    background = getDefaultColor("PyDEbackgroundColor")
    highlight  = getDefaultColor("PyDEHightLightColor")

    return {
        'background' : background,
        'highlight'  : highlight,
        'tokens'     : tokens,
    }


class ColorChangeObserver:

   def __init__(self):

       # setup a callback nsobject wrapper
       self.__callbackWrapper = VanillaCallbackWrapper(self._myAction)

       # get the default notification center
       N = NSNotificationCenter.defaultCenter()

       # add observer for `PyDEUserDefaultChanged` (when a font/color changed in the Preferences)
       N.addObserver_selector_name_object_(self.__callbackWrapper, "action:", "PyDEUserDefaultChanged", None)

   def _myAction(self, notification):
       print(notification)


class ColorThemesDialog:

    colorThemesFolder = os.path.join(os.getcwd(), 'themes')

    def __init__(self):
        self.w = FloatingWindow((246, 300), "CodeColors")
        x = y = p = 10
        self.w.colorThemesList = List(
            (x, y, -p, -p),
            sorted(self.colorThemes.keys()),
            selectionCallback=self.selectionCallback,
            allowsMultipleSelection=False,
            allowsEmptySelection=False)
        self.w.open()

    @property
    def colorThemes(self):
        return getColorThemes(self.colorThemesFolder)

    @property
    def colorTheme(self):
        i = self.w.colorThemesList.getSelection()[0]
        colorThemeName = sorted(self.colorThemes.keys())[i]
        return self.colorThemes[colorThemeName]

    def selectionCallback(self, sender):
        setColorTheme(self.colorTheme)


if __name__ == '__main__':

    ColorChangeObserver()
    ColorThemesDialog()
