def solution(total_lambs):
    # pay generously: 2^n
    # pay stingyly: fibonacci series
    res_min = 0
    res_max = 0
    
    t = total_lambs
    pay = 1
    while(t>=pay):
        t-=pay
        pay*=2
        res_min+=1
        
        
    t = total_lambs
    pay_prev = 1
    pay_cur = 1
    
    if(t>2):
        res_max+=2
        t-=2
        while(t>=(pay_prev+pay_cur)):
            t-=(pay_prev+pay_cur)
            t2 = pay_cur
            pay_cur+=pay_prev
            pay_prev = t2
            res_max+=1
    else:
        res_max = t
        
    return res_max-res_min