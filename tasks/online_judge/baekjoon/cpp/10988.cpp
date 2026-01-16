#include <iostream>
#include <string>
using namespace std;

int main() {
  string s;
  cin >> s;
  int n = s.length();

  bool is_pal = true;
  for (int i = 0; i < n / 2; ++i) {
    is_pal &= (s[i] == s[n - 1 - i]);
  }
  cout << (int)is_pal << endl;

  return 0;
}
