#Campeonato para alunos da FIAP onde só podem ser inscritos alunos maiores de idade.

rm = input("Olá! Por favor, digite seu RM: ")
idade = input("Beleza! Agora digite sua idade: ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas ao seu e-mail cadastrado!")
    #até aqui seria apenas o if condicional simples. Com o "else" logo abaixo se torna condicional composto.
    #sem o "else" não apareceria nenhuma mensagem em caso do aluno ser menor de idade.
else:
    print("Poxa... Você ainda não tem idade o suficiente para participar.")
