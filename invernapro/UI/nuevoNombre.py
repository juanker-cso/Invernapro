# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevoNombre.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormNombre(object):
    def setupUi(self, FormNombre):
        if not FormNombre.objectName():
            FormNombre.setObjectName(u"FormNombre")
        FormNombre.resize(242, 262)
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(12)
        FormNombre.setFont(font)
        self.gridLayout = QGridLayout(FormNombre)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(FormNombre)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEd_nombre = QLineEdit(self.frame)
        self.lineEd_nombre.setObjectName(u"lineEd_nombre")
        self.lineEd_nombre.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEd_nombre)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEd_idioma = QLineEdit(self.frame)
        self.lineEd_idioma.setObjectName(u"lineEd_idioma")
        self.lineEd_idioma.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEd_idioma)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.frame_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.pushButton_guardar = QPushButton(FormNombre)
        self.pushButton_guardar.setObjectName(u"pushButton_guardar")
        self.pushButton_guardar.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.pushButton_guardar, 1, 0, 1, 1)

        QWidget.setTabOrder(self.lineEd_nombre, self.lineEd_idioma)
        QWidget.setTabOrder(self.lineEd_idioma, self.pushButton_guardar)

        self.retranslateUi(FormNombre)

        QMetaObject.connectSlotsByName(FormNombre)
    # setupUi

    def retranslateUi(self, FormNombre):
        FormNombre.setWindowTitle(QCoreApplication.translate("FormNombre", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("FormNombre", u"Nombre com\u00fan*", None))
        self.label_3.setText(QCoreApplication.translate("FormNombre", u"Idioma", None))
        self.pushButton_guardar.setText(QCoreApplication.translate("FormNombre", u"Guardar", None))
    # retranslateUi

