#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WiFi 설정
const char* Wifi_SSID = "공유기 이름";
const char* Wifi_PWD  = "공유기 비번";

// MQTT 브로커 설정
const char* MQTT_SERVER = "123.123.123.123";
const char* MQTT_TOPIC  = "HID/#";

// MQTT 브로커 계정 설정
const char* MQTT_USER = "arduino";
const char* MQTT_PWD  = "계정 비번";

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  turnOffLight();

  // 시리얼 통신 (초기화에 시간이 걸림)
  Serial.begin(9600);
  delay(1000);

  // 와이파이 연결
  WiFi.mode(WIFI_STA);
  WiFi.begin(Wifi_SSID, Wifi_PWD);
  while (WiFi.status() != WL_CONNECTED)
    delay(100);
  
  // MQTT 클라 초기화 (포트는 1883으로 고정)
  mqttClient.setServer(MQTT_SERVER, 1883);
  mqttClient.setCallback(callback);
}

void loop() {
  if (!mqttClient.connected())
    mqttClientConnect();
  else
    mqttClient.loop();
}

// MQTT 서버에 연결해서 메시지 구독
void mqttClientConnect() {
  blinkLight();

  const char* id = "arduino(ESP8266)";
  if (!mqttClient.connect(id, MQTT_USER, MQTT_PWD)) {    
    delay(1000); // 연결 실패. 잠시 후 재시도
    return;
  }

  mqttClient.subscribe(MQTT_TOPIC);
  turnOnLight();
}

// 메시지가 오면 단순히 시리얼 통신으로 출력
void callback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (int i = 0; i < length; i++)
    msg += (char)payload[i];

  Serial.println(msg);
}

// 아두이노 기기 자체에 붙어 있는 불빛
void blinkLight() {
  for (int i = 0; i < 3; i++) {
    turnOnLight();
    delay(200);
    turnOffLight();
    delay(200);
  }
}

void turnOnLight() {
  digitalWrite(LED_BUILTIN, LOW); // 낮은 전력이 불빛 켜기임
}

void turnOffLight() {
  digitalWrite(LED_BUILTIN, HIGH);
}
