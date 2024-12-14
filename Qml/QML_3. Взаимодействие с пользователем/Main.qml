import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    width: 400
    height: 600
    visible: true
    title: "Task_for_Signal"

    Column {
        anchors.fill: parent
        spacing: 0

        Rectangle {
            id: header
            width: parent.width
            height: 50
            color: "lightgrey"
            border.color: "black"

            Text {
                id: headerText
                anchors.centerIn: parent
                text: "Header"
                font.pixelSize: 20
            }
        }

        Rectangle {
            id: content
            width: parent.width
            height: parent.height - header.height - footer.height
            color: "white"
            border.color: "black"

            Text {
                id: contentText
                anchors.centerIn: parent
                text: "Some content"
                font.pixelSize: 16
            }
        }

        Row {
            id: footer
            width: parent.width
            height: 50
            spacing: 0

            Repeater {
                model: 3
                Rectangle {
                    width: footer.width / 3
                    height: footer.height
                    color: "lightgrey"
                    border.color: "black"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            headerText.text = "Header " + (index + 1);
                            contentText.text = "Item " + (index + 1) + " content";
                            for (var i = 0; i < footer.children.length; i++) {
                                footer.children[i].opacity = (i === index ? 1.0 : 0.5);
                            }
                        }
                    }

                    Text {
                        anchors.centerIn: parent
                        text: "Item " + (index + 1)
                        font.pixelSize: 14
                    }
                }
            }
        }
    }
}
