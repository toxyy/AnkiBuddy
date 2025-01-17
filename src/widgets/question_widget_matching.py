# Copyright: Axel Moreen, 2022
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
Contains the Matching Widget - widget for a matching
question.

Widget manages its own state and passes signals to its parent. The layout is
also generated from code in this class. See ./question_widget.py for more info
about the question widgets.
"""
from .question_widget import QuestionWidget
from .answer_button import AnswerButton

from aqt.qt import QVBoxLayout, QGridLayout, Qt, QMouseEvent

import random
from ..style import button_style, button_style_custom_border


class MatchingWidget(QuestionWidget):
    """Matching widget. Shows the user two columns of buttons,
    in a randomized order. The user has to select one button on
    the left and one button on the right in order to match the
    related cards. 

    When the program is meant to show the correct answer, the
    widget will choose random colors to highlight the two sides with
    matching colors. Currently this could be improved to be color-blind
    friendly.
    """
    def load(self):
        """Load the matching widget."""
        self.conf = self.model.options_store.get_homework_config(
            self.model.note_store.deck_name
        )
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addLayout(self.left_layout, 0, 0, 10, 1)
        self.gridLayout.addLayout(self.right_layout, 0, 1, 10, 1)
        # build randomized mapping
        self.size = len(self.options["questions"])

        self.order = [i for i in range(self.size)]
        random.shuffle(self.order)

        # assume len(questions) = len(answers)
        self.l_buttons = []
        self.r_buttons = []
        for i in range(self.size):
            buttonL = AnswerButton(text=self.options["questions"][i],
                                   parent=self)
            buttonL.clicked.connect(lambda ch, i=i: self.left_callback(i))
            buttonL.setStyleSheet(button_style)
            buttonL.setAutoDefault(False)
            buttonL.setFocusPolicy(Qt.FocusPolicy.NoFocus)

            self.handle_font(
                buttonL,
                self.conf["matching_answer_size"],
                self.options["question_field"],
            )
            self.handle_field_sound(
                buttonL, self.options["question_field"],
                self.options["cards"][i]
            )
            self.l_buttons.append(buttonL)
            self.left_layout.addWidget(self.l_buttons[i])

            buttonR = AnswerButton(
                text=self.options["answers"][self.order[i]], parent=self
            )
            buttonR.clicked.connect(lambda ch, i=i: self.right_callback(i))
            buttonR.setStyleSheet(button_style)
            buttonR.setAutoDefault(False)
            buttonR.setFocusPolicy(Qt.FocusPolicy.NoFocus)

            self.handle_font(
                buttonR, self.conf["matching_answer_size"],
                self.options["answer_field"]
            )
            self.handle_field_sound(
                buttonR,
                self.options["answer_field"],
                self.options["cards"][self.order[i]],
            )
            self.r_buttons.append(buttonR)
            self.right_layout.addWidget(self.r_buttons[i])

        self.sel_left = -1
        self.sel_right = -1
        self.answered = []

    def unsel_buttons(self):
        """Helper method to "reset" the buttons so nothing is selected."""
        if self.sel_left > -1:
            buttonL = self.l_buttons[self.sel_left]
            buttonL.setEnabled(True)
            self.sel_left = -1
        if self.sel_right > -1:
            buttonR = self.r_buttons[self.sel_right]
            buttonR.setEnabled(True)
            self.sel_right = -1

    def left_callback(self, i: int):
        """Callback for the left side of buttons to compare with the right.
        The button index increases down the left side from 0 -> number of
        answers.
        Args:
            i (int): The button index that was pressed.
        """
        button = self.l_buttons[i]
        button.setEnabled(False)
        # try match first
        if self.sel_right > -1:
            self.sel_left = i
            self.model.last_card = self.options["cards_inds"][i]
            if self.order[self.sel_right] == i:  # correct
                self.answered.append(i)
                button2 = self.r_buttons[self.sel_right]
                button.setFlat(True)
                button2.setFlat(True)
                button.setEnabled(False)
                button2.setEnabled(False)
                self.sel_left = -1
                self.sel_right = -1

                self.questionAnswered.emit(
                    True, len(self.answered) < self.size)

            else:
                self.questionAnswered.emit(False, True)
                self.unsel_buttons()

        # right is not selected
        else:
            if self.sel_left > -1:
                self.l_buttons[self.sel_left].setEnabled(True)
            self.sel_left = i

    def right_callback(self, i: int):
        """Callback for the right side of buttons to compare with the left.
        The button index increases down the right side from 0 -> number of
        answers.
        Args:
            i (int): The button index that was pressed.
        """
        button = self.r_buttons[i]
        button.setEnabled(False)
        # try match
        if self.sel_left > -1:
            self.sel_right = i
            self.model.last_card = self.options["cards_inds"][self.order[i]]
            if self.order[i] == self.sel_left:  # correct
                self.answered.append(self.sel_left)
                button2 = self.l_buttons[self.sel_left]
                button.setFlat(True)
                button2.setFlat(True)
                button.setEnabled(False)
                button2.setEnabled(False)
                self.sel_left = -1
                self.sel_right = -1

                self.questionAnswered.emit(
                    True, len(self.answered) < self.size)
            else:
                self.questionAnswered.emit(False, True)
                self.unsel_buttons()

        # left is not selected
        else:
            if self.sel_right > -1:
                self.r_buttons[self.sel_right].setEnabled(True)
            self.sel_right = i

    def mousePressEvent(self, event: QMouseEvent):
        """Mouse press event, use this to clear the current selection of
        buttons.
        Since the event is called here, it must have not been handled by one
        of the child widgets
        (i.e. it wasn't handled by a button).
        """
        super().mousePressEvent(event)
        self.unsel_buttons()

    def show_answer(self):
        """Visually display the correct answers for matching by
        making the left and right button the same color.

        Currently, this uses random colors some distance apart,
        which may not be optimal or color-blind friendly at all. There is also
        no guarantee that the color may not accidentally blend in with the
        parent layout's background, etc.

        This behavior is "fine" for now, but it could be improved
        significantly. Perhaps drawing lines from button to button would be
        the most color-friendly improvement.
        """
        used_bgcols = []
        for i in range(len(self.l_buttons)):
            buttonL = self.l_buttons[self.order[i]]
            buttonR = self.r_buttons[i]

            # pick a color
            def r():
                return random.randint(0, 255)

            # try to avoid similar colors...
            def d(col1, col2, i):  # square dist fn
                return (col1[i] - col2[i]) ** 2

            su_sq = (
                lambda col1, col2: d(col1, col2, 0)
                + d(col1, col2, 1)
                + d(col1, col2, 2)
            )
            min_sq_dist = 11000  # like +- 30 diff per color.

            def valid_col(col, col_array):
                for other in col_array:
                    if su_sq(col, other) < min_sq_dist:
                        return False
                return True

            bgcol_pick = (r(), r(), r())
            i = 0
            while not valid_col(bgcol_pick, used_bgcols):
                bgcol_pick = (r(), r(), r())
                i += 1
                min_sq_dist -= 100
                if i > 50:
                    break  # preventing infinite recursion here

            used_bgcols.append(bgcol_pick)
            col = "#%02X%02X%02X" % bgcol_pick

            buttonL.setStyleSheet(button_style_custom_border % col)
            buttonR.setStyleSheet(button_style_custom_border % col)
            buttonL.setFlat(False)
            buttonR.setFlat(False)
            buttonL.setEnabled(True)
            buttonR.setEnabled(True)
            buttonL.clicked.disconnect()
            buttonR.clicked.disconnect()
            buttonL.setCheckable(False)
            buttonR.setCheckable(False)
            buttonL.setChecked(False)
            buttonR.setChecked(False)
