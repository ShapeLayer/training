#include <stdio.h>

int main() {
  int score = 95;

  printf("90점 이상 100점 이하인가? : %d\n",
    score >= 90 && score <= 100);
  
  printf("0점 또는 100점인가? : %d\n",
    score == 0 || score == 100);
  
  printf("0점인가? : %d\n", !score);

  return 0;
}