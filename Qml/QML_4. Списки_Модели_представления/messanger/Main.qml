import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Window {
    width: 360
    height: 640
    visible: true
    title: "Messenger with RSS"

    // Модель для хранения сообщений
    ListModel {
        id: messageModel
        ListElement { name: "Alice"; message: "Hello!"; time: "10:30" }
        ListElement { name: "Bob"; message: "Hi! How are you?"; time: "10:31" }
    }

    // Главная страница
    Page {
        anchors.fill: parent

        // Список сообщений
        ListView {
            id: listView
            anchors.fill: parent
            model: messageModel
            spacing: 6

            // Делегат для отображения сообщений
            delegate: Item {
                width: listView.width
                height: 60

                Rectangle {
                    anchors.fill: parent
                    radius: 5
                    gradient: Gradient {
                        GradientStop { position: 0; color: "lightblue" }
                        GradientStop { position: 1; color: "white" }
                    }
                    border.color: "gray"

                    RowLayout {
                        anchors.margins: 10
                        anchors.fill: parent
                        spacing: 10

                        Text {
                            text: model.name + ":"
                            font.bold: true
                            Layout.alignment: Qt.AlignTop
                        }
                        Text {
                            text: model.message
                            Layout.fillWidth: true
                            wrapMode: Text.WordWrap
                        }
                        Text {
                            text: model.time
                            font.pixelSize: 10
                            color: "gray"
                            Layout.alignment: Qt.AlignRight
                        }
                    }
                }
            }
        }

        // Footer для ввода новых сообщений
        Rectangle {
            id: footer
            height: 60
            width: parent.width
            anchors.bottom: parent.bottom
            color: "#2E3B4E" // Темно-синий фон
            border.color: "#1E2933" // Тёмная граница
            border.width: 1

            RowLayout {
                anchors.fill: parent
                anchors.margins: 5 // Небольшие отступы
                spacing: 10

                TextField {
                    id: messageInput
                    Layout.fillWidth: true
                    placeholderText: "Write a message..."
                    placeholderTextColor: "#B0BEC5" // Серый текст для плейсхолдера
                    color: "white" // Белый текст
                    background: Rectangle {
                        color: "#1E2933" // Тёмный фон для текстового поля
                        radius: 5
                    }
                }

                Button {
                    text: "Send"
                    font.bold: true
                    Layout.preferredWidth: 80
                    background: Rectangle {
                        color: "#4CAF50" // Зеленый фон кнопки
                        radius: 5
                    }
                    contentItem: Text {
                        text: parent.text
                        color: "white" // Белый цвет текста кнопки
                        font.bold: true
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                    onClicked: {
                        if (messageInput.text !== "") {
                            // Добавляем новое сообщение в модель
                            var currentTime = Qt.formatTime(new Date(), "hh:mm");
                            messageModel.append({
                                "name": "You",
                                "message": messageInput.text,
                                "time": currentTime
                            });
                            messageInput.text = ""; // Очищаем поле ввода
                        }
                    }
                }
            }
        }
    }
}
