#include <iostream>
using namespace std;
int main(){
long long x;
while(cin>>x,x){
long long t=0,r,a=0,b=0;
r=x;
while(r)r>>=1,t++;
r=t;
bool ch=true;
while(t--){
    if(ch && x&(1<<t))
        a|=(1<<t),ch=false;
    else if(x&(1<<t))
        b|=(1<<t),ch=true;

}
cout<<a<<' '<<b<<endl;
}
return 0;
}