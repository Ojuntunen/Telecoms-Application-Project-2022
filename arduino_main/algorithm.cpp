#include "algorithm.h"
#include "centerpoints.h"

void calc_distance(double accel_values[], double distances[])
{
    double difference[3];
    for (int x = 0; x < 4; x++)
    {
        for (int i = 0; i < 3; i++)
        {
            difference[i] = center_points[x][i] - accel_values[i];
        }
        distances[x] = sqrt(pow(difference[0], 2.0) + pow(difference[1], 2.0) + pow(difference[2], 2.0));
    }
}

void predict_alignment()
{
    int alignment = 3; //the data used for the algorithm is missing alignment data so we give the expected result here (0-3)
    double accel_values[3];
    double distances[4];
    
    accel_values[0] = analogRead(A1);
    accel_values[1] = analogRead(A2);
    accel_values[2] = analogRead(A3);
    calc_distance(accel_values, distances);

    Serial.print(alignment);
    Serial.print(";");
    for (int i = 0; i<3; i++)
    {
        Serial.print(int(accel_values[i]));
        Serial.print(";");
    }
    
    int lowest = 0;
    double min_value = distances[0];
    for (int i = 0; i < 4; i++)
    {
        if (distances[i] < min_value)
        {
            lowest = i;
            min_value = distances[i];
        }
    }
    switch (lowest)
        {
        case 0:
            Serial.println(int(center_points[lowest][3]));
            break;
        case 1:
            Serial.println(int(center_points[lowest][3]));
            break;
        case 2:
            Serial.println(int(center_points[lowest][3]));
            break;
        case 3:
            Serial.println(int(center_points[lowest][3]));
            break;
        default:
            Serial.println("\nLOGIC ERROR");
            break;
        }   
}
