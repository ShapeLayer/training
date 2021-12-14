#include <iostream>
#include <vector>
using namespace std;

int main(void) {
  vector<int> t;
  t.push_back(1);
  for (int i = 2; t.back() < 1001; i++) t.push_back(t.back()+i);
  int n;
  cin >> n;
  for (int _ = 0; _ < n; _++) {
    int puts, limit = 0, is_t = 0;
    cin >> puts;
    for (int i = 0; t[i] < puts; i++) limit = i;
    for (int i = 0; i <= limit; i++) for (int j = 0; j <= limit; j++) for (int k = 0; k <= limit; k++) if (t[i]+t[j]+t[k] == puts) { is_t = 1; break; }
    cout << is_t << endl;
  }
  return 0;
}