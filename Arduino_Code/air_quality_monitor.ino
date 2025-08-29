#include <DHT.h>

#define DHTPIN 2     
#define DHTTYPE DHT11
#define MQ135_PIN A0 

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int air_quality = analogRead(MQ135_PIN);

  Serial.print("Temp: ");
  Serial.print(t);
  Serial.print(" °C, Humidity: ");
  Serial.print(h);
  Serial.print(" %, Air Quality: ");
  Serial.println(air_quality);

  delay(2000); 
}
