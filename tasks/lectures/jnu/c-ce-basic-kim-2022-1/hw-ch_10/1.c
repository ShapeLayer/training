#include <stdio.h>

typedef struct vector VECTOR;
void PrintVector(const VECTOR* v);
void SumVector(VECTOR* res, VECTOR a, VECTOR b);

typedef struct vector {
  int x;
  int y;
  int z;
} VECTOR;

int main() {
  VECTOR vec1 = { 1,3,5 };
  VECTOR vec2 = { 5,1,2 };
  VECTOR vec3;

  printf("vec1 = ");
  PrintVector(&vec1);

  printf("vec2 = ");
  PrintVector(&vec2);

  SumVector(&vec3, vec1, vec2);

  printf("결과 = ");
  PrintVector(&vec3);

  return 0;
}

void PrintVector(const VECTOR* v) {
  printf("(%d, %d, %d)\n", v -> x, v -> y, v -> z);
}

void SumVector(VECTOR* res, VECTOR a, VECTOR b) {
  res -> x = a.x + b.x;
  res -> y = a.y + b.y;
  res -> z = a.z + b.z;
}
