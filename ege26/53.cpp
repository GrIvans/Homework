#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    fstream fin;
    fin.open("26data/26-53.txt");
    int n;
    fin >> n;
    vector<int> chet;
    vector<int> nechet;
    for (int i = 0; i < n; i++)
    {
        int temp;
        fin >> temp;
        if (temp % 2 == 0)
        {
            chet.push_back(temp);
        }
        else
        {
            nechet.push_back(temp);
        }
    }
    int k = 0;
    int mx = 0;
    int size = nechet.size();
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = i + 1; j < n; i++)
        {
            int sr = (nechet[i] + nechet[j]) / 2;
            if (sr % 2 == 0)
            {
                for (int f = 0; f < chet.size(); f++)
                {
                    if (chet[f] == sr)
                    {
                        k++;
                        mx = max(mx, sr);
                    }
                }
            }
            else{
                for (int nf = 0; nf < nechet.size(); nf++)
                {
                    if (nechet[nf] == sr)
                    {
                        k++;
                        mx = max(mx, sr);
                    }
                }
            }
        }
    }
    cout << k << " " << mx << endl;
    return 0;
}