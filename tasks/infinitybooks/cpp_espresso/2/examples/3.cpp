#include <iostream>
using namespace std;

int main(void) {
    int answer = 59, tries = 0, guess;
    do {
        cout << "Answer: ";
        cin >> guess;
        
        if (guess > answer) cout << "Down" << endl;
        if (guess < answer) cout << "Up" << endl;
        tries++;
    } while (guess != answer);

    cout << "Success (" << tries << " tries)";
}