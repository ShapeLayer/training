#include <iostream>
#include <string>
using namespace std;

int main(void) {
  int cnt[26] = { 0 };
  string content;
  getline(cin, content);
  for (int c: content) {
    cnt[c-97]++;
  }
  for (int i: cnt) {
    cout << i << ' ';
  }
  return 0;
}