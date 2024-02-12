#include "bits/stdc++.h"
using namespace std;

int main() {
  int n;
  cin >> n;
  int count = 0, tmp = 1;
  while (true) {
    if (n < 10) break;
    tmp = 1;
    while (n) {
      tmp *= n % 10;
      n /= 10;
    }
    count++;
    n = tmp;
  }
  cout << count << endl;
  return 0;
}
