from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from source.lib.core import find_match, get_file_extension

from os import path, listdir, rename

import pandas as pd


class MainWindow(QObject):
    filePathChanged = pyqtSignal()
    folderPathChanged = pyqtSignal()
    startEnabled = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        self._filePath = None
        self._folderPath = None

    @pyqtProperty(bool, notify=startEnabled)
    def isStartEnabled(self):
        if self.folderPath and self.filePath:
            return True
        return False

    @pyqtProperty(str, notify=filePathChanged)
    def filePath(self):
        return self._filePath

    @filePath.setter
    def filePath(self, value):
        self._filePath = value
        self.startEnabled.emit()

    @pyqtProperty(str, notify=folderPathChanged)
    def folderPath(self):
        return self._folderPath

    @folderPath.setter
    def folderPath(self, value):
        self._folderPath = value
        self.startEnabled.emit()

    @pyqtSlot()
    def selectFolder(self):
        self.folderPath = QFileDialog.getExistingDirectory()
        self.folderPathChanged.emit()

    @pyqtSlot()
    def selectFile(self):
        self.filePath = QFileDialog.getOpenFileName(filter="Excel (*.xls, *.xlsx)")[0]
        self.filePathChanged.emit()

    @pyqtSlot()
    def start(self):
        targets = list(pd.read_excel(self.filePath, usecols=(0), squeeze=True, header=None))
        files = list(filter(lambda x: x.endswith('.jpg'), listdir(self.folderPath)))

        for file in files:
            try:
                target = find_match(file, targets)

                if target:
                    target += get_file_extension(file)

                    print(f'Renaming {file} -> {target}')
                    rename(path.join(self.folderPath, file), path.join(self.folderPath, target))

            except Exception as e:
                print(e)
