#include <bits/stdc++.h>
#define MAX (int)1e9
using namespace std;

int n, m;
vector<pair<int, int>> houses, chickens;
vector<int> selected;
int len_houses, len_chickens;
int min_town_diff = MAX;

int compute() {
  int town_diff = 0;
  for (auto house: houses) {
    int hi = house.first, hj = house.second;
    int min_diff = MAX;
    for (auto each: selected) {
      pair<int, int> chicken = chickens[each];
      int ci = chicken.first, cj = chicken.second;
      min_diff = min(min_diff, abs(hi - ci) + abs(hj - cj));
    }
    town_diff += min_diff;
  }
  min_town_diff = min(min_town_diff, town_diff);
  return 0;
}

int step(int invoke, int counted) {
  if (counted == m) {
    compute();
  }
  for (int i = invoke + 1; i < len_chickens; i++) {
    selected.push_back(i);
    step(i, counted + 1);
    selected.pop_back();
  }
  return 0;
}

int main() {
  cin >> n >> m;
  int gets;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> gets;
      if (gets != 0) {
        pair<int, int> now = make_pair(i, j);
        if (gets == 1) houses.push_back(now);
        else if (gets == 2) chickens.push_back(now);
      }
    }
  }
  len_houses = houses.size(), len_chickens = chickens.size();
  step(-1, 0);
  cout << min_town_diff << endl;
  return 0;
}
