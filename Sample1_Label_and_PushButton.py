import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	
	w = QtWidgets.QWidget()
	w.setWindowTitle("Sample1")
	w.setGeometry(100,100,300,130)
	w.setStyleSheet("QWidget {background-color: gray}")

	l1 = QtWidgets.QLabel(w)
	l1.setPixmap(QtGui.QPixmap("logo.png"))
	l1.move(50, 5)

	l2 = QtWidgets.QLabel(w)
	l2.setText("Hello World")
	l2.move(130,60)

	b1 = QtWidgets.QPushButton(w)
	b1.setText("Button")
	b1.move(120, 90)
	b1.setStyleSheet("QPushButton {background-color: white}")

	w.show()
	sys.exit(app.exec_())

window()