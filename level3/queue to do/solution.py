def solution(start, length):
    def xor_from_1(number):
        #define f(n)= 1^2^...^n
        #we will discover a rule... try: f(1), f(2),f(3),f(4),f(5)
        mod= number%4
        if(mod==0):
            return number
        if(mod==1):
            return 1
        if(mod==2):
            return number+1
        if(mod==3):
            return 0

        #also note x^x=0
        #0^x = x

    prev = start
    res = 0
    for i in range(length):
        row_cnt = length-i
        res ^=(xor_from_1(start+row_cnt-1)^xor_from_1(prev-1))
        start+=length
        prev = start
    return res

# print(solution(17,4))
# print(solution(0,3))
# print(solution(14,1))