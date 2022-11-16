#include "messaging.h"
#include "accelerator.h"

Accelerator Aobject(A0, A1, A2, A3, A4);
Messaging Mobject;
uint8_t flags = 1;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  
  int number_of_measurements = 0;

  Serial.println("Enter number of measurements");

  while (number_of_measurements == 0)
  {
    if (Serial.available() > 0)
    {
      number_of_measurements = Serial.parseInt();
    }
  }

  for (int M = 0; M < number_of_measurements; M++)
  {
    Aobject.make_measurement();
    Measurement m = Aobject.get_measurement();
    uint8_t id = M;

    Mobject.create_message(m);
    if (Mobject.send_message(id, flags))
    {
      Serial.println("Successful transmission");
    }
    else
    {
      Serial.println("Transmission failed. We'll get 'em next time.");
    }
    if (Mobject.receive_ACK())
    {
      Serial.println("ACK received");
    }
    else
    {
      Serial.println("NO ACK. Retransmitting");
      M--;
    }
  }
  Serial.println("Measurements and transmissions finished");
}