import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: root

    // Свойства для настройки страницы
    property alias backgroundColor: background.color
    property alias buttonText1: button1.text
    property alias buttonText2: button2.text
    property string pageTitle: ""
    property bool useReplace: false  // Новый флаг для выбора навигации

    signal button1Clicked()
    signal button2Clicked()

    // Фон страницы
    Rectangle {
        id: background
        anchors.fill: parent
        color: backgroundColor

        Column {
            anchors.centerIn: parent
            spacing: 20

            // Кнопка 1
            Button {
                id: button1
                text: "Button 1"
                onClicked: root.button1Clicked()

                contentItem: Text {
                    text: parent.text
                    color: "black"
                }
            }

            // Кнопка 2
            Button {
                id: button2
                text: "Button 2"
                onClicked: root.button2Clicked()

                contentItem: Text {
                    text: parent.text
                    color: "black"
                }
            }
        }
    }

    // Заголовок страницы
    header: ToolBar {
        RowLayout {
            spacing: 10

            ToolButton {
                text: "<-"
                visible: stackView.depth > 1  // Показываем кнопку "Назад", если глубина > 1
                onClicked: stackView.pop()
            }

            Label {
                text: pageTitle
                font.pixelSize: 18
                Layout.alignment: Qt.AlignCenter
            }
        }
    }
}
