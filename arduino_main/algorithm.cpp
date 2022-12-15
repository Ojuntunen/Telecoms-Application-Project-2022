#include "algorithm.h"
#include "centerpoints.h"

double calc_distance(double cp[], double accel_values[])
{
    double difference[3];
    for (int i; i<3; i++)
    {
        difference[i] = cp[i] - accel_values[i];
    }
    double distance;
    distance = sqrt(pow(difference[0], 2.0) + pow(difference[1], 2.0) + pow(difference[2], 2.0));
    return distance;
}

void button_interrupt()
{
    int alignment = 4;
    double accel_values[3];
    double distances[4];
    Serial.print(alignment);
    Serial.print(";");
    
    accel_values[0] = analogRead(A1);
    accel_values[1] = analogRead(A2);
    accel_values[2] = analogRead(A3);
    
    distances[0] = calc_distance(accel_values, center_point_1);
    distances[1] = calc_distance(accel_values, center_point_2);
    distances[2] = calc_distance(accel_values, center_point_3);
    distances[3] = calc_distance(accel_values, center_point_4);
    for (int i = 0; i<3; i++)
    {
        Serial.print(int(accel_values[i]));
        Serial.print(";");
    }
    
    int minimum = 0;
    double min_value = distances[0];
    for (int i = 0; i < 4; i++)
    {
        if (distances[i] < min_value)
        {
            minimum = i;
            min_value = distances[i];
        }
    }
    switch (minimum)
        {
        case 0:
            Serial.println(1);
            break;
        case 1:
            Serial.println(2);
            break;
        case 2:
            Serial.println(3);
            break;
        case 3:
            Serial.println(4);
            break;
        default:
            Serial.println("logic error");
            break;
        }   
}
