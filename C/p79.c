#include <stdio.h>
#include <string.h>


char codes[151] = "319680180690129620762689762318368710720710629168160689716731736729316729729710769290719680318389162289162718729319790680890362319760316729380319728716";

int getCode(int n){
    int num = 0;
    return (codes[n*3] - '0')*100 + (codes[n*3 + 1] - '0')*10 + (codes[n*3+2] - '0');
}

int substring(char substring[3], char code[10]){
    int limit = 10-3;
    for(int i = 0; i < limit; i++){
        char snippet[3];
        snippet[0] = code[i]; snippet[1] = code[i+1]; snippet[2] = code[i+2];

        if(strcmp(substring, snippet) == 0)
            return 1;
    }
    return 0;
}

int correctOrder(char substring[3], char code[10]){
    int found = 0;
    
    for(int i = 0; i < 10; i++){
        char next = substring[found];
        char cur = code[i];
        if(next == cur)
            found ++;

        if(found == 3)
            return 1;
    }
    return 0;
}

int main(){

    //test
    char code[10] = {'a','b','c','e'};
    char x[3] = {'a', 'a', 'c'};
    printf("%d", correctOrder(x, code));

} 

