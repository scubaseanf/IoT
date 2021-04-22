//#include <stdio.h>
int i = 0;
int n1 = 0;
int n2 = 1;
int x = 0;


void setup() {
   Serial.begin(9600);
}

void loop() {
  
    if (i<6) {
    Serial.println (n1);
    x = (n1 + n2);
    n1 = n2;
    n2 = x;
    i++;
    }
}
