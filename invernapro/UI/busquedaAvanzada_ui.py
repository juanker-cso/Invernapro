# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'busquedaAvanzada.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_busquedaAvanzada(object):
    def setupUi(self, busquedaAvanzada):
        if not busquedaAvanzada.objectName():
            busquedaAvanzada.setObjectName(u"busquedaAvanzada")
        busquedaAvanzada.resize(619, 309)
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(14)
        busquedaAvanzada.setFont(font)
        self.verticalLayout = QVBoxLayout(busquedaAvanzada)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(busquedaAvanzada)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEd_nombrePlanta = QLineEdit(self.page)
        self.lineEd_nombrePlanta.setObjectName(u"lineEd_nombrePlanta")

        self.gridLayout.addWidget(self.lineEd_nombrePlanta, 1, 1, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.lineEd_idPlanta = QLineEdit(self.page_2)
        self.lineEd_idPlanta.setObjectName(u"lineEd_idPlanta")

        self.verticalLayout_2.addWidget(self.lineEd_idPlanta)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.dateEd_busqueda = QDateEdit(self.page_3)
        self.dateEd_busqueda.setObjectName(u"dateEd_busqueda")
        self.dateEd_busqueda.setEnabled(False)

        self.verticalLayout_3.addWidget(self.dateEd_busqueda)

        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.lineEd_idPlanta_2 = QLineEdit(self.page_4)
        self.lineEd_idPlanta_2.setObjectName(u"lineEd_idPlanta_2")

        self.verticalLayout_4.addWidget(self.lineEd_idPlanta_2)

        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.tableWidget_resultados = QTableWidget(busquedaAvanzada)
        self.tableWidget_resultados.setObjectName(u"tableWidget_resultados")

        self.verticalLayout.addWidget(self.tableWidget_resultados)


        self.retranslateUi(busquedaAvanzada)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(busquedaAvanzada)
    # setupUi

    def retranslateUi(self, busquedaAvanzada):
        busquedaAvanzada.setWindowTitle(QCoreApplication.translate("busquedaAvanzada", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("busquedaAvanzada", u"Plantas:", None))
        self.label.setText(QCoreApplication.translate("busquedaAvanzada", u"Nombre com\u00fan:", None))
        self.label_4.setText(QCoreApplication.translate("busquedaAvanzada", u"ID de planta:", None))
        self.label_3.setText(QCoreApplication.translate("busquedaAvanzada", u"Nombres:", None))
        self.label_6.setText(QCoreApplication.translate("busquedaAvanzada", u"Fecha:", None))
        self.label_5.setText(QCoreApplication.translate("busquedaAvanzada", u"Plantas:", None))
        self.label_7.setText(QCoreApplication.translate("busquedaAvanzada", u"Variedad:", None))
        self.label_8.setText(QCoreApplication.translate("busquedaAvanzada", u"Plantas en existencia:", None))
    # retranslateUi

