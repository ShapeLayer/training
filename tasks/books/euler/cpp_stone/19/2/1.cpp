#include <cstdio>

int main() {
    int n, cnt = 0;
    scanf("%d", &n);
    for (int i = 1; i < n; i++) {
        if (n % i == 0) cnt += i;
    }
    if (cnt < n) printf("DEFICIENT");
    else if (cnt > n) printf("ABUNDANT");
    else printf("PERFECT");
    return 0;
}
