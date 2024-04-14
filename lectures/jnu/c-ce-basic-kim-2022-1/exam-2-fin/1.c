#include <stdio.h>
#define MAX_SIZE 3
#define STR_SIZE 20

typedef struct book {
	char name[STR_SIZE], author[STR_SIZE], publisher[STR_SIZE];
} Book;

int main(void) {
	Book myBook[MAX_SIZE] = {
		{"어린왕자", "생텍쥐페리", "출판사A"},
		{"모비딕", "허먼 멜빌", "출판사B"},
		{"리어왕", "셰익스피어", "출판사C"}
	};

	printf("%20s %20s %20s\n", "책 이름", "저자", "출판사");
	for (int i = 0; i < MAX_SIZE * STR_SIZE + 3; i++) printf("=");
	printf("\n");
	for (int i = 0; i < MAX_SIZE; i++) {
		printf("%20s %20s %20s\n", myBook[i].name, myBook[i].author, myBook[i].publisher);
	}
	return 0;
}