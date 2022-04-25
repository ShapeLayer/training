// 이중 포인터: 포인터 변수의 주소를 가리키는 포인터
#include <stdio.h>

int main(void) {
  int x;
  int* p = &x;
  int** pp = &p;
  int* pp_ = &p; // 가능은 하나 권장되지 않음 (imcompatible pointer types)

  /*
    p => x의 주소값
    pp => p의 주소값
    *p => x의 값
    *pp => p의 값 => x의 주소값
    **pp => x의 값
    *가 앞에 붙으면 그 값이 가리키는 주소로 가라는 의미
    
    &x => x의 주소값 (= p)
    &p => p의 주소값 (= pp)
    &pp => pp의 주소값
  */

  printf("%p %p %p\n", p, pp, pp_);

  return 0;
}