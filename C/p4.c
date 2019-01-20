#include <stdio.h>
#include <string.h>

char *strrev(char *str){
  char *p1, *p2;

  if (! str || ! *str)
        return str;
  for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
  {
        *p1 ^= *p2;
        *p2 ^= *p1;
        *p1 ^= *p2;
  }
  return str;
}

int main(){
  int product;
  int largest = 0;
  for(int i = 1; i<1000; i++){
    for(int j = 1; j<1000; j++){
      product = i*j;

      char s1[100], s2[100];
      sprintf(s1, "%d" , product);
      strcpy(s2, s1);
      strrev(s2);
      if(strcmp(s1, s2) == 0){
        //printf("palindrome: %d*%d = %s \n", i,j, s1);
        if(product>largest){
          largest = product;
        }
      }
    }
  }
  printf("awns: %d\n", largest);
}
