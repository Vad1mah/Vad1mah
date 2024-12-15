import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "StackView Test"

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: redPage
    }

    // Красная страница
    Component {
        id: redPage
        MyPage {
            pageTitle: "Red Page"
            backgroundColor: "red"
            buttonText1: "Go to Green"
            buttonText2: "Go to Yellow"
            onButton1Clicked: stackView.push(greenPage)
            onButton2Clicked: stackView.push(yellowPage)
        }
    }

    // Зеленая страница
    Component {
        id: greenPage
        MyPage {
            pageTitle: "Green Page"
            backgroundColor: "green"
            buttonText1: "Go to Red"
            buttonText2: "Go to Yellow"
            onButton1Clicked: stackView.push(redPage)
            onButton2Clicked: stackView.push(yellowPage)
        }
    }

    // Желтая страница
    Component {
        id: yellowPage
        MyPage {
            pageTitle: "Yellow Page"
            backgroundColor: "yellow"
            buttonText1: "Go to Red"
            buttonText2: "Go to Green"
            onButton1Clicked: stackView.push(redPage)
            onButton2Clicked: stackView.push(greenPage)
        }
    }
}
