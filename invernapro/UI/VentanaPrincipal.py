# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import placeholder_rc

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(971, 773)
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(16)
        VentanaPrincipal.setFont(font)
        self.actionCulivos = QAction(VentanaPrincipal)
        self.actionCulivos.setObjectName(u"actionCulivos")
        self.actionNombres = QAction(VentanaPrincipal)
        self.actionNombres.setObjectName(u"actionNombres")
        self.actionMetodos = QAction(VentanaPrincipal)
        self.actionMetodos.setObjectName(u"actionMetodos")
        self.actionVer = QAction(VentanaPrincipal)
        self.actionVer.setObjectName(u"actionVer")
        self.actionPlantas_por_nombre = QAction(VentanaPrincipal)
        self.actionPlantas_por_nombre.setObjectName(u"actionPlantas_por_nombre")
        self.actionNombres_de_planta = QAction(VentanaPrincipal)
        self.actionNombres_de_planta.setObjectName(u"actionNombres_de_planta")
        self.actionEn_temporada = QAction(VentanaPrincipal)
        self.actionEn_temporada.setObjectName(u"actionEn_temporada")
        self.actionPlantas_de_variedad = QAction(VentanaPrincipal)
        self.actionPlantas_de_variedad.setObjectName(u"actionPlantas_de_variedad")
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.ArrowCursor))
        self.label.setPixmap(QPixmap(u":/plantvector/floral-2028345_640.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_cultivo = QPushButton(self.frame)
        self.pushButton_cultivo.setObjectName(u"pushButton_cultivo")
        self.pushButton_cultivo.setMinimumSize(QSize(0, 120))
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans")
        font1.setPointSize(18)
        self.pushButton_cultivo.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_cultivo)

        self.pushButton_nombre = QPushButton(self.frame)
        self.pushButton_nombre.setObjectName(u"pushButton_nombre")
        self.pushButton_nombre.setMinimumSize(QSize(0, 120))
        self.pushButton_nombre.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_nombre)

        self.pushButton_metodo = QPushButton(self.frame)
        self.pushButton_metodo.setObjectName(u"pushButton_metodo")
        self.pushButton_metodo.setMinimumSize(QSize(0, 120))
        self.pushButton_metodo.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_metodo)

        self.pushButton_lote = QPushButton(self.frame)
        self.pushButton_lote.setObjectName(u"pushButton_lote")
        self.pushButton_lote.setMinimumSize(QSize(0, 120))
        self.pushButton_lote.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_lote)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_eliminar = QPushButton(self.tab_2)
        self.pushButton_eliminar.setObjectName(u"pushButton_eliminar")

        self.gridLayout_2.addWidget(self.pushButton_eliminar, 4, 1, 1, 1)

        self.tableWidget_busqueda = QTableWidget(self.tab_2)
        self.tableWidget_busqueda.setObjectName(u"tableWidget_busqueda")
        font2 = QFont()
        font2.setFamily(u"DejaVu Sans Mono")
        font2.setPointSize(11)
        self.tableWidget_busqueda.setFont(font2)

        self.gridLayout_2.addWidget(self.tableWidget_busqueda, 2, 0, 1, 2)

        self.comboBox_busqueda_clase = QComboBox(self.tab_2)
        self.comboBox_busqueda_clase.addItem("")
        self.comboBox_busqueda_clase.addItem("")
        self.comboBox_busqueda_clase.addItem("")
        self.comboBox_busqueda_clase.addItem("")
        self.comboBox_busqueda_clase.addItem("")
        self.comboBox_busqueda_clase.setObjectName(u"comboBox_busqueda_clase")

        self.gridLayout_2.addWidget(self.comboBox_busqueda_clase, 0, 0, 1, 2)

        self.pushButton_seleccionar = QPushButton(self.tab_2)
        self.pushButton_seleccionar.setObjectName(u"pushButton_seleccionar")

        self.gridLayout_2.addWidget(self.pushButton_seleccionar, 4, 0, 1, 1)

        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 3, 0, 3)
        self.lineEdit_buscar_id = QLineEdit(self.frame_2)
        self.lineEdit_buscar_id.setObjectName(u"lineEdit_buscar_id")
        self.lineEdit_buscar_id.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_buscar_id, 0, 1, 1, 1)

        self.label_primaria = QLabel(self.frame_2)
        self.label_primaria.setObjectName(u"label_primaria")

        self.gridLayout_3.addWidget(self.label_primaria, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 2)

        self.label_results = QLabel(self.tab_2)
        self.label_results.setObjectName(u"label_results")
        font3 = QFont()
        font3.setFamily(u"DejaVu Sans")
        font3.setPointSize(10)
        self.label_results.setFont(font3)

        self.gridLayout_2.addWidget(self.label_results, 3, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)

        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 971, 30))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuBusquedas = QMenu(self.menuArchivo)
        self.menuBusquedas.setObjectName(u"menuBusquedas")
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.pushButton_cultivo)
        QWidget.setTabOrder(self.pushButton_cultivo, self.pushButton_nombre)
        QWidget.setTabOrder(self.pushButton_nombre, self.pushButton_metodo)
        QWidget.setTabOrder(self.pushButton_metodo, self.pushButton_lote)
        QWidget.setTabOrder(self.pushButton_lote, self.comboBox_busqueda_clase)
        QWidget.setTabOrder(self.comboBox_busqueda_clase, self.lineEdit_buscar_id)
        QWidget.setTabOrder(self.lineEdit_buscar_id, self.tableWidget_busqueda)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.menuBusquedas.menuAction())
        self.menuBusquedas.addAction(self.actionPlantas_por_nombre)
        self.menuBusquedas.addAction(self.actionNombres_de_planta)
        self.menuBusquedas.addAction(self.actionEn_temporada)
        self.menuBusquedas.addAction(self.actionPlantas_de_variedad)

        self.retranslateUi(VentanaPrincipal)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"InvernaPro", None))
        self.actionCulivos.setText(QCoreApplication.translate("VentanaPrincipal", u"Cultivos", None))
        self.actionNombres.setText(QCoreApplication.translate("VentanaPrincipal", u"Nombres", None))
        self.actionMetodos.setText(QCoreApplication.translate("VentanaPrincipal", u"M\u00e9todos", None))
        self.actionVer.setText(QCoreApplication.translate("VentanaPrincipal", u"Ver", None))
        self.actionPlantas_por_nombre.setText(QCoreApplication.translate("VentanaPrincipal", u"Variedades por nombre", None))
        self.actionNombres_de_planta.setText(QCoreApplication.translate("VentanaPrincipal", u"Nombres de variedad", None))
        self.actionEn_temporada.setText(QCoreApplication.translate("VentanaPrincipal", u"En temporada", None))
        self.actionPlantas_de_variedad.setText(QCoreApplication.translate("VentanaPrincipal", u"Plantas de variedad", None))
        self.label.setText("")
        self.pushButton_cultivo.setText(QCoreApplication.translate("VentanaPrincipal", u"Nuevo cultivo", None))
        self.pushButton_nombre.setText(QCoreApplication.translate("VentanaPrincipal", u"Nuevo nombre com\u00fan", None))
        self.pushButton_metodo.setText(QCoreApplication.translate("VentanaPrincipal", u"Nuevo m\u00e9todo de propagaci\u00f3n", None))
        self.pushButton_lote.setText(QCoreApplication.translate("VentanaPrincipal", u"Nuevo lote de reproducci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("VentanaPrincipal", u"Nuevo", None))
        self.pushButton_eliminar.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
        self.comboBox_busqueda_clase.setItemText(0, QCoreApplication.translate("VentanaPrincipal", u"Cultivos", None))
        self.comboBox_busqueda_clase.setItemText(1, QCoreApplication.translate("VentanaPrincipal", u"Nombres", None))
        self.comboBox_busqueda_clase.setItemText(2, QCoreApplication.translate("VentanaPrincipal", u"M\u00e9todos", None))
        self.comboBox_busqueda_clase.setItemText(3, QCoreApplication.translate("VentanaPrincipal", u"Lotes", None))
        self.comboBox_busqueda_clase.setItemText(4, QCoreApplication.translate("VentanaPrincipal", u"Plantas", None))

        self.pushButton_seleccionar.setText(QCoreApplication.translate("VentanaPrincipal", u"Seleccionar", None))
        self.label_primaria.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p>ID:</p></body></html>", None))
        self.label_results.setText(QCoreApplication.translate("VentanaPrincipal", u"Mostrando: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("VentanaPrincipal", u"Ver", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Archivo", None))
        self.menuBusquedas.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Busquedas", None))
    # retranslateUi

