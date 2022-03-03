#include <stdio.h>

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    int gets;
    scanf("%d", &gets);
    int pigs[6];
    for (int j = 0; j < 6; j++) {
      scanf("%d", &pigs[j]);
    }
    int day = 1;
    int sums = 0;
    for (int j = 0; j < 6; j++) sums += pigs[j];
    while (sums <= gets) {
      day++;
      int prev[6];
      for (int j = 0; j < 6; j++) {
        prev[j] = pigs[j];
      }
      for (int j = 0; j < 6; j++) {
        pigs[j] += prev[(j+5)%6];
        pigs[j] += prev[(j+1)%6];
        pigs[j] += prev[(j+3)%6];
      }
      sums = 0;
      for (int j = 0; j < 6; j++) sums += pigs[j];
    }
    printf("%d\n", day);
  }
}