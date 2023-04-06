#include <iostream>

using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  int arr[n];
  int res[n];
  int res_idx = 0, cnt = 0, now = 0;
  for (int i = 0; i < n; i++) arr[i] = i+1;
  while (res_idx < n) {
    if (arr[now] != -1) cnt++;
    if (cnt % k == 0 && arr[now] != -1) {
      arr[now] = -1;
      res[res_idx++] = now+1;
    }
    now = (now + 1) % n;
  }
  cout << "<";
  for (int i = 0; i < n-1; i++) cout << res[i] << ", ";
  cout << res[n-1] << ">" << endl;
  return 0;
}
