#include <stdio.h>

typedef struct point {
  int x;
  int y;
} POINT;

void PrintPoint(const POINT* p);
void MovePoint(POINT* p, int dx, int dy);

int main () {
  POINT pt1 = { 100, 200 };
  POINT pt2 = { 300, 400 };

  printf("pt1 = ");
  PrintPoint(&pt1);
  printf("pt2 = ");
  PrintPoint(&pt2);
  
  MovePoint(&pt1, 10, 10);

  printf("변경된 pt1의 좌표 : ");
  PrintPoint(&pt1);
}

void PrintPoint(const POINT* p) {
  printf("(%d, %d)\n", p->x, p->y);
}

void MovePoint(POINT* p, int dx, int dy) {
  p -> x += dx;
  p -> y += dy;
}