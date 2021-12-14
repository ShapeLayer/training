#include <iostream>
using namespace std;

int main(void) {
    int a = 10, b = a;
    int *c = NULL;
    c = &a;
    (*c)++;
    cout << a << ' ' << b << ' ' << *c;
    return 0;
}