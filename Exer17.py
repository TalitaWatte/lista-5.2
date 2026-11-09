#Sistema de Ataques:  Um herói ataca um monstro  5 vezes. A cada ataque, o monstro perde 10 de vida. 
#Se a  vida_monstro  começa  em 50, use um loop para mostrar a vida diminuindo a cada golpe. 

vida_monstro = 50
for ataque in range(1, 6):
    vida_monstro = vida_monstro - 10

    print("Ataque", ataque, "- Vida do monstro:", vida_monstro)