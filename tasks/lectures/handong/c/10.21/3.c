#include <stdio.h>
#include <stdlib.h>

int rndnum(int init, int fin) { return init + rand()%(fin - init); } // fin is not included.

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    for (int i = 0; i < 5; i++) printf("%d ", rndnum(a, b));
    return 0;
}