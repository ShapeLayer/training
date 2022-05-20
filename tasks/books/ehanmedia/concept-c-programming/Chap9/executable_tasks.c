/*
  P.90, Chapter 9.
*/

/* Lab09.c */
#include <stdio.h>
#define COUNT 5

struct rect {
  int left;
  int top;
  int right;
  int bottom;
};
typedef struct rect RECT;

int main() {
  RECT rects[COUNT] = {0};
  int i;

  for (i = 0; i < COUNT; i++) {
    printf("좌상단점/우하단점의 좌표를 입력하세요(left, top, right, bottom 순)\n");
    scanf("%d %d %d %d", rects[i].left, rects[i].top, rects[i].right, rects[i].bottom);
  }

  for (i = 0; )

  return 0;
}
