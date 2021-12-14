// 풀다 말았음
#include <iostream>
#include <vector>
using namespace std;

struct Step {
  int depth = 0;
  int select[3] = {-1, -1, -1};
  int target;
  int latest;
};

Step process(Step step) {
  if (step.depth == 2) {
  }
}
vector<int> f;
int main(void) {
  int n;
  f.push_back(0); f.push_back(1);
  cin >> n;
  int arr[n], max=0;
  for (int i = 0; i < n; i++) { cin >> arr[i]; if (max < arr[i]) max = arr[i]; }
  while (f[f.size()-1] < max) f.push_back(f[f.size()-1] + f[f.size()-2]);
  
  return 0;
}