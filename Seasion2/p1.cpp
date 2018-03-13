#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
string s;
void fun(int i,char x){
    while(s[--i]=='?')s[i]=x;
}
int main(){
    cin>>s;
    int di[27];di[26]=0;
    for(short i=0;i<26;i++)cin>>di[i];
    long long ma=0,ans=0,ch=123;
    for(int i=0;i<s.size();i++){
        if(s[i]!='?'){
            if(ma!=0){
                long long v1=di[ch-97],v2=di[int(s[i])-97];
                if(ch!=123)
                    ans+=abs(v1-v2);
                else
                    v1=v2;
                if(v1>v2)
                    swap(v1,v2);
                for(int j=0;j<26;j++)
                    if(di[j]>=v1 && di[j]<=v2){
                        ch=j+97;
                        break;
                    }
                fun(i,char(ch));
                ma=0;
            }
            else if(ch!=123)
                ans+=abs(di[int(s[i])-97]-di[ch-97]);
            ch=int(s[i]);
        }
    else
        ma++;
    }
if(ch==123)
    fun(s.size(),'a');
else if(ma!=0){
    for(short i=0;i<26;i++)if(di[i]==di[ch-97]){ch=i+97;break;}
    fun(s.size(),char(ch));
}
cout<<ans<<endl<<s<<endl;
return 0;
}