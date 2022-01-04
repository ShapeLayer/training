#include <cstdio>

int main(void) {
    int a, b, c;
    char x, y;
    scanf("%d %d %d", &a, &b, &c);
    if      (a + b == c) {x = '+'; y = '=';}
    else if (a - b == c) {x = '-'; y = '=';}
    else if (a * b == c) {x = '*'; y = '=';}
    else if (a / b == c) {x = '/'; y = '=';}
    else if (b + c == a) {x = '='; y = '+';}
    else if (b - c == a) {x = '='; y = '-';}
    else if (b * c == a) {x = '='; y = '*';}
    else if (b / c == a) {x = '='; y = '/';}
    printf("%d%c%d%c%d\n", a, x, b, y, c);
    return 0;
}
