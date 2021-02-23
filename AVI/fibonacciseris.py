# terms=int(input("how many terms "))
# a=0
# b=1
# count=0
# if terms<=0:
#     print("invaild input so enter positive number")
# elif terms==1:
#     print("fabinacci sequence upto {} term is {}".format(b,a))
# else:
#     print("fibonacci sequence")
#     while count<terms:
#         print(a)
#         c=a+b
#         a=b
#         b=c
#         count=count+1


terms=int(input("how many terms:"))
a=0
b=1
count=0
if terms<=0:
    print("invaild input so enter positive number")
elif terms==1:
    print("fabinacci sequence upto {} term is {}".format(b,a))
else:
    print("fibonacci sequence")
    while count<terms:
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1


        



