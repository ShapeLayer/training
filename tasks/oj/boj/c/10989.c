// Counting Sort

#include <stdio.h>

int main() {
  int cnt[10001] = { 0 };
  int n, gets;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &gets);
    cnt[gets]++;
  }
  for (int i = 0; i < 10001; i++)
    for (int j = 0; j < cnt[i]; j++)
      printf("%d\n", i);
  
  return 0;
}