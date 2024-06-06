# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevoMetodo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormMetodo(object):
    def setupUi(self, FormMetodo):
        if not FormMetodo.objectName():
            FormMetodo.setObjectName(u"FormMetodo")
        FormMetodo.resize(300, 512)
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(12)
        FormMetodo.setFont(font)
        self.gridLayout = QGridLayout(FormMetodo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_guardar = QPushButton(FormMetodo)
        self.pushButton_guardar.setObjectName(u"pushButton_guardar")
        self.pushButton_guardar.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.pushButton_guardar, 1, 0, 1, 1)

        self.frame = QFrame(FormMetodo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEd_idMetodo = QLineEdit(self.frame)
        self.lineEd_idMetodo.setObjectName(u"lineEd_idMetodo")
        self.lineEd_idMetodo.setEnabled(False)
        self.lineEd_idMetodo.setMinimumSize(QSize(128, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEd_idMetodo)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEd_organo = QLineEdit(self.frame)
        self.lineEd_organo.setObjectName(u"lineEd_organo")
        self.lineEd_organo.setMinimumSize(QSize(256, 25))

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.lineEd_organo)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lineEd_medio = QLineEdit(self.frame)
        self.lineEd_medio.setObjectName(u"lineEd_medio")
        self.lineEd_medio.setMinimumSize(QSize(256, 25))

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.lineEd_medio)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.plainTextEd_notas = QPlainTextEdit(self.frame)
        self.plainTextEd_notas.setObjectName(u"plainTextEd_notas")
        self.plainTextEd_notas.setMinimumSize(QSize(256, 192))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.plainTextEd_notas)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.frame_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.lineEd_idMetodo, self.lineEd_organo)
        QWidget.setTabOrder(self.lineEd_organo, self.lineEd_medio)
        QWidget.setTabOrder(self.lineEd_medio, self.plainTextEd_notas)
        QWidget.setTabOrder(self.plainTextEd_notas, self.pushButton_guardar)

        self.retranslateUi(FormMetodo)

        QMetaObject.connectSlotsByName(FormMetodo)
    # setupUi

    def retranslateUi(self, FormMetodo):
        FormMetodo.setWindowTitle(QCoreApplication.translate("FormMetodo", u"Metodo", None))
        self.pushButton_guardar.setText(QCoreApplication.translate("FormMetodo", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("FormMetodo", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("FormMetodo", u"\u00d3rgano de propagaci\u00f3n*", None))
        self.label_3.setText(QCoreApplication.translate("FormMetodo", u"Medio*", None))
        self.label_4.setText(QCoreApplication.translate("FormMetodo", u"Notas:", None))
    # retranslateUi

