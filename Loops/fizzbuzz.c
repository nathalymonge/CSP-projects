#include <stdio.h>
int i;
char fizz[50], buzz[50], fizzbuzz[50];

int main(){
    //create a loop that counts to 50
    for(i=1;i<=50;i++){
    //replace #'s divisible by both with "fizzbuzz"
    if(i%3==0 && i%5==0){
        printf("fizzbuzz\n", fizzbuzz);
    //replace #'s divisible by 3 with "fizz"
    }else if(i%3==0){
        printf("fizz\n", fizz);
    //replace #'s divisible by 5 with "buzz"
    }else if(i%5==0){
        printf("buzz\n", buzz);
    //print all other numbers
    }else{
        printf("%d\n",i);
    }
    }
}