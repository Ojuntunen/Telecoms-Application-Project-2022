#include "accelerator.h"

Accelerator::Accelerator()
{

}
Accelerator::Accelerator(int arg_1, int arg_2, int arg_3, int arg_4, int arg_5)
{
  pin_setup.gnd_pin = arg_1;
  pin_setup.x_pin = arg_2;
  pin_setup.y_pin = arg_3;
  pin_setup.z_pin = arg_4;
  pin_setup.vcc_pin = arg_5;
  pinMode(pin_setup.vcc_pin, OUTPUT);
  pinMode(pin_setup.gnd_pin, OUTPUT);
  digitalWrite(pin_setup.vcc_pin, HIGH);
  digitalWrite(pin_setup.gnd_pin, LOW);
}
Accelerator::~Accelerator()
{

}
void Accelerator::make_measurement()
{
  int i;
  measurement.x = 0;
  measurement.y = 0;
  measurement.z = 0;

  //getting average of 10 measurements to reduce errors
  for(i = 0; i < 10; i++)
  {
    measurement.x += analogRead(pin_setup.x_pin);
    measurement.y += analogRead(pin_setup.y_pin);
    measurement.z += analogRead(pin_setup.z_pin);
  }
  measurement.x /= 10;
  measurement.y /= 10;
  measurement.z /= 10;
}
Measurement Accelerator::get_measurement()
{
  return measurement;
}
