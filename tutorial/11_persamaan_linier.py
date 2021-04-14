import numpy as np

A = np.array([(2,3), (1,2)])
Y = np.array([23,14])

print (A)
print (Y)

#menyelesaikan persamaan linier
A_inv = np.linalg.inv(A)

X1 = np.dot(A_inv, Y)
print(X1)

#cara lain 
X2 = np.linalg.solve(A,Y)
print(X2)
