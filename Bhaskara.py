import math
#Cálculo fórmula de Bhaskara
# Ax²+ Bx + C = 0
# delta --> B² - 4.A.C (caso delta seja positivo, existem dois valores para ele. Caso seja zero, apenas um.)
# caso seja negativo, informamos que não há valor real para x.

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))
delta = b * b - 4 * a * c
print(delta)
# verificação das condições com elif
if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: {} e x2 = {}".format(a,b,c,x1,x2))
elif delta == 0.0:
    x = (-b + mathsqrt(delta)) / (2*a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}".format(a,b,c,x))
else:
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a,b,c))
