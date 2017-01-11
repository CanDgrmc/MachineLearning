import numpy as np

myArray= np.array([1,10,5,4])

# print(myArray.dtype) veri tipi

str_array=myArray.astype(str)

# print(str_array)

#for i in myArray:
#    print(i*2)

#for i in str_array:
#    print(i*2)

myArray2=np.array([[1,3,5],
                   [7,9,11],
                   [2,4,6],
                   [8,10,12]])
# print (myArray2.size)
#print(myArray2.shape) #https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html
#print(myArray2.ndim)
#print (np.mean(myArray2, axis=0)) #kolonların ortalamasını alır
#print (np.mean(myArray2, axis=1)) #satırların ortalamasını alır
#print (myArray2[:2])# dizinin ilk 2 satırı myArray[0:2] aynı sonucu verir
#print (myArray2[:2,:])# dizinin ilk 2 satırı ve tüm kolonları
#print (myArray2[:2,:2])#dizinin ilk 2 satırı ve ilk 2 kolonu
#print (myArray2[0][::-1])#diziyi tersine çevir
np.savetxt('Array.csv',myArray2,delimiter=',') #dizini kaydediyoruz  -- https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
print(np.genfromtxt('Array.csv',delimiter=',')) # kayıtlı dosyadan aynı şekilde çekiyoruz çekiyoruz


