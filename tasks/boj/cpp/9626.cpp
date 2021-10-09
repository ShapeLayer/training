#include <iostream>
using namespace std;
int before_line = 0, before_column = 0;
void step_column(void) { before_column = (before_column ? 0 : 1); }
void step_line(void) { before_line = (before_line ? 0 : 1); before_column = before_line; }
int main(void) {
  int m, n, u, l, r, d;
  cin >> m >> n >> u >> l >> r >> d;
  char puzzle[m][n];
  for (int i = 0; i < m; i++) cin >> puzzle[i];
  for (int y = 0; y < u; y++) {
    for (int x = 0; x < l+n+r; x++) {
      cout << (before_column ? "." : "#");
      step_column();
    }
    step_line();
    cout << endl;
  }
  for (int y = 0; y < m; y++) {
    for (int x = 0; x < l; x++) {
      cout << (before_column ? "." : "#");
      step_column();
    }
    for (int x = 0; x < n; x++) {
      cout << puzzle[y][x];
      step_column();
    }
    for (int x = 0; x < r; x++) {
      cout << (before_column ? "." : "#");
      step_column();
    }
    step_line();
    cout << endl;
  }
  for (int y = 0; y < d; y++) {
    for (int x = 0; x < l+n+r; x++) {
      cout << (before_column ? "." : "#");
      step_column();
    }
    step_line();
    cout << endl;
  }
  return 0;
}