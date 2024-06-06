import mysql.connector as mdb
from PySide2 import QtWidgets
from UI.nuevaPlanta import Ui_FormPlanta

class ventanaPlanta_modificar(QtWidgets.QWidget):
    def __init__(self,idvar,contlote,contplanta,venta,merma,reproducir):
        super().__init__()

        self.lote = contlote
        self.planta = contplanta
        self.ui = Ui_FormPlanta()
        self.ui.setupUi(self)

        self.ui.lineEd_idVar_in.setText(idvar)
        self.ui.spinBox_contLote_in.setValue(int(contlote))
        self.ui.lineEdit_numPlanta.setText(str(contplanta))
        self.ui.checkBox_venta.setChecked(bool(venta))
        self.ui.checkBox_merma.setChecked(bool(merma))
        self.ui.checkBox_repro.setChecked(bool(reproducir))
        if bool(merma):
            self.ui.checkBox_venta.setDisabled(True)
            self.ui.checkBox_repro.setDisabled(True)
        else:
            self.ui.checkBox_venta.setEnabled(True)
            self.ui.checkBox_repro.setEnabled(True)
            

        self.ui.checkBox_merma.stateChanged.connect(self.perder)

        self.ui.pushButton_guardar.clicked.connect(self.guardar)

    def guardar(self):
        venta = int(self.ui.checkBox_venta.isChecked())
        merma = int(self.ui.checkBox_merma.isChecked())
        reproducir = int(self.ui.checkBox_repro.isChecked())
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor.execute("UPDATE plantas SET venta = %s"
                       ", merma = %s, reproducir = %s"
                       " WHERE contLote = %s AND contPlanta = %s",
                       (venta,merma,reproducir,self.lote,self.planta))
        db.commit()
        db.close()
        self.close()
    
    def perder(self):
        merma = self.ui.checkBox_merma.isChecked()
        if merma is True:
            self.ui.checkBox_repro.setDisabled(True)
            self.ui.checkBox_repro.setChecked(False)
            self.ui.checkBox_venta.setDisabled(True)
            self.ui.checkBox_venta.setChecked(False)
        else:
            self.ui.checkBox_repro.setEnabled(True)
            self.ui.checkBox_venta.setEnabled(True)
