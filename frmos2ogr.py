# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmos2ogr.ui'
#
# Created: Tue Jul 02 10:43:46 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_os2ogrDialog(object):
    def setupUi(self, os2ogrDialog):
        os2ogrDialog.setObjectName(_fromUtf8("os2ogrDialog"))
        os2ogrDialog.resize(380, 288)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/osTrans.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        os2ogrDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(os2ogrDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(os2ogrDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.inputDirLineEdit = QtGui.QLineEdit(os2ogrDialog)
        self.inputDirLineEdit.setObjectName(_fromUtf8("inputDirLineEdit"))
        self.gridLayout.addWidget(self.inputDirLineEdit, 1, 0, 1, 2)
        self.inputDirBrowsePushButton = QtGui.QPushButton(os2ogrDialog)
        self.inputDirBrowsePushButton.setObjectName(_fromUtf8("inputDirBrowsePushButton"))
        self.gridLayout.addWidget(self.inputDirBrowsePushButton, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(os2ogrDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.outputDirLineEdit = QtGui.QLineEdit(os2ogrDialog)
        self.outputDirLineEdit.setObjectName(_fromUtf8("outputDirLineEdit"))
        self.gridLayout.addWidget(self.outputDirLineEdit, 3, 0, 1, 2)
        self.outputDirBrowsePushButton = QtGui.QPushButton(os2ogrDialog)
        self.outputDirBrowsePushButton.setObjectName(_fromUtf8("outputDirBrowsePushButton"))
        self.gridLayout.addWidget(self.outputDirBrowsePushButton, 3, 2, 1, 1)
        self.label_3 = QtGui.QLabel(os2ogrDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.outputFormatComboBox = QtGui.QComboBox(os2ogrDialog)
        self.outputFormatComboBox.setObjectName(_fromUtf8("outputFormatComboBox"))
        self.gridLayout.addWidget(self.outputFormatComboBox, 5, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(225, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 2)
        self.line = QtGui.QFrame(os2ogrDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 6, 0, 1, 3)
        self.label_4 = QtGui.QLabel(os2ogrDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.tempDirLineEdit = QtGui.QLineEdit(os2ogrDialog)
        self.tempDirLineEdit.setObjectName(_fromUtf8("tempDirLineEdit"))
        self.gridLayout.addWidget(self.tempDirLineEdit, 8, 0, 1, 2)
        self.tempDirBrowsePushButton = QtGui.QPushButton(os2ogrDialog)
        self.tempDirBrowsePushButton.setObjectName(_fromUtf8("tempDirBrowsePushButton"))
        self.gridLayout.addWidget(self.tempDirBrowsePushButton, 8, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.aboutBtn = QtGui.QPushButton(os2ogrDialog)
        self.aboutBtn.setObjectName(_fromUtf8("aboutBtn"))
        self.horizontalLayout.addWidget(self.aboutBtn)
        spacerItem1 = QtGui.QSpacerItem(63, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(os2ogrDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(os2ogrDialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 3)

        self.retranslateUi(os2ogrDialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), os2ogrDialog.accept)
        QtCore.QObject.connect(self.inputDirBrowsePushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), os2ogrDialog.browseInputFolder)
        QtCore.QObject.connect(self.outputDirBrowsePushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), os2ogrDialog.browseOutputFolder)
        QtCore.QObject.connect(self.tempDirBrowsePushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), os2ogrDialog.browseTempFolder)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), os2ogrDialog.close)
        QtCore.QObject.connect(self.aboutBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), os2ogrDialog.about)
        QtCore.QMetaObject.connectSlotsByName(os2ogrDialog)

    def retranslateUi(self, os2ogrDialog):
        os2ogrDialog.setWindowTitle(QtGui.QApplication.translate("os2ogrDialog", "Ordnance Survey Translator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("os2ogrDialog", "Folder Containing Input Files (.gml, .gz)", None, QtGui.QApplication.UnicodeUTF8))
        self.inputDirBrowsePushButton.setText(QtGui.QApplication.translate("os2ogrDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("os2ogrDialog", "Folder For Outputs", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirBrowsePushButton.setText(QtGui.QApplication.translate("os2ogrDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("os2ogrDialog", "Output Format", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("os2ogrDialog", "Temporary Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.tempDirBrowsePushButton.setText(QtGui.QApplication.translate("os2ogrDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutBtn.setText(QtGui.QApplication.translate("os2ogrDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("os2ogrDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("os2ogrDialog", "Convert", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
