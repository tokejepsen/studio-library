from studioqt import QtGui
from studioqt import QtCore
from studioqt import QtWidgets
__all__ = ['SeparatorAction']

class Line(QtWidgets.QFrame):
    pass


class SeparatorWidgetAction(QtWidgets.QFrame):
    pass


class SeparatorAction(QtWidgets.QWidgetAction):

    def __init__(self, label = '', parent = None):
        """
        :type parent: QtWidgets.QMenu
        """
        QtWidgets.QWidgetAction.__init__(self, parent)
        self._widget = SeparatorWidgetAction(parent)
        self._label = QtWidgets.QLabel(self._widget)
        self._label.setText(label)
        self._line = Line(self._widget)
        self._line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    def setText(self, text):
        """
        Set the text of the separator.

        :type text: str
        :rtype: None
        """
        self.label().setText(text)

    def widget(self):
        """
        Return the QFrame object.

        :rtype: Frame
        """
        return self._widget

    def label(self):
        """
        Return the QLabel object.

        :rtype: QtWidgets.QLabel
        """
        return self._label

    def line(self):
        """
        Return the line widget.

        :rtype: Line
        """
        return self._line

    def createWidget(self, menu):
        """
        This method is called by the QWidgetAction base class.

        :type parent: QtWidgets.QMenu
        """
        actionWidget = self.widget()
        actionLayout = QtWidgets.QHBoxLayout(actionWidget)
        actionLayout.setContentsMargins(0, 0, 0, 0)
        actionLayout.addWidget(self.label())
        actionLayout.addWidget(self.line())
        actionWidget.setLayout(actionLayout)
        return actionWidget
