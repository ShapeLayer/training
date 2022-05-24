#include <stdio.h>

int main() {
  int x[3] = { 1, 2, 3 };
  int y[3] = { 4, 5, 6 };
  int z[3] = { 7, 8, 9 };
  int* arr[3] = { x, y, z };
  // arr[0] => x 배열 (=x의 0번째 주소값)
  // arr[1] => y 배열 (=y의 0번째 주소값)
  // arr[2] => z 배열 (=z의 0번째 주소값)

  // arr[0] + 1 => x의 1번째 원소의 주소
  // *(arr[0]+1) => x의 1번째 원소의 주소가 가리키는 변수값
  //             = x의 1번째 원소값
  // arr[0][1]
  
  int i, j;

  for (i = 0; i < 3; i++) {
    for (j = 0; j < 3; j++) {
      printf("%d ", arr[i][j]);
    }
    printf("\n");
  }
}