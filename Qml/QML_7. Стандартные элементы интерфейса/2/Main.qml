import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 320
    height: 480
    title: "Password Input Page"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Text {
            text: "Enter your password:"
            font.pixelSize: 18
            Layout.alignment: Qt.AlignCenter
        }

        RowLayout {
            id: passwordRow
            spacing: 10
            Layout.alignment: Qt.AlignCenter

            Repeater {
                model: 6
                Rectangle {
                    width: 20; height: 20
                    color: index < passwordField.text.length ? "black" : "lightgrey"
                    radius: 10
                    Text {
                        text: "*"
                        font.pixelSize: 16
                        anchors.centerIn: parent
                        color: "white"
                    }
                }
            }
        }

        TextInput {
            id: passwordField
            echoMode: TextInput.Password
            visible: false
        }

        GridLayout {
            columns: 3
            rowSpacing: 10
            columnSpacing: 10
            Layout.alignment: Qt.AlignCenter

            Repeater {
                model: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Clear"]
                Button {
                    text: modelData
                    Layout.preferredWidth: 50
                    Layout.preferredHeight: 50
                    onClicked: {
                        if (modelData === "Clear") {
                            passwordField.text = "";
                        } else if (passwordField.text.length < 6) {
                            passwordField.text += modelData;
                        }
                    }
                }
            }
        }

        Button {
            text: "Log In"
            Layout.alignment: Qt.AlignCenter
            onClicked: {
                console.log("Entered Password: " + passwordField.text);
            }
        }
    }
}
