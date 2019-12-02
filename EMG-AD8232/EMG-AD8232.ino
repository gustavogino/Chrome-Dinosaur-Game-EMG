
#define MAX_BUFFER 10
#define OFFSET 1.5

uint32_t data = 0;
uint32_t sumData=0;
uint32_t countData=0;
uint32_t newData;
uint32_t avgData = 0;
bool pronto = false;

void getdata()
{
 if (countData<MAX_BUFFER) {
    countData++;
    sumData+=newData;
 }else{
    data = sumData / countData;
    countData = 0;
    sumData = 0;
    Serial.println(data);
    if(data > (avgData * OFFSET)){
      Serial.println(99999);
    }
 }   
}

void calibrar()
{
 if (countData<1000) {
    countData++;
    sumData+=newData;
 }else{
    avgData = sumData / countData;
    countData = 0;
    sumData = 0;
    pronto = true;
 }
}

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
  pinMode(10, INPUT); // Setup for leads off detection LO +
  pinMode(11, INPUT); // Setup for leads off detection LO -
}

void loop() {
  
  if((digitalRead(10) == 1)||(digitalRead(11) == 1)){
     delay(0.1);
  }
  else{
    if(!pronto){
        newData = analogRead(A0);
        calibrar();
      }else{
        newData = analogRead(A0);
        getdata();
      }
  }
}
