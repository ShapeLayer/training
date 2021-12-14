#include <cstdio>

int main() {
  for (int i = 5; i > 0; i--) {
    for (int j = 0; j < 5; j++) {
      if (i < 5-j) printf(" ");
      else printf("#");
    }
    for (int j = 1; j < 5; j++) {
      if (j < i) printf("#");
    }
    printf("\n");
  }
}
