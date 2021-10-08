#include <iostream>
using namespace std;

int main(void) {
  while (true) {
    string content;
    getline(cin, content);
    if (content == "#") break;
    int cnt = 0;
    for (int i = 0; i < content.size(); i++) {
      switch (content[i]) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
          cnt++;
          break;
        default:
          break;
      }
    }
    cout << cnt << endl;
  }
  return 0;
}