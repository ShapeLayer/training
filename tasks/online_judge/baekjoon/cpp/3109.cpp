#include "bits/stdc++.h"
using namespace std;

int r, c;
string gets;
vector<vector<char>> v;
vector<vector<bool>> visited;
int counts;
int dt[][2] = {{-1, 1}, {0, 1}, {1, 1}};

inline bool visit(int y, int x) {
  if (x == c - 1) {
    counts++;
    return true;
  }
  for (auto each : dt) {
    int dy = each[0], dx = each[1];
    int ny = y + dy, nx = x + dx;
    if (ny < 0 || ny >= r) { continue; }
    if (v[ny][nx] == 'x') { continue; }
    if (visited[ny][nx]) { continue; }
    visited[ny][nx] = visit(ny, nx);
    if (visited[ny][nx]) {
      return true;
    }
  }
  return false;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  cin >> r >> c;
  for (int i = 0; i < r; i++) {
    cin >> gets;
    vector<char> _new;
    v.push_back(_new);
    visited.push_back(*new vector<bool>(c));
    for (int j = 0; j < c; j++) {
      v[i].push_back(gets[j]);
      visited[i][j] = false;
    }
  }

  for (int i = 0; i < r; i++) {
    visited[i][0] = true;
    visit(i, 0);
  }
  
  cout << counts << '\n';

  return 0;
}
