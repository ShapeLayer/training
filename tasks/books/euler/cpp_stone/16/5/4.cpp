#include <cstdio>

int main(void) {
    int init, fina;
    scanf("%d %d", &init, &fina);
    for (int i = init; i >= fina; i--) printf("%d ", i);
    return 0;
}
