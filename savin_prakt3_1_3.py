# Умножение матрицы на вектор
from random import randint

# Функция вывода на печать для наглядности
def print_prod(a,b,n):
    print("Матрица A    Вектор b\n")
    for i in range(n):
            for j in range(n):
                print(a[i][j],end=" ")
            print(" | ",b[i])
            
            
    print("\nПроизведение:\n")
    for i in range(n):
        for j in range(n):
            if j<(n-1):
                print(a[i][j],"x",b[j],"+",end=" ")
            else:
                print(a[i][j],"x",b[j],end=" ")
        print()
    
    print("\nИтоговый вектор:\n")
    for i in range(n):
        s=0
        for j in range(n):
            s+=(a[i][j]*b[j])
        print(s)

    
# формирование матрицы и вектора
n=5

matr_A=[[randint(1,9) for j in range(n)] for i in range(n)] 
vect_b=[randint(1,9) for i in range(n)]

print_prod(matr_A,vect_b,n)
                  

