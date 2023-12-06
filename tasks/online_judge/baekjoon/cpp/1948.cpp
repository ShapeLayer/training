#include <bits/stdc++.h>
using namespace std;

inline void dfs();

int main() {
  int n, m;
  cin >> n;
  cin >> m;
  vector<int> conn_fw[n + 1], conn_rw[n + 1];
  int costs[n + 1][n + 1] = { 0 };
  int src, dst;
  for (int i = 0; i < m; i++) {
    int from, to, cost;
    cin >> from >> to >> cost;
    conn_fw[from].push_back(to);
    conn_rw[to].push_back(from);
    costs[from][to] = cost;
  }
  cin >> src >> dst;

  int indegree[n + 1] = { 0 };
  for (int i = 1; i < n + 1; i++) {
    for (int each : conn_fw[i]) {
      indegree[each]++;
    }
  }
  deque<int> queue;
  for (int i = 1; i < n + 1; i++) {
    if (indegree[i] == 0) {
      queue.push_back(i);
    }
  }
  int max_costs[n + 1] = { 0 };
  while (queue.size()) {
    int now = queue.front();
    queue.pop_front();
    for (int each : conn_fw[now]) {
      max_costs[each] = max(max_costs[each], max_costs[now] + costs[now][each]);
      indegree[each]--;
      if (!indegree[each]) {
        queue.push_back(each);
      }
    }
  }

  queue.clear();
  queue.push_back(dst);
  bool visits[n + 1][n + 1] = { false };
  int path_count = 0;
  while (queue.size() > 0) {
    int now = queue.front();
    queue.pop_front();
    for (int each : conn_rw[now]) {
      if (visits[now][each]) continue;
      if (max_costs[now] == max_costs[each] + costs[each][now]) {
        queue.push_back(each);
        visits[now][each] = true;
        path_count++;
      }
    }
  }

  cout << max_costs[dst] << endl << path_count << endl;
}
