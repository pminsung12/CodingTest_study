#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    int r;
    char arr[3]={'4','1','2'};
    while(n!=0){
        r=n%3;
        answer=arr[r]+answer;
        if(!(n%3))n=(n-1)/3;
        else n/=3;
    }
    
    return answer;
}

/*
#include <string>
#include <vector>
#include <cmath>
using namespace std;
string solution(int n) {
    string answer = "";
    int i=1;
    int a=0;
    while(n>0){
        a=pow(3,i);
        if(n-a>0) n-=a;
        else break;
        i++;
    }
    for(int j=0;j<i;j++){
        answer+='1';
    }
    for(int j=0;j<n-1;j++){
        for(int k=i-1;k>=0;k--){
            if(answer[k]=='1') {
                answer[k]='2';
                break;
            }
            else if(answer[k]=='2') {
                answer[k]='4';
                break;
            }
            else {
                answer[k]='1';
                continue;
            }
        }
    }
    
    return answer;
}
*/