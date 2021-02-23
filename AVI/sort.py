# fruits=['cherry','banana','orange','mango']
# fruits.sort(reverse=True)
# print(fruits)


def length_of_car(i):
    return len(i)

car=['mercedes','bmw','vw','ford']
car.sort(key=length_of_car,reverse=True)
print(car)

list=('1','2','3','4','ś5')
emptylist=[]
for i in list:
    a=i**2
    emptylist.append(a)

print(emptylist)

