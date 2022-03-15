#include <stdio.h>

int main(void)
{
  char grade = '\x41';
  int data = 0x7b;
  unsigned int age = 75U;
  long fileSize = 1234567L;
  double area = 123.25;
  double taxRate = 25e-2;
  float temperature = 17.5F;

  printf("grade = %c\n", grade);
  printf("data = %d, %o, %x\n", data, data, data);
  printf("age = %u\n", age);
  printf("fileSize = %d", fileSize);
  printf("area = %f, %e, %g\n", area, area, area);
  printf("taxRate = %f\n", taxRate);
  printf("temperature = %f\n", temperature);
}