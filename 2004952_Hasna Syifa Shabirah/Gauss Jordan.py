from numpy import*
#~~~~~~inisialisasi matrik augment~~~~~#
A = array([[1.,1.,0.,3.,4],
           [2.,1.,-1.,1.,1],
           [3.,-1.,-1.,2.,-3],
           [-1.,2.,3.,-1,4]])
print ("Matriks A=",A)
#===== METODE ELIMINASI GAUSS =========#
n=len(A)
#~~~~~~proses triangularisasi~~~~~~~~~~#
for k in range(0,n-1):
    for i in range(k+1,n):
        m=A[i][k]/A[k][k]
        for j in range(0,n+1):
            A[i][j]=A[i][j]-m*A[k][j]
#~~~~~~proses substitusi-mundur~~~~~~~~#
X = zeros((n,1))
X[n-1][0]=A[n-1][n]/A[n-1][n-1]
for j in range(n-2,-1,-1):
    S=0
    for i in range(j+1,n):
        S=S+A[j][i]*X[i][0]
        X[j][0]=(A[j][n]-S)/A[j][j]
#======================================#
print ("X=",X)