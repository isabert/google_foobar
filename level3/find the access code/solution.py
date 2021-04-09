def solution(l):
    # Your code here
    res = 0
    pair = [0]*len(l)
    for i in range(1,len(l)):
        for j in range(0,i):
            if(l[i]%l[j]==0):
                pair[i]+=1
                res+=pair[j]
    return res


print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))