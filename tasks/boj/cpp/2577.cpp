#include <iostream>
using namespace std;

int main(void) {
  int a, b, c, i, j, n;
  int nums[10] = {0};
  cin >> a >> b >> c;
  n = a * b * c;
  while (n != 0) {
    i = n % 10;
    nums[i]++;
    n /= 10;
  }
  for (int j = 0; j < 10; j++) cout << nums[j] << ' ';
  return 0;
}