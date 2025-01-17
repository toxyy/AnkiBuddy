# Copyright: Axel Moreen, 2022
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
Contains the Write the Answer Widget - widget for a written
question.

Widget manages its own state and passes signals to its parent. The layout is
also generated from code in this class. See ./question_widget.py for more info
about the question widgets.
"""

from .question_widget import QuestionWidget
from .event_line_edit import EventLineEdit
from .question_label import QuestionLabel

from ..keyboards import KeyboardView, KB_JAPANESE_HIRAGANA

from aqt.qt import (
    QVBoxLayout,
    QHBoxLayout,
    Qt,
    QLabel,
    QPushButton,
    QTimer,
    QKeyEvent,
    QInputMethodEvent,
)
from aqt import mw

from ..style import confirm_button_style


class WriteTheAnswerWidget(QuestionWidget):
    """Write the answer widget. Shows a question label at the top, and has
    the user write the answer in the LineEdit below.

    Currently there is also support for Japanese learners to use a virtual
    keyboard to help learn to type there, but it is incomplete - could be
    extended to more languages.

    See QuestionWidget for more info.
    """
    def load(self):
        """Load this question widget."""
        self.conf = self.model.options_store.get_homework_config(
            self.model.note_store.deck_name
        )
        self.layout = QVBoxLayout(self)
        self.questionLabel = QuestionLabel(self)
        self.handle_font(
            self.questionLabel,
            self.conf["write_question_size"],
            self.options["question_field"],
        )
        self.questionLabel.setText(self.options["question"])
        # self.questionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.questionLabel.setTextFormat(Qt.TextFormat.RichText)

        # self.set_font_size(self.questionLabel, 30)

        self.ansLayout = QHBoxLayout()
        self.ansBox = EventLineEdit()
        self.ansBox.setFixedHeight(60)
        self.model.last_card = self.options["card_ind"]
        self.ansBox.returnPressed.connect(self.submit_callback)
        self.set_font_size(self.ansBox, 20)
        # self.set_font_size(self.ansBox, self.conf["write_question_size"])
        # self.handle_font(self.ansBox, self.conf["write_question_size"],
        #    self.options["question_field"])
        self.boxTypeLabel = QLabel(self.ansBox)
        self.boxTypeLabel.setText("(" + self.options["answer_field"] + ")")

        self.set_font_size(self.boxTypeLabel, 9)
        self.ansSubmit = QPushButton()
        self.ansSubmit.setFixedHeight(60)
        self.ansSubmit.setText("Submit")
        self.ansSubmit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        # self.ansSubmit.setAutoDefault(True)
        self.set_font_size(self.ansSubmit, 15)
        self.ansSubmit.setStyleSheet(confirm_button_style)
        self.ansSubmit.clicked.connect(self.submit_callback)
        self.ansLayout.addWidget(self.ansBox)
        self.ansLayout.addWidget(self.ansSubmit)
        self.layout.addWidget(self.questionLabel)
        self.layout.addLayout(self.ansLayout)
        self.ansBox.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.show_keyboard = self.conf["write_show_keyboard"]
        if self.show_keyboard:
            if not hasattr(mw, "_bKeyboard"):
                if self.conf["write_keyboard_type"] == 0:
                    mw._bKeyboard = KeyboardView(
                        translation=KB_JAPANESE_HIRAGANA)

            if not mw._bKeyboard.isVisible():
                mw._bKeyboard.showNormal()
            mw._bKeyboard.link_field(self.ansBox)

        QTimer.singleShot(
            0, lambda: self.ansBox.setFocus()
        )  # ez hack to make the ans box auto-focus.

    def submit_callback(self):
        """Return was pressed or the submit button was pressed."""
        text = self.ansBox.text()
        self.questionAnswered.emit(
            text.casefold() == self.options["answer"].casefold(), False
        )

    # sending key events to virtual keyboard to display key strokes
    def on_key(self, event: QKeyEvent):
        """Handle key event."""
        if self.show_keyboard:
            # TODO: support caps shift etc
            if len(event.text()) > 0:
                mw._bKeyboard.on_key(event.text())

    # sending ime events to virtual keyboard to display key strokes
    def inputMethodEvent(self, event: QInputMethodEvent):
        """Handle IME events."""
        if self.show_keyboard:
            mw._bKeyboard.on_key(event.preeditString()[-1:])

    def keyPressEvent(self, event: QKeyEvent):
        """Handle key event.

        #TODO: get rid of QuestionWidget.on_key() entirely?
        """
        self.on_key(event)

    def get_answer(self) -> str:
        """Return answer string."""
        return self.options["answer"]
