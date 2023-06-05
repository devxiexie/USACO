#include <bits/stdc++.h>
using namespace std;

int n;

int main()
{
    freopen("lifeguards.in", "r", stdin);
    freopen("lifeguards.out", "w", stdout);
    cin >> n;
    vector<pair<int, int>> guards(n);
    for (int i = 0; i < n; i++)
    {
        cin >> guards[i].first >> guards[i].second;
    }
    sort(guards.begin(), guards.end());
    int tottime = 0;

    int left = 0, right = 0;
    for (int i = 0; i < n; i++)
    {
        if (guards[i].second > right)
        {
            left = max(right, guards[i].first);
            tottime += (guards[i].second - left);
            right = guards[i].second;
        }
    }

    pair<int, int> last;
    last.first = guards[n - 1].second;
    guards.push_back(last);

    int minalone = tottime;
    right = 0;
    for (int i = 0; i < n; i++)
    {
        int currans = min(guards[i + 1].first, guards[i].second) - max(guards[i].first, right);
        minalone = min(minalone, currans);
        right = max(right, guards[i].second);
    }
    cout << tottime - max(minalone, 0) << endl;
}
