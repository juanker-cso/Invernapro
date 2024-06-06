import sys
from PySide2 import QtCore, QtWidgets
import ventanaPrincipal as VP

app =  QtWidgets.QApplication()
window = VP.MainWindow()

File = QtCore.QFile("UI/themes/Diplaytap.qss")

File.open( QtCore.QFile.ReadOnly | QtCore.QFile.Text)
qss = QtCore.QTextStream(File)
app.setStyleSheet(qss.readAll())

window.show()
sys.exit(app.exec_())
