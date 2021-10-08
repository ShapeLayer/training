#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int m[n];
  for (int i = 0; i < n; i++) {
    cin >> m[i];
  }
  int max = 0;
  for (int i = 0; i < n; i++) {
    int k = 0;
    for (int j = i+1; j < n; j++) {
      if (m[i] <= m[j]) break;
      k++;
    }
    if (max < k) max = k;
  }
  cout << max << endl;
  return 0;
}