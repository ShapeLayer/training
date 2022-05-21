/*
  P.106, Chapter 10.
*/

/* Lab10.c */
#include <stdio.h>

typedef struct point {
  int x, y;
} POINT;

typedef struct rect {
  int left, top, right, bottom;
} RECT;

void Swap(int *x, int *y);
void PrintRect(const char* title, const RECT *rt);
int NormalizeRect(const RECT *rt);
int IsPointInRect(const POINT *pt, const RECT *rt);

int main() {
  RECT rect1 = { 0 };
  POINT pt;

  printf("좌상단점/우하단점의 좌표를 입력하세요(left, top, right, bottom 순)\n");
  scanf("%d %d %d %d", &rect1.left, &rect1.top, &rect1.right, &rect1.bottom);

  PrintRect("입력된 직사각형", &rect1);
  if (NormalizeRect(&rect1))
    PrintRect("정규화된 직사각형", &rect1);

  printf("한점의 좌표를 입력하세요(x, y) : ");
  scanf("%d %d", &pt.x, &pt.y);

  printf("(%d, %d)는 ", pt.x, pt.y);
  if (IsPointInRect(&pt, &rect1))
    printf("직사각형 내부에 있습니다.\n");
  else
    printf("직사각형 외부에 있습니다.\n");

  return 0;
}

void Swap(int *x, int *y) {
  int temp = *x;
  *x = *y;
  *y = temp;
}

void PrintRect(const char* title, const RECT *rt) {
  printf("%s : 좌상단점=(%d,%d), 우하단점=(%d,%d)\n",
    title, rt->left, rt->top, rt->right, rt->bottom);
}

int NormalizeRect(const RECT *rt) {
  int result = 0;
  if (rt->left > rt->right) {
    Swap(&(rt->left), &(rt->right));
    result = 1;
  }
  if (rt->bottom > rt->top) {
    Swap(&(rt->bottom), &(rt->top));
    result = 1;
  }
  return result;
}

int IsPointInRect(const POINT *pt, const RECT *rt) {
  if ((rt->left <= pt->x && rt->right >= pt->x) && (rt->top >= pt->y && rt->bottom <= pt->y)) return 1;
  return 0;
}
