#include <stdio.h>

/*
  함수도 주소로 저장할 수 있다

  [선언]
  리턴형 (*포인터명)(매개변수) = (함수원형의 주소)
  int (*pFunc)(int n) = &GetFactorial;

*/

/*
  typedef 리턴형 (*포인터형명)(매개변수)
  typedef int (*FP)(double, double);

  FP pFunc = Add;
  FP pFunc2 = Minus;
*/

int GetFactorial(int n);
double Add(double x, double y);

int main() {
  int (*pFunc)(int n) = &GetFactorial;
  double (*pf)(double, double) = Add; // &를 빼도 정상 작동하긴 함
  int num;

  printf("점수를 입력하세요 : ");
  scanf("%d", &num);
  printf("%d! = %d\n", num, (*pFunc)(num));

  printf("0.5 + 1.3 = %f\n", pf(0.5, 1.3));
}

int GetFactorial(int n) {
  int fact = 1;
  for (int i = 1; i <= n; i++)
    fact *= i;
  return fact;
}

double Add(double a, double b) {
  return a + b;
}