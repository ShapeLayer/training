#include <stdio.h>

int main() {
  int score = 95;

  // 논리 연산과 관계 연산 중 관계 연산 먼저 처리
  score < 0 || score >= 90 && score <= 100;
  0 || 1 && 1;
  // 논리 연산은 뒤에서부터 처리함
  0 || 1;

  return 0;
}