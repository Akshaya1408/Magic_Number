def magic(num):

    sum=0
    while num>0:
        sum+=num%10
        num//=10
    if sum>9:
        return magic(sum)
    else:
        if sum==1:
            return 1
        else:
            return 0

num=int(input())
print(magic(num))