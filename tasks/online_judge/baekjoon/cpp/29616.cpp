#include <iostream>
#include <tuple>
#include <cmath>
#define max(a, b) (a > b ? a : b)
using namespace std;

int gcd(long long a, long long b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int multiple_gcd(long long n, long long arr[]) {
    int gcd_val = 0;
    for (int i = 0; i < n; i++)
        gcd_val = gcd(gcd_val, arr[i]);
    return gcd_val;
}

tuple<long long, long long> compute(int n, int p, long long prev_votes[], long long curr_votes[]) {
    int prev_gcd = multiple_gcd(n, prev_votes), curr_gcd = multiple_gcd(n, curr_votes);
    int offset = 1;
    long long sum__prev_proc = 0;
    for (int i = 0; i < n; i++) {
        prev_votes[i] = prev_votes[i] / prev_gcd;
        curr_votes[i] = curr_votes[i] / curr_gcd;
        if (curr_votes[i] > 0)
            offset = max(offset, (prev_votes[i] + curr_votes[i] - 1) / curr_votes[i]);
        sum__prev_proc += prev_votes[i];
    }
    long long sum__curr_proc = 0;
    for (int i = 0; i < n; i++)
        sum__curr_proc += curr_votes[i] * offset;
    return make_tuple(sum__prev_proc, sum__curr_proc);
}

int main() {
    int n, p;
    cin >> n >> p;
    int offset = pow(10, p);
    long long prev_votes[n], curr_votes[n];
    for (int i = 0; i < n; i++) {
        cin >> prev_votes[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> curr_votes[i];
    }
    tuple<long long, long long> result = compute(n, p, prev_votes, curr_votes);
    cout << get<0>(result) << ' ' << get<1>(result) << endl;
    return 0;
}
