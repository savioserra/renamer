import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from source.view.main_window.main_window import MainWindow


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    mainWindow = MainWindow()
    engine.rootContext().setContextProperty('MainWindow', mainWindow)

    engine.load(resource_path('./source/view/main_window/main_window.qml'))
    engine.quit.connect(app.quit)

    sys.exit(app.exec_())