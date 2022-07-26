# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.resize(425, 649)
        OptionsDialog.setMaximumSize(QtCore.QSize(505, 695))
        self.gridLayout = QtWidgets.QGridLayout(OptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(OptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(OptionsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.generalOptions = QtWidgets.QWidget()
        self.generalOptions.setMaximumSize(QtCore.QSize(483, 626))
        self.generalOptions.setObjectName("generalOptions")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.generalOptions)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.generalLayout = QtWidgets.QGridLayout()
        self.generalLayout.setObjectName("generalLayout")
        self.genBehaviorBox = QtWidgets.QGroupBox(self.generalOptions)
        self.genBehaviorBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.genBehaviorBox.setFlat(True)
        self.genBehaviorBox.setObjectName("genBehaviorBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.genBehaviorBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.genBehaviorLayout = QtWidgets.QVBoxLayout()
        self.genBehaviorLayout.setObjectName("genBehaviorLayout")
        self.gen_showAnswer = QtWidgets.QCheckBox(self.genBehaviorBox)
        self.gen_showAnswer.setObjectName("gen_showAnswer")
        self.genBehaviorLayout.addWidget(self.gen_showAnswer)
        self.gen_cbTimed = QtWidgets.QCheckBox(self.genBehaviorBox)
        self.gen_cbTimed.setObjectName("gen_cbTimed")
        self.genBehaviorLayout.addWidget(self.gen_cbTimed)
        self.gen_timedAmount = QtWidgets.QSpinBox(self.genBehaviorBox)
        self.gen_timedAmount.setEnabled(False)
        self.gen_timedAmount.setMinimumSize(QtCore.QSize(0, 0))
        self.gen_timedAmount.setMinimum(10)
        self.gen_timedAmount.setMaximum(1000000000)
        self.gen_timedAmount.setSingleStep(1)
        self.gen_timedAmount.setProperty("value", 60)
        self.gen_timedAmount.setObjectName("gen_timedAmount")
        self.genBehaviorLayout.addWidget(self.gen_timedAmount)
        self.gridLayout_8.addLayout(self.genBehaviorLayout, 0, 0, 1, 1)
        self.generalLayout.addWidget(self.genBehaviorBox, 0, 0, 1, 1)
        self.genAnswersBox = QtWidgets.QGroupBox(self.generalOptions)
        self.genAnswersBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.genAnswersBox.setFlat(True)
        self.genAnswersBox.setObjectName("genAnswersBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.genAnswersBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.genAnswersLayout = QtWidgets.QVBoxLayout()
        self.genAnswersLayout.setObjectName("genAnswersLayout")
        self.gen_groupSizeLabel = QtWidgets.QLabel(self.genAnswersBox)
        self.gen_groupSizeLabel.setWhatsThis("")
        self.gen_groupSizeLabel.setObjectName("gen_groupSizeLabel")
        self.genAnswersLayout.addWidget(self.gen_groupSizeLabel)
        self.gen_groupSize = QtWidgets.QSpinBox(self.genAnswersBox)
        self.gen_groupSize.setMinimumSize(QtCore.QSize(0, 0))
        self.gen_groupSize.setToolTip("")
        self.gen_groupSize.setWhatsThis("")
        self.gen_groupSize.setMinimum(5)
        self.gen_groupSize.setMaximum(200)
        self.gen_groupSize.setSingleStep(5)
        self.gen_groupSize.setProperty("value", 20)
        self.gen_groupSize.setObjectName("gen_groupSize")
        self.genAnswersLayout.addWidget(self.gen_groupSize)
        self.gen_doTrueRandom = QtWidgets.QCheckBox(self.genAnswersBox)
        self.gen_doTrueRandom.setObjectName("gen_doTrueRandom")
        self.genAnswersLayout.addWidget(self.gen_doTrueRandom)
        self.gen_cbDoRevisit = QtWidgets.QCheckBox(self.genAnswersBox)
        self.gen_cbDoRevisit.setObjectName("gen_cbDoRevisit")
        self.genAnswersLayout.addWidget(self.gen_cbDoRevisit)
        self.gen_revisitStepsLabel = QtWidgets.QLabel(self.genAnswersBox)
        self.gen_revisitStepsLabel.setObjectName("gen_revisitStepsLabel")
        self.genAnswersLayout.addWidget(self.gen_revisitStepsLabel)
        self.gen_revisitSteps = QtWidgets.QSpinBox(self.genAnswersBox)
        self.gen_revisitSteps.setEnabled(False)
        self.gen_revisitSteps.setMinimumSize(QtCore.QSize(0, 0))
        self.gen_revisitSteps.setObjectName("gen_revisitSteps")
        self.genAnswersLayout.addWidget(self.gen_revisitSteps)
        self.gridLayout_9.addLayout(self.genAnswersLayout, 0, 0, 1, 1)
        self.generalLayout.addWidget(self.genAnswersBox, 1, 0, 1, 1)
        self.genSoundsBox = QtWidgets.QGroupBox(self.generalOptions)
        self.genSoundsBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.genSoundsBox.setFlat(True)
        self.genSoundsBox.setObjectName("genSoundsBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.genSoundsBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.genSoundsLayout = QtWidgets.QVBoxLayout()
        self.genSoundsLayout.setObjectName("genSoundsLayout")
        self.gen_cbDoSounds = QtWidgets.QCheckBox(self.genSoundsBox)
        self.gen_cbDoSounds.setChecked(True)
        self.gen_cbDoSounds.setObjectName("gen_cbDoSounds")
        self.genSoundsLayout.addWidget(self.gen_cbDoSounds)
        self.gen_SoundVolumeLabel = QtWidgets.QLabel(self.genSoundsBox)
        self.gen_SoundVolumeLabel.setObjectName("gen_SoundVolumeLabel")
        self.genSoundsLayout.addWidget(self.gen_SoundVolumeLabel)
        self.gen_soundVolume = QtWidgets.QSlider(self.genSoundsBox)
        self.gen_soundVolume.setOrientation(QtCore.Qt.Horizontal)
        self.gen_soundVolume.setObjectName("gen_soundVolume")
        self.genSoundsLayout.addWidget(self.gen_soundVolume)
        self.gridLayout_10.addLayout(self.genSoundsLayout, 0, 0, 1, 1)
        self.generalLayout.addWidget(self.genSoundsBox, 2, 0, 1, 1)
        self.genDisplayBox = QtWidgets.QGroupBox(self.generalOptions)
        self.genDisplayBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.genDisplayBox.setFlat(True)
        self.genDisplayBox.setObjectName("genDisplayBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.genDisplayBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.genDisplayLayout = QtWidgets.QVBoxLayout()
        self.genDisplayLayout.setObjectName("genDisplayLayout")
        self.gen_sortByLabel = QtWidgets.QLabel(self.genDisplayBox)
        self.gen_sortByLabel.setObjectName("gen_sortByLabel")
        self.genDisplayLayout.addWidget(self.gen_sortByLabel)
        self.gen_sortByCb = QtWidgets.QComboBox(self.genDisplayBox)
        self.gen_sortByCb.setObjectName("gen_sortByCb")
        self.genDisplayLayout.addWidget(self.gen_sortByCb)
        self.genFieldsLabel = QtWidgets.QLabel(self.genDisplayBox)
        self.genFieldsLabel.setObjectName("genFieldsLabel")
        self.genDisplayLayout.addWidget(self.genFieldsLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gen_fieldsCb = QtWidgets.QComboBox(self.genDisplayBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_fieldsCb.sizePolicy().hasHeightForWidth())
        self.gen_fieldsCb.setSizePolicy(sizePolicy)
        self.gen_fieldsCb.setObjectName("gen_fieldsCb")
        self.horizontalLayout.addWidget(self.gen_fieldsCb)
        self.gen_editFieldButton = QtWidgets.QPushButton(self.genDisplayBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_editFieldButton.sizePolicy().hasHeightForWidth())
        self.gen_editFieldButton.setSizePolicy(sizePolicy)
        self.gen_editFieldButton.setMinimumSize(QtCore.QSize(80, 0))
        self.gen_editFieldButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.gen_editFieldButton.setObjectName("gen_editFieldButton")
        self.horizontalLayout.addWidget(self.gen_editFieldButton)
        self.genDisplayLayout.addLayout(self.horizontalLayout)
        self.gridLayout_11.addLayout(self.genDisplayLayout, 0, 0, 1, 1)
        self.generalLayout.addWidget(self.genDisplayBox, 3, 0, 1, 1)
        self.gridLayout_17.addLayout(self.generalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.generalOptions, "")
        self.listOptions = QtWidgets.QWidget()
        self.listOptions.setObjectName("listOptions")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.listOptions)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_label = QtWidgets.QLabel(self.listOptions)
        self.list_label.setObjectName("list_label")
        self.verticalLayout.addWidget(self.list_label)
        self.list_topLayout = QtWidgets.QHBoxLayout()
        self.list_topLayout.setObjectName("list_topLayout")
        self.list_fieldSelCo = QtWidgets.QComboBox(self.listOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_fieldSelCo.sizePolicy().hasHeightForWidth())
        self.list_fieldSelCo.setSizePolicy(sizePolicy)
        self.list_fieldSelCo.setObjectName("list_fieldSelCo")
        self.list_topLayout.addWidget(self.list_fieldSelCo)
        self.list_addButton = QtWidgets.QPushButton(self.listOptions)
        self.list_addButton.setObjectName("list_addButton")
        self.list_topLayout.addWidget(self.list_addButton)
        self.list_removeButton = QtWidgets.QPushButton(self.listOptions)
        self.list_removeButton.setObjectName("list_removeButton")
        self.list_topLayout.addWidget(self.list_removeButton)
        self.verticalLayout.addLayout(self.list_topLayout)
        self.list_list = QtWidgets.QListWidget(self.listOptions)
        self.list_list.setObjectName("list_list")
        self.verticalLayout.addWidget(self.list_list)
        self.list_bottomLayout = QtWidgets.QHBoxLayout()
        self.list_bottomLayout.setObjectName("list_bottomLayout")
        self.list_moveUpButton = QtWidgets.QPushButton(self.listOptions)
        self.list_moveUpButton.setObjectName("list_moveUpButton")
        self.list_bottomLayout.addWidget(self.list_moveUpButton)
        self.list_moveDownButton = QtWidgets.QPushButton(self.listOptions)
        self.list_moveDownButton.setObjectName("list_moveDownButton")
        self.list_bottomLayout.addWidget(self.list_moveDownButton)
        self.list_setFrontButton = QtWidgets.QPushButton(self.listOptions)
        self.list_setFrontButton.setObjectName("list_setFrontButton")
        self.list_bottomLayout.addWidget(self.list_setFrontButton)
        self.verticalLayout.addLayout(self.list_bottomLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.listOptions, "")
        self.multipleChoiceOptions = QtWidgets.QWidget()
        self.multipleChoiceOptions.setObjectName("multipleChoiceOptions")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.multipleChoiceOptions)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mcLayout = QtWidgets.QVBoxLayout()
        self.mcLayout.setObjectName("mcLayout")
        self.mcBehaviorBox = QtWidgets.QGroupBox(self.multipleChoiceOptions)
        self.mcBehaviorBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mcBehaviorBox.setFlat(True)
        self.mcBehaviorBox.setCheckable(False)
        self.mcBehaviorBox.setChecked(False)
        self.mcBehaviorBox.setObjectName("mcBehaviorBox")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.mcBehaviorBox)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.mcBehaviorLayout = QtWidgets.QVBoxLayout()
        self.mcBehaviorLayout.setObjectName("mcBehaviorLayout")
        self.mc_cbConfirm = QtWidgets.QCheckBox(self.mcBehaviorBox)
        self.mc_cbConfirm.setObjectName("mc_cbConfirm")
        self.mcBehaviorLayout.addWidget(self.mc_cbConfirm)
        self.gridLayout_12.addLayout(self.mcBehaviorLayout, 0, 0, 1, 1)
        self.mcLayout.addWidget(self.mcBehaviorBox)
        self.mcDisplayBox = QtWidgets.QGroupBox(self.multipleChoiceOptions)
        self.mcDisplayBox.setFlat(True)
        self.mcDisplayBox.setObjectName("mcDisplayBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.mcDisplayBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mcDisplayLayout = QtWidgets.QVBoxLayout()
        self.mcDisplayLayout.setObjectName("mcDisplayLayout")
        self.mc_questionFontsizeLabel = QtWidgets.QLabel(self.mcDisplayBox)
        self.mc_questionFontsizeLabel.setObjectName("mc_questionFontsizeLabel")
        self.mcDisplayLayout.addWidget(self.mc_questionFontsizeLabel)
        self.mc_questionFontSize = QtWidgets.QSpinBox(self.mcDisplayBox)
        self.mc_questionFontSize.setObjectName("mc_questionFontSize")
        self.mcDisplayLayout.addWidget(self.mc_questionFontSize)
        self.mc_answerFontSizeLabel = QtWidgets.QLabel(self.mcDisplayBox)
        self.mc_answerFontSizeLabel.setObjectName("mc_answerFontSizeLabel")
        self.mcDisplayLayout.addWidget(self.mc_answerFontSizeLabel)
        self.mc_answerFontSize = QtWidgets.QSpinBox(self.mcDisplayBox)
        self.mc_answerFontSize.setObjectName("mc_answerFontSize")
        self.mcDisplayLayout.addWidget(self.mc_answerFontSize)
        self.gridLayout_4.addLayout(self.mcDisplayLayout, 0, 0, 1, 1)
        self.mcLayout.addWidget(self.mcDisplayBox)
        self.gridLayout_2.addLayout(self.mcLayout, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.multipleChoiceOptions, "")
        self.matchingOptions = QtWidgets.QWidget()
        self.matchingOptions.setObjectName("matchingOptions")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.matchingOptions)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.maLayout = QtWidgets.QGridLayout()
        self.maLayout.setObjectName("maLayout")
        self.maDisplayBox = QtWidgets.QGroupBox(self.matchingOptions)
        self.maDisplayBox.setFlat(True)
        self.maDisplayBox.setObjectName("maDisplayBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.maDisplayBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.maDisplayLayout = QtWidgets.QVBoxLayout()
        self.maDisplayLayout.setObjectName("maDisplayLayout")
        self.ma_answerFontSizeLabel = QtWidgets.QLabel(self.maDisplayBox)
        self.ma_answerFontSizeLabel.setObjectName("ma_answerFontSizeLabel")
        self.maDisplayLayout.addWidget(self.ma_answerFontSizeLabel)
        self.ma_answerFontSize = QtWidgets.QSpinBox(self.maDisplayBox)
        self.ma_answerFontSize.setObjectName("ma_answerFontSize")
        self.maDisplayLayout.addWidget(self.ma_answerFontSize)
        self.gridLayout_13.addLayout(self.maDisplayLayout, 0, 0, 1, 1)
        self.maLayout.addWidget(self.maDisplayBox, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.maLayout, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.matchingOptions, "")
        self.writeTheAnswerOptions = QtWidgets.QWidget()
        self.writeTheAnswerOptions.setObjectName("writeTheAnswerOptions")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.writeTheAnswerOptions)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.waLayout = QtWidgets.QVBoxLayout()
        self.waLayout.setObjectName("waLayout")
        self.waInputBox = QtWidgets.QGroupBox(self.writeTheAnswerOptions)
        self.waInputBox.setFlat(True)
        self.waInputBox.setObjectName("waInputBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.waInputBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.waInputLayout = QtWidgets.QVBoxLayout()
        self.waInputLayout.setObjectName("waInputLayout")
        self.wr_cbKeyboard = QtWidgets.QCheckBox(self.waInputBox)
        self.wr_cbKeyboard.setChecked(True)
        self.wr_cbKeyboard.setObjectName("wr_cbKeyboard")
        self.waInputLayout.addWidget(self.wr_cbKeyboard)
        self.wr_virtualKeyboardTypeLabel = QtWidgets.QLabel(self.waInputBox)
        self.wr_virtualKeyboardTypeLabel.setObjectName("wr_virtualKeyboardTypeLabel")
        self.waInputLayout.addWidget(self.wr_virtualKeyboardTypeLabel)
        self.wr_coKeyboardType = QtWidgets.QComboBox(self.waInputBox)
        self.wr_coKeyboardType.setObjectName("wr_coKeyboardType")
        self.wr_coKeyboardType.addItem("")
        self.waInputLayout.addWidget(self.wr_coKeyboardType)
        self.gridLayout_5.addLayout(self.waInputLayout, 0, 0, 1, 1)
        self.waLayout.addWidget(self.waInputBox)
        self.waDisplayBox = QtWidgets.QGroupBox(self.writeTheAnswerOptions)
        self.waDisplayBox.setFlat(True)
        self.waDisplayBox.setObjectName("waDisplayBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.waDisplayBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.waDisplayLayout = QtWidgets.QVBoxLayout()
        self.waDisplayLayout.setObjectName("waDisplayLayout")
        self.wr_questionFontSizeLabel = QtWidgets.QLabel(self.waDisplayBox)
        self.wr_questionFontSizeLabel.setObjectName("wr_questionFontSizeLabel")
        self.waDisplayLayout.addWidget(self.wr_questionFontSizeLabel)
        self.wr_questionFontSize = QtWidgets.QSpinBox(self.waDisplayBox)
        self.wr_questionFontSize.setObjectName("wr_questionFontSize")
        self.waDisplayLayout.addWidget(self.wr_questionFontSize)
        self.gridLayout_6.addLayout(self.waDisplayLayout, 0, 0, 1, 1)
        self.waLayout.addWidget(self.waDisplayBox)
        self.gridLayout_15.addLayout(self.waLayout, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.writeTheAnswerOptions, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(OptionsDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(OptionsDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(OptionsDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)

    def retranslateUi(self, OptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        OptionsDialog.setWindowTitle(_translate("OptionsDialog", "Dialog"))
        self.genBehaviorBox.setTitle(_translate("OptionsDialog", "Behavior"))
        self.gen_showAnswer.setText(_translate("OptionsDialog", "Show Answer Before Next Question"))
        self.gen_cbTimed.setText(_translate("OptionsDialog", "Timer (seconds)"))
        self.genAnswersBox.setTitle(_translate("OptionsDialog", "Cards"))
        self.gen_groupSizeLabel.setText(_translate("OptionsDialog", "Group Size"))
        self.gen_doTrueRandom.setText(_translate("OptionsDialog", "True Random"))
        self.gen_cbDoRevisit.setText(_translate("OptionsDialog", "Revisit Wrong Answers"))
        self.gen_revisitStepsLabel.setText(_translate("OptionsDialog", "Revisit Steps"))
        self.genSoundsBox.setTitle(_translate("OptionsDialog", "Sounds"))
        self.gen_cbDoSounds.setText(_translate("OptionsDialog", "Play Correct / Incorrect Sounds"))
        self.gen_SoundVolumeLabel.setText(_translate("OptionsDialog", "Sound Volume"))
        self.genDisplayBox.setTitle(_translate("OptionsDialog", "Fields"))
        self.gen_sortByLabel.setText(_translate("OptionsDialog", "Sort By"))
        self.genFieldsLabel.setText(_translate("OptionsDialog", "Fields Options"))
        self.gen_editFieldButton.setText(_translate("OptionsDialog", "Edit.."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalOptions), _translate("OptionsDialog", "General"))
        self.list_label.setText(_translate("OptionsDialog", "List Columns"))
        self.list_addButton.setText(_translate("OptionsDialog", "Add"))
        self.list_removeButton.setText(_translate("OptionsDialog", "Remove"))
        self.list_moveUpButton.setText(_translate("OptionsDialog", "Move Up"))
        self.list_moveDownButton.setText(_translate("OptionsDialog", "Move Down"))
        self.list_setFrontButton.setText(_translate("OptionsDialog", "Set Front/Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.listOptions), _translate("OptionsDialog", "List"))
        self.mcBehaviorBox.setTitle(_translate("OptionsDialog", "Behavior"))
        self.mc_cbConfirm.setText(_translate("OptionsDialog", "Always Confirm Answer"))
        self.mcDisplayBox.setTitle(_translate("OptionsDialog", "Display"))
        self.mc_questionFontsizeLabel.setText(_translate("OptionsDialog", "Question Font Size"))
        self.mc_answerFontSizeLabel.setText(_translate("OptionsDialog", "Answer Button Font Size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multipleChoiceOptions), _translate("OptionsDialog", "Multiple Choice"))
        self.maDisplayBox.setTitle(_translate("OptionsDialog", "Display"))
        self.ma_answerFontSizeLabel.setText(_translate("OptionsDialog", "Answer Button Font Size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.matchingOptions), _translate("OptionsDialog", "Matching"))
        self.waInputBox.setTitle(_translate("OptionsDialog", "Input"))
        self.wr_cbKeyboard.setText(_translate("OptionsDialog", "Show virtual keyboard"))
        self.wr_virtualKeyboardTypeLabel.setText(_translate("OptionsDialog", "Virtual Keyboard Type"))
        self.wr_coKeyboardType.setItemText(0, _translate("OptionsDialog", "Japanese - Hiragana"))
        self.waDisplayBox.setTitle(_translate("OptionsDialog", "Display"))
        self.wr_questionFontSizeLabel.setText(_translate("OptionsDialog", "Question Font Size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.writeTheAnswerOptions), _translate("OptionsDialog", "Write the Answer"))
