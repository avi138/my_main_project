# var=lambda x,y: x**2+y+1
# print(var(2,1000000))

# def fun(n):
#     return lambda a,b:a*n+b

# var=fun(3)

# val=var(2,3)
# print(val)

n=int(input("enter a number"))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")

else:
    print(n,"is not a prime number")

