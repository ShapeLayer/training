/*
  P.150, Chapter 13.
*/

/* Lab13.c */
#include <stdio.h>
#include <ctype.h>

int main(int argc, char* argv[]) {
  FILE *fp1, *fp2;
  char buff[256];
  int i;

  if (argc < 3) {
    printf("Usage: Convert src_file dest_file\n");
    return -1;
  }

  fp1 = ; // 입력용 파일 열기
  if (fp1 == NULL) {
    printf("%s 파일 열기 실패\n", argv[1]);
    return -1;
  }

  fp2 = // 출력용 파일 열기
  if (fp2 == NULL) {
    printf("%s 파일 열기 실패\n", argv[2]);
    return -1;
  }
  while () { // fp1이 가리키는 파일의 끝이 아닌 동안
    // 입력용 파일에서 한 줄의 문자열 읽기
  }
}