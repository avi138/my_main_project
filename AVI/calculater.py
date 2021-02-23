
# def calculater(a,b,op):
#     if op=='+':
#         print("the sum of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a+b))
#     elif op=='-':
#         print("the difference of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a-b))
#     elif op=='*':
#         print("the multiplication of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a*b))
#     elif op=='/':
#         print("the division of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a/b))
    
# def main():
#     a=int(input("enter a 1 digit :"))
#     b=int(input("enter a 2 digit :"))
#     # c=int(input("enter a 3 digit :"))
#     operation=(input("what would you like to do? \n choose betwen +,-,*,/  :"))

#     calculater(a,b,operation)

# if __name__=='__main__':
#     main()


def calculater(a,b,c,op):
    if op=='+':
        print("the sum of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a+b))
    elif op=='-':
        print("the difference of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a-b))
    elif op=='*':
        print("the multiplication of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a*b))
    elif op=='/':
        print("the division of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a/b))
    elif op=='**':
        print("the square of "+ str(a) + " "  + op + " "+str(b) + ' = '+ str(a**c))

def main():
    a=int(input("enter a 1 digit :"))
    b=int(input("enter a 2 digit :"))
    c=int(input("enter a square :"))
    operation=(input("what would you like to do? \n choose betwen (+,-,*,**,/) :"))

    calculater(a,b,c,operation)

if __name__=='__main__':
    main()































