#include <stdio.h>
#include <math.h>

unsigned long triangleNum(int nth){
  return nth*(nth+1)/2;
}

//needs optimization
unsigned long countFactors(unsigned long number) {
  unsigned long sum = 0;
  for(unsigned long i = 1; i<= number; i++){
    if(number%i == 0){
      sum++;
    }
  }
  return sum;
}

int main(){
  int i = 1;
  while(1){
    unsigned int num = triangleNum(i);
    unsigned int cf =  countFactors(num);
    if(cf>500){
      printf("i: %d num: %lu factors %lu\n",i, num, cf);
      break;
    }
    i++;
  }

}
