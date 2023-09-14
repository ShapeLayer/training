#include <bits/stdc++.h>
using namespace std;

int n, vals[3][3];

bool dfs(int y, int x) {
  if (vals[y][x] == -1)
    return true;
  else if (vals[y][x] == 0)
    return false;

  bool result = false;
  int ny = y + vals[y][x], nx = x + vals[y][x];
  if (0 <= ny && ny < n)
    result |= dfs(ny, x);
  if (0 <= nx && nx < n)
    result |= dfs(y, nx);
  return result;
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      cin >> vals[i][j];
  cout << (dfs(0, 0) ? "HaruHaru" : "Hing") << endl;
  return 0;
}
