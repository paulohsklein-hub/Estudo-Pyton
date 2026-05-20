a = float(input('altura='))
b = float(input('base='))
c = a * b
t = c / 4
print(f'Area total:{c} quantidade de tinta:{t}')
pt = t * 4
dc = pt * 0.05
vf= pt - dc
print( f'valor das tintas;{pt} com 5% de desconto fica:{vf}')
