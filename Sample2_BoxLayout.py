import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	
	w = QtWidgets.QWidget()
	w.setWindowTitle("Sample2")
	w.setGeometry(100,100,300,130)
	w.setStyleSheet("QWidget {background-color: gray}")

	l1 = QtWidgets.QLabel(w)
	l1.setPixmap(QtGui.QPixmap("logo.png"))

	l2 = QtWidgets.QLabel(w)
	l2.setText("Hello World")

	b1 = QtWidgets.QPushButton(w)
	b1.setText("Button")
	b1.setStyleSheet("QPushButton {background-color: white}")

	h1_box = QtWidgets.QHBoxLayout()
	h1_box.addStretch()
	h1_box.addWidget(l1)
	h1_box.addStretch()

	h2_box = QtWidgets.QHBoxLayout()
	h2_box.addStretch()
	h2_box.addWidget(l2)
	h2_box.addStretch()

	v_box = QtWidgets.QVBoxLayout()
	v_box.addLayout(h1_box)
	v_box.addLayout(h2_box)
	v_box.addWidget(b1)
	w.setLayout(v_box)

	w.show()
	sys.exit(app.exec_())

window()