// Not Done
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void) {
  int n, m;
  cin >> n >> m;
  int c[n];
  string s[n][m];
  while (true) {
    int cls;
    string name;
    cin >> cls >> name;
    cls--;
    cout << cls << endl;
    if (cls == -1) break;
    if (c[cls] < m) {
      s[cls][c[cls]] = name;
      c[cls]++;
    }
  }
  for (int i = 0; i < n; i += 2) {
    sort(s[i], s[i]+1);
    for (int j = 0; j < 2; j++) if (s[i][j] != "") cout << i+1 << ' ' << s[i][j] << endl;
  }
  for (int i = 1; i < n; i += 2) {
    sort(s[i], s[i]+1);
    for (int j = 0; j < 2; j++) if (s[i][j] != "") cout << i+1 << ' ' << s[i][j] << endl;
  }
  return 0;
}