import sys
from PyQt5 import QtWidgets, QtGui

class window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.start()
	def start(self):
		self.setWindowTitle("Sample3")
		self.setGeometry(100,100,300,130)
		self.setStyleSheet("QWidget {background-color: gray}")
		self.ui_setup()
		self.show()
	def ui_setup(self):
		self.l1 = QtWidgets.QLabel(self)
		self.l1.setPixmap(QtGui.QPixmap("logo.png"))

		self.l2 = QtWidgets.QLabel(self)
		self.l2.setText("Hello World")

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Button")
		self.b1.setStyleSheet("QPushButton {background-color: white}")
		self.b1.clicked.connect(self.b1_clicked)

		self.h1_box = QtWidgets.QHBoxLayout()
		self.h1_box.addStretch()
		self.h1_box.addWidget(self.l1)
		self.h1_box.addStretch()

		self.h2_box = QtWidgets.QHBoxLayout()
		self.h2_box.addStretch()
		self.h2_box.addWidget(self.l2)
		self.h2_box.addStretch()

		self.v_box = QtWidgets.QVBoxLayout()
		self.v_box.addLayout(self.h1_box)
		self.v_box.addLayout(self.h2_box)
		self.v_box.addWidget(self.b1)
		self.setLayout(self.v_box)
	def b1_clicked(self):
		self.l2.setText("I have been clicked")

app = QtWidgets.QApplication(sys.argv)
w = window()
sys.exit(app.exec_())