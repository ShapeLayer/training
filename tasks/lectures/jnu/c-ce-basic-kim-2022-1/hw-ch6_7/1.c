#include <stdio.h>

double getArithMean(double a, double b) {
  return (a+b)/2;
}
double getHarmonicMean(double a, double b) {
  return (2*a*b)/(a+b);
}

int main() {
  double a, b;
  printf("평균을 낼 실수를 입력하세요 : ");
  scanf("%lf %lf", &a, &b);
  double am = getArithMean(a, b), hm = getHarmonicMean(a, b);
  printf("산술평균 : %f\n", am);
  printf("조화평균 : %f\n", hm);
  printf("이 둘 중 더 큰 값은 %f입니다.\n", am > hm ? am : hm);
  return 0;
}

