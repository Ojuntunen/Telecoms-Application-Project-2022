#include "accelerator.h"

Accelerator accelerator(A0,A1,A2,A3,A4);
char val;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
    val=Serial.read();
    if(val=='R')
    {
        accelerator.make_measurement();
        Measurement meas = accelerator.get_measurement();
        Serial.print(meas.x);
        Serial.print(" ");
        Serial.print(meas.y);
        Serial.print(" ");
        Serial.println(meas.z);
    }
}
