// PROGRAM START

/* trackuino copyright (C) 2010  EA5HAV Javi
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

// Detector Custim Libs Import
#include <dht.h>

// Input Analog Pins
#define dht_apin A1 // Analog Pin sensor is connected to
int smokeA5 = A5;

// Smoke Threshold
int SmokeParameter = 0;

// Define dht Library as DHT
dht DHT;

void setup() {
  pinMode(smokeA5, INPUT);
  Serial.begin(9600);
  delay(1500);
}

void loop() {
  int analogSmokeSensor = analogRead(smokeA5);
  DHT.read11(dht_apin);

  Serial.print("Smoke Reading: ");
  Serial.println(analogSmokeSensor);
  Serial.print("Temperature Reading (Celsius): ");
  Serial.println(DHT.temperature);
  Serial.print("--------------------------------------------\n"); 

  // Checks if it has reached the threshold value
  while (analogSmokeSensor >= SmokeParameter)
  { 
    Serial.print("Smoke Reading: ");
    Serial.println(analogSmokeSensor);
    Serial.print("Temperature Reading (Celsius): ");
    Serial.println(DHT.temperature); 

    Serial.print("============================================\n");

    delay(1000);
  }
  if (analogSmokeSensor < SmokeParameter)
  {
    Serial.begin(9600);
    Serial.print("\nUnder Threshold. \n");
  }
  
  delay(1000);
}

// FILE PROGRAM END
