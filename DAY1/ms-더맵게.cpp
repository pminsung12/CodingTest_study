#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq;
    for(int e:scoville)pq.push(e);
    
    while(pq.top()<K){
        if(pq.size()==1) return -1;
        int tmp1=pq.top();
        pq.pop();
        int tmp2=pq.top();
        pq.pop();
        pq.push(tmp1+tmp2*2);
        answer++;
    }
    return answer;
}



/* 효율성 탈락
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int solution(vector<int> scoville, int K) {
    int answer = 0,flag=0,tmp=0,i=0;
    
    for(auto i:scoville){
        if(i!=0) flag =1;
    }
    if(!flag) return -1;
    
    sort(scoville.begin(),scoville.end());
    
    while(scoville.front()<K&&scoville.size()>1){
        tmp=scoville[0]+2*scoville[1];
        scoville.erase(scoville.begin());
        scoville.front()=tmp;
        
        while(i<scoville.size()-1){
            if(scoville[i]>scoville[i+1]){
                tmp=scoville[i];
                scoville[i]=scoville[i+1];
                scoville[i+1]=tmp;
            }
            i++;
        }
        i=0;
        answer++;
    }
    if(scoville.size()==1&&scoville.front()<K) return -1;
    return answer;
}
*/