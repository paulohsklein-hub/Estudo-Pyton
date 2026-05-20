n = input('Valor=')
n2 =input('Valor=')
try:
    n1r = float(n)
    n2r = float(n2)
    nr3 = n1r+n2r
    print(f'Seu resultado é: {nr3}')
except ValueError:
    print("Digite apenas numeros!")







