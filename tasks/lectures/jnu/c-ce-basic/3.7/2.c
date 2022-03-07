#include <stdio.h>

int main() {
  float num;
  int i_part;
  float f_part;

  printf("실수를 입력하세요: ");
  scanf("%f", &num);

  i_part = num;
  f_part = num - i_part;
  
  printf("%f의 정수부는 %d이고, 실수부는 %f입니다.\n", num, i_part, f_part);
}