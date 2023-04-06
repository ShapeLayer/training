#include <cstdio>

int main(void) {
    int n, s = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) s += (i * (n+1-i));
    printf("%d", s);
    return 0;
}
