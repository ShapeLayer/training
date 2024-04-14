#include <stdio.h>
#include <math.h>

typedef struct point {
  int x, y;
} POINT;

double GetDistance(POINT* p1, POINT* p2) {
  // -> 연산자
  // p2 -> x = point p2::x
  int dx = p2 -> x - p1 -> x;
  int dy = p2 -> y - p1 -> y;

  return sqrt(dx * dx + dy * dy);
}

int main() {
  POINT pt1 = { 0, 0 };
  POINT pt2 = { 10, 10 };
  double distance;

  // GetDistance의 매개변수가 변수의 주소임
  distance = GetDistance(&pt1, &pt2);
  printf("두 점 사이의 거리 : %5.2f\n", distance);

  return 0;
}