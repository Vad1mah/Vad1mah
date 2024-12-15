import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Прокручиваемый светофор"

    SwipeView {
        id: swipeView
        anchors.fill: parent
        interactive: true

        // Красная страница
        Item {
            width: swipeView.width
            height: swipeView.height
            Rectangle {
                anchors.fill: parent
                color: "red"
                Text {
                    anchors.centerIn: parent
                    text: "Red"
                    color: "white"
                    font.pixelSize: 50
                }
            }
        }

        // Жёлтая страница
        Item {
            width: swipeView.width
            height: swipeView.height
            Rectangle {
                anchors.fill: parent
                color: "yellow"
                Text {
                    anchors.centerIn: parent
                    text: "Yellow"
                    color: "black"
                    font.pixelSize: 50
                }
            }
        }

        // Зелёная страница
        Item {
            width: swipeView.width
            height: swipeView.height
            Rectangle {
                anchors.fill: parent
                color: "green"
                Text {
                    anchors.centerIn: parent
                    text: "Green"
                    color: "white"
                    font.pixelSize: 50
                }
            }
        }
    }

    PageIndicator {
        id: pageIndicator
        count: swipeView.count
        currentIndex: swipeView.currentIndex
        anchors.bottom: swipeView.bottom
        anchors.horizontalCenter: swipeView.horizontalCenter
    }
}
