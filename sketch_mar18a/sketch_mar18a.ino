#include <NewPing.h>

NewPing sonar(10, 11, 100);

void setup() {
  Serial.begin(9600);
  delay(50);  
}

void loop() {
  Serial.println(sonar.ping_cm());
  /*if(sonar.ping_cm() > 0) {
    Serial.println("Someone passed by");
  }*/
  delay(1000);
}