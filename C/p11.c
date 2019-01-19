#include <stdio.h>

char num[] = "08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748";

int getNum(int row, int col){
  row = 40 * row;     // 20 number where each num has 2 digits - 20 * 2
  col = 2 * col;      // each num is 2 digits

  int ret = num[col+row] - '0';    //first digit
  int ret1 = num[col+row+1] - '0'; // secound digit

  //printf("row: %d, col: %d (%d) -> %d\n",row,col,row+col, ret*10 + ret1);

  return ret*10 + ret1;
}

unsigned long rightH(int row, int col, int table[20][20], int len){

  if( ((row + len)>20) || (col+len)>20){
    return 1;
  }

  int height = row;
  unsigned long prod = 1;

  for(int i=col; i<(len+col); i++){
    //printf("%d, ", table[row][i]);
    prod *= table[height][i];
    height++;
  }
  //printf(": %lu /\n", prod);
  return prod;
}

unsigned long leftH(int row, int col, int table[20][20], int len){

  if(((row - len+1)<0) || (col+len)>20)
    return 1;

  int height = row;
  unsigned long prod = 1;

  for(int i=col; i<(len+col); i++){
    //printf("%d, ", table[row][i]);
    prod *= table[height][i];
    height--;
  }
  //printf(": %lu \\ \n", prod);
  return prod;
}

unsigned long vertical(int row, int col, int table[20][20], int len){
  if((row + len)>20)
    return 1;

  unsigned long prod = 1;

  for(int i=row; i<(row+len); i++){
    //printf("%d, ", table[row][i]);
    prod *= table[i][col];
  }
  //printf(": %lu |\n", prod);
  return prod;
}

unsigned long horizontal(int row, int col, int table[20][20], int len){
  if((col+len)>20)
    return 1;

  unsigned long prod = 1;

  for(int i=col; i<(col+len); i++){
    //printf("%d, ", table[row][i]);
    prod *= table[row][i];
  }
  //printf(": %lu -\n", prod);
  return prod;
}

unsigned long max(unsigned long list[]){
  unsigned long b = 0;
  for(int i=0; i<4;i++){
    if(list[i]>b)
      b = list[i];
  }
  return b;
}

int main(){
  int table[20][20];

  for(int i = 0; i<20; i++){
    for(int j = 0; j<20; j++){
      table[i][j] = getNum(i,j);
    }
  }

  unsigned long largestProd = 0;
  int length = 4;

  //search
  for(int i = 0; i<20; i++){
    for(int j = 0; j<20; j++){

      unsigned long list[4] = {rightH(i,j,table,length), leftH(i,j,table,length), vertical(i,j,table,length), horizontal(i,j,table,length)};
      unsigned long b = max(list);

      if(b>largestProd)
        largestProd = b;
    }
  }
  printf("awns: %lu\n", largestProd);
}
