#include <NewPing.h>
//install dependencies under tools > manage dependencies

//pin and max distance in cm defined
NewPing sonar(10, 11, 100);
NewPing sonar2(6, 7, 100);

int visitors = 0;
bool reset = false;


void setup() {
  Serial.begin(9600);
  delay(50);  
}

void loop() {

  //checks which sensor is triggered to determine increast or decrease
  //reset check ensures no repeat scans in case of still standing target
  if((sonar.ping_cm() > 0) && (sonar2.ping_cm() == 0) && (reset == true)){
    visitors++;
    Serial.println(visitors);
    reset = false;
    delay(1000);
  }
  else if((sonar.ping_cm() == 0) && (sonar2.ping_cm() > 0) && (reset == true)){
    visitors--;
    Serial.println(visitors);
    reset = false;
    delay(1000);
  }
  else{
    Serial.print("NOTHING NEW ");
    Serial.println(visitors);
    reset = true;
  }

 
  /*
  // Checks distance
  Serial.print("1 ");
  Serial.println(sonar.ping_cm());
  delay(100);
  Serial.print("2 ");
  Serial.println(sonar2.ping_cm());
  }*/

  delay(1000);
}