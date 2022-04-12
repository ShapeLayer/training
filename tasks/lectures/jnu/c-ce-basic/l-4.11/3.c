#include <stdio.h>
#include <string.h>

int main() {
  char str1[20], str2[20] = "ABCDE";
  strcpy(str1, "abcde");

  // strcmp returns 0 when target is same
  if (strcmp(str1, "abcde") == 0)
    printf("같음\n");
  else
    printf("다름\n");
  if (strcmp(str1, str2) == 0)
    printf("같음\n");
  else
    printf("다름\n");

  return 0;
}
