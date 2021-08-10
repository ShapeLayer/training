#include <cstdio>

int main() {
    int n, sum = 1;
    scanf("%d", &n);
    printf("%d!=(", n);
    for (int i = 1; i < n; i++) {
        printf("%d*", i);
        sum *= i;
    }
    sum *= n;
    printf("%d)=%d", n, sum);
    return 0;
}
