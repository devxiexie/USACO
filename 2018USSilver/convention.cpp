#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
int n, m, c;
int cows[N];

bool pos(int wait)
{
    int buses = 1;
    int start = cows[0];
    int ind = 0;
    for (int i = 1; i < n; i++)
    {
        if (cows[i] - start > wait || i + 1 - ind > c)
        {
            buses++;
            start = cows[i];
            ind = i;
        }
    }
    return (buses <= m);
}

int search(int low, int high)
{
    if (low == high)
        return low;
    if (low + 1 == high)
    {
        if (pos(low))
            return low;
        else
            return high;
    }
    int mid = (low + high) / 2;
    if (pos(mid))
        return search(low, mid);
    else
        return search(mid + 1, high);
}

int main()
{
    freopen("convention.in", "r", stdin);
    freopen("convention.out", "w", stdout);
    cin >> n >> m >> c;
    for (int i = 0; i < n; i++)
    {
        cin >> cows[i];
    }
    sort(cows, cows + n);
    cout << search(0, 100000010) << endl;
}
