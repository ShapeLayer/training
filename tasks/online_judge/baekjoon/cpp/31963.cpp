#include <iostream>
#include <cmath>
using namespace std;

int N;
int main()
{
  cin >> N;
  long long counts = 0;

  int arr[N];
  for (int i = 0; i < N; i++)
    cin >> arr[i];

  int multiplies[N];
  for (int i = 0; i < N; i++)
    multiplies[i] = 0;

  for (int i = 1; i < N; i++)
  {
    multiplies[i] = max(
        (int)ceil(log2((double)arr[i - 1] / (double)arr[i]) + (double)multiplies[i - 1]),
        0);

    counts += multiplies[i];
  }

  cout << counts << endl;

  return 0;
}
