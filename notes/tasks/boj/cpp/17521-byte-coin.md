# 17521: Byte Coin

## 답안 1: 맞음
(일부 코드)
```cpp
  /* for (int i = 0; i < n; i++) 일 때 틀림:
     i == n일 때, arr[i]와 0 비교.. 어차피 일 안하지 않나? */
  for (int i = 0; i < n-1; i++) {
    if (arr[i] < arr[i+1]) {
      c = w / arr[i];
      w %= arr[i];
      c *= arr[i+1]; // 이게 지뢰네
      w += c;
    }
  }
```

## 답안 2: 틀림
틀린 이유: 초기화 안해서 ㅋㅋ;  
컴파일러가 알아서 초기화해줘서 문제를 확인할수가 없었음
```cpp
#include <iostream>
using namespace std;

int main(void) {
  int n; long long int c, w;
  cin >> n >> w;
  int arr[n];
  for (int i = 0; i < n; i++) cin >> arr[i];
  for (int i = 0; i < n; i++) {
    if (i < n-1) {
      if (arr[i] < arr[i+1]) {
        c += w / arr[i];
        w %= arr[i];
      } else if (arr[i] > arr[i+1]) {
        w += arr[i] * c;
        c = 0;
      }
    } else { // i == n-1
      w += arr[i] * c;
    }
  }
  cout << w << endl;
  return 0;
}
```