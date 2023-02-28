#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Pos {
public:
  int x;
  int y;
  Pos() {}
  Pos(int x, int y): x(x), y(y) {}
  friend bool operator==(Pos const &a, Pos const &b);
  friend bool operator!=(Pos const &a, Pos const &b);
  friend bool operator>(Pos const &a, Pos const &b);
  friend bool operator>=(Pos const &a, Pos const &b);
  friend bool operator<(Pos const &a, Pos const &b);
  friend bool operator<=(Pos const &a, Pos const &b);
};
bool operator== (Pos const &a, Pos const &b) { return a.x == b.x and a.y == b.y; }
bool operator!= (Pos const &a, Pos const &b) { return a.x != b.x or a.y != b.y; }
bool operator>  (Pos const &a, Pos const &b) { return a.y > b.y or (a.y == b.y and a.x > b.x); }
bool operator>= (Pos const &a, Pos const &b) { return a == b or a > b; }
bool operator<  (Pos const &a, Pos const &b) { return a.y < b.y or (a.y == b.y and a.x < b.x); }
bool operator<= (Pos const &a, Pos const &b) { return a == b or a < b; }


int main(void) {
  int n, x, y;
  cin >> n;
  vector<Pos> pos;
  for (int i = 0; i < n; i++) {
    cin >> x >> y;
    pos.push_back(Pos {x, y});
  }
  sort(pos.begin(), pos.end());
  for (int i = 0; i < n; i++) {
    cout << pos[i].x << ' ' << pos[i].y << '\n';
  }
  return 0;
}