#include <stdio.h>

unsigned long collatz(unsigned long n){
    return (n % 2 == 0) ? n/2 : 3*n + 1;
}

int countCollatz(int start){

    unsigned long number = collatz(start);
    int cnt = 1;
    while(number != 1){
        number = collatz(number);
        cnt++;
    }
    return cnt+1;
}

int main(){

    int i = 1;
    int Lchain = 0;
    int num = 0;
    
    while(i < 1000000){

        int chain = countCollatz(i);
        if(chain>Lchain){
            Lchain = chain;
            num = i;
        }

        i++;
    }

    printf("longest chain: %d with starting number %d", Lchain, num);

}
