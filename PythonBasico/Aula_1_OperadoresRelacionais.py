print('Operadores Relacionais Lógicos')
print('Insira dois números para comparar')
n1 = input('N1: ')
n2 = input('N2: ')

resultadoEquiv = n1 == n2
resultadoMaior = n1 > n2
resultadoMenor = n1 < n2
resultadoMaiorIgual = n1 >= n2
resultadoMenorIgual = n1 <= n2
resultadoDiferente = n1 != n2

print(f'N1 {n1} é (==) equivalente a N2 {n2}: {resultadoEquiv}')
print(f'N1 {n1} é (>) maior que o N2 {n2}: {resultadoMaior}')
print(f'N1 {n1} é (<) menor que o N2 {n2}: {resultadoMenor}')
print(f'N1 {n1} é (>=) maior ou igual o N2 {n2}: {resultadoMaiorIgual}')
print(f'N1 {n1} é (<=) menor ou igual o N2 {n2}: {resultadoMenorIgual}')
print(f'N1 {n1} é (!=) Diferente do N2 {n2}: {resultadoDiferente}')