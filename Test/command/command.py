import json


# 키보드 또는 마우스에 대한 하나의 행동
class BaseCommand:
    def __init__(self):
        self._device = None
        self._command = None
        self._keyboardKey = None
        self._mouseButton = None
        self._mouseX = None
        self._mouseY = None

    def Device(self):
        if self._device is None:
            return ""

        return self._device

    def ToString(self):
        if self._device is None:
            return ""
        if self._command is None:
            return ""

        jsonVal = {"device": self._device, "command": self._command}
        if self._keyboardKey is not None:
            jsonVal["key"] = self._keyboardKey
        if self._mouseButton is not None:
            jsonVal["button"] = self._mouseButton
        if self._mouseX is not None:
            jsonVal["x"] = self._mouseX
        if self._mouseY is not None:
            jsonVal["y"] = self._mouseY

        return json.dumps(jsonVal)


class KeyboardCommand(BaseCommand):
    def __init__(self):
        super().__init__()
        self._device = "keyboard"

    def Press(self, key):
        self._command = "press"
        self._keyboardKey = key

    def Release(self, key):
        self._command = "release"
        self._keyboardKey = key

    def Click(self, key):
        self._command = "click"
        self._keyboardKey = key


class MouseCommand(BaseCommand):
    def __init__(self):
        super().__init__()
        self._device = "mouse"

    def Press(self, button):
        self._command = "press"
        self._mouseButton = button

    def Release(self, button):
        self._command = "release"
        self._mouseButton = button

    def Click(self, button):
        self._command = "click"
        self._mouseButton = button

    def Move(self, mouseX, mouseY):
        self._command = "move"
        self._mouseX = mouseX
        self._mouseY = mouseY
