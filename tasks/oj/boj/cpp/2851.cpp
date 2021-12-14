#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
  int c = 0;
  vector<int> possible;
  while (true) {
    if (cin.eof() == true) break;
    int i = 0;
    cin >> i;
    c += i;
    possible.push_back(c);
  }
  int max = possible[0];
  for (int i = 1; i < possible.size(); i++) {
    if (abs(max - 100) >= abs(possible[i] - 100) && possible[i] > max) max = possible[i];
  }
  cout << max << endl;
  return 0;
}
// (eof) Windows: Ctrl+z / Unix: Ctrl+d