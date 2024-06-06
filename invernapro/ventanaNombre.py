import mysql.connector as mdb
import datos as d
from PySide2 import QtWidgets
from UI.nuevoNombre import Ui_FormNombre

class ventanaNombre(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_FormNombre()
        self.ui.setupUi(self)

        self.ui.pushButton_guardar.clicked.connect(self.guardar)

    def guardar(self):
        if self.ui.lineEd_nombre.text() == "":
            QtWidgets.QMessageBox.warning(self,"Error:","Nombre requerido")
            return

        datos ="'"
        datos += self.ui.lineEd_nombre.text().capitalize() +"','"
        datos += self.ui.lineEd_idioma.text().capitalize() +"'"

        database = mdb.connect(user='invernadmin',
                                   password='password',
                                   host='localhost',
                                   database='invernapro')
        mensage = d.agregar_datos(database,datos,"nombres")
        if mensage == "E":
            self.clearAll()
            QtWidgets.QMessageBox.information(self,"Exito","Registro Guardado",button0=QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self,"Error:",mensage,button0=QtWidgets.QMessageBox.Ok)

        database.close()

    def clearAll(self):
        self.ui.lineEd_nombre.clear()
        self.ui.lineEd_idioma.clear()