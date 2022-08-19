#include<iostream>
using namespace std;

int main(){
    int test;
    cin >> test;

    while(test != 0 ){
        int n; cin >> n;
        int m; cin >> m;
        if( n%2 == m%2 ){
            cout<< "Tonya"<<endl;
        }
        else{
            cout<< "Burenka"<<endl;
        }
        test--;
    } 
}