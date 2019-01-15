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
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        anchors.fill: parent
        flow: Grid.TopToBottom
        columns: 2
        rows: 4

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

        Flickable {
            Layout.columnSpan: 2
            Layout.fillWidth: true
            Layout.fillHeight: true

            TextArea.flickable: TextArea {
                id: logArea
                wrapMode: Text.NoWrap
                anchors.fill: parent
            }
        }

        Button {
            text: "Iniciar"
            Layout.fillWidth: true
            Layout.columnSpan:  2
            onClicked: MainWindow.start()
            enabled: MainWindow.isStartEnabled
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

    Connections {
        target: MainWindow

        onLog: {
            logArea.append(log)
        }
    }
}
