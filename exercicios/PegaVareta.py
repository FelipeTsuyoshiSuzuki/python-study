#           ENTRADAS
# primeira entrada jogador que irá iniciar
# Numero de jogadores é três
# caso essa entrada seje -1 encerrar
# segunda entrada varios numeros que representam a vareta que é retirada
# 1 - amarela 5 pontos
# 2 - verde 10 pontos
# 3 - azul 15 pontos
# 4 - vermelha 20 pontos
# 5 - preta 50
# 0 - perdeu a vez
# -1 - fim da rodada
#           SAÍDA
# Primeira linha número da rodada
# Segunda linha pontos do ganhador ou ganhadores caso de empate
# Terceira linha ganhaor ou ganhadores
# Uma linha em branco entre cada rodada

def main():
    round = 0
    result_list = []
    while True:
        first_player = int(input())
        if first_player == -1:
            break
        else:
            round += 1
            game_score = game(first_player)
            result_list.append(format_result(game_score, round))
    for i in result_list:
        print(f"{i}\n")


def format_result(game_score, round):
    best_player_temp = max(game_score, key = lambda k: game_score[k])
    best_score = game_score[best_player_temp]
    winners_string = ""
    winners = 0
    for i in game_score:
        if game_score[i] == best_score:
            winners_string += f" Jogador{i}"
            winners += 1
    round_string = f"RODADA {round}"
    result = round_string + "\n" + points_string(best_score, winners) + "\n" + format_winners(winners_string)
    return result


def points_string(best_score, n_winners):
    if n_winners > 1:
        return f"Empate com {best_score} pontos"
    else:
        return f"Ganhador com {best_score} pontos"


def format_winners(winner_string):
    result = winner_string.strip().replace(" ", ", ").replace("or", "or ")
    return result


def game(first_player):
    game_dict = {1: 0, 2: 0, 3: 0}
    turn = first_player
    stick = input().split(" ")
    for i in stick:
        match int(i):
            case 1:
                game_dict[turn] += 5
            case 2:
                game_dict[turn] += 10
            case 3:
                game_dict[turn] += 15
            case 4:
                game_dict[turn] += 20
            case 5:
                game_dict[turn] += 50
            case 0:
                turn += 1
                if turn > 3:
                    turn = 1
            case -1:
                break
    return game_dict


if __name__ == "__main__":
    main()