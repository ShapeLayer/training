#include <cstdio>
#define max(a,b) (((a) > (b)) ? (a) : (b))

int main(void) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a == b && b == c) printf("%d", 10000 + a * 1000);
    else if (a != b && b != c && c != a) printf("%d", max(max(a, b), c)*100);
    else {
        int n;
        if (a == b && a != c) n = a;
        else n = c; // b == c || c == a
        printf("%d", 1000 + n * 100);
    }
    return 0;
}
