#include<stdio.h>

 char aname[] = "Randy";
 char bname[] = "Jessica";
 char cname[] = "Eva";
 char dname[] = "Nathaly";
 char ename[] = "Israel";

void hello(char name[]){
    printf("Hello %s\n", name);
}

   
int main(void){
   hello("Randy");
   hello("Jessica");
   hello("Eva");
   hello("Nathaly");
   hello("Israel");
    return 0;

}