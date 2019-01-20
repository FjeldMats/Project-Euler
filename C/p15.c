#include <stdio.h>
#include <math.h>


unsigned long long factorial(unsigned long long n){
    if(n>= 1)
        return n*factorial(n-1);
    else
        return 1;
}

int main(){
    long long unsigned a = factorial(40);
    long long unsigned b = factorial(20);
    long long unsigned c = pow(b,2);
    long long d = a/c;
    printf("awns %llu", d);
}