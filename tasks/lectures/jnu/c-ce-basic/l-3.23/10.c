#include <stdio.h>

int main() {
  int score;

  printf("정수를 입력하세요 : ");
  scanf("%d", &score);

  /* === */
  if (score < 60)
    printf("%d점은 불합격입니다.\n", score);
  else
    printf("%d점은 합격입니다.\n", score);

  /* === */
  score < 60 ? printf("%d점은 불합격입니다.\n", score) : printf("%d점은 합격입니다.\n", score);

  /* === */
  if (score < 60)
    printf("%d점은 불합격입니다.\n", score);
    // score < 60
  else if (score < 80)
    printf("%d점은 재응시입니다.\n", score);
    // !(score < 60) && score < 80
    // (score >= 60) && (score < 80)
  else
    printf("%d점은 합격입니다.\n", score);
    // !(score < 60) && !(score < 80)

  return 0;
}