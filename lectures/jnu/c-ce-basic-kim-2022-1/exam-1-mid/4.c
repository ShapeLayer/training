#include <stdio.h>

int main() {
	int gets, puts = 0, isNegative = 0;
	printf("정수를 입력하세요 : ");
	scanf("%d", &gets);
	if (gets < 0) {
		isNegative = 1;
		gets *= -1;
	}
	while (gets) {
		int val = gets % 10;
		puts = puts * 10 + val;
		gets /= 10;
	}
	puts = !isNegative ? puts : -puts;
	printf("변환 후 : %d", puts);
}