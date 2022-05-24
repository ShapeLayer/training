/*
  P.138, Chapter 12.
*/

/* Lab12.c */
#include <stdio.h>

int main(int argc, char* argv[]) {
  int i, j;

  printf("%d\n", sizeof(argv[i])/sizeof(char));
  for (i = 1; i < argc; i++) {
    for (j = 0; j < sizeof(argv[i])/sizeof(char); j++) {
      char character = argv[i][j];
        printf("%s", argv[i][j]);
      if (character < 97 || character > 122) {
        argv[i][j] -= 32;
        printf("%s", argv[i][j]);
      }
    }
    printf("%d\n", sizeof(argv[i]));
  }

  for (i = 1; i < argc; i++)
    printf("%s ", argv[i]);
  printf("\n");

  return 0;
}