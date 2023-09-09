#include <iostream>
using namespace std;

int main(void) {
  int t;
  cin >> t;
  while(t--) {
    int n;
    cin >> n;
    int votes[n];
    int max_votes = 0, max_gets = 0, total_votes = 0;
    bool max_duplicates = false;
    for (int i = 0; i < n; i++) {
      cin >> votes[i];
      if (max_votes < votes[i]) {
        max_votes = votes[i];
        max_gets = i;
        max_duplicates = false;
      } else if (max_votes == votes[i]) {
        max_duplicates = true;
      }
      total_votes += votes[i];
    }
    if (max_duplicates) {
      cout << "no winner" << endl;
    } else if (max_votes > total_votes - max_votes) {
      cout << "majority winner " << (max_gets + 1) << endl;
    } else {
      cout << "minority winner " << (max_gets + 1) << endl;
    }
  }
  return 0;
}
