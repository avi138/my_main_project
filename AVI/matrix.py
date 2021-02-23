# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=[3,4,5,6,6]
# d=[6,7,8,9,10]
# matrix = [a,b,c,d]
# print(matrix)

# print(matrix[1][2])
# print(matrix[2][2])

# print(matrix[1][4])
# print(matrix[3][4])
# element = (matrix[1][4]) + (matrix[3][4])
# print(element)
# print(float(element))

# matrix = [c]
# print(matrix)


# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=[3,4,8,9,0]
# d=[6,7,8,9,10]

# matrix = [a,b,c,d]
# print(matrix)

# print(matrix[1][1])
# print(matrix[3][4])

# print(len(matrix))

# list=[1,2,3,3,4]
# for i in range

# a=[]
# b=[8,9,0,1,2,3]
# c=[3,4,5,6,7,8]
# d=[2,3,4,4,5,6]

# matrix = [a,b,c,d]
# print(matrix)


r=int(input("enter a number of rows:"))
c=int(input("enter a number of column:"))

matrix = []
print("entert enteries row wise:")

for i in range(r):
    a=[ ]
    print("enter {}th row".format(i+1))
    for i in range(c):
        a.append(int(input()))

    matrix.append(a)
print("your matrix is:") 

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()


# for i in range:
#     s=int(input("enter a digit"))
#     a.append(s)
#     print(a)


# r=int(input("enter a number of rows:"))
# c=int(input("enter a number of column:"))
# matrix=[]
# print("enter enteries row wise")

# for i in range(r):
#     a=[]
#     print("enter {}th row".format(i+1))
#     for j in range(c):
#         a.append(int(input("enter :")))
    
#     matrix.append(a)
# print("this is your marix")
# for i in range(r):
#     for j in range(c):
#         print(matrix[i][j],end=' ')
#     print()
