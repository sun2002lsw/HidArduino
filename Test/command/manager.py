import sys
import pygame
from time import time
from .keycode import KeycodeConverter
from .command import KeyboardCommand, MouseCommand


# 현재 입력에 따른 적절한 command 리스트를 반환
class CommandManager:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        screen.fill("white")
        pygame.display.flip()

        self._keycodeConverter = KeycodeConverter()
        self._pressedKeyboardKeys = set()
        self._pressedMouseButtons = set()

        self._lastMouseCheck = time()
        self._lastMousePosition = pygame.mouse.get_pos()

    def GetCommands(self):
        commands = list()

        # 키보드나 마우스 입력
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # 화면창에서 X 표시 눌러서 나감
            elif event.type == pygame.KEYDOWN:
                command = self._handleKeyboardDown(event.key)
                if command is not None:
                    commands.append(command)
            elif event.type == pygame.KEYUP:
                command = self._handleKeyboardUp(event.key)
                if command is not None:
                    commands.append(command)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                command = self._handleMouseDown(event.button)
                if command is not None:
                    commands.append(command)
            elif event.type == pygame.MOUSEBUTTONUP:
                command = self._handleMouseUp(event.button)
                if command is not None:
                    commands.append(command)

        # 마우스 이동
        command = self._handleMouseMove()
        if command is not None:
            commands.append(command)

        return commands

    def _handleKeyboardDown(self, key):
        if key in self._pressedKeyboardKeys:
            return None

        self._pressedKeyboardKeys.add(key)
        arduinoKey = self._keycodeConverter.ConvertKey(key)

        command = KeyboardCommand()
        command.Press(arduinoKey)
        return command

    def _handleKeyboardUp(self, key):
        if key not in self._pressedKeyboardKeys:
            return None

        self._pressedKeyboardKeys.remove(key)
        arduinoKey = self._keycodeConverter.ConvertKey(key)

        command = KeyboardCommand()
        command.Release(arduinoKey)
        return command

    def _handleMouseDown(self, button):
        if button in self._pressedMouseButtons:
            return None

        self._pressedMouseButtons.add(button)
        arduinoButton = self._keycodeConverter.ConvertButton(button)

        command = MouseCommand()
        command.Press(arduinoButton)
        return command

    def _handleMouseUp(self, button):
        if button not in self._pressedMouseButtons:
            return None

        self._pressedMouseButtons.remove(button)
        arduinoButton = self._keycodeConverter.ConvertButton(button)

        command = MouseCommand()
        command.Release(arduinoButton)
        return command

    def _handleMouseMove(self):
        now = time()
        if now - self._lastMouseCheck < 0.1:
            return None

        curMousePosition = pygame.mouse.get_pos()
        if curMousePosition == self._lastMousePosition:
            return None

        x = curMousePosition[0] - self._lastMousePosition[0]
        y = curMousePosition[1] - self._lastMousePosition[1]

        self._lastMouseCheck = now
        self._lastMousePosition = curMousePosition

        command = MouseCommand()
        command.Move(x, y)
        return command
