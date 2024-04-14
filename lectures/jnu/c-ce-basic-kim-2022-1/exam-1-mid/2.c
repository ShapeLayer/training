#include <stdio.h>

int main() {
	char gets;
	char range[][2][5] = { { "4.0", "4.5" },{ "3.0", "4.0" },{ "2.0", "3.0" },{ "55dB", "70dB" },{ "70dB", "90dB" } };
	printf("평균학점을 입력하세요 : ");
	scanf("%c", &gets);
	switch (gets) {
	case 'A':
		printf("학점 범위는 %s ~ %s입니다.\n", range[0][0], range[0][1]);
		break;
	case 'B':
		printf("학점 범위는 %s ~ %s입니다.\n", range[1][0], range[1][1]);
		break;
	case 'C':
		printf("학점 범위는 %s ~ %s입니다.\n", range[2][0], range[2][1]);
		break;
	// 학점이 D와 F인 경우 난청 강도를 출력하도록 되어있으나,
	// 출력 예시는 A와 B인 경우만 제시되어 있으므로 일단 아래와 같이 출력하도록 함
	case 'D':
		// printf("난청 강도는 %s ~ %s입니다.\n", range[4][0], range[4][1]);
		printf("학점 범위는 %s ~ %s입니다.\n", range[3][0], range[3][1]);
		break;
	case 'F':
		// printf("난청 강도는 %s ~ %s입니다.\n", range[4][0], range[4][1]);
		printf("학점 범위는 %s ~ %s입니다.\n", range[4][0], range[4][1]);
		break;
	}
	return 0;
}