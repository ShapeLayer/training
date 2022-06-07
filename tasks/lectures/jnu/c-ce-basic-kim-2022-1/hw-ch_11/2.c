#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NAME_LIM 100

// CLASS 구조체 선언 후 Class 타입으로 선언
typedef struct CLASS {
  char name[NAME_LIM];
  double grade;
} Class;

int main() {
  Class classes[3] = { {"이산수학", 3.5}, {"C프로그래밍기초및실습", 4.5}, {"논리회로설계", 2.5} };
  Class* classesp[3] = { classes, classes+1, classes+2 };
  for (int i = 0; i < 3; i++) {
    printf("과목 이름 : %-20s \t%s 학점 : %.1lf %s \n", classesp[i] -> name, strlen(classesp[i] -> name) < 20 ? "\t" : "", classesp[i] -> grade, classesp[i] -> grade > 2.5 ? "" : "-> 재수강");
  }
  return 0;
}