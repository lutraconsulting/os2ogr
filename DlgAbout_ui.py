# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgAbout.ui'
#
# Created: Sun Jul 10 16:21:05 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgAbout(object):
    def setupUi(self, DlgAbout):
        DlgAbout.setObjectName(_fromUtf8("DlgAbout"))
        DlgAbout.resize(470, 250)
        self.gridLayout = QtGui.QGridLayout(DlgAbout)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.logo = QtGui.QLabel(DlgAbout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(85, 70))
        self.logo.setMaximumSize(QtCore.QSize(85, 70))
        self.logo.setText(_fromUtf8(""))
        self.logo.setScaledContents(True)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.gridLayout.addWidget(self.logo, 0, 0, 2, 1)
        self.title = QtGui.QLabel(DlgAbout)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DlgAbout)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.description = QtGui.QLabel(DlgAbout)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setWordWrap(True)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 1, 1, 1, 1)
        self.txt = QtGui.QTextBrowser(DlgAbout)
        self.txt.setOpenExternalLinks(True)
        self.txt.setObjectName(_fromUtf8("txt"))
        self.gridLayout.addWidget(self.txt, 2, 0, 1, 2)

        self.retranslateUi(DlgAbout)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgAbout.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgAbout.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgAbout)

    def retranslateUi(self, DlgAbout):
        DlgAbout.setWindowTitle(QtGui.QApplication.translate("DlgAbout", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("DlgAbout", "$PLUGIN_NAME$", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setText(QtGui.QApplication.translate("DlgAbout", "$PLUGIN_DESCRIPTION$", None, QtGui.QApplication.UnicodeUTF8))
        self.txt.setHtml(QtGui.QApplication.translate("DlgAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">$PLUGIN_NAME$ is being developed by Peter Wells for Faunalia (</span><a href=\"http://www.faunalia.it\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">http://www.faunalia.it</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\"> &amp; </span><a href=\"http://www.faunalia.co.uk/en\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">http://www.faunalia.co.uk/en</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\">).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">$PLUGIN_NAME$ makes use of </span><a href=\"https://github.com/AstunTechnology/osmmloader\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">osmmloader</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">For support, contact us at </span><a href=\"mailto:info@faunalia.co.uk?subject=$MAIL_SUBJECT$&amp;body=$MAIL_BODY$\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">info@faunalia.co.uk</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

