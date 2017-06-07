import sys
import speech_recognition as sr
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.start()
	def start(self):
		self.setWindowTitle("Sample8")
		self.resize(300, 150)
		self.ui_setup()
		self.show()
	def ui_setup(self):
		self.txt = QtWidgets.QTextEdit(self)
		self.txt.setText("กดปุ่มเพื่ออัดเสียงแล้วพูดเลย")

		self.btn = QtWidgets.QPushButton(self)
		self.btn.setText("อัดเสียง")
		self.btn.clicked.connect(self.btn_clicked)

		self.v_box = QtWidgets.QVBoxLayout(self)
		self.v_box.addWidget(self.txt)
		self.v_box.addWidget(self.btn)
		self.setLayout(self.v_box)

	def btn_clicked(self):
		self.txt.setText("")

		rec = sr.Recognizer()

		with sr.Microphone() as source:
			audio = rec.listen(source)
		try:
			text = rec.recognize_google(audio, language = "th-TH") 
			print(text)
			self.txt.setText(text)
		except sr.RequestError as e:
			print("Could not understand audio")
			print("ไม่เข้าใจเสียง !")

app = QtWidgets.QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())