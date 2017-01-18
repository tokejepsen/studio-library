"""

Example:

    sf = SearchFilter("red AND apples")
    sf.match("Are red apples better than green apples")
    # True

    sf = SearchFilter("red AND apples")
    sf.match("Do cats like green apples")
    # False

    sf = SearchFilter("red OR apples")
    sf.setSpaceOperator(SearchFilter.Operator.OR)
    sf.match("Do cats like green apples")
    # True


Please see the search filter tests for more example.
"""
import re
from studioqt import QtCore

class SearchFilter(QtCore.QObject):
    searchChanged = QtCore.Signal()

    class Operator:
        OR = ' or '
        AND = ' and '

    def __init__(self, pattern, spaceOperator = Operator.AND):
        """
        :type pattern: str
        :type spaceOperator: SearchFilter.Operator
        """
        QtCore.QObject.__init__(self)
        self._matches = 0
        self._pattern = None
        self._resolvedPattern = None
        self._spaceOperator = spaceOperator
        self.setPattern(pattern)
        return

    def pattern(self):
        """
        Return the pattern for the search filter.

        :rtype: str
        """
        return self._pattern

    def setPattern(self, pattern):
        """
        Set the pattern for the search filter.

        :type pattern: str
        """
        self._pattern = pattern
        self._searchChanged()

    def _searchChanged(self):
        """
        Triggered when the search filter changes.

        :rtype: None
        """
        self.resolvePattern()
        self.searchChanged.emit()

    def resolvedPattern(self):
        """
        Return the resolved pattern.

        :rtype: str
        """
        return self._resolvedPattern

    def setResolvedPattern(self, resolvedPattern):
        """
        Set the resolved pattern.

        :type resolvedPattern: str
        :rtype: None
        """
        self._resolvedPattern = resolvedPattern

    def spaceOperator(self):
        """
        Return the operator for all white spaces in the pattern.

        :rtype: SearchFilter.Operator
        """
        return self._spaceOperator

    def setSpaceOperator(self, operator):
        """
        Set the operator for all white spaces in the pattern.

        :type: SearchFilter.Operator
        """
        self._spaceOperator = operator
        self._searchChanged()

    def settings(self):
        """
        Return the state of the search filter as a dict object.

        :rtype: dict
        """
        settings = {}
        settings['pattern'] = self.pattern()
        settings['spaceOperator'] = self.spaceOperator()
        return settings

    def setSettings(self, settings):
        """
        Set the state of the search filter from a dict object.

        :type settings: dict
        :rtype: None
        """
        pattern = settings.get('pattern', '')
        self.setPattern(pattern)
        spaceOperator = settings.get('spaceOperator', self.Operator.AND)
        self.setSpaceOperator(spaceOperator)

    def resolvePattern(self):
        """
        Resolve the pattern to speed up the match method.

        :rtype: None
        """
        pattern = self.pattern()
        spaceOperator = self.spaceOperator()
        pattern = pattern.strip()
        pattern = pattern.lower()
        pattern = re.sub(' +', ' ', pattern)
        pattern = pattern.replace(self.Operator.OR, '_OR_')
        pattern = pattern.replace(self.Operator.AND, '_AND_')
        pattern = pattern.replace(' ', spaceOperator)
        pattern = pattern.replace('_OR_', self.Operator.OR)
        pattern = pattern.replace('_AND_', self.Operator.AND)
        self.setResolvedPattern(pattern)

    def matches(self):
        """
        Return the number of matches from the last match.

        :rtype: int
        """
        return self._matches

    def match(self, text):
        """
        Match the given text to the resolved pattern.

        :type text: str
        :rtype: bool
        """
        match = False
        matches = 0
        pattern = self.resolvedPattern()
        groups = pattern.split(self.Operator.OR)
        for group in groups:
            match = True
            labels = [ label.lower() for label in group.split(self.Operator.AND) ]
            for label in labels:
                if label not in text.lower():
                    matches += 1
                    match = False
                    break
                matches += 1

            if match:
                break
            matches += 1

        if not match:
            matches = 0
        self._matches = matches
        return match
