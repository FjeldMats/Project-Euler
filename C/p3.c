#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define NUMBER 600851475143

int isPrime(unsigned long value){
  for(unsigned long i = 2; i < value-1; i++){
    if(value % i == 0){
      return 0;
    }
  }
  return 1;
}

int main(){
  clock_t begin = clock();
  unsigned long n = (int) sqrt(NUMBER);

  for(unsigned long i = 2; i<n; n--){
    if(isPrime(n) == 1){
      if(NUMBER % n == 0){
        clock_t end = clock();
        double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
        printf("awns: %lu, time spendt: %f\n", n, time_spent);
        exit(0);
      }
    }
  }

}
