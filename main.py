from matrix import Matrix
A=Matrix([[1,2,3],[3,4,5]])
B=Matrix([[3,4,5],[6,7,8]])
C=A+B
D=A-B
E=A*5
print(C.data)
print(D.data)
print(E.data)