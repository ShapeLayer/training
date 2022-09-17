#include <stdio.h>
#include <math.h>
#include <time.h>
#define ABS(N) N >= 0 ? N : -N

int exec_select_menu();
void exec_get_sqrt();
void exec_get_abs();
void exec_print_now();

int main() {
  while (1) {
    switch (exec_select_menu()) {
      case 0:
        return 0;
      case 1:
        exec_get_sqrt();
        break;
      case 2:
        exec_get_abs();
        break;
      case 3:
        exec_print_now();
        break;
      default:
        printf("잘못된 입력입니다.\n");
        break;
    }
    printf("\n");
  }

  return 0;
}

int exec_select_menu() {
  printf("1. 제곱근 구하기\n");
  printf("2. 절대값 구하기\n");
  printf("3. 현재시각 출력\n");
  printf("0. 종료\n");
  printf(">>> 선택 : ");
  int gets;
  scanf("%d", &gets);
  return gets;
}

void exec_get_sqrt() {
  printf("정수를 입력하세요 : ");
  int gets;
  scanf("%d", &gets);
  printf("제곱근값 : %.4f\n", sqrt((double)gets));
}

void exec_get_abs() {
  printf("절대값을 씌울 수를 입력하세요 : ");
  double gets;
  scanf("%lf", &gets);
  printf("%lf의 절대값은 %lf입니다.\n", gets, ABS(gets));
}

void exec_print_now() {
  time_t rawtime;
  time(&rawtime);
  struct tm* now = localtime(&rawtime);
  printf("현재 : %d년 %d월 %d일 %d시 %d분 %d초\n", 
    (now->tm_year + 1900), (now->tm_mon + 1), now->tm_mday, now->tm_hour, now->tm_min, now->tm_sec
  );
}
