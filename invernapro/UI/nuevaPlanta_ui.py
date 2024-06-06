# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevaPlanta.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_FormPlanta(object):
    def setupUi(self, FormPlanta):
        if not FormPlanta.objectName():
            FormPlanta.setObjectName(u"FormPlanta")
        FormPlanta.resize(183, 339)
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(12)
        FormPlanta.setFont(font)
        self.gridLayout = QGridLayout(FormPlanta)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_guardar = QPushButton(FormPlanta)
        self.pushButton_guardar.setObjectName(u"pushButton_guardar")
        self.pushButton_guardar.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.pushButton_guardar, 2, 0, 1, 1)

        self.frame = QFrame(FormPlanta)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEd_idVar_in = QLineEdit(self.frame)
        self.lineEd_idVar_in.setObjectName(u"lineEd_idVar_in")
        self.lineEd_idVar_in.setEnabled(False)
        self.lineEd_idVar_in.setMinimumSize(QSize(0, 25))
        self.lineEd_idVar_in.setMouseTracking(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEd_idVar_in)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.spinBox_contLote_in = QSpinBox(self.frame)
        self.spinBox_contLote_in.setObjectName(u"spinBox_contLote_in")
        self.spinBox_contLote_in.setEnabled(False)
        self.spinBox_contLote_in.setMinimumSize(QSize(0, 25))
        self.spinBox_contLote_in.setMaximum(99999)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.spinBox_contLote_in)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_numPlanta = QLineEdit(self.frame)
        self.lineEdit_numPlanta.setObjectName(u"lineEdit_numPlanta")
        self.lineEdit_numPlanta.setEnabled(False)
        self.lineEdit_numPlanta.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lineEdit_numPlanta)

        self.checkBox_venta = QCheckBox(self.frame)
        self.checkBox_venta.setObjectName(u"checkBox_venta")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.checkBox_venta)

        self.checkBox_merma = QCheckBox(self.frame)
        self.checkBox_merma.setObjectName(u"checkBox_merma")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.checkBox_merma)

        self.checkBox_repro = QCheckBox(self.frame)
        self.checkBox_repro.setObjectName(u"checkBox_repro")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.checkBox_repro)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.lineEd_idVar_in, self.spinBox_contLote_in)
        QWidget.setTabOrder(self.spinBox_contLote_in, self.lineEdit_numPlanta)
        QWidget.setTabOrder(self.lineEdit_numPlanta, self.pushButton_guardar)

        self.retranslateUi(FormPlanta)

        QMetaObject.connectSlotsByName(FormPlanta)
    # setupUi

    def retranslateUi(self, FormPlanta):
        FormPlanta.setWindowTitle(QCoreApplication.translate("FormPlanta", u"Planta", None))
        self.pushButton_guardar.setText(QCoreApplication.translate("FormPlanta", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("FormPlanta", u"Id de Variedad", None))
        self.label_2.setText(QCoreApplication.translate("FormPlanta", u"Lote n\u00famero", None))
        self.label_3.setText(QCoreApplication.translate("FormPlanta", u"N\u00famero de planta", None))
        self.checkBox_venta.setText(QCoreApplication.translate("FormPlanta", u"Venta", None))
        self.checkBox_merma.setText(QCoreApplication.translate("FormPlanta", u"Merma", None))
        self.checkBox_repro.setText(QCoreApplication.translate("FormPlanta", u"Reproducci\u00f3n", None))
    # retranslateUi

