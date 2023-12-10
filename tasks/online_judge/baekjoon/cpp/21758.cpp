#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n;
  cin >> n;
  int honey[n];
  for (int i = 0; i < n; i++) cin >> honey[i];
  for (int i = 1; i < n; i++) honey[i] += honey[i - 1];

  int _max = -1;
  for (int i = 2; i < n; i++) _max = max(_max, (honey[i - 1] - honey[0]) + (honey[n - 2] - honey[i - 2]));
  for (int i = 2; i < n; i++) _max = max(_max, (honey[n - 1] - honey[0] - (honey[i - 1] - honey[i - 2])) + (honey[n - 1] - honey[i - 1]));
  for (int i = 2; i < n; i++) _max = max(_max, (honey[n - 2] - (honey[i - 1] - honey[i - 2])) + honey[i - 2]);
  
  cout << _max << endl;
  return 0;
}
