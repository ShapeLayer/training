#include <iostream>
using namespace std;

int main(void) {
  int n; long long int c = 0, w;
  cin >> n >> w;
  int arr[n];
  for (int i = 0; i < n; i++) cin >> arr[i];
  for (int i = 0; i < n; i++) {
    if (i < n-1) {
      if (arr[i] < arr[i+1]) {
        c += w / arr[i];
        w %= arr[i];
      } else if (arr[i] > arr[i+1]) {
        w += arr[i] * c;
        c = 0;
      }
    } else { // i == n-1
      w += arr[i] * c;
    }
  }
  cout << w << endl;
  return 0;
}