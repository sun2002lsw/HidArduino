from mqtt.client import MQTTclient
from command.manager import CommandManager

IP = "123.123.123.123"
userName = "계정 이름"
userPwd = "계정 비번!"

client = MQTTclient(IP, userName, userPwd)
commandManager = CommandManager()

while True:
    commands = commandManager.GetCommands()
    for command in commands:
        client.Publish(command)
