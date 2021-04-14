import numpy as np

a = np.array([1,2,3,4,5])
b = [1,2,3,4,5]

#perbedaan array dan list(dalam python)
a = a + 1
b = b + [1]

#membuat vektor
c = np.array([1,2,3,4,5])
d = np.array([1.5 , 2.5 , 4,5 ,6])

#membuat vector dengan range
e = np.arange(1, 10, 0.5)

#membuat linspace
f = np.linspace(1,10,4)

#array multidimensi / matrix
g = np.array([ (1,2,3), (4,5,6) ])

#matriks dengan nilai nol
h = np.zeros((5,5))

#matriks dengan nilai 1
i = np.ones((5,5))

#matriks identitas
j1 = np.identity(5)
j2 = np.eye(5)

print (j1)