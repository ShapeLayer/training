#include <iostream>
using namespace std;

int main(void) {
    int number;
    cout << "Input Number: ";
    cin >> number;
    switch (number) {
        case 0:
            cout << "zero\n";
            break;
        case 1:
            cout << "first\n";
            break;
        default:
            cout << "lots\n";
            break;
    }
    return 0;
}