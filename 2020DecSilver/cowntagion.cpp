#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
int n, ans;
int roads[N];

int main()
{
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        a--, b--;
        roads[a]++, roads[b]++;
    }
    for (int i = 0; i < n; i++)
    {
        if (roads[i] > 1 || i == 0)
        {
            int children = roads[i];
            if (i != 0)
            {
                children--;
                // the infected cow must've came from somewhere else, and since there are only n-1 roads, and all farms are reachable, there are no "extra" infected cows that come
            }

            int log_children = 0;
            int pow = 1;
            while (pow < children + 1)
            {
                log_children++;
                pow *= 2;
            }
            ans += log_children;
        }
    }
    cout << ans + (n - 1) << endl;
    // the n-1 is from the roads needed to be travelled, and ans is the amount of days it takes to duplicate
}
