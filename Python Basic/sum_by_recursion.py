def recur_sum(n):
    if n <= 1:
        return n 
    else:
        return n + recur_sum (n-1)
n=10
ans= recur_sum(n)
print(ans)
