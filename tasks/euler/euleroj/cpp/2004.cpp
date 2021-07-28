#include <cstdio>

int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);
    if (n <= k) printf("2\n");
    else if ((n * 2) % k == 0) printf("%d\n", n * 2 / k);
    else printf("%d\n", (n * 2) / k + 1);
    return 0;
}
