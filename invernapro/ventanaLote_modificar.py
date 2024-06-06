import mysql.connector as mdb
from PySide2 import QtWidgets, QtCore
from UI.NuevoLote import Ui_FormLote

import datos as d

class ventanaLote(QtWidgets.QWidget):
    def __init__(self,cont:str,idvar:str,idmetodo:str,fecha:str,cantidad:str):
        super().__init__()

        self.ui = Ui_FormLote()
        self.ui.setupUi(self)

        self.cont = cont

        self.ui.lineEd_contLote.setText(cont)
        self.ui.lineEd_idVar_in.setText(idvar)
        self.ui.lineEdit_idMetodo.setText(idmetodo)
        y = int(fecha[:4])
        m = int(fecha[5:7])
        d = int(fecha[8:10])
        self.ui.dateEdit.setDate(QtCore.QDate(y,m,d))
        self.ui.lineEdit_numPlantas.setText(cantidad)

        self.ui.pushButton_guardar.clicked.connect(self.guardar)


    def guardar(self):
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
                       "WHERE idMetodo = %s AND idVar = %s;",(idmetodo,id_variedad))
        x = cursor.fetchone()[0]
        cursor.fetchall()
        if x == 0:
            QtWidgets.QMessageBox.warning(self,"Error:","Metodo no encontrado para variedad")
            db.close()
            return
        fecha = self.ui.dateEdit.date().toString(QtCore.Qt.ISODate)
        contplantas = self.ui.lineEdit_numPlantas.text()
        cursor = db.cursor()
        try:
            cursor.execute("UPDATE lotes SET idVar = %s, idMetodo = %s, fecha = %s, "
                        "cantidad = %s WHERE cont = %s",
                        (id_variedad,idmetodo,fecha,contplantas,self.cont))
            db.commit()
            db.close()
            self.close()
        except mdb.Error as e:
            QtWidgets.QMessageBox.warning(self,"Error:",str(e.msg),
                                          button0=QtWidgets.QMessageBox.Ok)
            db.close()
            return
