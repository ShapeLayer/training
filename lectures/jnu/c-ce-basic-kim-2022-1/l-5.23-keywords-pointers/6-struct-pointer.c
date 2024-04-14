#include <stdio.h>
#include <string.h>

typedef struct product {
  char name[20];
  int price;
  int stock;
} PRODUCT;

int main() {
  PRODUCT prod1 = { "A4용지", 5000, 50 };
  PRODUCT prod2 = { "충전기", 10000, 3 };
  PRODUCT prod3 = { "이어폰", 25000, 10 };
  PRODUCT* prd[] = { &prod1, &prod2, &prod3 };

  int count = sizeof(prd) / sizeof(prd[0]);

  for (int i = 0; i < count; i++) {
    printf("%-15s   %8d   %10d", 
      prd[i]->name, prd[i]->price, prd[i]->stock);
    // (*prd[i]).name, (*prd[i]).price, (*prd[i]).stock

    if (prd[i]->stock < 10)
      printf(" ==> 주문 필요!!\n");
    else
      printf("\n");
  }
}