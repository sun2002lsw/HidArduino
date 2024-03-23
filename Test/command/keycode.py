import pygame


# 몇몇 키는 아두이노랑 코드가 다르기에, 해당 키는 적절히 변환
class KeycodeConverter:
    def __init__(self):
        self._pygameToArduino = dict()
        self._arduinoKeycode = dict()

        self._initPygameToArduino()
        self._initArduinoKeycode()

    # 키보드 입력 변환
    def ConvertKey(self, eventKey):
        if eventKey not in self._pygameToArduino:
            return eventKey  # 코드 같음. 그대로 쓰면 됨

        arduinoKey = self._pygameToArduino[eventKey]
        return self._arduinoKeycode[arduinoKey]

    # 마우스 입력 변환 (휠은 없음. 클릭만 취급)
    def ConvertButton(self, eventButton):
        if eventButton > 3:
            return 0  # 휠 입력
        elif eventButton == 1:
            return 1  # 왼쪽 클릭
        elif eventButton == 2:
            return 4  # 가운데 클릭
        elif eventButton == 3:
            return 2  # 오른족 클릭

    def _initPygameToArduino(self):
        self._pygameToArduino[pygame.K_LCTRL] = "KEY_LEFT_CTRL"
        self._pygameToArduino[pygame.K_LSHIFT] = "KEY_LEFT_SHIFT"
        self._pygameToArduino[pygame.K_LALT] = "KEY_LEFT_ALT"
        self._pygameToArduino[pygame.K_LGUI] = "KEY_LEFT_GUI"
        self._pygameToArduino[pygame.K_RCTRL] = "KEY_RIGHT_CTRL"
        self._pygameToArduino[pygame.K_RSHIFT] = "KEY_RIGHT_SHIFT"
        self._pygameToArduino[pygame.K_RALT] = "KEY_RIGHT_ALT"
        self._pygameToArduino[pygame.K_RGUI] = "KEY_RIGHT_GUI"

        self._pygameToArduino[pygame.K_RETURN] = "KEY_RETURN"
        self._pygameToArduino[pygame.K_ESCAPE] = "KEY_ESC"
        self._pygameToArduino[pygame.K_BACKSPACE] = "KEY_BACKSPACE"
        self._pygameToArduino[pygame.K_TAB] = "KEY_TAB"
        self._pygameToArduino[pygame.K_CAPSLOCK] = "KEY_CAPS_LOCK"

        self._pygameToArduino[pygame.K_F1] = "KEY_F1"
        self._pygameToArduino[pygame.K_F2] = "KEY_F2"
        self._pygameToArduino[pygame.K_F3] = "KEY_F3"
        self._pygameToArduino[pygame.K_F4] = "KEY_F4"
        self._pygameToArduino[pygame.K_F5] = "KEY_F5"
        self._pygameToArduino[pygame.K_F6] = "KEY_F6"
        self._pygameToArduino[pygame.K_F7] = "KEY_F7"
        self._pygameToArduino[pygame.K_F8] = "KEY_F8"
        self._pygameToArduino[pygame.K_F9] = "KEY_F9"
        self._pygameToArduino[pygame.K_F10] = "KEY_F10"
        self._pygameToArduino[pygame.K_F11] = "KEY_F11"
        self._pygameToArduino[pygame.K_F12] = "KEY_F12"

        self._pygameToArduino[pygame.K_PRINT] = "KEY_PRINT_SCREEN"
        self._pygameToArduino[pygame.K_SCROLLOCK] = "KEY_SCROLL_LOCK"
        self._pygameToArduino[pygame.K_PAUSE] = "KEY_PAUSE"
        self._pygameToArduino[pygame.K_INSERT] = "KEY_INSERT"
        self._pygameToArduino[pygame.K_HOME] = "KEY_HOME"
        self._pygameToArduino[pygame.K_PAGEUP] = "KEY_PAGE_UP"
        self._pygameToArduino[pygame.K_DELETE] = "KEY_DELETE"
        self._pygameToArduino[pygame.K_END] = "KEY_END"
        self._pygameToArduino[pygame.K_PAGEDOWN] = "KEY_PAGE_DOWN"

        self._pygameToArduino[pygame.K_RIGHT] = "KEY_RIGHT_ARROW"
        self._pygameToArduino[pygame.K_LEFT] = "KEY_LEFT_ARROW"
        self._pygameToArduino[pygame.K_DOWN] = "KEY_DOWN_ARROW"
        self._pygameToArduino[pygame.K_UP] = "KEY_UP_ARROW"

        self._pygameToArduino[pygame.K_NUMLOCK] = "KEY_NUM_LOCK"
        self._pygameToArduino[pygame.K_KP_DIVIDE] = "KEY_KP_SLASH"
        self._pygameToArduino[pygame.K_KP_MULTIPLY] = "KEY_KP_ASTERISK"
        self._pygameToArduino[pygame.K_KP_MINUS] = "KEY_KP_MINUS"
        self._pygameToArduino[pygame.K_KP_PLUS] = "KEY_KP_PLUS"
        self._pygameToArduino[pygame.K_KP_ENTER] = "KEY_KP_ENTER"

        self._pygameToArduino[pygame.K_KP1] = "KEY_KP_1"
        self._pygameToArduino[pygame.K_KP2] = "KEY_KP_2"
        self._pygameToArduino[pygame.K_KP3] = "KEY_KP_3"
        self._pygameToArduino[pygame.K_KP4] = "KEY_KP_4"
        self._pygameToArduino[pygame.K_KP5] = "KEY_KP_5"
        self._pygameToArduino[pygame.K_KP6] = "KEY_KP_6"
        self._pygameToArduino[pygame.K_KP7] = "KEY_KP_7"
        self._pygameToArduino[pygame.K_KP8] = "KEY_KP_8"
        self._pygameToArduino[pygame.K_KP9] = "KEY_KP_9"
        self._pygameToArduino[pygame.K_KP0] = "KEY_KP_0"
        self._pygameToArduino[pygame.K_KP_PERIOD] = "KEY_KP_DOT"

        self._pygameToArduino[pygame.K_MENU] = "KEY_MENU"

    # https://www.arduino.cc/reference/en/language/functions/usb/keyboard/keyboardmodifiers/
    def _initArduinoKeycode(self):
        self._arduinoKeycode["KEY_LEFT_CTRL"] = 128
        self._arduinoKeycode["KEY_LEFT_SHIFT"] = 129
        self._arduinoKeycode["KEY_LEFT_ALT"] = 130
        self._arduinoKeycode["KEY_LEFT_GUI"] = 131
        self._arduinoKeycode["KEY_RIGHT_CTRL"] = 132
        self._arduinoKeycode["KEY_RIGHT_SHIFT"] = 133
        self._arduinoKeycode["KEY_RIGHT_ALT"] = 134
        self._arduinoKeycode["KEY_RIGHT_GUI"] = 135

        self._arduinoKeycode["KEY_RETURN"] = 176
        self._arduinoKeycode["KEY_ESC"] = 177
        self._arduinoKeycode["KEY_BACKSPACE"] = 178
        self._arduinoKeycode["KEY_TAB"] = 179
        self._arduinoKeycode["KEY_CAPS_LOCK"] = 193

        self._arduinoKeycode["KEY_F1"] = 194
        self._arduinoKeycode["KEY_F2"] = 195
        self._arduinoKeycode["KEY_F3"] = 196
        self._arduinoKeycode["KEY_F4"] = 197
        self._arduinoKeycode["KEY_F5"] = 198
        self._arduinoKeycode["KEY_F6"] = 199
        self._arduinoKeycode["KEY_F7"] = 200
        self._arduinoKeycode["KEY_F8"] = 201
        self._arduinoKeycode["KEY_F9"] = 202
        self._arduinoKeycode["KEY_F10"] = 203
        self._arduinoKeycode["KEY_F11"] = 204
        self._arduinoKeycode["KEY_F12"] = 205

        self._arduinoKeycode["KEY_PRINT_SCREEN"] = 206
        self._arduinoKeycode["KEY_SCROLL_LOCK"] = 207
        self._arduinoKeycode["KEY_PAUSE"] = 208
        self._arduinoKeycode["KEY_INSERT"] = 209
        self._arduinoKeycode["KEY_HOME"] = 210
        self._arduinoKeycode["KEY_PAGE_UP"] = 211
        self._arduinoKeycode["KEY_DELETE"] = 212
        self._arduinoKeycode["KEY_END"] = 213
        self._arduinoKeycode["KEY_PAGE_DOWN"] = 214

        self._arduinoKeycode["KEY_RIGHT_ARROW"] = 215
        self._arduinoKeycode["KEY_LEFT_ARROW"] = 216
        self._arduinoKeycode["KEY_DOWN_ARROW"] = 217
        self._arduinoKeycode["KEY_UP_ARROW"] = 218

        self._arduinoKeycode["KEY_NUM_LOCK"] = 219
        self._arduinoKeycode["KEY_KP_SLASH"] = 220
        self._arduinoKeycode["KEY_KP_ASTERISK"] = 221
        self._arduinoKeycode["KEY_KP_MINUS"] = 222
        self._arduinoKeycode["KEY_KP_PLUS"] = 223
        self._arduinoKeycode["KEY_KP_ENTER"] = 224

        self._arduinoKeycode["KEY_KP_1"] = 225
        self._arduinoKeycode["KEY_KP_2"] = 226
        self._arduinoKeycode["KEY_KP_3"] = 227
        self._arduinoKeycode["KEY_KP_4"] = 228
        self._arduinoKeycode["KEY_KP_5"] = 229
        self._arduinoKeycode["KEY_KP_6"] = 230
        self._arduinoKeycode["KEY_KP_7"] = 231
        self._arduinoKeycode["KEY_KP_8"] = 232
        self._arduinoKeycode["KEY_KP_9"] = 233
        self._arduinoKeycode["KEY_KP_0"] = 234
        self._arduinoKeycode["KEY_KP_DOT"] = 235

        self._arduinoKeycode["KEY_MENU"] = 237
