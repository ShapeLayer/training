// 틀렸습니다
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
  long long n, b, c, inspector;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  cin >> b >> c;
  for (int i = 0; i < n; i++) {
    int leave = a[i] - b;
    inspector++;
    if (leave > 0) {
      inspector += ((leave % c == 0) ? leave/c : leave/c+1);
    }
  }
  cout << inspector << endl;
  return 0;
}