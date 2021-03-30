def solution(x, y):
    # Your code here
    res1 = [0]*2000
    res2  =[0]*2000
    
    for e in x:
        res1[e+1000]+=1
        
    for e in y:
        res2[e+1000]+=1
        
    for i in range(0,2001):
        if(res1[i]!=res2[i]):
            return i-1000
