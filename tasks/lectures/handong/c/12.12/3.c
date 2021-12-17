#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void display(int array[], int n) {
  for (int i = 1; i <= n; i++) {
    printf("%3d", array[i-1]);
    if (i % 10 == 0) printf("\n");
  }
}
void frequency(int freq[]) {
  for (int i = 0; i < 11; i++) printf("%02d:%3d   ", i, freq[i]);
}
void std_dev(int freq[], int n) {
  int sum = 0; float e = 0, v = 0;
  for (int i = 0; i < 11; i++) sum += (freq[i] * i);
  e = sum / n;
  for (int i = 0; i < 11; i++) v += pow(e - freq[i], 2) * freq[i];
  v /= (n - 1);
  printf("Standard deviation: %f\n", pow(v, .5));
}
void find(int array[], int n) {
  int target;
  printf("input find number: ");
  scanf("%d", &target);
  for (int i = 0; i < n; i++) {
    if (array[i] == target) printf("data[%d] ", i);
  }
  printf("\n");
}
void mode(int freq[]) {
  int max = 0, idx = 0;
  for (int i = 0; i < 11; i++) {
    if (max < freq[i]) {
      max = freq[i];
      idx = i;
    }
  }
  printf("Mode: %d, %d번 생성됨", idx, max);
}
int main(void) {
  int size;
  printf("input number of data: ");
  scanf("%d", &size);
  int array[size];
  srand(size);
  for (int i = 0; i < size; i++) array[i] = rand() % 11;
  int freq[11];
  for (int i = 0; i < 11; i++) freq[i] = 0;
  for (int i = 0; i < size; i++) freq[array[i]]++;

  int select = 0;
  while (select != 6) {
    printf("********************************************\n");
    printf("** (1) 생성된 데이터의 내용 출력(display)   **\n");
    printf("** (2) 각 숫자의 빈도수(frequency)를 출력   **\n");
    printf("** (3) 입력된 data의 표준편차 출력          **\n");
    printf("** (4) 입력 숫자를 DATA array에서 찾기      **\n");
    printf("** (5) 최빈수(mode) 찾기                   **\n");
    printf("** (6) 종료                               **\n");
    printf("********************************************\n");
    printf("input menu: ");
    scanf("%d", &select);
    printf("\n");
    if (select == 1) display(array, size);
    else if (select == 2) frequency(freq);
    else if (select == 3) std_dev(freq, size);
    else if (select == 4) find(array, size);
    else if (select == 5) mode(freq);
    else if (select != 6) printf("\n");
  }
  printf("Good Bye\n");
  return 0;
}