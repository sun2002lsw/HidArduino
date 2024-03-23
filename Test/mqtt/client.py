import sys
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion


class MQTTclient:
    def __init__(self, IP, userName, userPwd):
        self._client = mqtt.Client(CallbackAPIVersion.VERSION2)
        self._client.username_pw_set(userName, userPwd)

        errCode = self._client.connect(IP, 1883)
        if errCode is not mqtt.MQTT_ERR_SUCCESS:
            sys.exit('MQTT connect error: {0}'.format(errCode))
        print("MQTT client connect")

        errCode = self._client.loop_start()
        if errCode is not mqtt.MQTT_ERR_SUCCESS:
            sys.exit('MQTT start error: {0}'.format(errCode))
        print("MQTT client start")

    def Publish(self, command):
        topic = "HID/" + command.Device()
        payload = command.ToString()

        print("{0}: {1}".format(topic, payload))
        self._client.publish(topic, payload, 1)
