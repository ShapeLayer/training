#include <stdio.h>
#define DEBUG
#define ARRAY_LIMITS (int)10e7

int dp[ARRAY_LIMITS] = { 0 };

int fib(int num) {
	dp[1] = 1;
	dp[2] = 1;
	for (int i = 3; i <= num; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}
#ifdef DEBUG
	for (int i = 1; i < num; i++) {
		printf("%d -> ", dp[i]);
	}
	printf("%d\n", dp[num]);
#endif
	return dp[num];
}

int main(void) {
	int num;
	printf("몇번째 피보나치 값을 얻고 싶습니까? : ");
	scanf("%d", &num);
	printf("결과값 : %d\n", fib(num));
	return 0;
}
