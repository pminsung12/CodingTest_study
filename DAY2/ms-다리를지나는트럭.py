from collections import deque

def solution(bl, w, tw):
    answer = 0
    bridge=[0 for _ in range(bl)]
    
    while bridge:
        answer+=1
        bridge.pop(0)
        if tw:
            if sum(bridge)+tw[0]<=w: 
                t=tw.pop(0)
                bridge.append(t) #맨뒤에 트럭올리고, 무게 가능하면 한대 또 올리고
            else:
                bridge.append(0) #안올리면 0만 넣어서 while돌면서 트럭이 앞으로 한대씩 결국 이동함.
    
    return answer