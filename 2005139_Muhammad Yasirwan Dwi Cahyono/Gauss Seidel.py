# Gauss Seidel

# Defini Matriks yang akan diselesaikan
f1 = lambda x, y, z: (17 - y + 2 * z) / 20
f2 = lambda x, y, z: (-18 - 3 * x + z) / 20
f3 = lambda x, y, z: (25 - 2 * x + 3 * y) / 20

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Memasukkan nilai Galat yang diinginkan
e = float(input('Enter tolerable error: '))

# Implementasi Gauss Seidel
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1))
    e1 = abs(x0 - x1);
    e2 = abs(y0 - y1);
    e3 = abs(z0 - z1);

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e

#Print Output penyelesaian
print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))