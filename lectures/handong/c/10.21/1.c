#include <stdio.h>

int Morgan(int a, int b) { return !(!a*!b); }

int main() {
    int a, b;
    printf("input bool data: ");
    scanf("%d %d", &a, &b);
    printf("OR 연산 출력: ");
    printf(Morgan(a, b) ? "TRUE" : "FALSE");
    return 0;
}