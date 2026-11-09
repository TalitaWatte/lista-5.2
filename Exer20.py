#Verificação de Vencedor:  Imagine uma corrida com  5 ciclistas (como no exercício de lógica do seu material). 
#Use um loop para ler o tempo de cada um e identificar quem teve o menor tempo. 

menor_tempo = None
vencedor = 0

for ciclista in range(1, 6):
    tempo = float(input("Tempo do ciclista " + str(ciclista) + ": "))

    if menor_tempo == None or tempo < menor_tempo:
        menor_tempo = tempo
        vencedor = ciclista

print("O vencedor é o ciclista", vencedor, "com o tempo", menor_tempo)

