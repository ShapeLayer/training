#include <iostream>
using namespace std;

int N, *arr;
int main() {
  cin >> N;
  arr = (int*)calloc(N, sizeof(int));
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }

  int count = 0, max_height = 0;
  for (int i = N - 1; i >= 0; i--) {
    if (arr[i] > max_height) {
      count++;
      max_height = arr[i];
    }
  }

  cout << count << endl;

  free(arr);
  return 0;
}
