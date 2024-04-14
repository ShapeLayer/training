#include <stdio.h>

int main(void) {
	int numArr1[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
	int numArr2[3][3] = { {0, 1, 0}, {1, 3, 5}, {2, 4, 6} };
	int numArrRes[3][3] = { 0 };
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			for (int k = 0; k < 3; k++) {
				numArrRes[i][j] += numArr1[i][k] * numArr2[k][j];
			}
		}
	}
	printf("결과값 :\n");
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			printf("%d ", numArrRes[i][j]);
		}
		printf("\n");
	}
	return 0;
}