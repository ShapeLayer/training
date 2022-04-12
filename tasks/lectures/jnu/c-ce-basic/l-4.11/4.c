#include <stdio.h>
#include <string.h>

int main() {
  char str1[20], str2[20] = "ABCDE";
  strcpy(str1, "abcde");
  printf("%d\n", strlen(str1));
  return 0;
}
