#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;


int delit(int a){
    int k = 0, mx = 0;
    for (int i = 1; i <= int(sqrt(a)); i++){
        if (a % i == 0){
            if (i % 2 == 1){
                k++;
                mx = max(mx, i);
            }
            if ((a / i) % 2 == 1){
                k++;
                mx = max(a / i, mx);
            }
        }
    }
    if (k == 5){
        return mx;
    }
    return -1;
}

int main(){
    for (int i = 63000000; i < 75000001; i++){
        int ch = delit(i);
        if (ch != -1){
            cout << i << " " << ch << endl;
        }
    }
    return 0;
}