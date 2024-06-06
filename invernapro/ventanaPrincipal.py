import mysql.connector as mdb
from PySide2 import QtWidgets,QtCore
import datos as d
from UI.VentanaPrincipal import Ui_VentanaPrincipal
import ventanaVariedad as vv
import ventanaVariedad_modificar as vvm
import ventanaMetodo as vm
import ventanaMetodo_modificar as vmm
import ventanaNombre as vn
import ventanaNombre_modificar as vnm
import ventanaLote as vl
import ventanaLote_modificar as vln
import ventanaPlanta as vp
import busquedaAvanzada as BA


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        
        self.wvariedad = None
        self.wnombre = None
        self.wmetodo = None
        self.wlote = None
        self.wplanta = None
        self.busquedaAvanzada = None

        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        #tab2 propiedades
        self.ui.comboBox_busqueda_clase.setCurrentIndex(-1)
        self.ui.comboBox_busqueda_clase.currentIndexChanged.connect(self.busqueda_labels)
        self.ui.tableWidget_busqueda.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableWidget_busqueda.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_busqueda.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) 

        ####### tab1
        self.ui.pushButton_cultivo.clicked.connect(self.abrir_ventanaVariedad)
        self.ui.pushButton_nombre.clicked.connect(self.abrir_ventanaNombre)
        self.ui.pushButton_metodo.clicked.connect(self.abrir_ventanaMetodo)
        self.ui.pushButton_lote.clicked.connect(self.abrir_ventanaLote)

        ####### tab2
        self.ui.comboBox_busqueda_clase.currentIndexChanged.connect(self.combo_despliegue)
        self.ui.lineEdit_buscar_id.returnPressed.connect(self.buscar_id)
        self.ui.pushButton_seleccionar.clicked.connect(self.modificar_select)
        self.ui.pushButton_eliminar.clicked.connect(self.eliminar_select)

        ####### menu
        self.ui.actionPlantas_por_nombre.triggered.connect(lambda: self.avanzada(0))
        self.ui.actionNombres_de_planta.triggered.connect(lambda: self.avanzada(1))
        self.ui.actionEn_temporada.triggered.connect(lambda: self.avanzada(2))
        self.ui.actionPlantas_de_variedad.triggered.connect(lambda:self.avanzada(3))

    ######funciones de configuracion
    def abrir_ventanaVariedad(self):
        self.wvariedad = vv.ventanaVariedad()
        self.wvariedad.show()
    def abrir_ventanaNombre(self):
        self.wnombre = vn.ventanaNombre()
        self.wnombre.show()
    def abrir_ventanaMetodo(self):
        self.wmetodo = vm.ventanaMetodo()
        self.wmetodo.show()
    def abrir_ventanaLote(self):
        self.wlote = vl.ventanaLote()
        self.wlote.show()
    def closeEvent(self, event) -> None:
        """Cierra todas las ventanas activas"""
        self.wvariedad = None
        self.wnombre = None
        self.wmetodo = None
        self.wlote = None
        self.wplanta = None
        return super().closeEvent(event)

    ######funciones auxiliares
    def busqueda_labels(self):
        """Resuelve los diccionarios para el término de búsqueda principal"""
        self.ui.lineEdit_buscar_id.clear()
        indice = self.ui.comboBox_busqueda_clase.currentIndex()
        self.ui.label_primaria.setText(d.dict_primaria[indice]['b'] +":")
        self.ui.lineEdit_buscar_id.setEnabled(True)
        if indice == 4:
            self.ui.pushButton_eliminar.setDisabled(True)
        else:
            self.ui.pushButton_eliminar.setEnabled(True)

    def make_table(self,contents:list):
        """Imprime en el qtablewidget los resultados de un query"""
        self.ui.tableWidget_busqueda.setRowCount(len(contents))
        row=0
        for result in contents:
            col=0
            for data in result:
                cell = QtWidgets.QTableWidgetItem(str(data))
                self.ui.tableWidget_busqueda.setItem(row,col,cell)
                col +=1
            row += 1
        self.ui.tableWidget_busqueda.resizeColumnsToContents()

    def modificar_variedad(self,sql_res):
        """extrae los datos de una entrada en variedades 
        y llama a la ventada de modificación
        """
        self.wvariedad = vvm.ventanaVariedad(
                 id_var = sql_res['id'],
                 especie = sql_res['especie'],
                 variedad = sql_res['nombre'],
                 luz = sql_res['luz'],
                 riego = sql_res['riego'],
                 temporadas = sql_res['temporada'],
                 temperaturas = sql_res['temperatura'],
                 ph = sql_res['ph'])
        self.wvariedad.show()

    def modificar_nombre(self,sql_res):
        """Leé la linea de un nombre y llama a la ventada de modificación"""
        self.wnombre = vnm.ventanaNombre(nombre= sql_res['nombre'],idioma= sql_res['idioma'])
        self.wnombre.show()

    def modificar_metodo(self,sql_res):
        """leé la linea de un método y llama a la ventana de modificiación"""
        self.wmetodo = vmm.ventanaMetodo(idmetodo= sql_res['id'],
                                         organo= sql_res['organo'],
                                         medio= sql_res['medio'],
                                         notas= sql_res['notas'])
        self.wmetodo.show()

    def modificar_lote(self,sql_res):
        """Lee el cont de lote y recupera los datos para la ventada de modificación"""
        self.wlote = vln.ventanaLote(str(sql_res['cont']),
                                     sql_res['idVar'],
                                     sql_res['idMetodo'],
                                     str(sql_res['fecha']),
                                     str(sql_res['cantidad']))
        self.wlote.show()
    
    def modificar_planta(self,sql_res):
        """Recibe datos de un query  en plantas y los integra a la ventada de modificación"""
        self.wplanta = vp.ventanaPlanta_modificar(sql_res['variedad'],
                                                  sql_res['contLote'],
                                                  sql_res['contPlanta'],
                                                  sql_res['venta'],
                                                  sql_res['merma'],
                                                  sql_res['reproducir'])
        self.wplanta.show()

    #####funciones de acciones
    def combo_despliegue(self):
        """Despliegue inicial de tablas en la iu"""
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        indice = self.ui.comboBox_busqueda_clase.currentIndex()
        vista = d.dict_vistas[indice]
        headers = []
        contents = []
        cont = 0
        if indice == 4:
            self.ui.pushButton_eliminar.setDisabled(True)
        else:
            self.ui.pushButton_eliminar.setEnabled(True)
        cursor.execute("SELECT * from {};".format(vista))
        for x in cursor.description:
            headers.append(x[0])
        for x in cursor:
            contents.append(x)
            cont += 1
        self.ui.tableWidget_busqueda.setColumnCount(len(headers))
        self.ui.tableWidget_busqueda.setHorizontalHeaderLabels(headers)
        self.make_table(contents)
        self.ui.label_results.setText(f"Mostrando: {cont} resultados")
        db.close()

    def buscar_id(self):
        """Búsqueda en las tablas por llave principal"""
        self.ui.tableWidget_busqueda.clear()
        buscar = self.ui.lineEdit_buscar_id.text()
        indice = self.ui.comboBox_busqueda_clase.currentIndex()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        if indice == 1:
            cursor.execute("SELECT * from nombres WHERE nombre LIKE %s ORDER BY idioma;"
                           ,(buscar+'%',))
        else:
            cursor.execute("SELECT * from {}"
                    " WHERE {}"
                    " LIKE %s;"
                    .format(d.dict_vistas[indice],d.dict_primaria_vistas[indice]['a'])
                    ,(buscar+'%',))
        headers = []
        contents = []
        cont = 0
        for h in cursor.description:
            headers.append(h[0])
        for x in cursor:
            contents.append(x)
            cont +=1
        self.ui.tableWidget_busqueda.setHorizontalHeaderLabels(headers)
        self.make_table(contents)
        self.ui.label_results.setText(f"Mostrando: {cont} resultados")
        db.close()

    def modificar_select(self):
        """Selecciona la función de modificación a efectuar"""
        indice = self.ui.comboBox_busqueda_clase.currentIndex()
        tabla = d.dict_tablas[indice]
        atributo = d.dict_primaria[indice]['a']
        renglon = self.ui.tableWidget_busqueda.currentRow()
        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor(dictionary=True)
        if indice == 4:
            llave_p = self.ui.tableWidget_busqueda.item(renglon,1).text()
            llave_s = self.ui.tableWidget_busqueda.item(renglon,2).text()
            cursor.execute("SELECT * FROM cultivo_plantas WHERE contLote = %s "
                           "AND contPlanta = %s",(llave_p,llave_s))
        else:
            llave_p = self.ui.tableWidget_busqueda.item(renglon,0).text()
            cursor.execute("SELECT * FROM {} WHERE {} = %s".format(tabla,atributo),(llave_p,))
        x = cursor.fetchone()
        db.close()
        if indice == 0:
            self.modificar_variedad(x)
        elif indice == 1:
            self.modificar_nombre(x)
        elif indice == 2:
            self.modificar_metodo(x)
        elif indice == 3:
            self.modificar_lote(x)
        elif indice == 4:
            self.modificar_planta(x)

    def eliminar_select(self):
        """Elimina entradas de todas las tablas"""
        indice = self.ui.comboBox_busqueda_clase.currentIndex()
        clase = d.dict_tablas[indice]
        llave = d.dict_primaria[indice]['a']
        renglon = self.ui.tableWidget_busqueda.currentRow()
        busqueda = self.ui.tableWidget_busqueda.item(renglon,0).text()

        db = mdb.connect(user='invernadmin',
                        password='password',
                        host='localhost',
                        database='invernapro')
        cursor = db.cursor()
        cursor.execute("DELETE FROM {} WHERE {} = %s;".format(clase,llave),(busqueda,))
        db.commit()
        db.close()
        self.combo_despliegue()

    # @QtCore.Slot()
    def avanzada(self,tab):
        """Ventana de búsquedas especiales"""
        self.busquedaAvanzada = BA.busquedaAvanzada(tab)
        self.busquedaAvanzada.show()
