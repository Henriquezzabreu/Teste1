x=int(input("digite um numero"))
y=int(input("digite outro numero"))
soma= x + y
subtração= x - y
multiplicação= x * y
divisão= x / y
escolha=int(input('escolha uma dessas funções: soma[1],subtração[2],multiplicação[3],divisão[4]'))
if escolha==1:
   print(soma)
elif escolha==2:
   print(subtração)
elif escolha==3:
   print(multiplicação)
elif escolha==4:
   print(divisão)
else:
   print('erro')