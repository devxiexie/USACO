#include <bits/stdc++.h>
using namespace std;

int n;

struct COW
{
    int arrival;
    int duration;
    int seniority;
};
vector<COW> cows;
bool sortingorder(COW a, COW b)
{
    return (a.arrival < b.arrival);
}

struct sortingranking
{
    bool operator()(COW a, COW b) const
    {
        return a.seniority < b.seniority;
    }
};

int solve()
{
    int ans = 0;
    set<COW, sortingranking> line;
    int curtime = cows[0].arrival + cows[0].duration;
    int nextcow = 1;
    while (nextcow < cows.size() || line.size() > 0) // if there are not cows we have measured yet or there is a line
    {
        while (nextcow < cows.size() && cows[nextcow].arrival <= curtime)
        {
            // insert cows into the line that arrive while the previous cow is still eating
            line.insert(cows[nextcow]);
            nextcow++;
        }
        if (nextcow < cows.size() && line.size() == 0)
        {
            // move on to the next cow if there is no line, and adding to the current time
            curtime = cows[nextcow].arrival + cows[nextcow].duration;
            nextcow++;
        }
        else if (line.size() > 0)
        {
            // if there is a line, see how much time the first cow in line will have to wait until they can eat
            // what works is that for the next cows in line, the current time does not get fully updated until there is no more line, so their waiting times will be compounded
            auto cow = line.begin();
            ans = max(ans, curtime - (cow->arrival));
            curtime += cow->duration;
            line.erase(cow);
        }
    }
    return ans;
}

int main()
{
    freopen("convention2.in", "r", stdin);
    freopen("convention2.out", "w", stdout);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int arrival, duration;
        cin >> arrival >> duration;
        COW x = COW();
        x.arrival = arrival;
        x.duration = duration;
        x.seniority = i;
        cows.push_back(x);
    }
    sort(cows.begin(), cows.end(), sortingorder);
    // for (auto a : cows)
    // {
    //     cout << a.arrival << ' ' << a.duration << ' ' << a.seniority << endl;
    // }
    cout << solve() << endl;
}
