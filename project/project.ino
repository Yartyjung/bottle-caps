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
  bs.write(0);
  gs.write(0);
  ws.write(0);
  ys.write(0);
  delay(1500);
}
void loop()
{
  // put your main code here, to run repeatedly:
  while (Serial.available())
  {
    incomingData = Serial.read();
    Serial.println(incomingData);
    switch (incomingData)
    {
    case '1': //blue
      delay(200);
      reset();
      bs.write(65)
    case '2': //green
      delay(200);
      reset();
      gs.write(65)
    case '3': //white
      delay(200);
      reset();
      ws.write(65)
    case '4': // yellow
      delay(200);
      reset();
      ys.write(65)
    case '0': // reset
      delay(200);
      reset();
      continue;
    } // end of switch()
  }
}
