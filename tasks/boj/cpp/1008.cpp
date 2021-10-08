#include <iostream>
using namespace std;

int main(void) {
    double a, b;
    cin >> a >> b;
    cout.precision(10);
    cout << fixed << a / b << endl;
    return 0;
}