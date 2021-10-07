// 백준 메모리제한 초과
// long long 부분 때문인가..?
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int main(void) {
  const int size_of_content[] = {26, 10};
  string format;
  vector<int> format_type, format_len;
  cin >> format;
  for (int i=0; i < format.size(); i++) {
    int format_to_int = (format[i] == 'c') ? 0 : 1; // 0: alphabet, 1: number
    if (i == 0) {
      format_len.push_back(1);
      format_type.push_back(format_to_int);
    } else {
      if (format_type[i-1] == format_to_int) {
        format_len[i-1]++;
      } else {
        format_len.push_back(1);
        format_type.push_back(format_to_int);
      }
    }
  }
  // (Debugging..)
  long long count = 1;
  for (int i = 0; i < format_len.size(); i++) {
    for (int j = 0; j < format_len[i]; j++) {
      cout << format_type[i] << " | ";
      cout << count << ' ';
      count *= (size_of_content[format_type[i]] - (j == 0 ? 0 : 1));
      cout << count << ' ';
      count %= 1000000009;
      cout << count << endl;
    }
  }
  cout << count << endl;
  return 0;
}