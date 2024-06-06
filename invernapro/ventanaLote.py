import mysql.connector as mdb
from PySide2 import QtWidgets, QtCore
from UI.NuevoLote import Ui_FormLote

import datos as d

class ventanaLote(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_FormLote()
        self.ui.setupUi(self)

        self.ui.dateEdit.setDate(
            QtCore.QDate.currentDate()
        )
        self.ui.lineEd_contLote.setText(str(self.gen_cont()))

        self.ui.pushButton_guardar.clicked.connect(self.agregar)

    def gen_cont(self) -> str:
        """Busca el número de id más alto guardado en la base"""
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor = db.cursor()
        cursor.execute("SELECT MAX(cont) FROM lotes;")
        res = cursor.fetchone()
        cont = res[0]
        if cont is None:
            return '1'
        db.close()
        return str(cont+1)

    def agregar(self):
        id_variedad = self.ui.lineEd_idVar_in.text().upper()
        idmetodo = self.ui.lineEdit_idMetodo.text()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        if not d.check_id(db,"variedades","id",id_variedad):
            QtWidgets.QMessageBox.warning(self,"Error:","Variedad no encontrada")
            db.close()
            return
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM variedadmetodos "
                       "WHERE idMetodo = %s AND idVar = %s",(idmetodo,id_variedad))
        x = cursor.fetchone()[0]
        cursor.fetchall()
        if x == 0:
            QtWidgets.QMessageBox.warning(self,"Error:","Metodo no encontrado para variedad")
            db.close()
            return
        datos = "'"
        datos += self.ui.lineEd_contLote.text() + "','"
        datos += id_variedad + "','"
        datos += idmetodo + "','"
        datos += self.ui.dateEdit.date().toString(QtCore.Qt.ISODate) + "','"
        datos += self.ui.lineEdit_numPlantas.text() + "'"

        mensage = d.agregar_datos(db,datos,"lotes")
        if mensage == "E":
            QtWidgets.QMessageBox.information(self,"Exito","Registro Guardado",button0=QtWidgets.QMessageBox.Ok)
            db.close()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self,"Error:",mensage,button0=QtWidgets.QMessageBox.Ok)
            db.close()
            return
