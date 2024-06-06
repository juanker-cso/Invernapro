import time
import random
import mysql.connector as mdb
from PySide2 import QtWidgets#, QtSql
from UI.nuevaVariedad import Ui_FormVariedad

import datos as d


class ventanaVariedad(QtWidgets.QWidget):
    """Ventana de registro de plantas"""
    def __init__(self):
        super().__init__()

        self.ui = Ui_FormVariedad()
        self.ui.setupUi(self)

        self.ui.doubleSpinBox_ph.setValue(7.0)
        self.ui.comboBox_luz.setCurrentIndex(0)
        self.ui.lineEdit_temp1.setPlaceholderText("Mínimo")
        self.ui.lineEdit_temp2.setPlaceholderText("Máximo")
        self.ui.lineEd_mes1.setPlaceholderText("num inicio")
        self.ui.lineEd_mes2.setPlaceholderText("num fin")

        self.ui.lineEd_nombre.textEdited.connect(self.calc_ID)
        self.ui.lineEd_variedad.textEdited.connect(self.calc_ID)
        self.ui.pushButton_guardar.clicked.connect(self.agregar)
        self.ui.pushButton_newnombre.clicked.connect(self.check_nombre)
        self.ui.lineEdit_addnombre.returnPressed.connect(self.check_nombre)
        self.ui.pushButton_deletenombre.clicked.connect(self.remove_nombre)
        self.ui.pushButton_newmetodo.clicked.connect(self.check_metodo)
        self.ui.lineEdit_addmetodo.returnPressed.connect(self.check_metodo)
        self.ui.pushButton_deletemetodo.clicked.connect(self.remove_metodo)

    def check_nombre(self):
        """Añade nombre a la lista de nombres"""
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        nombreC = self.ui.lineEdit_addnombre.text()
        if not d.check_id(db,"nombres","nombre",nombreC):
            QtWidgets.QMessageBox.warning(self,"Error:","Nombre no encontrado")
            self.ui.lineEdit_addnombre.clear()
            return
        self.ui.listWidget_nombres.addItem(nombreC.capitalize())
        self.ui.lineEdit_addnombre.clear()
        db.close()

    def remove_nombre(self):
        """Quita nombre de la lista"""
        r = self.ui.listWidget_nombres.currentRow()
        it = self.ui.listWidget_nombres.takeItem(r)
        del it

    def check_metodo(self):
        """Añade id de metodo a lista de metodos"""
        metodoN = self.ui.lineEdit_addmetodo.text()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        if not d.check_id(db,"metodos","id",metodoN):
            QtWidgets.QMessageBox.warning(self,"Error:","Método no encontrado")
            self.ui.lineEdit_addmetodo.clear()
            return
        self.ui.listWidget_metodos.addItem(metodoN)
        self.ui.lineEdit_addmetodo.clear()
        

    def remove_metodo(self):
        """Quitar metodo de la lista"""
        r = self.ui.listWidget_metodos.currentRow()
        it = self.ui.listWidget_metodos.takeItem(r)
        del it

    def calc_ID(self):
        """Calcula el id a partir de los cambios de linea"""
        Idgen=""
        especie = variedad = ""
        especie = self.ui.lineEd_nombre.text()
        variedad = self.ui.lineEd_variedad.text()
        especie = d.remove_vocales(especie)
        variedad = d.remove_vocales(variedad)
        Idgen = especie[0:4]
        Idgen += variedad[0:4]
        Idgen = d.fill_cadena_suffix(Idgen,8,"-")
        Idgen = Idgen.upper()
        random.seed(time.time())
        Idgen += str(random.randrange(0,9))
        Idgen += str(random.randrange(0,9))
        self.ui.lineEd_idVar.setText(Idgen)

    def agregar(self):
        if (self.ui.lineEd_nombre.text() == ""
            or self.ui.lineEd_variedad.text() == ""
            or self.ui.spinBox_luz.text() == "0"):
            QtWidgets.QMessageBox.warning(self,"Error:","Campos requeridos faltantes")
            return
        idvar = self.ui.lineEd_idVar.text()
        datos = "'"
        datos += idvar +"','"
        datos += self.ui.lineEd_nombre.text().capitalize() +"','"
        datos += self.ui.lineEd_variedad.text().capitalize() +"','"

        luzT = self.ui.comboBox_luz.currentText()
        luzH = self.ui.spinBox_luz.text()
        luzH = d.fill_cadena_prefix(luzH,2,"0")
        datos += luzT + luzH +"','"
        datos += str(self.ui.spinBox_riego.value() / 100) +"','"

        mes1 = self.ui.lineEd_mes1.text()
        mes1 = d.fill_cadena_prefix(mes1,2,"0")
        mes2 = self.ui.lineEd_mes2.text()
        mes2 = d.fill_cadena_prefix(mes2,2,"0")
        datos += mes1 + mes2 +"','"

        temp1 = self.ui.lineEdit_temp1.text()
        temp1 = d.fill_cadena_prefix(temp1,3,"0")
        temp2 = self.ui.lineEdit_temp2.text()
        temp2 = d.fill_cadena_prefix(temp2,3,"0")

        datos += temp1 + temp2 +"','"
        datos += self.ui.doubleSpinBox_ph.text() +"'"

        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')

        mensage = d.agregar_datos(db,datos,"variedades")
        if mensage == "E":
            QtWidgets.QMessageBox.information(self,"Exito","Registro Guardado",
                                              button0=QtWidgets.QMessageBox.Ok)
            self.calc_ID()
        else:
            QtWidgets.QMessageBox.warning(self,"Error:",mensage,button0=QtWidgets.QMessageBox.Ok)
            db.close()
            return
        cur = db.cursor()
        self.ui.listWidget_nombres.count()
        for renglon in range (self.ui.listWidget_nombres.count()):
            n = self.ui.listWidget_nombres.item(renglon).text()
            cur.execute("INSERT INTO variedadnombres values (%s,%s);",(idvar,n))
        for renglon in range (self.ui.listWidget_metodos.count()):
            m = self.ui.listWidget_metodos.item(renglon).text()
            cur.execute("INSERT INTO variedadmetodos values (%s,%s);",(idvar,m))
        db.commit()
        self.clearAll()

    def clearAll(self):
        self.ui.lineEd_nombre.clear()
        self.ui.lineEd_variedad.clear()
        self.ui.lineEd_idVar.clear()
        self.ui.comboBox_luz.setCurrentIndex(0)
        self.ui.spinBox_luz.clear()
        self.ui.spinBox_riego.clear()
        self.ui.lineEd_mes1.clear()
        self.ui.lineEd_mes2.clear()
        self.ui.lineEdit_temp1.clear()
        self.ui.lineEdit_temp2.clear()
        self.ui.doubleSpinBox_ph.setValue(7.0)
        self.ui.listWidget_nombres.clear()
        self.ui.listWidget_metodos.clear()
