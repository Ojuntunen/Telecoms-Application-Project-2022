const int VccPin = A0;
const int xPin   = A1;
const int yPin   = A2;
const int zPin   = A3;
const int GNDPin = A4;

unsigned long time = 0;

int x = 0;
int y = 0;
int z = 0;
float ax = 0.0;
float ay = 0.0;
float az = 0.0;
int startFlag = 0;
int i = 0;

void setup() {
  Serial.begin(19200);

  pinMode(VccPin, OUTPUT);
  pinMode(GNDPin, OUTPUT);
  
  digitalWrite(VccPin, HIGH);
  delayMicroseconds(2);
  digitalWrite(GNDPin, LOW);
  delayMicroseconds(2);

  while (Serial.available() != 0)
  {
    
  }
}

void loop() {
  
  if (startFlag == 0)
  {
    delay(1);
    startFlag = 1;
  }
  
  x = 0;
  y = 0;
  z = 0;
  
  for (i = 0; i < 10; i++)
  {
    x = x + analogRead(xPin);
    y = y + analogRead(yPin);
    z = z + analogRead(zPin);
  }

  time = millis();

  x = x / 10;
  y = y / 10;
  z = z / 10;

  ax = 0.1401 * x - 49.093;
  ay = 0.1378 * y - 48.106;
  az = 0.1451 * z - 52.533;
/*
  #for accelerometer calibration
  Serial.print(" ");
  Serial.print(x);
  Serial.print(" ");
  Serial.print(y);
  Serial.print(" ");
  Serial.println(z);
  */

  Serial.print(" ");
  Serial.print(ax);
  Serial.print(" ");
  Serial.print(ay);
  Serial.print(" ");
  Serial.println(az);
  delay(2);
}
