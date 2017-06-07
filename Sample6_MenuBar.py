import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.start()
	def start(self):
		self.screen = QtWidgets.QDesktopWidget().availableGeometry()
		self.setWindowTitle("Sample6")
		self.setStyleSheet("QWidget {background-color: gray}")
		self.setGeometry((self.screen.width()/2)-130, (self.screen.height()/2)-50, 260, 100)
		self.menubar_set()
		self.show()
	def menubar_set(self):
		self.menubar = self.menuBar()

		self.m_file = self.menubar.addMenu("File")

		self.m_file_exit = QtWidgets.QAction("Exit", self)
		self.m_file_exit.setShortcut("Ctrl+Q")
		self.m_file_exit.triggered.connect(self.trigger_quit)

		self.m_file.addAction(self.m_file_exit)

		self.m_edit = self.menubar.addMenu("Edit")
		self.m_edit_color = self.m_edit.addMenu("Colors")

		self.m_edit_color_red = QtWidgets.QAction("Red", self)
		self.m_edit_color_green = QtWidgets.QAction("Green", self)
		self.m_edit_color_blue = QtWidgets.QAction("Blue", self)
		self.m_edit_color_gray = QtWidgets.QAction("Gray", self)

		self.m_edit_color_red.triggered.connect(lambda: self.trigger_color("red"))
		self.m_edit_color_green.triggered.connect(lambda: self.trigger_color("green"))
		self.m_edit_color_blue.triggered.connect(lambda: self.trigger_color("blue"))
		self.m_edit_color_gray.triggered.connect(lambda: self.trigger_color("gray"))

		self.m_edit_color.addAction(self.m_edit_color_red)
		self.m_edit_color.addAction(self.m_edit_color_green)
		self.m_edit_color.addAction(self.m_edit_color_blue)
		self.m_edit_color.addAction(self.m_edit_color_gray)
	def trigger_quit(self):
		QtWidgets.qApp.quit()
	def trigger_color(self, cols):
		self.setStyleSheet("QWidget {background-color: %s}" %cols)

app = QtWidgets.QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())