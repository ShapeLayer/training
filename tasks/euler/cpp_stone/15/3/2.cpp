#include <cstdio>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    if (a == 1 && b == 1) printf("1");
    else if (a != 1 && b != 1) printf("3");
    else printf("2");
    return 0;
}
