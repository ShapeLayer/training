#include <iostream>
#include <cmath>
using namespace std;

#define FOLD(X, MID) (X < MID ? X : 2 * MID - X)

// [0]: red
// [1]: blue
// [2]: yellow
pair<double, double> dots[3];
double total_size;

void compute() {
  double mid;
  double offset;
  for (int i = 0; i < 3; i++) {
    if (dots[i].first == dots[i].second) continue;
    mid = (dots[i].first + dots[i].second) / 2.0;
    offset = 0;

    // make mid into origin
    // fold using origin as folding point
    for (int j = 0; j < 3; j++) {
      dots[j].first = FOLD(dots[j].first, mid);
      dots[j].second = FOLD(dots[j].second, mid);
      offset = min(offset, min(dots[j].first, dots[j].second));
    }

    offset = min(offset, mid * 2 - total_size);

    for (int j = 0; j < 3; j++) {
      dots[j].first -= offset;
      dots[j].second -= offset;
    }

    total_size = max(mid - offset, total_size - mid);
  }
}

int main() {
  cin >> total_size;
  total_size *= 100;
  for (int i = 0; i < 3; i++) {
    cin >> dots[i].first >> dots[i].second;
    dots[i].first *= 100;
    dots[i].second *= 100;
  }

  compute();
  cout << fixed;
  cout.precision(1);
  cout << total_size / 100 << endl;

  return 0;
}
