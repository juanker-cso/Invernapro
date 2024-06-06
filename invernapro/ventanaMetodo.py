import time
import random
import mysql.connector as mdb
from PySide2 import QtWidgets
from UI.nuevoMetodo import Ui_FormMetodo
import datos as d

class ventanaMetodo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_FormMetodo()
        self.ui.setupUi(self)

        self.ui.lineEd_medio.textChanged.connect(self.calc_ID)
        self.ui.lineEd_organo.textChanged.connect(self.calc_ID)
    
        self.ui.pushButton_guardar.clicked.connect(self.agregar)

    def calc_ID(self):
        idgen = ""
        organo = self.ui.lineEd_medio.text().lower()
        medio = self.ui.lineEd_organo.text().lower()
        idgen += medio[0:2]
        idgen += organo[0:2]

        random.seed(time.time())
        idgen += str(random.randrange(0,9))
        idgen += str(random.randrange(0,9))

        self.ui.lineEd_idMetodo.setText(idgen)

    def agregar(self):
        if self.ui.lineEd_medio.text() == "" or self.ui.lineEd_organo.text() == "":
            QtWidgets.QMessageBox.warning(self,"Error:","Campos requeridos faltantes")
            return
        
        datos = "'"
        datos += self.ui.lineEd_idMetodo.text() + "','"
        datos += self.ui.lineEd_organo.text().capitalize() + "','"
        datos += self.ui.lineEd_medio.text().capitalize() + "','"
        datos += self.ui.plainTextEd_notas.toPlainText() + "'"

        db = mdb.connect(user='invernadmin',
                                   password='password',
                                   host='localhost',
                                   database='invernapro')
        mensage = d.agregar_datos(db,datos,"metodos")
        if mensage == "E":
            self.clearAll()
            db.close()
            QtWidgets.QMessageBox.information(self,"Exito","Registro Guardado",button0=QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self,"Error:",mensage,button0=QtWidgets.QMessageBox.Ok)


    def clearAll(self):
        self.ui.lineEd_idMetodo.clear()
        self.ui.lineEd_organo.clear()
        self.ui.lineEd_medio.clear()
        self.ui.plainTextEd_notas.clear()