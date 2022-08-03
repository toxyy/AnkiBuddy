# Copyright: Axel Moreen, 2022
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
Contains BTableWidgetItem, which is a modified Label used
in the List View to dynamically show and hide the text.

It was originally a subclass of QWidgetItem, so could use
refactoring to a name that makes more sense. 
"""
from aqt.qt import Qt, QLabel

# Table widget (originally used to subclass QWidgetItem, but moved to QLabel for rich text)
# - Can hide and show text without changing the layout of the table.
class BTableWidgetItem(QLabel):
    def __init__(self, text: str):
        """Instantiate custom table widget item with text.

        Args:
            text (str): Text for the table cell.
        """
        text = text.strip()
        super().__init__(text)
        self._text = text
        self._isBlank = False

        self.setTextFormat(Qt.RichText)

    def hide_value(self):
        """Hide the value in this cell."""
        self._isBlank = True
        self.setText("")

    def show_value(self):
        """Show the value in this cell."""
        self._isBlank = False
        self.setText(self._text)
