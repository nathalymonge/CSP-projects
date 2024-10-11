#include <stdio.h>
char fam[8][20] = {"Jessica", "Eva",  "Nathaly", "Israel"};
int i;
int main(){
    for(i=0; i < 4; i++){
        printf("Hello %s\n", fam[i]);
    }
    return 0;
}