#O Loop de Confirmação: Use um while para pedir ao usuário que digite "S" para continuar. 
# O programa deve repetir a pergunta enquanto ele digitar qualquer outra coisa.

resposta = ""
while resposta != "S":
    resposta = input("Digite S para continuar: ")
    
print("Você continuou!")
