#include <iostream>
#include <algorithm>
#define abs(x) ((x) < 0 ? -(x) : (x))
using namespace std;

long long i, N, M, *arr, max_sum = 1e10;

long long compute() {
  long long left = 0, right = 0;
  long long current_sum;

  while (left < N && right < N) {
    current_sum = abs(arr[right] - arr[left]);
    if (current_sum < M) { right++; }
    else {
      max_sum = min(max_sum, current_sum);
      left++;
    }
  }
  
  return max_sum;
}

int main() {
  cin >> N >> M;
  arr = (long long*)calloc(N, sizeof(long long));
  for (i = 0; i < N; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + N);

  cout << compute() << endl;

  free(arr);
  return 0;
}
