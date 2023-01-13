import numpy as np

# n = int(input("Masukan banyak titik (x,y):"))


# x = np.zeros((n))
# y = np.zeros((n))

# print('masukan nilai x dan y ')
# for i in range(n):
#     x[i] = float(input( 'x['+str(i)+']='))
#     y[i] = float(input( 'y['+str(i)+']='))

x = [4, 5, 6]
y = [2, 3, 4]

n = len(x)

xp = float(input('Masukan nilai Interpolasi: '))

yp = 0

for i in range(n):

    p = 1

    for j in range(n):
        if i != j:
            p = p * (xp - x[j]) / (x[i] - x[j])
            print(p)

    yp = yp + p * y[i]

# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xp, yp))