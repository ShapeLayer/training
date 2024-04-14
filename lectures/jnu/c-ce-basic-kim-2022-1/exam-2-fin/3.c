#include <stdio.h>
#include <string.h>
#define STR_SIZE 20

void upper(char* str) {
	for (int i = 0; i < STR_SIZE; i++) {
		if (str[i] == '\0') return;
		if (str[i] >= 97 && str[i] <= 122) {
			str[i] -= 32;
		}
	}
}

int main(void) {
	char arr[20] = "BLANK";
	char* pstr1 = "Hello World";
	char* pstr2 = arr;
	printf("%-20s : %s (%p)\n", "문자열 리터럴", "Hello World", pstr1);
	printf("%-20s : %s (%p)\n", "문자 배열(대입 전)", arr, pstr2);
	strcpy(arr, pstr1);
	printf("%-20s : %s (%p)\n", "문자 배열(대입 후)", arr, pstr2);
	upper(arr);
	printf("%-20s : %s (%p)\n", "문자 배열(변경 후)", arr, pstr2);
	return 0;
}