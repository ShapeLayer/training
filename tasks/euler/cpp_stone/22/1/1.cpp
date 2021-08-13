#include <cstdio>

int main() {
  for (int i = 1; i <= 5; i++) {
    for (int j = 1; i >= j; j++) {
      printf("%d", j);
    }
    printf("\n");
  }
  return 0;
}
