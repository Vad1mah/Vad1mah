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
            buttonText1: "Replace with Green"
            buttonText2: "Push Yellow"
            useReplace: true  // Используем replace для первой кнопки
            onButton1Clicked: stackView.replace(greenPage)
            onButton2Clicked: stackView.push(yellowPage)
        }
    }

    // Зеленая страница
    Component {
        id: greenPage
        MyPage {
            pageTitle: "Green Page"
            backgroundColor: "green"
            buttonText1: "Replace with Red"
            buttonText2: "Push Yellow"
            useReplace: true
            onButton1Clicked: stackView.replace(redPage)
            onButton2Clicked: stackView.push(yellowPage)
        }
    }

    // Желтая страница
    Component {
        id: yellowPage
        MyPage {
            pageTitle: "Yellow Page"
            backgroundColor: "yellow"
            buttonText1: "Push Red"
            buttonText2: "Replace with Green"
            useReplace: false
            onButton1Clicked: stackView.push(redPage)
            onButton2Clicked: stackView.replace(greenPage)
        }
    }
}
