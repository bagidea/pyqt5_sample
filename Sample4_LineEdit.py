import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.start()
	def start(self):
		self.screen = QtWidgets.QDesktopWidget().availableGeometry()
		self.setWindowTitle("Sample4")
		self.setGeometry((self.screen.width()/2)-150, (self.screen.height()/2)-50, 300, 100)
		self.setStyleSheet("QWidget {background-color: gray}")
		self.ui_setup()
		self.show()
	def ui_setup(self):
		self.l1 = QtWidgets.QLabel(self)
		self.l1.setText("Hello World")

		self.le = QtWidgets.QLineEdit()
		self.le.setStyleSheet("QLineEdit {background-color: white}")

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Enter")
		self.b1.setStyleSheet("QPushButton {background-color: white}")
		self.b1.clicked.connect(self.btn_clicked)

		self.b2 = QtWidgets.QPushButton(self)
		self.b2.setText("Clear")
		self.b2.setStyleSheet("QPushButton {background-color: red}")
		self.b2.clicked.connect(self.btn_clicked)

		self.h_box = QtWidgets.QHBoxLayout()
		self.h_box.addStretch()
		self.h_box.addWidget(self.l1)
		self.h_box.addStretch()

		self.v_box = QtWidgets.QVBoxLayout()
		self.v_box.addLayout(self.h_box)
		self.v_box.addWidget(self.le)
		self.v_box.addWidget(self.b1)
		self.v_box.addWidget(self.b2)
		self.setLayout(self.v_box)
	def btn_clicked(self):
		sender = self.sender()
		if sender.text() == "Enter" and self.le.text() != "":
			self.l1.setText(self.le.text())
			self.le.setText("")
		elif sender.text() == "Clear":
			self.le.setText("") 

app = QtWidgets.QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())