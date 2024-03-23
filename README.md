# HidArduino
human interface device 용도로 사용할 아두이노에 대한 코드  
`Leonardo` 기기를 컴퓨터에 연결해서 HID 신호를 보낸다

### ESP8266_NodeMCU
1. 전원 공급되면 와이파이 연결 시도
2. 와이파이 연결 성공하면 MQTT 브로커 연결 시도 (불빛 깜빡임)
3. MQTT 브로커 연결 성공하면 토픽 구독 (불빛 들어옴)
4. 토픽으로 메시지 오면 시리얼 통신으로 전송

### Arduino_Leonardo
1. 시리얼 통신으로 들어오는 문자열 받음 (불빛 들어옴)
2. 문자열을 JSON 형식으로 파싱
3. JSON 값에 따라 적절히 키보드&마우스 조작
4. 처리가 실패했건 성공했건 로그 없이 종료 (불빛 꺼짐)

### 아두이노끼리 연결 방법
1. 전원 공급
- `ESP8266`의 VIN 핀을 `Leonardo`의 5V 핀에 연결
- `ESP8266`의 GND 핀을 `Leonardo`의 GND 핀에 연결
2. 시리얼 통신 연결
- `ESP8266`의 TX 핀을 `Leonardo`의 8 핀에 연결
- `ESP8266`의 RX 핀을 `Leonardo`의 9 핀에 연결
