#include <cstdio>

int main(void) {
    int s;
    scanf("%d", &s);
    if (s < 60) printf("F");
    else if (s < 70) printf("D");
    else if (s < 80) printf("C");
    else if (s < 90) printf("B");
    else printf("A");
    return 0;
}
