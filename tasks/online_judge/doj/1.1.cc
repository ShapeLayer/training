#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  cin >> N;

  vector<int> st;
  st.reserve(N);
  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    if (!st.empty() && st.back() != a) st.pop_back();
    else st.push_back(a);
  }

  cout << (st.empty() || (st.back() == 1 && st.size() % 3 == 0) ? "Yes" : "No") << '\n';
}
