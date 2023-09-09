#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int rating[21][21];
int n;
int min_diff = 2e9;
bool visits[21];

int step(int select_count, int invoke) {
  if (select_count == n / 2) {
    int scores[] = {0, 0};
    vector<int> selects[2];
    for (int i = 1; i <= n; i++) {
      int ptr = (int)(visits[i]);
      selects[ptr].push_back(i);
    }

    for (int i = 0; i < n / 2 - 1; i++) {
      for (int j = i + 1; j < n / 2; j++) {
        scores[0] += rating[selects[0][i]][selects[0][j]] + rating[selects[0][j]][selects[0][i]];
        scores[1] += rating[selects[1][i]][selects[1][j]] + rating[selects[1][j]][selects[1][i]];
      }
    }

    min_diff = min(min_diff, abs(scores[0] - scores[1]));
    return 0;
  }

  for (int i = invoke + 1; i <= n; i++) {
    visits[i] = true;
    step(select_count + 1, i);
    visits[i] = false;
  }
  return 0;
}

int main(void) {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      cin >> rating[i][j];
    }
  }

  step(0, 0);
  cout << min_diff << endl;
}
