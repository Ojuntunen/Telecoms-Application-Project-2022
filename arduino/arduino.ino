#include "accelerator.h"
#include "messaging.h"

Accelerator accelerator(A0,A1,A2,A3,A4);
Messaging driver;
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
        Measurement measurement = accelerator.get_measurement();
        Serial.print(measurement.x, BIN);
        Serial.print(" ");
        Serial.print(measurement.y, BIN);
        Serial.print(" ");
        Serial.println(measurement.z, BIN);
        driver.create_message(measurement);
        
    }
}
