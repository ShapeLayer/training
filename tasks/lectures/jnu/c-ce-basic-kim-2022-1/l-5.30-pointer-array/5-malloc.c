#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct rect {
  int x, y;
  int width, height;
} RECT;

int main() {
  RECT* arr[100] = { NULL };
  int count = 0;
  while(1) {
    char choice;
    printf("직사각형을 만들겠습니까? (Y/N) : ");
    scanf("%c", &choice);

    while (getchar() != '\n');
    if (toupper(choice) == 'N')
      break;
    
    arr[count] = malloc(sizeof(RECT));
    arr[count] -> x = rand() % 400;
    arr[count] -> y = rand() % 400;
    arr[count] -> width = rand() % 100;
    arr[count] -> height = rand() % 100;
    count++;
  }

  printf("%d개의 직사각형이 만들어졌습니다.\n", count);
  for (int i = 0; i < count; i++) {
    printf("(x, y) = (%d, %d) width %d height %d\n", arr[i]->x, arr[i]->y, arr[i]->width, arr[i]->height);
  }
}