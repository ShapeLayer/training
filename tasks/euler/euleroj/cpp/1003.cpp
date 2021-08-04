#include <cstdio>

int main() {
    int n, odd = 0, even = 0;
    scanf("%d", &n);
    for (int i=1; i<=n; i++) {
        if (i % 2 == 0) even += i;
        else odd += i;
    }
    printf("%d\n%d", even, odd);
    return 0;
}
