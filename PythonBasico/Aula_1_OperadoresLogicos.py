n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira um número inteiro: '))

print('Ver a lógica agora.')
p = n1 > n2
q = n1 != n2
r = not (p or q) and (not p)
print('p =', p)
print('q =', q)
print('r =', r)