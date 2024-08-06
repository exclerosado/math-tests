#include <stdio.h>

long long int fibonacci(int number){
    if (number <= 0){
        printf("Invalid input...\n");
        return -1;
    } else if (number == 1){
        return 0;
    } else if (number == 2){
        return 1;
    }else{
        return fibonacci(number - 1) + fibonacci(number - 2);
    }
}

int main(){
    long long int n = 10; //Insert here the n term you want to know
    printf("%lld\n", fibonacci(n));
    return 0;
}