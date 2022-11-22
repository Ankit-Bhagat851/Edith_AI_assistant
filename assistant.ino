#define door 3
#define bulb 10
#include<Servo.h>
int servoPin = 3;
Servo Servol;

void setup() {
  Serial.begin(9600);
  Servol.attach(servoPin);
  pinMode(bulb,OUTPUT);
  Servol.write(0);
}

void loop() {
  if(Serial.available() == 1)
  {
    String val = Serial.readString();
    Serial.println(val);
    if(val == "light on")
    {
      digitalWrite(bulb, HIGH);
    }
    if(val == "light off")
    {
      digitalWrite(bulb, LOW);
    }
    if(val == "close door")
    {
      Servol.write(0);
      digitalWrite(door, HIGH);
    }
    if(val == "open door")
    {
      Servol.write(80);
      delay(5000);
      digitalWrite(door, LOW);
    }
  }
}
