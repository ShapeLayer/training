#include <iostream>
#define MAX 100'000
#define proc_min(a, b) (gets[a] == gets[b] ? (a < b ? a : b) : (gets[a] < gets[b] ? a : b))
using namespace std;

int init(int start, int end, int each);
int update(int start, int end, int each, int idx);
int main();
void compute(int n, int m);

int gets[MAX + 1];
int tree[MAX * 4 + 1];

int init(int start, int end, int each) {
    if (start == end) return tree[each] = start;
    int mid = (start + end) / 2;
    int front = init(start, mid, each * 2), back = init(mid + 1, end, each * 2 + 1);
    return tree[each] = proc_min(front, back);
}

int update(int start, int end, int each, int idx) {
    if (idx < start || idx > end || start == end)
        return tree[each];
    int mid = (start + end) / 2;
    int front = update(start, mid, each * 2, idx), back = update(mid + 1, end, each * 2 + 1, idx);
    return tree[each] = proc_min(front, back);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int n, m;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> gets[i];
    cin >> m;
    init(0, n - 1, 1);
    compute(n, m);

    return 0;
}

void compute(int n, int m) {
    for (int i = 0; i < m; i++) {
        int q, idx, val;
        cin >> q;
        if (q == 1) { // update
            cin >> idx >> val;
            gets[idx - 1] = val;
            update(0, n - 1, 1, idx - 1);
        } else if (q == 2) { // print
            cout << tree[1] + 1 << '\n';
        }
    }
}
