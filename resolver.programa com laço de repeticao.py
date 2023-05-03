'''fzr um programa que solicite 2 valores inteiros positivos e imprima a soma de todos os 
inteiros entre esses valores, incluindo eles.
y>x'''

x=int(input("informe o primeiro valor:"))
y=int(input("informe o segundo valor:"))
 
if y>x:
    n= y-x +1
    soma= (y+x)*n/2
    i=x
    while i<=y:
        print(f"a soma entre o primeiro valor {x} e o segundo valor {y} é {soma}")
        i+=1
else:
    print("informe valores inteiros e positivos")







'''x = int(input("informe o primeiro valor:"))
y = int(input("informe o segundo valor:"))

if y > x:
    n = y - x + 1
    soma = (x + y) * n / 2
    i = x
    while i <= y:
        print(i)
        i += 1
    print(f"A soma dos valores entre {x} e {y} é {soma}")
else:
    print("Valores inválidos")'''
