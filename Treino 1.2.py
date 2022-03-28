# verificar se os batimentos cardíacos por minuto se encontram na faixa adequada.
# dentro da faixa adequada, acima ou abaixo.
print("Olá! Aqui vamos te ajudar a identificar se seus batimentos por minuto estão adequados à sua faixa etária.")
bpm = int(input("Informe seu número de batimentos por minuto: "))
idade = int(input("Informe a sua idade: "))

if idade <= 2 and (bpm >= 120 <= 140):
    print("Seus batimentos por minuto estão dentro da faixa adequada para sua idade.")
elif idade <= 2 and bpm < 120:
    print("Seus batimentos por minuto estão abaixo da faixa adequada para sua idade.")
elif idade <= 2 and bpm > 140:
    print("Seus batimentos por minuto estão acima da faixa adequada para sua idade.")


# de 8 até 17 anos
elif (idade >= 2 <= 18) and (bpm >= 80 <= 100):
    print("Seus batimentos por minuto estão dentro da faixa adequada para sua idade.")
elif (idade >= 2 < 18) and bpm < 80:
    print("Seus batimentos por minuto estão abaixo da faixa adequada para sua idade.")
elif (idade >= 2 < 18) and bpm > 100:
    print("Seus batimentos por minuto estão acima da faixa adequada para sua idade.")


# adulto sedentário
elif (idade >= 18 <= 60) and (bpm >= 70 <= 80):
    print("Seus batimentos por minuto estão dentro da faixa adequada para sua idade.")
elif (idade >= 18 <= 60) and bpm < 70:
    print("Seus batimentos por minuto estão abaixo da faixa adequada para sua idade.")
elif (idade >= 18 <= 60) and bpm > 80:
    print("Seus batimentos por minuto estão acima da faixa adequada para sua idade.")

# +60anos
elif idade >= 60 and (bpm >= 50 <= 60):
    print("Seus batimentos por minuto estão dentro da faixa adequada para sua idade.")
elif idade >= 60 and bpm < 50:
    print("Seus batimentos por minuto estão abaixo da faixa adequada para sua idade.")
else:
    print("Seus batimentos por minuto estão acima da faixa adequada para sua idade.")
