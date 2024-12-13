import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "Task_for_Layout"

    Rectangle {
        anchors.fill: parent

        Rectangle {
            id: header
            height: parent.height * 0.1
            width: parent.width
            color: "lightgray"
            anchors.top: parent.top
            Text {
                anchors.centerIn: parent
                text: "Header"
            }
        }

        Rectangle {
            id: content
            anchors.top: header.bottom
            anchors.bottom: footer.top
            anchors.left: parent.left
            anchors.right: parent.right
            color: "white"
            border.color: "black"
            border.width: 2
            anchors.margins: 10
            Text {
                anchors.centerIn: parent
                text: "Content"
            }
        }

        Rectangle {
            id: footer
            height: parent.height * 0.1
            width: parent.width
            color: "lightgray"
            anchors.bottom: parent.bottom

            Row {
                anchors.fill: parent
                spacing: 10
                anchors.margins: 10

                Rectangle {
                    width: (parent.width - 20) / 3
                    height: parent.height
                    color: "lightgray"
                    Text {
                        anchors.centerIn: parent
                        text: "1"
                    }
                }

                Rectangle {
                    width: (parent.width - 20) / 3
                    height: parent.height
                    color: "lightgray"
                    Text {
                        anchors.centerIn: parent
                        text: "2"
                    }
                }

                Rectangle {
                    width: (parent.width - 20) / 3
                    height: parent.height
                    color: "lightgray"
                    Text {
                        anchors.centerIn: parent
                        text: "3"
                    }
                }
            }
        }
    }
}
