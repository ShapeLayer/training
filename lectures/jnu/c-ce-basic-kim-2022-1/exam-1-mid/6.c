#include <stdio.h>
#include <string.h>

char toUpper(char c) {
	if (c >= 97 && c <= 122) c -= 32;
	return c;
}
char toLower(char c) {
	if (c >= 65 && c <= 90) c += 32;
	return c;
}

int main() {
	int upper_flag = 0, put_idx = 0;
	char get[50], put[50];
	// 알파벳 캐릭터 범위 확인
	// printf("%d %d %d %d\n", 'A', 'Z', 'a', 'z');
	printf("문장입력 : ");
	gets(get);
	for (int i = 0; i < 50; i++) {
		if (get[i] == '\0') { put[put_idx] = '\0'; break; }
		if (get[i] == ' ') { upper_flag = 1; continue; }
		put[put_idx] = upper_flag ? toUpper(get[i]) : toLower(get[i]);
		put_idx++;
		upper_flag = 0;
	}
	printf("변환 후 : %s", put);
	return 0;
}