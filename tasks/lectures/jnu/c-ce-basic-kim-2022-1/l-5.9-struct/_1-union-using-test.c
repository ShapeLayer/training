#include <stdio.h>

typedef struct union_test {
  int n;
  union {
    int first;
    int second;
  } unions;
} UnionTest;

int main() {
  UnionTest unions1 = {1, -1};
  // unions를 초기화하면 unions의 멤버들이 한번에 초기화됨
  printf("unions1: n = %d, unions = %d, unions.first = %d, unions.first = %d\n", unions1.n, unions1.unions, unions1.unions.first, unions1.unions.second);

  // 아래와 같이 작성하더라도 1과 -1까지만 사용함
  // UnionTest unions2 = {1, -1, -2};
  UnionTest unions2 = {1, -1, -2, -3};
  printf("unions2: n = %d, unions = %d, unions.first = %d, unions.first = %d\n", unions2.n, unions2.unions, unions2.unions.first, unions2.unions.second);

  // 구조체는 일반 타입처럼 작동함
  // 참조형은 구조체 포인터를 사용했을 때 작동함
  printf("\n");
  UnionTest unions3 = unions2;
  unions3.unions.second = -100;
  printf("unions2: n = %d, unions = %d, unions.first = %d, unions.first = %d\n", unions2.n, unions2.unions, unions2.unions.first, unions2.unions.second);
  printf("unions3: n = %d, unions = %d, unions.first = %d, unions.first = %d\n", unions3.n, unions3.unions, unions3.unions.first, unions3.unions.second);
  return 0;
}