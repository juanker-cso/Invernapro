import mysql.connector as mdb
from PySide2 import QtWidgets, QtCore
from UI.busquedaAvanzada import Ui_busquedaAvanzada

class busquedaAvanzada(QtWidgets.QWidget):
    """Ventana de las búsquedas"""
    def __init__(self, tab) -> None:
        super().__init__()

        self.ui = Ui_busquedaAvanzada()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(tab)
        self.ui.lineEd_idPlanta_2.setPlaceholderText("ID completo")

        if tab == 2:
            self.ui.dateEd_busqueda.setDate(QtCore.QDate.currentDate())
            self.plantas_de_temporada()

        self.ui.lineEd_nombrePlanta.returnPressed.connect(self.variedad_de_nombre)
        self.ui.lineEd_idPlanta.returnPressed.connect(self.nombres_de_variedad)
        self.ui.lineEd_idPlanta_2.returnPressed.connect(self.plantas_de_variedad)
    
    def print_table(self,cursor):
        headers = []
        contents = []
        for h in cursor.description:
            headers.append(h[0])
        for c in cursor:
            contents.append(c)
        self.ui.tableWidget_resultados.setColumnCount(len(headers))
        self.ui.tableWidget_resultados.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget_resultados.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_resultados.setRowCount(len(contents))
        row=0
        for result in contents:
            col=0
            for data in result:
                cell = QtWidgets.QTableWidgetItem(str(data))
                self.ui.tableWidget_resultados.setItem(row,col,cell)
                col +=1
            row += 1

    def variedad_de_nombre(self):
        nombre_busqueda = self.ui.lineEd_nombrePlanta.text()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor.execute("SELECT id,especie,nombre FROM variedades "
                       "WHERE id IN (SELECT idVar FROM variedadnombres "
                       "WHERE nombrecomun LIKE %s);",(nombre_busqueda+'%',))
        self.print_table(cursor)
        db.close()

    def nombres_de_variedad(self):
        variedad_busqueda = self.ui.lineEd_idPlanta.text()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM nombres WHERE nombre "
                       "IN (SELECT nombrecomun from variedadnombres "
                       "WHERE idVar = %s) ORDER BY idioma;",(variedad_busqueda,))
        self.print_table(cursor)
        db.close()

    def plantas_de_temporada(self):
        self.ui.dateEd_busqueda.setDate(QtCore.QDate.currentDate())
        fecha = QtCore.QDate.month(QtCore.QDate.currentDate())
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor.execute("SELECT id, especie, nombre, cast(`mes inicio` AS UNSIGNED) AS inicio,"
                       " cast(`mes fin` AS UNSIGNED) as fin FROM ver_variedades"
                       " WHERE cast(`mes inicio` AS UNSIGNED) <= %s"
                       " AND  cast(`mes fin` AS UNSIGNED) >= %s;",(fecha,fecha))
        self.print_table(cursor)
        db.close()
    
    def plantas_de_variedad(self):
        variedad_busqueda = self.ui.lineEd_idPlanta_2.text()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        try:
            cursor.execute("SELECT contLote, contPlanta FROM cultivo_plantas"
                       " WHERE variedad = %s AND merma = 0;",(variedad_busqueda,))
        except mdb.Error:
            QtWidgets.QMessageBox.warning(self,"Error:","ID no encontrado")
            db.close()
            return
        self.print_table(cursor)
        db.close()
