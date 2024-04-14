#include <stdio.h>

struct point {
  int x;
  int y;
};

typedef struct point POINT;

int main() {
  struct point pt1 = { 10, 20 };
  POINT pt2;
  pt2 = pt1;
  printf("pt2의 좌표: %d, %d\n", pt2.x, pt2.y);
  return 0;
}