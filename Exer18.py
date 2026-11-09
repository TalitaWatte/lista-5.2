#Crie um loop  while  que permita  ao jogador adicionar itens a uma lista de inventário até que ele digite "sair". 

inventario = []
item = ""
while item != "sair":
    item = input("Digite um item (ou 'sair'): ")
    
    if item != "sair":
        inventario.append(item)
print("Inventário:", inventario)