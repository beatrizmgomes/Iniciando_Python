#todos os que obtiverem a nota maior do que 8,5 na sua prova semestral serão convidados para uma visita de campo
# na América do Sul
#solicitar e-mail e a nota do aluno, exibindo a mensagem "ENVIANDO CONVITE" casp a nota satisfaça a condição.

nota = input("Digite sua nota: ")
email = input("Digite seu e-mail: ")
if float (nota) >= 8.5:
    print("Enviando convite para o e-mail {}".format(email))
else:
    print("Infelizmente sua nota não atingiu o valor mínimo para obter o convite.")