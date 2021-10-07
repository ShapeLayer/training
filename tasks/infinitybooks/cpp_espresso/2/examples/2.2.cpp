#include <iostream>
using namespace std;

int main(void) {
    int vowel=0, consonant=0;
    char ch;
    cout << "Type converstation and hit ctrl-z\n";
    while (cin >> ch) {
        switch(ch) {
            case 'a':
            case 'i':
            case 'u':
            case 'e':
            case 'o':
                vowel++;
                break;
            default:
                consonant++;
                break;
        }
    }
    cout << "vowel: " << vowel << '\n';
    cout << "consonant: " << consonant << '\n';
    return 0;
}