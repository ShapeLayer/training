#include <stdio.h>
#define LIMIT (int)2e8

int prime_table[LIMIT + 1];

int isPrime(int n) {
	// 에라토스테네스의 체로 C언어 상에서 소수 판별이 불가능한 범위의 수를 입력했을 때
	// 잘못된 메모리 참조가 발생하지 않도록 처리
	if (n > LIMIT) return 0;
	return prime_table[n];
}

int main() {
	// 에라토스테네스의 체
	// LIMIT은 C언어 메모리 한계까지 설정 가능 (=소수 판별은 LIMIT까지 유효함).
	for (int i = 0; i <= LIMIT; i++) prime_table[i] = 1;
	prime_table[0] = 0; prime_table[1] = 0;
	for (int i = 2; i <= LIMIT; i++) {
		if (prime_table[i]) {
			for (int j = 2 * i; j <= LIMIT; j += j) {
				prime_table[j] = 0;
			}
		}
	}

	int gets, proc = 1;
	do {
		printf("숫자를 입력하세요 : ");
		scanf("%d", &gets);
		int res = isPrime(gets);
		if (res) {
			if (res == 1)
				printf("%d은(는) 소수입니다.\n", gets);
			// else
			// 	printf("판별 불가\n");
		} else {
			printf("%d은(는) 소수가 아닙니다.\n", gets);
		}
		int ans_loop = 1;
		while (ans_loop) {
			char nl, gets_cont;
			printf("계속하시겠습니까?(Y/N) : ");
			// '\n'이 입력 버퍼에 잔존하여 "계속하시겠습니까?"가 2회 발생하는 문제 확인
			// 해결을 위해 char형 데이터를 2회 받아오는 것으로 하고 첫번째 char 데이터를 버림
			scanf("%c%c", &nl, &gets_cont);
			if (gets_cont == 'Y' || gets_cont == 'y') ans_loop = 0;
			else if (gets_cont == 'N' || gets_cont == 'n') { ans_loop = 0; proc = 0; }
			else printf("잘못입력하셨습니다.\n");
		}
	} while (proc);
	return 0;
}