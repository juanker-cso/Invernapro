# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevaVariedad.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormVariedad(object):
    def setupUi(self, FormVariedad):
        if not FormVariedad.objectName():
            FormVariedad.setObjectName(u"FormVariedad")
        FormVariedad.resize(535, 613)
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(12)
        FormVariedad.setFont(font)
        self.gridLayout = QGridLayout(FormVariedad)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_8 = QGroupBox(FormVariedad)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_4 = QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_12 = QFrame(self.groupBox_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(1, 1, 1, 1)
        self.frame_8 = QFrame(self.frame_12)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(90, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.pushButton_newmetodo = QPushButton(self.frame_8)
        self.pushButton_newmetodo.setObjectName(u"pushButton_newmetodo")
        self.pushButton_newmetodo.setMinimumSize(QSize(30, 27))
        self.pushButton_newmetodo.setMaximumSize(QSize(30, 16777215))
        self.pushButton_newmetodo.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_6.addWidget(self.pushButton_newmetodo)

        self.pushButton_deletemetodo = QPushButton(self.frame_8)
        self.pushButton_deletemetodo.setObjectName(u"pushButton_deletemetodo")
        self.pushButton_deletemetodo.setMinimumSize(QSize(30, 27))
        self.pushButton_deletemetodo.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_deletemetodo)


        self.gridLayout_7.addWidget(self.frame_8, 0, 1, 1, 1)

        self.lineEdit_addmetodo = QLineEdit(self.frame_12)
        self.lineEdit_addmetodo.setObjectName(u"lineEdit_addmetodo")
        self.lineEdit_addmetodo.setEnabled(True)

        self.gridLayout_7.addWidget(self.lineEdit_addmetodo, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_12, 0, 0, 1, 1)

        self.listWidget_metodos = QListWidget(self.groupBox_8)
        self.listWidget_metodos.setObjectName(u"listWidget_metodos")
        self.listWidget_metodos.setMinimumSize(QSize(172, 0))
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans")
        font1.setPointSize(10)
        self.listWidget_metodos.setFont(font1)

        self.gridLayout_4.addWidget(self.listWidget_metodos, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_8, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(FormVariedad)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_3 = QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.listWidget_nombres = QListWidget(self.groupBox_6)
        self.listWidget_nombres.setObjectName(u"listWidget_nombres")
        self.listWidget_nombres.setMinimumSize(QSize(172, 0))
        self.listWidget_nombres.setFont(font1)

        self.gridLayout_3.addWidget(self.listWidget_nombres, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.groupBox_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(1, 1, 1, 1)
        self.frame_7 = QFrame(self.frame_11)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(90, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.pushButton_newnombre = QPushButton(self.frame_7)
        self.pushButton_newnombre.setObjectName(u"pushButton_newnombre")
        self.pushButton_newnombre.setMinimumSize(QSize(30, 27))
        self.pushButton_newnombre.setMaximumSize(QSize(30, 16777215))
        self.pushButton_newnombre.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_4.addWidget(self.pushButton_newnombre)

        self.pushButton_deletenombre = QPushButton(self.frame_7)
        self.pushButton_deletenombre.setObjectName(u"pushButton_deletenombre")
        self.pushButton_deletenombre.setMinimumSize(QSize(30, 27))
        self.pushButton_deletenombre.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_deletenombre)


        self.gridLayout_6.addWidget(self.frame_7, 0, 1, 1, 1)

        self.lineEdit_addnombre = QLineEdit(self.frame_11)
        self.lineEdit_addnombre.setObjectName(u"lineEdit_addnombre")
        self.lineEdit_addnombre.setEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_addnombre, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_11, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.frame = QFrame(FormVariedad)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(17, 19))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEd_idVar = QLineEdit(self.frame)
        self.lineEd_idVar.setObjectName(u"lineEd_idVar")
        self.lineEd_idVar.setEnabled(False)
        self.lineEd_idVar.setMinimumSize(QSize(201, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEd_idVar)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(158, 19))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEd_nombre = QLineEdit(self.frame)
        self.lineEd_nombre.setObjectName(u"lineEd_nombre")
        self.lineEd_nombre.setMinimumSize(QSize(201, 25))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEd_nombre)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(166, 19))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lineEd_variedad = QLineEdit(self.frame)
        self.lineEd_variedad.setObjectName(u"lineEd_variedad")
        self.lineEd_variedad.setMinimumSize(QSize(201, 25))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lineEd_variedad)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(125, 19))

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_luz = QComboBox(self.frame_2)
        self.comboBox_luz.addItem("")
        self.comboBox_luz.addItem("")
        self.comboBox_luz.addItem("")
        self.comboBox_luz.addItem("")
        self.comboBox_luz.setObjectName(u"comboBox_luz")
        self.comboBox_luz.setMinimumSize(QSize(39, 25))

        self.horizontalLayout.addWidget(self.comboBox_luz)

        self.spinBox_luz = QSpinBox(self.frame_2)
        self.spinBox_luz.setObjectName(u"spinBox_luz")
        self.spinBox_luz.setMinimumSize(QSize(0, 25))
        self.spinBox_luz.setMaximum(24)

        self.horizontalLayout.addWidget(self.spinBox_luz)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(12, 25))

        self.horizontalLayout.addWidget(self.label_10)


        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.frame_2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(145, 19))

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox_riego = QSpinBox(self.frame_3)
        self.spinBox_riego.setObjectName(u"spinBox_riego")
        self.spinBox_riego.setMinimumSize(QSize(0, 25))
        self.spinBox_riego.setMaximum(100)
        self.spinBox_riego.setSingleStep(10)

        self.horizontalLayout_2.addWidget(self.spinBox_riego)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_2.addWidget(self.label_8)


        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.frame_3)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(183, 19))

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_6)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.lineEdit_temp1 = QLineEdit(self.frame_4)
        self.lineEdit_temp1.setObjectName(u"lineEdit_temp1")
        self.lineEdit_temp1.setMinimumSize(QSize(0, 25))
        self.lineEdit_temp1.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_temp1)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(6, 25))

        self.horizontalLayout_3.addWidget(self.label_9)

        self.lineEdit_temp2 = QLineEdit(self.frame_4)
        self.lineEdit_temp2.setObjectName(u"lineEdit_temp2")
        self.lineEdit_temp2.setMinimumSize(QSize(0, 25))
        self.lineEdit_temp2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_temp2)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)


        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.frame_4)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(209, 19))

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_13)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamily(u"DejaVu Sans")
        font2.setPointSize(8)
        self.groupBox.setFont(font2)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.lineEd_mes1 = QLineEdit(self.groupBox)
        self.lineEd_mes1.setObjectName(u"lineEd_mes1")
        self.lineEd_mes1.setMinimumSize(QSize(0, 25))
        self.lineEd_mes1.setMaximumSize(QSize(60, 16777215))
        self.lineEd_mes1.setFont(font)

        self.horizontalLayout_5.addWidget(self.lineEd_mes1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(6, 25))
        self.label_14.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.lineEd_mes2 = QLineEdit(self.groupBox)
        self.lineEd_mes2.setObjectName(u"lineEd_mes2")
        self.lineEd_mes2.setMinimumSize(QSize(0, 25))
        self.lineEd_mes2.setMaximumSize(QSize(60, 16777215))
        self.lineEd_mes2.setFont(font)

        self.horizontalLayout_5.addWidget(self.lineEd_mes2)


        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.groupBox)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(102, 19))

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_12)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.doubleSpinBox_ph = QDoubleSpinBox(self.frame_5)
        self.doubleSpinBox_ph.setObjectName(u"doubleSpinBox_ph")
        self.doubleSpinBox_ph.setMinimumSize(QSize(0, 25))
        self.doubleSpinBox_ph.setDecimals(1)
        self.doubleSpinBox_ph.setMaximum(14.000000000000000)
        self.doubleSpinBox_ph.setSingleStep(0.500000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_ph, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(22, 25))

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)


        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.frame_5)


        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)

        self.pushButton_guardar = QPushButton(FormVariedad)
        self.pushButton_guardar.setObjectName(u"pushButton_guardar")
        self.pushButton_guardar.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.pushButton_guardar, 2, 0, 1, 2)

        QWidget.setTabOrder(self.lineEd_idVar, self.lineEd_nombre)
        QWidget.setTabOrder(self.lineEd_nombre, self.lineEd_variedad)
        QWidget.setTabOrder(self.lineEd_variedad, self.comboBox_luz)
        QWidget.setTabOrder(self.comboBox_luz, self.spinBox_luz)
        QWidget.setTabOrder(self.spinBox_luz, self.spinBox_riego)
        QWidget.setTabOrder(self.spinBox_riego, self.lineEdit_temp1)
        QWidget.setTabOrder(self.lineEdit_temp1, self.lineEdit_temp2)
        QWidget.setTabOrder(self.lineEdit_temp2, self.lineEd_mes1)
        QWidget.setTabOrder(self.lineEd_mes1, self.lineEd_mes2)
        QWidget.setTabOrder(self.lineEd_mes2, self.doubleSpinBox_ph)
        QWidget.setTabOrder(self.doubleSpinBox_ph, self.lineEdit_addnombre)
        QWidget.setTabOrder(self.lineEdit_addnombre, self.pushButton_newnombre)
        QWidget.setTabOrder(self.pushButton_newnombre, self.pushButton_deletenombre)
        QWidget.setTabOrder(self.pushButton_deletenombre, self.listWidget_nombres)
        QWidget.setTabOrder(self.listWidget_nombres, self.lineEdit_addmetodo)
        QWidget.setTabOrder(self.lineEdit_addmetodo, self.pushButton_newmetodo)
        QWidget.setTabOrder(self.pushButton_newmetodo, self.pushButton_deletemetodo)
        QWidget.setTabOrder(self.pushButton_deletemetodo, self.listWidget_metodos)
        QWidget.setTabOrder(self.listWidget_metodos, self.pushButton_guardar)

        self.retranslateUi(FormVariedad)

        QMetaObject.connectSlotsByName(FormVariedad)
    # setupUi

    def retranslateUi(self, FormVariedad):
        FormVariedad.setWindowTitle(QCoreApplication.translate("FormVariedad", u"Variedad", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("FormVariedad", u"M\u00e9todos", None))
        self.pushButton_newmetodo.setText(QCoreApplication.translate("FormVariedad", u"+", None))
        self.pushButton_deletemetodo.setText(QCoreApplication.translate("FormVariedad", u"-", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("FormVariedad", u"Nombres", None))
        self.pushButton_newnombre.setText(QCoreApplication.translate("FormVariedad", u"+", None))
        self.pushButton_deletenombre.setText(QCoreApplication.translate("FormVariedad", u"-", None))
        self.label.setText(QCoreApplication.translate("FormVariedad", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("FormVariedad", u"Nombre de especie*", None))
        self.label_3.setText(QCoreApplication.translate("FormVariedad", u"Nombre de variedad*", None))
        self.label_4.setText(QCoreApplication.translate("FormVariedad", u"R\u00e9gimen de luz", None))
        self.comboBox_luz.setItemText(0, QCoreApplication.translate("FormVariedad", u"D", None))
        self.comboBox_luz.setItemText(1, QCoreApplication.translate("FormVariedad", u"A", None))
        self.comboBox_luz.setItemText(2, QCoreApplication.translate("FormVariedad", u"M", None))
        self.comboBox_luz.setItemText(3, QCoreApplication.translate("FormVariedad", u"B", None))

        self.label_10.setText(QCoreApplication.translate("FormVariedad", u"H", None))
        self.label_5.setText(QCoreApplication.translate("FormVariedad", u"Humedad de suelo", None))
        self.label_8.setText(QCoreApplication.translate("FormVariedad", u"%", None))
        self.label_6.setText(QCoreApplication.translate("FormVariedad", u"Temperaturas toleradas", None))
        self.label_9.setText(QCoreApplication.translate("FormVariedad", u"-", None))
        self.label_11.setText(QCoreApplication.translate("FormVariedad", u"\u00b0C", None))
        self.label_13.setText(QCoreApplication.translate("FormVariedad", u"Temporada  de crecimiento", None))
        self.groupBox.setTitle(QCoreApplication.translate("FormVariedad", u"meses inicio - fin", None))
        self.label_14.setText(QCoreApplication.translate("FormVariedad", u"-", None))
        self.label_12.setText(QCoreApplication.translate("FormVariedad", u"Tipo de suelo", None))
        self.label_7.setText(QCoreApplication.translate("FormVariedad", u"pH", None))
        self.pushButton_guardar.setText(QCoreApplication.translate("FormVariedad", u"Guardar", None))
    # retranslateUi

