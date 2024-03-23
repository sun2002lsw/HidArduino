#include <SoftwareSerial.h>
#include <ArduinoJson.h>
#include <Keyboard.h>
#include <Mouse.h>

// usb를 컴퓨터에 연결해서 사용하기 때문에,
// rx, tx 핀을 사용할 수 없음
// 다른 핀을 추가 rx, tx로 설정해서 사용하자
#define PIN_RX 8 // rx로 사용가능한 핀이 정해져 있음
#define PIN_TX 9
SoftwareSerial JsonSerial(PIN_RX, PIN_TX);

// 시리얼 통신으로 들어오는 입력은 json 형식임
StaticJsonDocument<100> jsonDoc;

void setup() {
  JsonSerial.begin(9600);
  Keyboard.begin();
  Mouse.begin();
  
  pinMode(LED_BUILTIN, OUTPUT);
  turnOffLight();
}

void loop() {
  if (JsonSerial.available() == 0)
    return; // 입력 들어온게 없음
  
  turnOnLight();
  ParseAndHandle();
  turnOffLight();
}

// 시리얼 통신으로 들어온 json 문자열 파싱해서 처리하기
void ParseAndHandle() {
  String jsonStr = JsonSerial.readStringUntil('\n');
  auto error = deserializeJson(jsonDoc, jsonStr);
  if (error) {
    return;
  }

  String device = jsonDoc["device"];
  if (device == "keyboard")
    HandleKeyboard();
  else if (device == "mouse")
    HandleMouse();
}

// 키보드 입력 처리
void HandleKeyboard() {
  String command = jsonDoc["command"];
  uint8_t key = jsonDoc["key"];

  if (command == "press")
    Keyboard.press(key);
  else if (command == "release")
    Keyboard.release(key);
  else if (command == "click")
    Keyboard.write(key);
}

// 마우스 입력 처리
void HandleMouse() {
  String command = jsonDoc["command"];
  uint8_t button = jsonDoc["button"];
  int x = jsonDoc["x"];
  int y = jsonDoc["y"];

  if (command == "press")
    Mouse.press(button);
  else if (command == "release")
    Mouse.release(button);
  else if (command == "click")
    Mouse.click(button);
  else if (command == "move")
    Mouse.move(x, y);
}

// 아두이노 기기 자체에 붙어 있는 불빛
void turnOnLight() {
  digitalWrite(LED_BUILTIN, HIGH);
}

void turnOffLight() {  
  digitalWrite(LED_BUILTIN, LOW);
}
