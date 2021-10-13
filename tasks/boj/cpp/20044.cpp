#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int stu[n*2], team[n];
  for (int i = 0; i < 2*n; i++) cin >> stu[i];
  sort(stu, stu+2*n);
  for (int i = 0; i < n; i++) team[i] = stu[i];
  for (int i = 0; i < n; i++) team[i] += stu[2*n-1-i];
  int min = team[0];
  for (int i = 0; i < n; i++) if (team[i] < min) min = team[i];
  cout << min << endl;
  return 0;
}