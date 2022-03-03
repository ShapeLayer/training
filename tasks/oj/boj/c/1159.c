#include <stdio.h>

int main() {
  int t = 0;
  int chars[26];
  for (int i = 0; i < 26; i++) {
    chars[i] = 0;
  }
  char gets[30] = "";
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%s", gets);
    chars[((int)gets[0])-97]++;
  }
  int flag = 0;
  for (int i = 0; i < 26; i++) {
    if (chars[i] >= 5) {
      flag = 1;
      printf("%c", (char)(i+97));
    }
  }
  if (flag == 0) {
    printf("PREDAJA");
  }
  printf("\n");
}