// 배열과 포인터의 차이점

int main() {
  int x[5], y[5];
  int* p = x;

  // 배열 간 대입 연산 안됨
  // x = y;
  // x++;

  // 하지만 포인터라면?
  // p = y;
  // p++;

  return 0;
}