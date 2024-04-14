#include <stdio.h>
#include <stdlib.h>
#include "myMath.h"
#define swap(a, b) int c = a; a = b; b = c

double (*pAdd)(double a, double b) = &add;
double (*pSub)(double a, double b) = &sub;
double (*pMul)(double a, double b) = &mul;
double (*pDivs)(double a, double b) = &divs;
double (*pSpr)(double a, double b) = &spr;
double (*pGcd)(double a, double b) = &gcd;

int main(void) {
	printf("덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/), 거듭제곱(^), 최대공약수(%%)\n");
	printf("0 0 0 입력 시 종료\n");
	double a = -1, b = -1;
	char o = '\0';
	FILE* fp = fopen("log.txt", "w");
	int cnt = 0;
	while (a != 0 && b != 0 && o != '0') {
		printf("\n");
		scanf("%lf %c %lf", &a, &o, &b);
		if (a < 0 || b < 0) {
			printf("형식이 다릅니다.\n");
			fprintf(fp, "%02d번째 : %g %c %g = 형식 오류\n", cnt++, a, o, b);
			continue;
		}
		if (a == 0 && b == 0 && o == '0') break;
		double res = -2e10;
		int isWrong = 0;
		switch (o)
		{
			case '+':
				res = (pAdd)(a, b);
				break;
			case '-':
				res = (pSub)(a, b);
				break;
			case '*':
				res = (pMul)(a, b);
				break;
			case '/':
				res = (pDivs)(a, b);
				break;
			case '^':
				res = (pSpr)(a, b);
				break;
			case '%':
				res = (pGcd)(a, b);
				break;
			default:
				printf("잘못 입력하셨습니다.\n");
				isWrong = 1;
				break;
		}
		if (!isWrong)
		{
			printf("결과: %.6f\n", res);
			fprintf(fp, "%02d번째 : %g %c %g = %g\n", cnt++, a, o, b, res);
		}
		else
		{
			fprintf(fp, "%02d번째 : %g %c %g = 연산자 오류\n", cnt++, a, o, b);
		}
	}
	fclose(fp);
	return 0;
}
