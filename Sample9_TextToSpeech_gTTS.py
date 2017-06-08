import sys
import os
from PyQt5 import QtWidgets
from gtts import gTTS
from pygame import mixer

mixer.init()

class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.start()
	def start(self):
		self.resize(300, 150)
		self.ui_setup()
		self.show()
	def ui_setup(self):
		self.lang = "th"

		self.txt_lang = QtWidgets.QLabel(self)
		self.txt_lang.setText("Thai")

		self.txt = QtWidgets.QTextEdit(self)
		self.txt.setText("กดปุ่มเพื่ออ่านข้อความ")

		self.btn = QtWidgets.QPushButton(self)
		self.btn.setText("อ่านข้อความ")
		self.btn.clicked.connect(self.btn_clicked)

		self.v_box = QtWidgets.QVBoxLayout(self)
		self.v_box.addWidget(self.txt_lang)
		self.v_box.addWidget(self.txt)
		self.v_box.addWidget(self.btn)
		self.setLayout(self.v_box)

	def btn_clicked(self):
		self.remove_file()
		tts = gTTS(text=self.txt.toPlainText(), lang=self.lang)
		tts.save("echoSound.mp3")
		mixer.music.load("echoSound.mp3")
		mixer.music.play()

		while mixer.music.get_busy() == True:
			continue

		mixer.music.load("echoTemp.mp3")
		self.remove_file()
	def remove_file(self):
		if os.path.exists("echoSound.mp3"):
			os.remove("echoSound.mp3")
	def remove_file_all(self):
		if os.path.exists("echoSound.mp3"):
			os.remove("echoSound.mp3")

class WindowAndMenuBar(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.from_widget = Window()
		self.setCentralWidget(self.from_widget)

		self.start()
	def start(self):
		self.menubar = self.menuBar()
		self.m_lang = self.menubar.addMenu("Langauge")

		self.m_lang_th = QtWidgets.QAction("Thai", self)
		self.m_lang_th.triggered.connect(lambda: self.trigger_lang("Thai"))
		self.m_lang_en = QtWidgets.QAction("English", self)
		self.m_lang_en.triggered.connect(lambda: self.trigger_lang("English"))

		self.m_lang.addAction(self.m_lang_th)
		self.m_lang.addAction(self.m_lang_en)

		self.setWindowTitle("Sample9")
		self.show()
	def trigger_lang(self, lang):
		self.from_widget.txt_lang.setText(lang)
		if lang == "Thai":
			self.from_widget.lang = "th"
		elif lang == "English":
			self.from_widget.lang = "en"

app = QtWidgets.QApplication(sys.argv)
w = WindowAndMenuBar()
sys.exit(app.exec_())