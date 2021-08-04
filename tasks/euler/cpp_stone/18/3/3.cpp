#include <cstdio>

int main() {
    int n, cnt=0;
    scanf("%d", &n);
    for (int i=1; i <= 100; i++) {
        if (n%i == 0) cnt++;
    }
    printf("%d", cnt);
    return 0;
}