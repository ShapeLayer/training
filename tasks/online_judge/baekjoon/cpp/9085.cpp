#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int m, s = 0;
    cin >> m;
    for (int j = 0; j < m; j++) {
      int k = 0;
      cin >> k;
      s += k;
    }
    cout << s << endl;
  }
  return 0;
}