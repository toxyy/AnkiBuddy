# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/field_options.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from aqt.qt import *


class Ui_FieldOptions(object):
    def setupUi(self, FieldOptions):
        FieldOptions.setObjectName("FieldOptions")
        FieldOptions.resize(388, 305)
        self.gridLayout = QGridLayout(FieldOptions)
        self.gridLayout.setObjectName("gridLayout")
        self.fieldName = QLabel(FieldOptions)
        font = QFont()
        font.setPointSize(12)
        self.fieldName.setFont(font)
        self.fieldName.setObjectName("fieldName")
        self.gridLayout.addWidget(self.fieldName, 0, 0, 1, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(FieldOptions)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fontTypeBox = QFontComboBox(FieldOptions)
        self.fontTypeBox.setObjectName("fontTypeBox")
        self.verticalLayout.addWidget(self.fontTypeBox)
        self.label_3 = QLabel(FieldOptions)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.fontSizeOffsetBox = QSpinBox(FieldOptions)
        self.fontSizeOffsetBox.setMinimum(-15)
        self.fontSizeOffsetBox.setMaximum(15)
        self.fontSizeOffsetBox.setObjectName("fontSizeOffsetBox")
        self.verticalLayout.addWidget(self.fontSizeOffsetBox)
        self.label_4 = QLabel(FieldOptions)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.fieldAudioBox = QComboBox(FieldOptions)
        self.fieldAudioBox.setObjectName("fieldAudioBox")
        self.fieldAudioBox.addItem("")
        self.verticalLayout.addWidget(self.fieldAudioBox)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.buttonBox = QDialogButtonBox(FieldOptions)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(FieldOptions)
        self.buttonBox.accepted.connect(FieldOptions.accept) # type: ignore
        self.buttonBox.rejected.connect(FieldOptions.reject) # type: ignore
        QMetaObject.connectSlotsByName(FieldOptions)

    def retranslateUi(self, FieldOptions):
        _translate = QCoreApplication.translate
        FieldOptions.setWindowTitle(_translate("FieldOptions", "Dialog"))
        self.fieldName.setText(_translate("FieldOptions", "Field"))
        self.label.setText(_translate("FieldOptions", "Font"))
        self.label_3.setText(_translate("FieldOptions", "Font Size Offset"))
        self.label_4.setText(_translate("FieldOptions", "Field Audio"))
        self.fieldAudioBox.setItemText(0, _translate("FieldOptions", "(None)"))
