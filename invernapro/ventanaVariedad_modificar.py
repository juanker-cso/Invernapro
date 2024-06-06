import mysql.connector as mdb
from PySide2 import QtWidgets#, QtSql
from UI.nuevaVariedad import Ui_FormVariedad

import datos as d


class ventanaVariedad(QtWidgets.QWidget):
    """Ventana de registro de plantas"""
    def __init__(self,
                 id_var:str,
                 especie:str,
                 variedad:str,
                 luz:str,
                 riego:str,
                 temperaturas:str,
                 temporadas:str,
                 ph:str):
        super().__init__()

        self.datos = ""
        self.idvar = id_var
        self.ui = Ui_FormVariedad()
        self.ui.setupUi(self)

        self.ui.lineEd_nombre.setDisabled(True)
        self.ui.lineEd_variedad.setDisabled(True)

        self.ui.lineEd_idVar.setText(id_var)
        self.ui.lineEd_nombre.setText(especie)
        self.ui.lineEd_variedad.setText(variedad)
        luz_tipo = d.get_llave(d.dict_luces,luz[0])
        self.ui.comboBox_luz.setCurrentIndex(luz_tipo)
        self.ui.spinBox_luz.setValue( int(luz[1:]))
        self.ui.spinBox_riego.setValue(int(riego*100))
        self.ui.lineEdit_temp1.setText(temperaturas[:3])
        self.ui.lineEdit_temp2.setText(temperaturas[3:])
        self.ui.lineEd_mes1.setText(temporadas[:2])
        self.ui.lineEd_mes2.setText(temporadas[2:])
        self.ui.doubleSpinBox_ph.setValue(float(ph))
        self.query_listas()

        self.ui.pushButton_newnombre.clicked.connect(self.agregar_nombre)
        self.ui.lineEdit_addnombre.returnPressed.connect(self.agregar_nombre)
        self.ui.pushButton_deletenombre.clicked.connect(self.remover_nombre)
        
        self.ui.pushButton_newmetodo.clicked.connect(self.agregar_metodo)
        self.ui.lineEdit_addmetodo.returnPressed.connect(self.agregar_metodo)
        self.ui.pushButton_deletemetodo.clicked.connect(self.remover_metodo)
        
        self.ui.pushButton_guardar.clicked.connect(self.modificar)
    
    def query_listas(self):
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor.execute("SELECT nombrecomun FROM variedadnombres WHERE idVar = %s",
                       (self.idvar,))
        for n in cursor:
            self.ui.listWidget_nombres.addItem(n[0])
        cursor.execute("SELECT idmetodo FROM variedadmetodos WHERE idVar = %s",
                       (self.idvar,))
        for m in cursor:
            self.ui.listWidget_metodos.addItem(m[0])
        db.close()
    
    def agregar_nombre(self):
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        nombreC = self.ui.lineEdit_addnombre.text().capitalize()
        if not d.check_id(db,"nombres","nombre",nombreC):
            QtWidgets.QMessageBox.warning(self,"Error:","Nombre no encontrado")
            self.ui.lineEdit_addnombre.clear()
            return
        self.ui.listWidget_nombres.addItem(nombreC)
        cursor.execute("INSERT INTO variedadnombres VALUES (%s,%s);",(self.idvar,nombreC,))
        self.ui.lineEdit_addnombre.clear()
        db.commit()
        db.close()
    
    def remover_nombre(self):
        r = self.ui.listWidget_nombres.currentRow()
        nombre = self.ui.listWidget_nombres.currentItem().text()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor.execute("DELETE FROM variedadnombres "
                            "WHERE idVar = %s AND nombrecomun = %s;",
                            (self.idvar,nombre))
        it = self.ui.listWidget_nombres.takeItem(r)
        del it
        db.commit()
        db.close()
    
    def agregar_metodo(self):
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        metodoN = self.ui.lineEdit_addmetodo.text().lower()
        if not d.check_id(db,"metodos","id",metodoN):
            QtWidgets.QMessageBox.warning(self,"Error:","Método no encontrado")
            self.ui.lineEdit_addmetodo.clear()
            return
        self.ui.listWidget_metodos.addItem(metodoN)
        cursor.execute("INSERT INTO variedadmetodos VALUES (%s,%s)",(self.idvar,metodoN,))
        self.ui.lineEdit_addmetodo.clear()
        db.commit()
        db.close()
    
    def remover_metodo(self):
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        r = self.ui.listWidget_metodos.currentRow()
        metodo = self.ui.listWidget_metodos.currentItem().text()
        cursor.execute("DELETE FROM variedadmetodos "
                            "WHERE idVar = %s AND idMetodo = %s",
                            (self.idvar,metodo))
        it = self.ui.listWidget_metodos.takeItem(r)
        del it
        db.commit()
        db.close()

    def modificar(self):
        """Guardar los cambios"""
        luzT = self.ui.comboBox_luz.currentText()
        luzH = self.ui.spinBox_luz.text()
        luzH = d.fill_cadena_prefix(luzH,2,"0")
        
        luz = luzT + luzH
        riego= str(self.ui.spinBox_riego.value() / 100)

        mes1 = self.ui.lineEd_mes1.text()
        mes1 = d.fill_cadena_prefix(mes1,2,"0")
        mes2 = self.ui.lineEd_mes2.text()
        mes2 = d.fill_cadena_prefix(mes2,2,"0")
        
        temporada= mes1 + mes2

        temp1 = self.ui.lineEdit_temp1.text()
        temp1 = d.fill_cadena_prefix(temp1,3,"0")
        temp2 = self.ui.lineEdit_temp2.text()
        temp2 = d.fill_cadena_prefix(temp2,3,"0")

        temperatura = temp1 + temp2
        ph = self.ui.doubleSpinBox_ph.text()

        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        command = ("UPDATE variedades SET luz = %s,"
                   "riego = %s,"
                   "temporada = %s,"
                   "temperatura = %s,"
                   "ph = %s"
                   " WHERE id = %s")
        values = (luz,riego,temporada,temperatura,ph,self.idvar)
        cursor.execute(command, values)

        db.commit()
        db.close()
        self.close()
