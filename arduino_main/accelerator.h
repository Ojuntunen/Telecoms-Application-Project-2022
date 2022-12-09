#ifndef ACCELERATOR_H
#define ACCELERATOR_H
#include "arduino.h"

struct Measurement
{
    int x;
    int y;
    int z;
};

struct Accelerator_Pins
{
    int gnd_pin = A0;
    int x_pin = A1;
    int y_pin = A2;
    int z_pin = A3;
    int vcc_pin = A4;
};

class Accelerator
{
    public:
        Accelerator();
        //For initializing pins for the accelerometer
        Accelerator(int, int, int, int, int);
        ~Accelerator();
        void make_measurement();
        Measurement get_measurement();
    private:
        Measurement measurement;
        Accelerator_Pins pin_setup;
};


#endif
