import mysql.connector as mdb
from PySide2 import QtWidgets
from UI.nuevoMetodo import Ui_FormMetodo

class ventanaMetodo(QtWidgets.QWidget):
    def __init__(self, idmetodo:str,organo:str,medio:str,notas:str):
        super().__init__()
        
        self.ui = Ui_FormMetodo()
        self.ui.setupUi(self)

        self.ui.lineEd_idMetodo.setText(idmetodo)
        self.ui.lineEd_organo.setText(organo)
        self.ui.lineEd_organo.setDisabled(True)
        self.ui.lineEd_medio.setText(medio)
        self.ui.lineEd_medio.setDisabled(True)
        self.ui.plainTextEd_notas.setPlainText(notas)

        self.ui.pushButton_guardar.clicked.connect(self.modificar)

    def modificar(self):
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        idmetodo = self.ui.lineEd_idMetodo.text()
        notas_nuevas = self.ui.plainTextEd_notas.toPlainText()
        cursor = db.cursor()
        cursor.execute("UPDATE metodos SET notas = %s WHERE id=%s",
                       (notas_nuevas,idmetodo))
        db.commit()
        db.close()
        self.close()
