#include <stdio.h>

#define MAX 100

int main(void)
{
  int num1 = MAX;
  int num2 = MAX - 1;
  int num3 = -MAX;

  printf("num1 = %d\n", num1);
  printf("num2 = %d\n", num2);
  printf("num3 = %d\n", num3);
  
  printf("MAX = %d\n", MAX);

  return 0;
}