#include <stdio.h>
#include <string.h>

#define MAX_PRODUCT 5

// 타입 선언: PRODUCT
typedef struct product {
  char name[20];
  int price;
  int stock;
} PRODUCT;

int main() {
  PRODUCT prd[MAX_PRODUCT];

  printf("%d개의 상품 정보를 입력하세요.\n", MAX_PRODUCT);
  for (int i = 0; i < MAX_PRODUCT; i++) {
    printf("상품명 : ");
    scanf("%s", prd[i].name);
    printf("가격 재고량 : ");
    scanf("%d %d", &prd[i].price, &prd[i].stock);
  }

  printf("\n상품명               가격 재고량 \n");
  for (int i = 0; i < MAX_PRODUCT; i++) {
    printf("%-20s %d\t\t%-10d", prd[i].name, prd[i].price, prd[i].stock);
    if (prd[i].stock <= 5) printf(" => 재고 부족. 더 주문하세요.");
    printf("\n");
  }
  return 0;
}