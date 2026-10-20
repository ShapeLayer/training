#include "bits/stdc++.h"
using namespace std;

int main() {
  map<string, int> tree;
  string __get;
  long long int total = 0;
  while (getline(cin, __get)) {
    if (!__get.empty() && __get.back() == '\r')
      __get.pop_back();
    if (tree.find(__get) == tree.end()) {
      tree[__get] = 1;
    } else {
      tree[__get]++;
    }
    total++;
  }

  vector<pair<string, long long int>> results;
  for (auto i = tree.begin(); i != tree.end(); i++) {
    auto name = i->first;
    auto cnt = i->second;

    long long int now = cnt * 10'000'000 / total;
    now = (now / 10) + ((now % 10) >= 5 ? 1 : 0);
    results.push_back(make_pair(name, now));
  }

  sort(results.begin(), results.end());

  for (int i = 0; i < results.size(); i++) {
    int remains = results[i].second % 10'000;
    cout << results[i].first << ' ' << (results[i].second / 10'000) << '.'
      << (remains < 1000 ? "0" : "") 
      << (remains < 100 ? "0" : "") 
      << (remains < 10 ? "0" : "")
      << remains << endl;
  }

  return 0;
}
