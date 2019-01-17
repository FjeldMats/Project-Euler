#include <stdio.h>

int main(){
  long sumq, sumq2;
  sumq = 0;
  sumq2 = 0;
  for(long i = 1; i<=100; i++){
    sumq += i;
    sumq2 += i*i;
    printf("%ld %ld\n",sumq,sumq2);
  }

  sumq *= sumq;
  long diff = sumq - sumq2;

  printf("awns: %ld \n",diff);

}
