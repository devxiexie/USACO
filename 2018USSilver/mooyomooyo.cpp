#include <bits/stdc++.h>
using namespace std;

int n, k;
int board[110][10];
int region[110][10];
int regsizes[1010];

void floodfill(int i, int j, int r, int c)
{
    if (i < 0 || i >= n || j < 0 || j >= 10 || board[i][j] != c || region[i][j] != 0)
        return;
    region[i][j] = r;
    regsizes[r]++;
    floodfill(i - 1, j, r, c);
    floodfill(i + 1, j, r, c);
    floodfill(i, j - 1, r, c);
    floodfill(i, j + 1, r, c);
}

void gravity()
{
    for (int j = 0; j < 10; j++)
    {
        int top = n - 1;
        int bottom = n - 1;
        while (top >= 0)
        {
            while (top >= 0 && board[top][j] == 0)
                top--;
            if (top >= 0)
            {
                // take the highest actual number and bring it down
                board[bottom][j] = board[top][j];
                bottom--;
                top--;
            }
        }
        while (bottom >= 0)
        {
            board[bottom][j] = 0;
            bottom--;
        }
    }
}

bool doing()
{
    // board represents the given board, and region represents the unique code given to each region of numbers
    int r = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            region[i][j] = 0;
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (board[i][j] != 0 && region[i][j] == 0) // if the board is a number and the region number for this region has not been asigned yet
            {
                floodfill(i, j, r, board[i][j]);
                r++;
            }
        }
    }
    bool needtocontinue = false;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (board[i][j] != 0 && regsizes[region[i][j]] >= k) // if the board is a number and the size of that region the current place in is bigger than k
            {
                board[i][j] = 0;
                needtocontinue = true;
            }
        }
    }
    gravity();
    while (r)
    {
        regsizes[r] = 0;
        r--;
    }
    return needtocontinue;
}

int main()
{
    freopen("mooyomooyo.in", "r", stdin);
    freopen("mooyomooyo.out", "w", stdout);
    cin >> n >> k;
    string line;
    for (int i = 0; i < n; i++)
    {
        cin >> line;
        for (int x = 0; x < 10; x++)
        {
            board[i][x] = line[x] - '0';
        }
    }
    while (doing())
        ;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            cout << board[i][j];
        }
        cout << endl;
    }
}
