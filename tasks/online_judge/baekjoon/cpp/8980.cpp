#include <iostream>
#include <algorithm>
#include <tuple>
#include <queue>
using namespace std;
using delivery = tuple<int, int, int>;

bool compare(delivery a, delivery b) {
  if (get<1>(a) != get<1>(b)) return get<1>(a) < get<1>(b);
  if (get<0>(a) != get<0>(b)) return get<0>(a) > get<0>(b);
  return get<2>(a) > get<2>(b);
}

int compute(int N, int C, int M, delivery *deliveries) {
  sort(deliveries, deliveries + M, compare);
  // index of *deliveries
  int di = 0;

  // _to, _quantity
  queue<pair<int, int>> now_delivering;
  // loaded_at[N] = total quantity loaded at town N
  int *loaded_at = (int *)malloc(sizeof(int) * (N + 1));
  fill(loaded_at, loaded_at + N + 1, 0);

  int pos = 0;
  int delivered = 0;

  while (pos <= N) {
    while (!now_delivering.empty()) {
      pair<int, int> now = now_delivering.front();

      int _to = now.first;
      int _quantity = now.second;

      if (pos >= _to) {
        now_delivering.pop();
        delivered += _quantity;
      } else {
        break;
      }
    }

    while (di < M) {
      delivery now = deliveries[di];
      int _from = get<0>(now);
      int _to = get<1>(now);
      int _quantity = get<2>(now);

      int now_loading = _quantity;
      for (int i = _from; i < _to; i++) {
        now_loading = min(now_loading, C - loaded_at[i]);
      }

      if (now_loading > 0) {
        now_delivering.push(make_pair(_to, now_loading));
        for (int i = _from; i < _to; i++) {
          loaded_at[i] += now_loading;
        }
      }
      di++;
    }

    pos++;
  }

  return delivered;
}

int main() {
  int N, C, M;
  delivery *deliveries;

  cin >> N >> C >> M;
  deliveries = (delivery *)malloc(sizeof(delivery) * M);

  int _from, _to, _quantity;
  for (int i = 0; i < M; i++) {
    cin >> _from >> _to >> _quantity;
    deliveries[i] = make_tuple(_from, _to, _quantity);
  }

  cout << compute(N, C, M, deliveries) << endl;

  return 0;
}
