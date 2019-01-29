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

    int index = 0;
    int sum = 0;

    while(romanNum[index] != '\n'){

        if(romanNum[index] == 'I' & ( romanNum[index + 1] == 'V' || romanNum[index + 1] == 'X')){
            
            sum+= lookupLetter(romanNum[index+1]) - lookupLetter(romanNum[index]);
            index += 2;

        }
        else if(romanNum[index] == 'X' & ( romanNum[index + 1] == 'L' || romanNum[index + 1] == 'C')){
            sum+= lookupLetter(romanNum[index+1]) - lookupLetter(romanNum[index]);
            index += 2;

        }
        else if(romanNum[index] == 'C' & ( romanNum[index + 1] == 'D' || romanNum[index + 1] == 'M')){
            sum+= lookupLetter(romanNum[index+1]) - lookupLetter(romanNum[index]);
            index += 2;

        }else{
            sum += lookupLetter(romanNum[index]);
            index++;

        }

        
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
        printf("%d <- %s", romanToInt(str), str);
        index++;
    }
    fclose(fp);

    /*
    for(int i = 0;i<1000;i++){
        printf("%s \b = %d\n", roman[i], romanToInt(roman[i]));
    }
    */

    return 0;

}