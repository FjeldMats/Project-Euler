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

    return sum;
}

/*
char *minemalRomanNumeral(int n){

    const char *numeral[30];
    numeral = malloc(20*sizeof(char));
    // all roman numerals and subtractive combinations
    const char *letters[13] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
    int nums[13]     = {1,    4,    5,  9,    10,   40,  50,  90,   100,  400 ,500, 900, 1000};

     
    int stringCouner = 0;
    while(n != 0){
        for(int i = 0; i<13; i++){
            if(i == 12 && n > 1000){
                n -= 1000;
                numeral[stringCouner] = "M";
                stringCouner++;
                printf("M\n");
                break;
            }
            if(nums[i] > n){
                n-= nums[i-1];
                numeral[stringCouner] = letters[i-1];
                stringCouner++;
                printf("%s\n",letters[i-1]);
                break;
            }
        }
    }

    return numeral;
}
*/

int minemalRomanNumeralLength(int n){


    // all roman numerals and subtractive combinations
    const char *letters[13] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
    int nums[13]             = {1,    4,    5,  9,    10,   40,  50,  90,   100,  400 ,500, 900, 1000};

    int length = 0;
    int stringCouner = 0;
    while(n != 0){
        for(int i = 0; i<13; i++){
            if(i == 12 && n > 1000){
                n -= 1000;
                stringCouner++;
                //printf("M");
                length++;
                break;
            }
            if(nums[i] > n){
                n-= nums[i-1];
                //printf("%s",letters[i-1]);
                if(i%2 == 0){
                    length += 2;
                }else{
                    length++;
                }
                break;
            }
        }
    }
    //printf("\n");

    return length;
}


int countLetters(char str[]){

    int i = 0;

    while(str[i] != '\0'){
        i++;
    }
    return i;

}

int countLetters2(char str[]){

    int i = 0;

    while(str[i] != '\n'){
        i++;
    }
    return i;

}





int main(){
    int saved = 0;
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

        printf("number: %d length %d, optimalLength: %d, savedChars: %d   <- %s", romanToInt(str), countLetters2(str), minemalRomanNumeralLength(romanToInt(str)), (countLetters2(str) - minemalRomanNumeralLength(romanToInt(str))),str);
        saved += countLetters2(str) - minemalRomanNumeralLength(romanToInt(str));
        index++;
    }
    fclose(fp);
    //printf("%d",countLetters("XIX"));
    printf("aws: %d\n", saved);
    return 0;

}