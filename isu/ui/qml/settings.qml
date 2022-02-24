import QtQuick
ListView {
    width: 100
    height: 100
    required model

    delegate: Rectangle {
        required property string modelData
        height: 25
        width: 100
        Text { text: parent.modelData }
    }
}
// Rectangle {
//     id: page
//     width: 500; height: 300
//     color: "lightgray"

//     function updateRotator() {
//         rotator.angle = rotator.angle + 45
//     }

//     Rectangle {
//         id: rotator
//         property real angle: 0
//         x: 240; y: 95;
//         color: "black"
//         width: 100; height: 10

//         transform: Rotation {
//             angle: roator.angle
//             origin.x: 10; origin.y: 5
//             Behavior on angle {
//                 SpringAnimation {
//                     spring: 1.4
//                     damping: 0.05
//                 }
//             }
//         }
//     }
// }