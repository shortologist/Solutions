#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
string s="",ans="";
bool te=false;
void fun(){
    if(te)
        ans=s+ans;
    else
        ans+=s;
}
void fast()
{
	std::ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
}
int main(){
    fast();
    string x;
    while(getline(cin, x)){
            s="",ans="";
        for(int i=0;i<x.size();i++){
            if(x[i]=='['){
                fun();
                te=true;
                s="";
            }
            else if(x[i]==']'){
                fun();
                te=false;
                s="";
            }
            else
                s+=x[i];
        }
    fun();
    cout<<ans<<endl;
    }
return 0;
}
