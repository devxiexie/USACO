#include <bits/stdc++.h>
using namespace std;

set<int> yearnum;
vector<int> gaps;
int n, k;

int main()
{
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        int yearsbeen;
        cin >> yearsbeen;
        yearnum.insert((yearsbeen + 11) / 12);
    }
    int ans = *yearnum.rbegin();
    int last = 0;
    while (!yearnum.empty())
    {
        gaps.push_back(*yearnum.begin() - last - 1);
        last = *yearnum.begin();
        yearnum.erase(*yearnum.begin());
    }
    sort(gaps.rbegin(), gaps.rend());

    for (int i = 0; i < k - 1 && i < gaps.size(); i++)
        ans -= gaps[i];
    cout << ans * 12 << endl;
}
