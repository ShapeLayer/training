#include <iostream>
#define MAX 300
using namespace std;

int main() {
  int n;
  cin >> n;
  int gets[MAX] = { 0 }, dp[MAX] = { 0 };

  for (int i = 0; i < n; i++) cin >> dp[i];
  dp[0] = gets[0];
  dp[1] = gets[0] + gets[1];

  for (int i = 2; i < n; i++) {
    if (i - 2 >= 0) {
      dp[i] = max(dp[i], dp[i - 2] + gets[i]);
    } else if (i - 3 >= 0) {
      dp[i] = max(dp[i], dp[i - 3] + gets[i - 2] + gets[i]);
    } else if (i - 4 >= 0) {
      dp[i] = max(dp[i], dp[i - 4] + gets[i - 3] + gets[i - 2] + gets[i]);
    }
  }

  return 0;
}


/*
 * 1 1 2 => 4
 * 1 2 => 3
 * 2 => 2
 */
