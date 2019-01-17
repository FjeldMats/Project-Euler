#include <stdio.h>

int main(){
  int sum = 0;
  for(int n = 0; n < 1000; n++){
    if(n % 3 == 0 || n % 5 == 0)
      sum = sum + n;
  }
  printf("sum: %d\n", sum);

}
