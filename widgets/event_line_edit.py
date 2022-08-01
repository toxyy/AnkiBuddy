from aqt.qt import (
    QLineEdit,
    QKeyEvent,
    QInputMethodEvent,
)

# Line edit that passes key press events to its parent
class EventLineEdit(QLineEdit):
    def keyPressEvent(self, event: QKeyEvent):
        if self.parentWidget():
            self.parentWidget().keyPressEvent(event)
        super().keyPressEvent(event)
        
    def inputMethodEvent(self, event: QInputMethodEvent):
        if self.parentWidget():
            self.parentWidget().inputMethodEvent(event)
        super().inputMethodEvent(event)