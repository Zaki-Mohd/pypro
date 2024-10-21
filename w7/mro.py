class A:
    def process(self):
        print("Method in A")

class B(A):
    def process(self):
        print("Method in B")

class C(A):
    def process(self):
        print("Method in C")

class D(B, C):
    pass


d = D()
d.process()


print(D.mro())
