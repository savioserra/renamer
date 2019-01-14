import QtQuick 2.0
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.0

ApplicationWindow {
    id: applicationWindow
    title: "Renamer"
    visible: true
    height: 200
    width: 500

    GridLayout {
        id: grid
        anchors.rightMargin: 40
        anchors.leftMargin: 40
        anchors.bottomMargin: 40
        anchors.topMargin: 40
        flow: Grid.TopToBottom
        anchors.fill: parent
        columns: 2
        rows: 3

        TextField {
            placeholderText: "Caminho do arquivo .xlsx"
            Layout.fillWidth: true
            enabled: false
            text: MainWindow.filePath
        }

        TextField {
            placeholderText: "Caminho da pasta com imagens"
            Layout.fillWidth: true
            enabled: false
            text: MainWindow.folderPath
        }

        Button {
            text: "Iniciar"
            Layout.fillWidth: true
            Layout.columnSpan:  2
            enabled: MainWindow.isStartEnabled
            onClicked: MainWindow.start()
        }

        Button {
            text: "Selecionar arquivo .xlsx"
            Layout.maximumWidth: 150
            Layout.fillWidth: true
            onClicked: MainWindow.selectFile()
        }

        Button {
            text: "Selecionar pasta"
            Layout.maximumWidth: 150
            Layout.fillWidth: true
            onClicked: MainWindow.selectFolder()
        }
    }
}
