#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int oct_to_dec(int n) {
  int dec = 0, remain = 0, i = 0;
  while (n != 0) {
    remain = n % 10;
    n /= 10;
    dec += remain * pow(8, i);
    i++;
  }
  return dec;
}
int hex_to_dec(int n) {
  int dec = 0, remain = 0, i = 0;
  while (n != 0) {
    remain = n % 10;
    n /= 10;
    dec += remain * pow(16, i);
    i++;
  }
  return dec;
}

bool contains_9(int n) {
  while (n != 0) {
    if (n % 10 == 9 || n % 10 == 8) return true;
    n /= 10;
  }
  return false;
}

int main(void) {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int _, target;
    cin >> _ >> target;
    int conv[3] = {0, target, 0};
    conv[0] = contains_9(target) ? 0 : oct_to_dec(target);
    conv[2] = hex_to_dec(target);
    cout << _ << ' ' << conv[0] << ' ' << conv[1] << ' ' << conv[2] << endl;
  }
  return 0;
}