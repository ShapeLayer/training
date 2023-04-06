#include <iostream>
using namespace std;

int main(void) {
  int X, Y, x = 0, y = 0;
  cin >> X >> Y;
  if (X == Y || (X == 0 || Y == 0)) {
    cout << 7 << endl;
    x += X; y += Y;
    cout << x << ' ' << y << endl;
    x += Y; y -= X;
    cout << x << ' ' << y << endl;
    x += Y; y -= X;
    cout << x << ' ' << y << endl;
    x -= X; y -= Y;
    cout << x << ' ' << y << endl;
    x -= X; y -= Y;
    cout << x << ' ' << y << endl;
    x -= Y; y += X;
    cout << x << ' ' << y << endl;
    x += X; y += Y;
    cout << x << ' ' << y << endl;
  } else {
    cout << 15 << endl;
    x += X; y += Y;
    cout << x << ' ' << y << endl;
    x += X; y -= Y;
    cout << x << ' ' << y << endl;
    x += Y; y += X;
    cout << x << ' ' << y << endl;
    x -= X; y -= Y;
    cout << x << ' ' << y << endl;
    x += Y; y -= X;
    cout << x << ' ' << y << endl;
    x -= Y; y -= X;
    cout << x << ' ' << y << endl;
    x += X; y -= Y;
    cout << x << ' ' << y << endl;
    x -= Y; y += X;
    cout << x << ' ' << y << endl;
    x -= X; y -= Y;
    cout << x << ' ' << y << endl;
    x -= X; y += Y;
    cout << x << ' ' << y << endl;
    x -= Y; y -= X;
    cout << x << ' ' << y << endl;
    x += X; y += Y;
    cout << x << ' ' << y << endl;
    x -= Y; y += X;
    cout << x << ' ' << y << endl;
    x += Y; y += X;
    cout << x << ' ' << y << endl;
    x += Y; y -= X;
    cout << x << ' ' << y << endl;
  }
  return 0;
}