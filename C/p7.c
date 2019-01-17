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
  int c;
  c = 0;
  unsigned long i = 1;
  while(1){
    if(isPrime(i) == 1){
      c++;
    }
    if(c == 10001){
        break;
    }
    i++;
  }
    printf("awns: %lu\n", i);
}
