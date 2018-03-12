#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
short n;
vector<short>v;
void fun(){
    long long l=0,r=0;
    for(int i=0;i<v.size();i++)
        if((i+1)&1)
            l+=pow(2,v[i]-1);
        else
            r+=pow(2,v[i]-1);
    cout<<l<<' '<<r<<endl;
}
int main(){
long long x;
while(cin>>x,x){
        n=0;
        while(x){
           if(x&1)
                v.push_back(n+1);
            x>>=1;
            n++;
        }
        reverse(v.begin(),v.end());
        fun();
        v.clear();
}
return 0;
}
