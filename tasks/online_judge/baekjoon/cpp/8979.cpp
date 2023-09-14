#include <bits/stdc++.h>
using namespace std;

class Nation {
  public:
    int id;
    int gold;
    int silver;
    int bronze;
    Nation(int id, int gold, int silver, int bronze): id(id), gold(gold), silver(silver), bronze(bronze) {}

    bool operator==(Nation other) const {
      return this->gold == other.gold && this->silver == other.silver && this->bronze == other.bronze;
    }
};

bool compare(Nation a, Nation b) {
  if (a.gold != b.gold) return a.gold < b.gold;
  if (a.silver != b.silver) return a.silver < b.silver;
  return a.bronze > b.bronze;
}

int main() {
  int n, k;
  cin >> n >> k;
  vector<Nation> gets;
  for (int i = 0; i < n; i++) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    gets.push_back(Nation(a, b, c, d));
  }
  sort(gets.begin(), gets.end(), compare);
  int offset = 0;
  for (int i = 0; i < n; i++) {
    if (gets[i].id == k) {
      cout << i - offset << endl;
      break;
    }
    if (i != 0) {
      if (gets[i - 1] == gets[i]) {
        offset++;
      }
    } else {
      offset = 0;
    }
  }
  return 0;
}
