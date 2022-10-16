#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int arr[n];
  for (int i = 0; i < n; i++)
    cin >> arr[i];
  int u = 0, d = 0;
  if (arr[n-1] < 0) {
    cout << -1 << endl;
    return 0;
  }
  for (int i = n-1; i >= 0; i--) {
    if (arr[i] > 0) arr[i] = u++;
    else arr[i] = --d;
  }
  for (int i = 0; i < n; i++) {
    cout << arr[i] - d + 1 << ' ';
  }
  cout << endl;
  return 0;
}