#include <stdio.h>

int main() {
  int num;
  int* pnum = &num;
  int** ppnum = &pnum;
  
  printf("값을 입력하세요 : ");
  scanf("%d", &num);
  printf("num의 값 : %d\n", num);
  printf("num의 주소 : %d\n", &num);
  printf("\n");
  printf("포인터 변수의 값 : %d\n", pnum);
  printf("포인터 변수의 주소 : %d\n", &pnum);
  printf("\n");
  printf("이중 포인터의 값 : %d\n", ppnum);
  printf("이중 포인터의 주소 : %d\n", &ppnum);
  printf("\n");
  return 0;
}