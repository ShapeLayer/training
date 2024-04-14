#include <stdio.h>
#include <string.h>
#define SIZE 20

int main() {
  const char str[SIZE] = "HELLO WORLD";
  const char* literal = "hello world";
  const char* pstr = str;
  printf("문자열 리터럴: %s (%d)\n", literal, &literal);
  printf("문자 배열(변경전) : %s (%d)\n", str, pstr);
  strcpy(str, literal);
  printf("문자 배열(변경후) : %s (%d)\n", str, pstr);
  return 0;
}