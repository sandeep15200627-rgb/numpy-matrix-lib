import numpy as np
class Matrix:
    def __init__(self,data):
      self.data=np.array(data)
    def __add__(self, other):
       return Matrix(self.data + other.data)
    def __sub__(self,other):
       return Matrix(self.data - other.data)
    def __mul__(self, scalar):
      return Matrix(self.data*scalar)
      