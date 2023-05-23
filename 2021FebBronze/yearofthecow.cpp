#include <bits/stdc++.h>
using namespace std;

string animals[12] = {"Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"};

map<string, int> whenwasborn;

int n;

string getanimal(int year)
{
    int a = 0;
    int y = 2021;
    if (y < year)
        while (y < year)
        {
            y++;
            a++;
            if (a == 12)
                a = 0;
        }
    else
        while (y > year)
        {
            y--;
            a--;
            if (a == -1)
                a = 11;
        }
    return animals[a];
}

int main()
{
    cin >> n;
    whenwasborn["Bessie"] = 2021;
    string cowa, born, in, relation, animal, year, from, cowb;
    for (int i = 0; i < n; i++)
    {
        cin >> cowa >> born >> in >> relation >> animal >> year >> from >> cowb;
        whenwasborn[cowa] = whenwasborn[cowb];

        if (relation == "previous")
            whenwasborn[cowa]--;
        else
            whenwasborn[cowa]++;

        while (getanimal(whenwasborn[cowa]) != animal)
        {
            if (relation == "previous")
                whenwasborn[cowa]--;
            else
                whenwasborn[cowa]++;
        }
    }
    int ans = whenwasborn["Bessie"] - whenwasborn["Elsie"];
    cout << abs(ans) << endl;
}
