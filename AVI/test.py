# from module import x,y
# print(x,y)



# a=[1,2,3,4,5]
# b=[6,7,8,9,0]
# c=[1,3,5,7,8]
# d=[1,2,3,7,8]
# matrix=[a,b,c,d] 
# print(matrix)

# print(matrix[0][2])

# r=int(input("enter a number of rows:"))
# c=int(input("enter a number of column:"))

# matrix = []
# print("entert enteries row wise:")

# for i in range(r):
#     a=[ ]
#     print("enter {}th row".format(i+1))
#     for i in range(c):
#         a.append(int(input()))

#     matrix.append(a)
# print("your matrix is:") 

# for i in range(r):
#     for j in range(c):
#         print(matrix[i][j],end=" ")
#     print()

# sum=0
# for i in range(r):
#     for j in range(c):
#         if j==c-1:
#             sum=sum+matrix[i][j]

# print(sum)


# term=int(input("enter a number:"))
# a=0
# b=1
# count=0
# if term<=0:
#     print("enter a positive number")
# if term==1:
#     print("fibonacci series upto {} term is {}".format (a,b))
# else:
#     print("fibonacci series")
#     while count<term:
#         print(a)
#         c=a+b
#         a=b
#         b=c
#         count=count+1

a=int(input("enter a row :"))
for i in range(a):
    print(' *'*(i+1))





