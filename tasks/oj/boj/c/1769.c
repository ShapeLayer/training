#include <stdio.h>
#include <string.h>

int main() {
  int n = 0, counts = 0;
  char gets[1000000] = "";
  scanf("%s", gets);
  for (int i = 0; i < strlen(gets); i++) {
    n += (int)gets[i] - 48;
  }
  if (strlen(gets) >= 2) {
    counts++;
  }
  while (n >= 10) {
    int new = 0;
    while (n != 0) {
      new += n % 10;
      n /= 10;
    }
    n = new;
    counts++;
  }
  printf("%d\n", counts);
  printf("%s\n", n == 3 || n == 6 || n == 9 ? "YES" : "NO");
}