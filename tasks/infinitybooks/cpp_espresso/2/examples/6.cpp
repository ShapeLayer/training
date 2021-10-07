#include <iostream>
using namespace std;

int square(int n = 0) { return n*n; }
double square(double n = 0) { return n*n; }

int main(void) {
  int n; double m;
  cin >> n >> m;
  cout << square(n) << ' ' << square(m) << endl;
  return 0;
}
