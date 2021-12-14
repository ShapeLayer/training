#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int m;
    cin >> m;
    string yoty_university; int yoty_count = 0;
    for (int j = 0; j < m; j++) {
      string university; int count;
      cin >> university >> count;
      if (count > yoty_count) {
        yoty_count = count;
        yoty_university = university;
      }
    }
    cout << yoty_university << endl;
  }
  return 0;
}