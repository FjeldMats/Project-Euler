#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lookupLetter(char l){
    int num;

    char letters[7] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    int nums[7]     = { 1,   5,   10,  50, 100  ,500, 1000};

    for(int i = 0; i<7; i++){
        if(letters[i] == l)
            return nums[i];
    }
    return 0;
}

int romanToInt(char romanNum[15]){

    int numbers[15];
    int index = 0;
    int sum = 0;

    while(romanNum[index] != '\n'){
        numbers[index] = lookupLetter(romanNum[index]);
        //printf("%d \n", numbers[index]);
        index++;
    }
    //printf("\n");

    return sum;
}

int main(){

    FILE *fp;
    char str[1000];
    char* filename = "roman.txt";

    fp = fopen(filename, "r");
    if(fp == NULL){ 
        printf("cannot read %s", filename);
        return 1;
    }

    char roman[1000][15];
    int index = 0;
    while(fgets(str, 1000, fp) != NULL){
        strcpy(roman[index], str);
        //printf("%s", str);
        index++;
    }
    fclose(fp);
    printf("\n");

    /*
    for(int i = 0;i<1000;i++){
        printf("%s \b = %d\n", roman[i], romanToInt(roman[i]));
    }
    */

    printf("%d\n", romanToInt("VI\n"));
    return 0;

}