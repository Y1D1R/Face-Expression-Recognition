# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceCLcjas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(728, 440)
        self.videoLabel = QLabel(Form)
        self.videoLabel.setObjectName(u"videoLabel")
        self.videoLabel.setGeometry(QRect(240, 40, 371, 271))
        self.runBtn = QPushButton(Form)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setGeometry(QRect(290, 380, 191, 41))
        self.widget = roundProgressBar(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(39, 69, 181, 181))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.videoLabel.setText("")
        self.runBtn.setText(QCoreApplication.translate("Form", u"Run", None))
    # retranslateUi

