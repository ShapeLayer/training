#include <bits/stdc++.h>
#define i64 long long
using namespace std;

int n, s, gets[20], result_counts = 0;
bool visits[20];

int step(int invoke, i64 sums, int counts) {
  if (sums == s) {
    if (invoke != -1)
      result_counts += 1;
  }

  if (counts == n) {
    return 0;
  }

  for (int i = invoke + 1; i < n; i++) {
    step(i, sums + gets[i], counts += 1);
  }
  return 0;
}

int main() {
  cin >> n >> s;
  for (int i = 0; i < n; i++) {
    cin >> gets[i];
  }
  step(-1, 0, 0);
  cout << result_counts << endl;
}
