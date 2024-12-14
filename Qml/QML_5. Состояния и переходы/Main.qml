import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600

    StackView {
        id: stackView
        anchors.fill: parent

        popEnter: Transition {
            NumberAnimation {
                property: "opacity"
                from: 0
                to: 1
                duration: 500
            }
        }

        popExit: Transition {
            NumberAnimation {
                property: "opacity"
                from: 1
                to: 0
                duration: 500
            }
        }

        pushEnter: Transition {
            NumberAnimation {
                property: "opacity"
                from: 0
                to: 1
                duration: 500
            }
        }

        pushExit: Transition {
            NumberAnimation {
                property: "opacity"
                from: 1
                to: 0
                duration: 500
            }
        }

        initialItem: page1

        Component {
            id: page1
            Rectangle {
                color: "white"

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
                            anchors.centerIn: parent
                            text: "Header 1"
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
                            anchors.centerIn: parent
                            text: "Item 1 content"
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
                                color: index === 0? "lightblue" : "lightgrey"
                                border.color: "black"

                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        if (index === 1) {
                                            stackView.push(page2)
                                        } else if (index === 2) {
                                            stackView.push(page3)
                                        }
                                    }
                                }

                                Text {
                                    anchors.centerIn: parent
                                    text: "Item " + (index + 1)
                                    font.pixelSize: stackView.currentItem === page1? (index === 0? 18 : 14) : 14
                                    opacity: stackView.currentItem === page1? (index === 0? 1.0 : 0.5) : 0.5
                                }
                            }
                        }
                    }
                }
            }
        }

        Component {
            id: page2
            Rectangle {
                color: "white"

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
                            anchors.centerIn: parent
                            text: "Header 2"
                            font.pixelSize: 20
                        }

                        MouseArea {
                            anchors.left: parent.left
                            anchors.verticalCenter: parent.verticalCenter
                            width: 50
                            height: parent.height
                            onClicked: {
                                stackView.pop()
                            }
                        }

                        Text {
                            anchors.left: parent.left
                            anchors.verticalCenter: parent.verticalCenter
                            text: "Назад"
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
                            anchors.centerIn: parent
                            text: "Item 2 content"
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
                                color: index === 1? "lightblue" : "lightgrey"
                                border.color: "black"

                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        if (index === 0) {
                                            stackView.pop()
                                        } else if (index === 2) {
                                            stackView.push(page3)
                                        }
                                    }
                                }

                                Text {
                                    anchors.centerIn: parent
                                    text: "Item " + (index + 1)
                                    font.pixelSize: stackView.currentItem === page2? (index === 1? 18 : 14) : 14
                                    opacity: stackView.currentItem === page2? (index === 1? 1.0 : 0.5) : 0.5
                                }
                            }
                        }
                    }
                }
            }
        }

        Component {
            id: page3
            Rectangle {
                color: "white"

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
                            anchors.centerIn: parent
                            text: "Header 3"
                            font.pixelSize: 20
                        }

                        MouseArea {
                            anchors.left: parent.left
                            anchors.verticalCenter: parent.verticalCenter
                            width: 50
                            height: parent.height
                            onClicked: {
                                stackView.pop()
                            }
                        }

                        Text {
                            anchors.left: parent.left
                            anchors.verticalCenter: parent.verticalCenter
                            text: "Назад"
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
                            anchors.centerIn: parent
                            text: "Item 3 content"
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
                                color: index === 2? "lightblue" : "lightgrey"
                                border.color: "black"

                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        if (index === 0) {
                                            stackView.pop()
                                            stackView.pop()
                                        } else if (index === 1) {
                                            stackView.pop()
                                        }
                                    }
                                }
                                Text {
                                    anchors.centerIn: parent
                                    text: "Item " + (index + 1)
                                    font.pixelSize: stackView.currentItem === page3? (index === 2? 18 : 14) : 14
                                    opacity: stackView.currentItem === page3? (index === 2? 1.0 : 0.5) : 0.5
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
