import sys
import speech_recognition as sr
from PyQt5 import QtWidgets

rec = sr.Recognizer()
with sr.WavFile("Sample2.wav") as source:
	audio = rec.record(source)
try:
	text = rec.recognize_google(audio) 
	print(text)
except sr.RequestError as e:
	print("Could not understand audio")

class Window(QtWidgets.QWidget):
	def __init__(self, text):
		super().__init__()
		self.text = text
		self.start()
	def start(self):
		self.setWindowTitle("Sample7")
		self.resize(300, 100)
		self.ui_setup()
		self.show()
	def ui_setup(self):
		self.txt = QtWidgets.QTextEdit(self)
		self.txt.setText(self.text)

		self.v_box = QtWidgets.QVBoxLayout(self)
		self.v_box.addWidget(self.txt)
		self.setLayout(self.v_box)

app = QtWidgets.QApplication(sys.argv)
w = Window(text)
sys.exit(app.exec_())