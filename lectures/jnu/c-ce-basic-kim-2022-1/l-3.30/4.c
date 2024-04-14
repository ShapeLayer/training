#include <stdio.h>

void printh();

int main() {
  printh();
  return 0;
}

void printh() {
  printf("PRINTH\n");
}

// ln3 없다면 오류: 위에서부터 아래로 읽어내려가므로 선언이 먼저 되야함
// 해결 방법: 함수를 먼저 위에서 선언해서 사용할 수 있음
