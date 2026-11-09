#. Barra de Carregamento: Simule uma barra de carregamento que imprima
#"Carregando... 10%", "Carregando... 20%" até "100%", aumentando de 10 em 10.

for porcentagem in range(10, 101, 10):
    print("Carregando...", str(porcentagem) + "%")