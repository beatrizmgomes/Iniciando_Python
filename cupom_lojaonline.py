#FIAP wear disponibilizou um cupom no mês do seu aniversário, NIVER10, que concede 10% OFF no valor total da compra.
#Caso digite o cupom corretamente, deverá ser informado do valor da compra com o desconto.
#Mas caso digite errado, deverá também ser informado do valor total sem o desconto.

valor_compra = input("Qual o valor total da sua compra? ")
cupom = input("Digite o cupom de desconto: ")
# upper() é usado para que determinada string seja convertida para caracteres maiúsculos
if cupom.upper() == "NIVER10":
    #cálculo de 10% de desconto.
    valor_final = float(valor_compra) * 0.9
    print("Uhul! Você ganhou 10% de desconto em sua compra! Total a pagar:{:.2f}".format(valor_final))
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")

    print("Cupom inválido. Valor final: {}".format(valor_compra))

