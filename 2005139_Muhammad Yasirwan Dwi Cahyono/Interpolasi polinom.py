import numpy as np
import matplotlib.pyplot as plt


def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])  # membuat matrik 0 ber ordo n x n
    coef[:, 0] = y  # menyimpan Y pada matriks coef pada kolom pada indeks ke-0

    print(coef)
    """
    for (i=1; i<n; i++){
        ...
    }

    """
    for j in range(1, n):

        print("ini iterasi j ke-", j)

        for i in range(0, n - j):
            print("ini iterasi i ke-", i)

            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

            print(coef)

    return coef  # nilai dari Selisih terbagi


def newton_poly(coef, x_data, x_input):
    n = len(x_data) - 1
    p = coef[n]

    for k in range(1, n + 1):
        p = coef[n - k] + (x_input - x_data[n - k]) * p  # p(x) = a0 + a1(x-x0)+ a2(x-x0)(x-x1)+...

    return p

x = np.array([4,6,7])
y = np.array([2,4,5])

# get the divided difference coef
masukan = float(input("Masukan Nilai: "))
a_s = divided_diff(x, y)[0,:]

print(a_s)

# evaluate on new data points
# x_new = np.arange(0, 10, 1)

# print(x_new)

# y_new = newton_poly(a_s, x, x_new)
y_new = newton_poly(a_s, x, masukan)

print(y_new)



plt.figure(figsize = (7, 4)) #untuk bikin background grafiknya
plt.plot(x, y,'o')
plt.plot(x, y)
# plt.plot(x_new, y_new)