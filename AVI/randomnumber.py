# import random
# print(random.random())


# print(random.randint(10,100))


# print(random.randrange(5,80,4))


# student=[2,5,13,67,78]
# random.choice(student)


lowerletter='abcdefghijklmnopqrstuvwxyz'
upperletter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='0123456789'
special='#$*@+_-!/?'
concate=lowerletter+upperletter+number+special
import random
new=random.sample(concate,8)

password = " ".join(new)
print(password)
