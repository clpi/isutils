import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.4

Flow {
    visible: root.checked && model.repeat
    Layout.fillWidth: true

    Repeater {
        id: dayRepeater
        model: daysToRepeat
        delegate: RoundButton {
            text: Qt.locale().dayName(model.dayOfWeek, Locale.NarrowFormat)
            flat: true
            checked: model.repeat
            checkable: true
            Material.background: checked ? Material.accent : "transparent"
            onToggled: model.repeat = checked
        }
    }
}