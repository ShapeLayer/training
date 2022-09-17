#include <stdio.h>
#include <string.h>

int main() {
  FILE *fp = NULL;

  fp = fopen("gets.in", "r");
  if (fp == NULL) {
    printf("파일 읽기 실패\n");
  }

  /*
  char ch = fgetc(fp);
  while (ch != EOF) {
    printf("%c ", ch);
    ch = fgetc(fp);
  }
  */

  int arr[6];
  for (int i = 0; i < 6; i++) {
    fscanf(fp, "%d", arr+i);
    printf("%d\n", arr[i]);
  }
  return 0;
}