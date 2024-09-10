my_tuple=("Hello,",3.14,"World!!")
print(3.14 in my_tuple)

my_tuple=("Hello,",3.14,"World!!",[10,2],89)
elem=89
x=my_tuple.index(elem)
print(x)
if my_tuple.index(elem):
    print('Found')


