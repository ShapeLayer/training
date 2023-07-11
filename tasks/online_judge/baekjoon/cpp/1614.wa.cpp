#include <iostream>
#include <algorithm>
#define i64 long long

using namespace std;

int main(void) {
    int k, n;
    cin >> k >> n;
    int gets[k];
    for (int i = 0; i < k; i++)
        cin >> gets[i];
    sort(gets, gets + k);
    int _min = gets[0], _max = gets[k - 1];

    i64 low = 0, high = _max, mid = -1;
    int result = 0;
    int counts = 0;
    while (low <= high) {
        counts = 0;
        mid = (low + high) / 2;
        if (mid == 0) {
            result = mid;
            break;
        }
        for (int i = 0; i < k; i++)
            counts += gets[i] / mid;
        
        if (counts >= n) {
            low = mid + 1;
            if (result < mid) result = mid;
        } else {
            high = mid - 1;
        }
    }

    cout << result << '\n';
    return 0;
}
