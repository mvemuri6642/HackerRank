for _ in range(int(input())):
    a,b=map(int,input().split())
    x=min(a,b)
    y=max(a,b)
    print(y//x)