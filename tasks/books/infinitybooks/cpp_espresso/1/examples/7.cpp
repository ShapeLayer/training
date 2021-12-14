#include <iostream>
#include <string>
using namespace std;

int main(void) {
    int x = 1, y = 2;
    bool a, b, c;
    a = x <= y;
    b = x == y;
    c = x != y;
    
    // 0/1 => false/true
    cout.setf(cout.boolalpha);
    cout << a << ' ' << b << ' ' << c << '\n';
    cout << (a ? 30 : 40) << ' ' << (b ? 10 : 110) << ' ' << (c ? 100 : 1) << '\n';
}