// Файл для задания 1
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "Task1_Figure"

    Item {
        id: figureContainer
        anchors.fill: parent
        anchors.margins: 20

        // Пирамидка из прямоугольников
        Rectangle {
            id: base
            width: 150
            height: 50
            color: "brown"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.bottom
        }

        Rectangle {
            id: middle
            width: 100
            height: 50
            color: "orange"
            anchors.horizontalCenter: base.horizontalCenter
            anchors.bottom: base.top
        }

        Rectangle {
            id: top
            width: 50
            height: 50
            color: "yellow"
            anchors.horizontalCenter: middle.horizontalCenter
            anchors.bottom: middle.top
        }
    }
}
