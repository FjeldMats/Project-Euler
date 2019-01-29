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

char* minemalRomanNumeral(int n){

    char *numeral[20] = malloc(20*sizeof(char));

    // all roman numerals and subtractive combinations
    char letters[13] = {'I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'};
    int nums[13]     = {1,    4,    5,  9,    10,   40,  50,  90,   100,  400 ,500, 900, 1000};

     
    int stringCouner = 0;
    while(n != 0){
        for(int i = 0; i<13; i++){
            if(i == 12 && n > 1000){
                n -= 1000;
                numeral[stringCouner] = 'M';
                stringCouner++;
                break;
            }
            if(nums[i] > n){
                n-= nums[i-1];
                numeral[stringCouner] = letters[i-1];
                stringCouner++;
                break;
            }
        }
    }

    return *numeral;
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

   printf("\n");
   printf("350 -> %s", minemalRomanNumeral(350));

    return 0;

}