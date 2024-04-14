#include <stdio.h>
#include <stdlib.h>

int fib_recur(int n);
int fib_loop(int n);

int main() {
  int num;

  printf("몇번째 피보나치 값을 얻고 싶습니까? : ");
  scanf("%d", &num);

  printf("반복문 : %d\n", fib_loop(num));
  printf("재귀함수 : %d\n", fib_recur(num));

  return 0;
}

int fib_recur(int n) {
  if (n < 3) return 1;
  return fib_recur(n-1) + fib_recur(n-2);
}

int fib_loop(int n) {
  int* dp = NULL;
  dp = (int*)malloc(sizeof(int) * (n+1));
  dp[1] = 1;
  dp[2] = 1;
  for (int i = 3; i <= n; i++) {
    dp[i] = dp[i-1] + dp[i-2];
  }
  int res = *(dp+n);
  free(dp);
  return res;
}