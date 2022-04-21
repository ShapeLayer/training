#include <stdio.h>

int main(void)
{
  float grade1 = 3.75;
  double grade2 = 3.65;

  // 디자인을 복잡하게 할 수록 얼마나 많은 용량을 갖고 있는지 확인할 필요가 있음
  // 이 때 유용하게 쓰임
  printf("%d\n", sizeof(grade1));
  printf("%d\n", sizeof(grade2));
}