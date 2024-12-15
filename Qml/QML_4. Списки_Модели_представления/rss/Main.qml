import QtQuick 2.15
import QtQuick.Controls 2.5
import QtQuick.XmlListModel 2.0  // Импортируем модуль для работы с XML

Window {
    width: 360
    height: 640
    visible: true
    title: qsTr("RSS Reader")

    // Модель для парсинга RSS
    XmlListModel {
        id: rssModel
        source: "https://news.ycombinator.com/rss"  // Ссылка на RSS

        // Определяем структуру RSS (элементы, которые нам нужно извлечь)
        query: "/rss/channel/item"
        XmlRole { name: "title"; query: "title/string()" }
        XmlRole { name: "link"; query: "link/string()" }
        XmlRole { name: "description"; query: "description/string()" }
    }

    // Список, который будет отображать новости
    ListView {
        anchors.fill: parent
        model: rssModel
        delegate: Item {
            width: parent.width
            height: 60

            Rectangle {
                width: parent.width
                height: 60
                color: "white"
                border.color: "lightgray"
                radius: 5

                Row {
                    spacing: 10
                    anchors.centerIn: parent

                    Text {
                        text: model.title
                        font.bold: true
                        width: parent.width * 0.7
                        wrapMode: Text.Wrap
                    }

                    Button {
                        text: "Read"
                        onClicked: {
                            Qt.openUrlExternally(model.link)
                        }
                    }
                }
            }
        }
    }

    // Заголовок страницы
    header: ToolBar {
        Row {
            anchors.centerIn: parent
            Text {
                text: "RSS Feed"
                font.bold: true
                font.pixelSize: 18
            }
        }
    }
}
