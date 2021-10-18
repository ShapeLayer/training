// 틀렸습니다
#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int arr[n];
  bool trg = false;
  for (int i = 0; i < n; i++) cin >> arr[i];
  for (int i = 0; i < n; i++) {
    int cnt = 0;
    for (int j = 0; j < n; j++) {
      if (arr[j] >= arr[i]) cnt++;
    }
    if (arr[i] == cnt && !trg) {
      trg = true;
      cout << cnt << endl;
    }
  }
  if (!trg) cout << 0 << endl;
  return 0;
}