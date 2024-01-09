import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

class EmbeddedWebApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Twitter V1 By Sakusai")
        self.setGeometry(100, 100, 800, 600)
        icon_path = "twt.ico"
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("Twitter V1 By Sakusai")
        self.setWindowIcon(QIcon(icon_path))
        self.webview = QWebEngineView(self)
        self.setCentralWidget(self.webview)
        self.webview.setUrl(QUrl("https://twitter.com"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmbeddedWebApp()
    window.show()
    sys.exit(app.exec_())
