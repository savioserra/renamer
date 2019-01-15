import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

from source.view.main_window.main_window import MainWindow
from source.lib.core import resource_path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    mainWindow = MainWindow()
    engine.rootContext().setContextProperty('MainWindow', mainWindow)

    engine.load(resource_path('./source/view/main_window/main_window.qml'))
    engine.quit.connect(app.quit)

    sys.exit(app.exec_())
