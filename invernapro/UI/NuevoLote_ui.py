# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NuevoLote.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_FormLote(object):
    def setupUi(self, FormLote):
        if not FormLote.objectName():
            FormLote.setObjectName(u"FormLote")
        FormLote.resize(243, 370)
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(12)
        FormLote.setFont(font)
        self.gridLayout = QGridLayout(FormLote)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(FormLote)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEd_contLote = QLineEdit(self.frame)
        self.lineEd_contLote.setObjectName(u"lineEd_contLote")
        self.lineEd_contLote.setEnabled(False)
        self.lineEd_contLote.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEd_contLote)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEd_idVar_in = QLineEdit(self.frame)
        self.lineEd_idVar_in.setObjectName(u"lineEd_idVar_in")
        self.lineEd_idVar_in.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEd_idVar_in)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_idMetodo = QLineEdit(self.frame)
        self.lineEdit_idMetodo.setObjectName(u"lineEdit_idMetodo")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lineEdit_idMetodo)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 25))
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.dateEdit)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_numPlantas = QLineEdit(self.frame)
        self.lineEdit_numPlantas.setObjectName(u"lineEdit_numPlantas")
        self.lineEdit_numPlantas.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.lineEdit_numPlantas)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.pushButton_guardar = QPushButton(FormLote)
        self.pushButton_guardar.setObjectName(u"pushButton_guardar")
        self.pushButton_guardar.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.pushButton_guardar, 1, 0, 1, 1)

        QWidget.setTabOrder(self.lineEd_contLote, self.lineEd_idVar_in)
        QWidget.setTabOrder(self.lineEd_idVar_in, self.lineEdit_idMetodo)
        QWidget.setTabOrder(self.lineEdit_idMetodo, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.lineEdit_numPlantas)
        QWidget.setTabOrder(self.lineEdit_numPlantas, self.pushButton_guardar)

        self.retranslateUi(FormLote)

        QMetaObject.connectSlotsByName(FormLote)
    # setupUi

    def retranslateUi(self, FormLote):
        FormLote.setWindowTitle(QCoreApplication.translate("FormLote", u"Nuevo Lote", None))
        self.label.setText(QCoreApplication.translate("FormLote", u"N\u00famero", None))
        self.label_2.setText(QCoreApplication.translate("FormLote", u"ID de Variedad", None))
        self.label_4.setText(QCoreApplication.translate("FormLote", u"ID de m\u00e9todo", None))
        self.label_3.setText(QCoreApplication.translate("FormLote", u"Fecha", None))
        self.label_5.setText(QCoreApplication.translate("FormLote", u"Cantidad de plantas*", None))
        self.pushButton_guardar.setText(QCoreApplication.translate("FormLote", u"Guardar", None))
    # retranslateUi

