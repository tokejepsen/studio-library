import maya.OpenMayaUI as omui
from studioqt import QtGui
from studioqt import QtCore
from studioqt import QtWidgets
try:
    from shiboken import wrapInstance
except Exception:
    from shiboken2 import wrapInstance

from .framerangemenu import FrameRangeMenu
from .framerangemenu import showFrameRangeMenu
from .modelpanelwidget import ModelPanelWidget
from .thumbnailcapturedialog import *

def mayaWindow():
    """
    :rtype: QMainWindow
    """
    mainWindowPtr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(mainWindowPtr), QtWidgets.QMainWindow)
