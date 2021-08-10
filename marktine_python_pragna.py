def prime_number(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        return True
    else:
        return False

N=int(input())
prime_factor_list=[]
if 1<=N<=1015:
    for i in range(1,N+1):
        if N%i==0:
            e=prime_number(i)
            if e:
                prime_factor_list.append(i)

print(max(prime_factor_list))