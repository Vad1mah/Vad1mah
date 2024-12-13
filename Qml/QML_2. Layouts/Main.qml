import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "Task_for_Layout"

    ColumnLayout {
        anchors.fill: parent

        Rectangle {
            Layout.preferredHeight: parent.height * 0.1
            Layout.fillWidth: true
            color: "lightgray"
            Text {
                anchors.centerIn: parent
                text: "Header"
                font.pointSize: parent.height * 0.15
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            color: "white"
            border.color: "black"
            border.width: 2
            Layout.margins: parent.width * 0.05
            Text {
                anchors.centerIn: parent
                text: "Content"
                font.pointSize: parent.height * 0.1
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
        }

        Rectangle {
            Layout.preferredHeight: parent.height * 0.1
            Layout.fillWidth: true
            color: "lightgray"
            Layout.margins: 10

            RowLayout {
                anchors.fill: parent
                anchors.centerIn: parent
                spacing: 0

                Rectangle {
                    Layout.fillHeight: true
                    Layout.preferredWidth: (parent.width - 40 - 2 * (parent.width * 0.1)) / 3
                    color: "lightgray"
                    Text {
                        anchors.centerIn: parent
                        text: "1"
                        font.pointSize: parent.width * 0.1
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle {
                    Layout.fillHeight: true
                    Layout.preferredWidth: parent.width * 0.1
                    color: "gray" // Цвет палки-разделителя
                }

                Rectangle {
                    Layout.fillHeight: true
                    Layout.preferredWidth: (parent.width - 40 - 2 * (parent.width * 0.1)) / 3
                    color: "lightgray"
                    Text {
                        anchors.centerIn: parent
                        text: "2"
                        font.pointSize: parent.width * 0.1
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle {
                    Layout.fillHeight: true
                    Layout.preferredWidth: parent.width * 0.1
                    color: "gray" // Цвет палки-разделителя
                }

                Rectangle {
                    Layout.fillHeight: true
                    Layout.preferredWidth: (parent.width - 40 - 2 * (parent.width * 0.1)) / 3
                    color: "lightgray"
                    Text {
                        anchors.centerIn: parent
                        text: "3"
                        font.pointSize: parent.width * 0.1
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }
        }
    }
}
