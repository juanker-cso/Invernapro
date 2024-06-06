import mysql.connector as mdb
from PySide2 import QtWidgets
from UI.nuevoNombre import Ui_FormNombre

class ventanaNombre(QtWidgets.QWidget):
    def __init__(self, nombre:str, idioma:str):
        super().__init__()

        self.ui = Ui_FormNombre()
        self.ui.setupUi(self)

        self.nombre = nombre
        self.idioma = idioma

        self.ui.lineEd_nombre.setText(self.nombre)
        self.ui.lineEd_idioma.setText(self.idioma)
        self.ui.lineEd_nombre.setDisabled(True)

        self.ui.pushButton_guardar.clicked.connect(self.modificar)

    def modificar(self):
        if self.ui.lineEd_nombre.text() == "":
            QtWidgets.QMessageBox.warning(self,"Error:","Nombre requerido")
            return

        idioma = self.ui.lineEd_idioma.text().capitalize()

        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        vals = (idioma,self.nombre)
        cursor.execute("UPDATE nombres "
                       "SET idioma = %s "
                       "WHERE nombre = %s;",vals)
        db.commit()
        db.close()
        self.close()
