import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

ApplicationWindow {
    id: window
    width: 400
    height: 300
    visible: true

    background: Rectangle {
        gradient: Gradient {
            GradientStop { position: 0; color: "#ffffff" }
            GradientStop { position: 1; color: "#c1bbf9" }
        }
    }

    Column {
        anchors.centerIn: parent
        spacing: 20

        TextField {
            id: loginField
            placeholderText: "Login"
            font.pixelSize: 16
        }

        TextField {
            id: passwordField
            placeholderText: "Password"
            font.pixelSize: 16
            echoMode: TextInput.Password
        }

        Row {
            spacing: 10

            Button {
                text: "Log In"
                font.pixelSize: 16
                onClicked: {
                    // Здесь можно добавить обработчик нажатия кнопки "Log In"
                }
            }

            Button {
                text: "Clear"
                font.pixelSize: 16
                onClicked: {
                    loginField.text = ""
                    passwordField.text = ""
                }
            }
        }
    }
}
