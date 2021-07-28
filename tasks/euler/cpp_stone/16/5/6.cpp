#include <cstdio>

int main(void) {
    int init, fina, s = 0;
    scanf("%d %d", &init, &fina);
    for (int i = init; i <= fina; i++) s += i;
    printf("%d", s);
    return 0;
}
