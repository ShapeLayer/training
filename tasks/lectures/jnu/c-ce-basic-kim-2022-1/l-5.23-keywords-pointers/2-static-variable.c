#include <stdio.h>

void TestStatic(void);

int main() {
  TestStatic();
  TestStatic(); 

  return 0;
}

void TestStatic(void) {
  int num = 0;
  static int count = 0;

  printf("num = %d, ", ++num);
  printf("count = %d\n", ++count);
}