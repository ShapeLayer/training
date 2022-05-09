#include <stdio.h>
#include <string.h>

struct product {
  char name[20];
  int price;
  int stock;
} prd1, prd2;

int main() {
  // 위에서 구조체 정의 중에 전역 변수도 선언 가능함
  // struct product prd1;
  struct product prd2 = { "생수 2L", 9500, 20 };

  prd1.price = 15000;
  prd1.stock = 30;
  strcpy(prd1.name, "커피믹스");

  printf("%s : %d원, 재고량 = %d\n", prd1.name, prd1.price, prd1.stock);
  printf("%s : %d원, 재고량 = %d\n", prd2.name, prd2.price, prd2.stock);
  printf("%d\n", sizeof(struct product)); // 구조체 크기 출력: 28 Byte (20 + 4 + 4)
  return 0;
}