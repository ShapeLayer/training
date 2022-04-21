// Theme: 분기문
// break; continue; goto;
#include <stdio.h>

int main() {
  for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
    if (i == 3) goto exit;
  }
  exit:
  return 0;
}