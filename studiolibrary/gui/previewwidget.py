from studioqt import QtWidgets
import studioqt
__all__ = ['PreviewWidget']

class PreviewWidget(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        studioqt.loadUi(self)
