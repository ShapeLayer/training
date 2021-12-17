#include <stdio.h>

int main() {
    int min = 0; int max = 0;
    int puts;
    scanf("%d", &puts);
    min = puts;
    max = puts;

    while (1) {
        int puts;
        scanf("%d", &puts);
        if (puts == 0) {
            printf("MIN: %d, MAX: %d\n", min, max);
            return 0; // End Program by returning main function
        }
        if (puts < min) min = puts;
        if (puts > max) max = puts;
    }
    return 0;
}