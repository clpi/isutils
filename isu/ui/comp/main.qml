import QtQuick 2.15
import QtQuick.Controls 2.15

ListModel {
   ListElement {
       name: "Bill Jones"
       number: "+1 800 555 1212"
       icon: "pics/qtlogo.png"
   }
   ListElement {
       name: "Jane Doe"
       number: "+1 800 555 3434"
       icon: "pics/qtlogo.png"
   }
   ListElement {
       name: "John Smith"
       number: "1 800 555 5656"
       icon: "pics/qtlogo.png"
   }
}
ListView {

   width: 180; height: 200
   model: ContactModel {}
   delegate: Text {
       text: name + ": " + number
   }
}

Component {
    id: delegate
    PathView {
       anchors.fill: parent
       model: ContactModel {}
       delegate: delegate
       path: Path {
           startX: 120; startY: 100
           PathQuad { x: 120; y: 25; controlX: 260; controlY: 75 }
           PathQuad { x: 120; y: 100; controlX: -20; controlY: 75 }
       }
    }
    Column {
        Row {
            spacing: 10
            Button { text: "Add step" }
            Button { text: "Dupe step" }
            Button { text: "Remove step" }
            Button { text: "Clear steps" }
        }
        Button {
            id: loadDemo
            text: "Load demo"
            anchors.left: parent.left
            anchors.right: parent.right
            platformAutoRepeat: chkPlatformAutoRepeat.checked
            checkable: chkCheckable.checked
            onPlatformReleased: {
                txtLog.text = txtLog.text  "The 'platformReleased' signal."
            }
            onClicked: {
                txtLog.text = txtLog.text + "The 'clicked' signal. "
            }
            onPlatformPressAndHold: {
                txtLog.text = txtLog.text + "The 'platformPressAndHold' signal."
            }
        }
    }
}

Rectangle {
    id: parentRect
    opacity: 0.5
    border.width: 1
    radius: 5
    smooth: true
    property alias text: textItem.text
    width: 200; height: 350
    color: "red"
    gradient: Gradient {
        GradientStop { position: 0; color: "red" }
        GradientStop { position: 0.5; color: "orange" }
        GradientStop { position: 1; color: "blue" }
    }

    Text {
        id: textItem
        font.pointSize: 20
        color: "white"
        anchors.centerIn: parent
    }

    Rectangle {
        id: childRect
        color: "blue"
        x: 50; y: 50
        width: 100; height: 150
        states: State {
            name: "moved"
            PropertyChanges { target: rect; x: 50; y: 50 }
        }
        transitions: Transition {
            PropertyAnimation {
                properties: "x,y"
                easing.type: Easing.InOutQuad
            }
        }

    }
}

StepsModel {
    id: stepsModel
}

FileDownload {
    id: fileDownloader
    utl: "http://placehold.it/350x150"
    onStarted: status.text = "Downloading..."
    onProgressChanged: status.text = `Download ${progress}% finished`
    onError: status.text = "Download failed"
    onFinished: status.text = "Download finished"
}

Button {
    text: "Load demo"
    onClicked: fileDownloader.start()
}

Button {
    text: `the demo has ${stepsModel.count} steps`
    onClicked: stepsModel.refresh()
}

