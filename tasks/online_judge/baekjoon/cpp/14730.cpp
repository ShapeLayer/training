#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int result = 0;
  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    result += a * b;
  }
  cout << result;
  return 0;
}