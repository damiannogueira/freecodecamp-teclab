import random

def player(prev_play, opponent_history=[]):
    if prev_play == "":
        return random.choice(["R", "P", "S"])  # Elige aleatoriamente si no hay jugada previa
    
    # Estrategia simple: contrarrestar la última jugada del oponente
    if prev_play == "R":
        return "P"  # Papel gana a Piedra
    elif prev_play == "P":
        return "S"  # Tijeras ganan a Papel
    else:
        return "R"  # Piedra gana a Tijeras

