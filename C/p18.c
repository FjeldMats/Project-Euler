#include <stdio.h>

#define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; })

// 15 rows
// + 1 num every row down 
// every num 2 char
char nums[240] = "759564174782183587102004824765190123750334880277730763679965042806167092414126568340807033414872334732371694295371446525439152975114701133287773177839681757917152381714914358502729486366046889536730731669874031046298272309709873933853600423";


int getNum(int row, int col){
    int t = (row * (row + 1));
    int c  = col * 2;

    char num[2];
    num[0] = nums[t+c];
    num[1] = nums[t+c+1];

    return (num[0]-'0')*10 + (num[1] -'0');
}

int getMaxChild(int row, int col, int array[16][16]){
    int c1 = array[row+1][col];
    int c2 = array[row+1][col+1];
    return max(c1 , c2);
}

int main(){
    int array[16][16] = {0};

    //put data into 2D array
    int col, c;
    col = 0;
    c = 1;

    for(int i=0;i<15;i++){
        col = 0;
        for(int j=0;j<15;j++){
            if(j<c){
                array[i][j] = getNum(i, col);
                col++;
            }
            /*
            int val = array[i][j];
            if(val<10)
                printf("0%d ", val);
            else
                printf("%d ", val);
            */
        }
        //printf("\n");
        c++;
    }

    //calculate max sum

    int cCol = 13;

    for(int row = 13; row >= 0; row--){
        for(int col = 0; col<=cCol; col++){
            int max = getMaxChild(row,col,array);
            array[row][col] = array[row][col] +  max;
            //printf("%d %d %d\n",getNum(row,col), max, array[row][col]);
        }
        //printf("\n");
        cCol--;
    }

    /*
    for(int i= 0;i<15;i++){
        for(int j=0;j<15;j++){
            printf("%d ",array[i][j]);
        }
        printf("\n");
    }
    */

    printf("awns: %d\n", array[0][0]);
}