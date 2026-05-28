#inicialização de variáveis
nota1 = 8.5
nota2 = 9
nota3 = 4
nota4 = 1
qdeDeNotas = 4
mediaParaAprovacao = 6

#operações com variáveis
media = (nota1+nota2+nota3+nota4)/qdeDeNotas
status = media >= mediaParaAprovacao

#saída de dados
#imprimir conteúdo de variáveis
print(media)
print(status)

#imprimir mensagens personalizadas
print("Uma mensagem personalizada")

#imprimir uma mensagem personalizada com variáveis dentro dela usando f-string
print(f"a média do aluno é {media} e o status de aprovação é {status}")

#entrada de dados
umaVariavel = input("Digite um numero ")

#casting
outraVariavel = int(input("Digite um numero "))
