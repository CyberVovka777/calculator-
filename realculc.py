from PySide import QtCore, QtGui
import sys
from culc_ui import Ui_Dialog
import math
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#(1)def bp():
#ui.lineEdit.setText("9")
def clear():
	ui.lineEdit.clear()	
	ui.lineEdit_2.clear()
	ui.lineEdit_3.clear()
	ui.lineEdit_4.clear()
ui.pushButton_11.clicked.connect( clear )
def rus():
	a=int(ui.lineEdit.text())
	b=int(ui.lineEdit_2.text())
	c=int(ui.lineEdit_3.text())
	xxx=(b*b) -4 * a * c
	if xxx < 0:
		ui.lineEdit_4.setText("Дескриминант меньше нуля !!!")
	xxG=(math.sqrt(xxx))
	x1=(-b+xxG)//(2* a)
	x2=(-b-xxG)//(2* a)
	ui.lineEdit_4.setText("    "+"x1=" + str(x1) +"                          "+ "x2=" + str(x2))



ui.pushButton_13.clicked.connect( rus )
def mbox(self, body, title='Error'):
    dialog = QMessageBox(QMessageBox.Information, title, body)
    dialog.exec_()
#(1)ui.pushButton_8.clicked.connect( bp )	
sys.exit(app.exec_())