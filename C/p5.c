#include <stdio.h>

int evendiv(int num){
  for(int i = 1; i<=20; i++)
    if(num % i != 0)
      return 0;
  return 1;
}

int main(){
  int i = 1;
  while(1){
    if(evendiv(i) == 1){
      printf("awns: %d\n", i);
      break;
    }
    i++;
  }
}
