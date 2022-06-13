#include <stdio.h>
#define MAX_PRODUCT 3

typedef struct product {
  char name[20];
  int price;
  int stock;
} PRODUCT;

int main() {
  PRODUCT prd[MAX_PRODUCT];
  FILE *fp = NULL;

  printf("%d 개의 상품 정보를 입력하세요.\n", MAX_PRODUCT);
  for (int i = 0; i < MAX_PRODUCT; i++) {
    printf("상품명 : ");
    scanf("%s", prd[i].name);
    printf("가격, 재고량 : ");
    scanf("%d %d", &prd[i].price, &prd[i].stock);
  }

  fp = fopen("gets.out", "w");
  // r, w, a, r+, w+, a+, t, b

  if (fp == NULL) {
    printf("파일 열기 실패\n");
    return -1;
  } else {
    fprintf(fp, "상품명\t\t\t\t\t\t\t 가격\t재고량\n");
    for (int i = 0; i < MAX_PRODUCT; i++) {
      fprintf(fp, "%-20s %d\t%d\n", prd[i].name, prd[i].price, prd[i].stock);
    }
  }

  return 0;
}

