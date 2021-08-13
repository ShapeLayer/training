#include <cstdio>

int main() {
  int n, cnt = 0;
  scanf("%d", &n);
  
  for (int i = 0; i <= n; i++) {
    for (int j = i; j <= n; j++) {
      cnt += (i + j);
    }
  }
  printf("%d\n", cnt);

  return 0;
}
