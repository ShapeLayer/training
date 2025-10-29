#include "bits/stdc++.h"
using namespace std;

#define PR_FB(i) if (i % 3 == 0 && i % 5 == 0) cout << "FizzBuzz" << endl; \
                 else if (i % 3 == 0) cout << "Fizz" << endl; \
                 else if (i % 5 == 0) cout << "Buzz" << endl; \
                 else cout << i << endl; 

void print_fizzbuzz(int max = 30) {
  // verified:
  // FizzBuzz는 Fizz / Buzz와 연달아 등장할 수 없음
  for (int i = 0; i < max + 1; i++) {
    PR_FB(i);
  }
}

int main() {
  string _gets[3];
  int result;
  for (int i = 0; i < 3; i++) {
    cin >> _gets[i];
    if ('0' <= _gets[i][0] && _gets[i][0] <= '9') {
      result = stoi(_gets[i]) + 3 - i;
    }
  }
  PR_FB(result);
  return 0;
}
