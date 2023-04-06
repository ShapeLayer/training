#include <iostream>
using namespace std;

int main(void) {
  int n; long long int c, w;
  cin >> n >> w;
  int arr[n+1];
  for (int i = 0; i < n; i++) cin >> arr[i];
  /* for (int i = 0; i < n; i++) 일 때 틀림:
     i == n일 때, arr[i]와 0 비교.. 어차피 일 안하지 않나? */
  for (int i = 0; i < n-1; i++) {
    if (arr[i] < arr[i+1]) {
      c = w / arr[i];
      w %= arr[i];
      c *= arr[i+1]; // 이게 지뢰네
      w += c;
    }
  }
  cout << w << endl;
  return 0;
}