#include <stdio.h>


unsigned long long factorial(unsigned long long n){
    if(n>= 1)
        return n*factorial(n-1);
    else
        return 1;
}

int main(){

   unsigned long long number =  factorial(100);
   char nums[200];
    printf("%llu", number);
   sprintf(nums, "%llu", number);

   for(int i = 0; i<200; i++){
       //printf("%c \n", nums[i]);
   }

}