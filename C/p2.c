#include <stdio.h>

#define LIMIT 4000000

int main(){
  unsigned long num1, num2;
  unsigned long sum;

  num1 = 1;
  num2 = 2;

printf("Even valued fib terms > 4 000 000\n");
  while(num1 < LIMIT && num2 < LIMIT){

    if(num1 % 2 == 0){
      printf("%lu\n",num1);
      sum += num1;
    }
    if(num2 % 2 == 0){
      printf("%lu\n",num2);
      sum += num2;
    }

    num1 = num1 + num2;
    num2 = num1 + num2;
  }

  printf("\nsum: %lu\n",sum);

}
