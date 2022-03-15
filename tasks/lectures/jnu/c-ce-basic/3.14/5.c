#include <stdio.h>

int main(void)
{
  char grade = '\x41'; // ASCII Code

  printf("grade = %d, %c\n", grade, grade);
}