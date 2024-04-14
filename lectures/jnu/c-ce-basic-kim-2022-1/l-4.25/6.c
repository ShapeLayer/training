// 포인터 배열
// -> 배열과 포인터

#include <stdio.h>

int main() {
  int arr[5] = {10, 20, 30, 40, 50};

  for (int i = 0; i < 5; i++) {
    printf("&arr[%d] = %p,\t", i, &arr[i]);
    printf("arr+%d = %p\n", i, arr + i);
  }

  for (int i = 0; i < 5; i++) {
    // 왼쪽과 오른쪽의 문법이 같음: 배열은 포인터로 관리되므로
    printf("arr[%d] = %p,\t", i, arr[i]);
    printf("*(arr+%d) = %p\n", i, *(arr + i));
    // *(arr+4) = arr[4]
  }

  // 포인터를 사용하면 변수의 스코프를 무시할 수 있음
  // => 간편하나 위험
  return 0;
}