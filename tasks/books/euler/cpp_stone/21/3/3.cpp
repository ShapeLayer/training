#include <cstdio>

int main() {
  for (int i = 1; i < 6; i++) {
    for (int j = 0; j < 5; j++) {
      if (i < 5-j) printf(" ");
      else printf("#");
    }
    printf("\n");
  }
}
