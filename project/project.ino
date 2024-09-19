#include <Servo.h>

char incomingData;
int blue = 3;
int green = 9;
int white = 10;
int yellow = 11;
bool status = true;

Servo bs;
Servo gs;
Servo ws;
Servo ys;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  if (status == true)
  {
    bs.attach(blue);
    gs.attach(green);
    ws.attach(white);
    ys.attach(yellow);
  }
  delay(2000);
  reset();
}
void reset()
{
  bs.write(65);
  gs.write(65);
  ws.write(65);
  ys.write(65);
  delay(1500);
}
void loop()
{
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    incomingData = Serial.read();
    Serial.println(incomingData);
    switch (incomingData)
    {
    case '0': // reset
      delay(200);
      reset();
    case '4': // yellow
      delay(200);
      ys.write(70);
    case '3': //white
      delay(200);
      ws.write(70);
    case '2': //green
      delay(200);
      gs.write(70);
    case '1': //blue
      delay(200);
      bs.write(70);
    } // end of switch()
  }
}
