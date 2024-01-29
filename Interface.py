# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceZSZEWL.ui'
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
        Form.resize(900, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(900, 500))
        Form.setMaximumSize(QSize(900, 500))
        self.videoLabel = QLabel(Form)
        self.videoLabel.setObjectName(u"videoLabel")
        self.videoLabel.setGeometry(QRect(300, 30, 501, 341))
        self.videoLabel.setAlignment(Qt.AlignCenter)
        self.runBtn = QPushButton(Form)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setGeometry(QRect(500, 400, 191, 41))
        self.runBtn.setLayoutDirection(Qt.LeftToRight)
        self.widget_1 = roundProgressBar(Form)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setGeometry(QRect(10, 30, 111, 91))
        self.widget_2 = roundProgressBar(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 150, 111, 91))
        self.widget_3 = roundProgressBar(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(150, 30, 111, 91))
        self.widget_4 = roundProgressBar(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(150, 150, 111, 91))
        self.widget_5 = roundProgressBar(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(150, 270, 111, 91))
        self.widget_6 = roundProgressBar(Form)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 270, 111, 91))
        self.widget_0 = roundProgressBar(Form)
        self.widget_0.setObjectName(u"widget_0")
        self.widget_0.setGeometry(QRect(80, 390, 111, 91))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(86, 370, 101, 20))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 250, 111, 20))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 250, 111, 20))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 130, 111, 20))
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 130, 111, 21))
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 10, 111, 20))
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 111, 20))
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.videoLabel.setText("")
        self.runBtn.setText(QCoreApplication.translate("Form", u"Run", None))
        self.label.setText(QCoreApplication.translate("Form", u"Angry", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Neutral", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Surprised", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Sad", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Fearful", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Happy", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Disgusted", None))
    # retranslateUi

