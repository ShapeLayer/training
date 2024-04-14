#include <stdio.h>
#include <string.h>
#define STRING_SIZE 10
#define ARRAY_SIZE 5
#define swap(a,b) {int t; t=a; a=b; b=t;}

int main() {
  char gets[ARRAY_SIZE][STRING_SIZE];
  char tmp[STRING_SIZE];
  printf("단어들을 입력해주세요 : ");
  for (int i = 0; i < ARRAY_SIZE; i++) scanf("%s", &gets[i]);
  for (int i = 0; i < ARRAY_SIZE; i++) {
    for (int j = 0; j < ARRAY_SIZE; j++) {
      if (strcmp(gets[j], gets[j+1]) > 0) {
        strcpy(tmp, gets[j]);
        strcpy(gets[j], gets[j+1]);
        strcpy(gets[j+1], tmp);
      }
    }
  }
  for (int i = 0; i < ARRAY_SIZE; i++) {
    printf("%s\n", gets[i]);
  }
}