#include <stdio.h>
#define swap(a, b) {int tmp = a; a = b; b = tmp;}

int main() {
	int gets[10];
	printf("값 10개를 입력하세요 : ");
	for (int i = 0; i < 10; i++) scanf("%d", &gets[i]);

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (gets[i] < gets[j]) {
				swap(gets[i], gets[j]);
			}
		}
	}

	printf("정렬 결과 : ");
	for (int i = 0; i < 10; i++) printf("%d ", gets[i]);
	printf("\n");
	printf("최솟값은 %d, 최댓값은 %d 입니다.\n", gets[0], gets[9]);
	return 0;
}