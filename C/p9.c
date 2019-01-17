#include <stdio.h>

int main(){
  for(int i = 1; i<1000; i++){
    for(int j = 1; j<1000; j++){
      for(int k = 1; k<1000; k++){
        if(i*i + j*j == k*k && i<j && j<k && i<k && i+j+k == 1000){
          printf("%d^2 + %d^2 = %d^2\n",i,j,k);
          int prod = i*j*k;
          printf("%d\n", prod);
        }
      }
    }
  }
}
