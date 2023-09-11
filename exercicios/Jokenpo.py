p1 = input().upper().strip()
p2 = input().upper().strip()

if p1 == p2:
    print("Empate")

if p1 == "PEDRA" and p2 == "TESOURA":
    print("Jogador 1")
elif p1 == "PAPEL" and p2 == "PEDRA":
    print("Jogador 1")
elif p1 == "TESOURA" and p2 == "PAPEL":
    print("Jogador 1")
elif p1 == "PEDRA" and p2 == "PAPEL":
    print("Jogador 2")
elif p1 == "PAPEL" and p2 == "TESOURA":
    print("Jogador 2")
elif p1 == "TESOURA" and p2 == "PEDRA":
    print("Jogador 2")