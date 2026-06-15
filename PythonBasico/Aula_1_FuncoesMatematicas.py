import math
#Biblioteca math contém várias funções dentro dela
print('Funções matemáticas')
n = float(input('Insira um número decimal: '))


#tem que colocar o 'math.função' porque eu importei a biblioteca math completa

#Ceil() arredonda o número para cima
print('Ceil: ',math.ceil(n),'arredonda o número para cima')
#Floor() arredonda para baixo
print('Floor: ',math.floor(n),'arredonda para baixo')
#trunc() retorna a parte inteira do número
print('Trunc: ',math.trunc(n),'retorna a parte inteira do número')
#exp() retorna o expõente do número
print('Exp: ',math.exp(n),'retorna o expõente do número')
#log() descobre o expoente que gera o número x
print('Log: ',math.log(n),'descobre o expoente que gera o número x')
#srqrt() Famosa raiz do número
print(math.sqrt(n),'Famosa raiz do número')
#pi() é o pi
print(math.pi,'pipipi')