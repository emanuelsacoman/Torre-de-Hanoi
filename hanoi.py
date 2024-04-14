def hanoi(n, ini, t, dest):
    if n == 1:
        print(f"Mover disco {n} da torre {ini} para a torre {dest}")
        return 1  # Retorna 1 passo para o movimento de um disco
    passos1 = hanoi(n - 1, ini, dest, t)  # Movendo n-1 discos para o pino temporário
    print(f"Mover disco {n} da torre {ini} para a torre {dest}")
    passos2 = hanoi(n - 1, t, ini, dest)  # Movendo n-1 discos do pino temporário para o destino
    return passos1 + passos2 + 1  # Total de passos é a soma dos passos dos dois movimentos mais o movimento do disco restante

# Leitura do número de discos nas torres
n = int(input("Digite o número de discos: "))
print("A ordem é:")
passos_totais = hanoi(n, 1, 2, 3)
print(f"Total de passos necessários: {passos_totais}")
