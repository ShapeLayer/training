#include <cstdio>

int main(void) {
    int a, b, s = 0;
    scanf("%d %d", &a, &b);
    for (int i = ((int)a/5)*5; i <= b; i += 5) s += i;
    printf("%d", s);
    return 0;
}
