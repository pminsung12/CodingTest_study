//문제를 잘못 이해했었음. 테스트 5를 해보고 겨우 이해했네 
//단순 2개씩 묶어서 비교하는게 아니라 맨 앞에 거를 기준으로 그거보다 뒤에 것들이 덜 걸리면 다 묶는 것임.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer,days;
    int cnt=0;
    for(int i=0;i<progresses.size();i++){
        int res=100-progresses[i];
        if(res%speeds[i]){
            days.push_back(res/speeds[i]+1);
        }
        else days.push_back(res/speeds[i]);
    }
    
    while(!days.empty()){
        cnt=0;
        int cur=days.front();
        for(int i=0;i<days.size();i++){
            if(cur>=days[i]){
                cnt++;
            }
            else break;
        }
        for(int i=0;i<cnt;i++){
            days.erase(days.begin());
        }
        answer.emplace_back(cnt);
    }
    
    
    return answer;
}

/* 반례를 못찾음.
#include <string>
#include <vector>
using namespace std;
int days(int a, int b){
    int res=100-a;
    if(res%b){
        return res/b+1;
    }
    else return res/b;
}
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int cnt=1;
    for(int i=0;i<progresses.size()-1;i++){
        if(days(progresses[i],speeds[i])>=days(progresses[i+1],speeds[i+1])){
            cnt++;
        }
        else{
            answer.push_back(cnt);
            
        }
    }
    answer.push_back(cnt);
    
    return answer;
}
*/