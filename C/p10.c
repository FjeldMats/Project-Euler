#include <stdio.h>

#define LIMIT 2000000
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
  unsigned int sum = 0;
  for(unsigned int i = 1; i<LIMIT; i++){
    if(isPrime(i) == 1){
      sum += i;
    }
  }
  printf("%lu\n", sum);
}
