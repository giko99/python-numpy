import numpy as np

a = np. arange(10)**2

print(a)

# mengambil nilai 
print ('elemen ke 1 dari a adalah', a[0])
print ('elemen ke 8 dari a adalah', a[7])
print ('elemen ke akhir dari a adalah', a[-1])

# slicing 
print ('elemen dari 1-6 adalah',a[0:6])#[start,end]
print ('elemen dari 4 sampai akhir adalah',a[3:])
print ('elemen dari awal sampai 5 adalah',a[:5])


#iterasi

for i in a:
    print('value=',i)