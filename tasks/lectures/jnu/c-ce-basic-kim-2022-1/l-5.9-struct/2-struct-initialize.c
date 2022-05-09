#include <stdio.h>
#include <string.h>

struct point {
  int x, y;
};

int main() {
  struct point pt1 = { 10, 20 }, pt2 = { 30, 40 };
  struct point pt3 = pt1;
  struct point pt4;

  printf("pt1의 x, y 좌표를 입력하세요 : ");
  scanf("%d %d", &pt1.x, &pt1.y);
  printf("pt2의 x, y 좌표를 입력하세요 : ");
  scanf("%d %d", &pt2.x, &pt2.y);

  if (pt1.x == pt2.x && pt1.y == pt2.y)
    printf("두 점의 좌표가 같습니다.\n");
  else
    printf("두 점의 좌표가 다릅니다.\n");

  pt4 = pt2;
  return 0;
}