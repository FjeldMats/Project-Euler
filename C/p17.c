#include <stdio.h>


// 1 - 19     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
int L1[19] = {3,3,5,4,4,3,5,5,4,3, 6, 6, 8 ,8 ,7, 7, 9, 8, 8};

//20,30,40 ... 100    20  30 40 50 60 70 80 90
int L2[8] =           {6, 6, 5, 5, 5, 7, 6, 6};
int hundred = 7;
int and = 3;

int convert(int n){
    int temp = n;
    int x2 = n % 10;
    temp = temp / 10;
    int x1 = temp%10;

    if(x1 <= 1 && n != 10)
        return L1[n-1];
    else if(n == 10)
        return L1[9];
    else
        return L1[x2-1] + L2[x1-2];
}

int convert2(int n){
    int temp = n;
    int x1,x2,x3;
    x3 = n % 10;
    temp /= 10;
    x2 = temp % 10;
    temp /= 10;
    x1 = temp % 10;

    if(n % 100 == 0){
        return L1[x1-1] + hundred;
    }
    else{
        return L1[x1-1] + hundred + and + convert(x2*10 + x3);
    }
}

int main(){

    int sum = 0;

    //1 - 99
    for (int i=1; i<=99;i++){
        sum += convert(i);
    }

    //100 - 1000
    for (int i = 100; i<=999; i++){
        sum += convert2(i);
    }

    // one thousand = 11
    printf("sum: %d\n", sum+11);
}