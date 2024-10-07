#include<stdio.h>
char sibilings[8][20] = {"Jessica", "Eva", "Nathaly", "Israel"};
int i;
int main(){
    while (i < 8){
        printf("%s Nathaly", sibilings[i]);
        i+=1;
    }
return 0;
}