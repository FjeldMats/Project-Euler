#include <stdio.h>


int isPrime(unsigned long value){
  if(value  == 1 || value == 0){
    return 0;
  }
  for(unsigned long i = 2; i < value; i++){
    if(value % i == 0){
      return 0;
    }
  }
  return 1;
}

int main(){
  unsigned long sum = 0;
  for(unsigned int i = 2; i < 2000000; i++){
    if(isPrime(i) == 1){
      sum += i;
    }
    if(i % 10000 == 0){
      float progress = ((float)i/2000000.0)*100;
      printf("sum: %lu, %% %f\n", sum, progress);
    }
    }

  printf("%lu\n", sum);
}
