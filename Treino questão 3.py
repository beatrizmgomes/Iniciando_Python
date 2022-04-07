# Votação console. 5 membros
# O usuário deve digitar o voto de cada membro da equipe e, ao final, exibir o console escolhido E qt votos.
m1 = str(input("Primeiro voto: [1] PLAYSTATION; [2] XBOX; [3] NINTENDO."))
m2 = str(input("Segundo voto: [1] PLAYSTATION; [2] XBOX; [3] NINTENDO."))
m3 = str(input("Terceiro voto: [1] PLAYSTATION; [2] XBOX; [3] NINTENDO."))
m4 = str(input("Quarto voto: [1] PLAYSTATION; [2] XBOX; [3] NINTENDO."))
m5 = str(input("Quinto voto: [1] PLAYSTATION; [2] XBOX; [3] NINTENDO."))

c1 = [m1, m2, m3, m4, m5].count('1')
c2 = [m1, m2, m3, m4, m5].count('2')
c3 = [m1, m2, m3, m4, m5].count('3')

if (c1 > c2) and (c1 > c3):
    print("Playstation ganhou!")
elif (c2 > c1) and (c2 > c3):
    print("XBOX ganhou!")
else:
    print("Nintendo ganhou!")

# falta exibir a quantidade de votos







