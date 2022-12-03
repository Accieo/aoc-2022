from dataclasses import dataclass, field

@dataclass
class Moves:
    opponent: list = field(default_factory=list)
    player: list = field(default_factory=list)

outcome_scores = {
    'Rock': { 'Rock': 3, 'Paper': 0, 'Scissors': 6 },
    'Paper': { 'Rock': 6, 'Paper': 3, 'Scissors': 0 },
    'Scissors': { 'Rock': 0, 'Paper': 6, 'Scissors': 3 },
}

move_scores = { 'Rock': 1, 'Paper': 2, 'Scissors': 3 }

translation_part_one = {
    'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
    'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors',
}

translation_part_two = {
    'Rock': { 'W': 'Scissors', 'L': 'Paper' },
    'Paper': { 'W': 'Rock', 'L': 'Scissors' },
    'Scissors': { 'W': 'Paper', 'L': 'Rock' }
}

def common():
    with open('input/day02.txt', 'r') as file:
        data = file.readlines()

    moves = Moves()
    for line in data:
        opponent_move, player_move = line.strip().split(' ')
        moves.opponent.append(opponent_move)
        moves.player.append(player_move)

    return moves

def part_one():
    moves = common()
    player_score = 0
    for move in zip(moves.opponent, moves.player):
        opponent_translated = translation_part_one[move[0]]
        player_translated = translation_part_one[move[1]]
        player_score += outcome_scores[player_translated][opponent_translated]
        player_score += move_scores[player_translated]

    return player_score

def part_two():
    moves = common()
    player_score = 0
    for move in zip(moves.opponent, moves.player):
        opponent_translated = translation_part_one[move[0]]
        player_translated = ''
        match move[1]:
            case 'X':
                player_translated = translation_part_two[opponent_translated]['W'] 
            case 'Y':
                player_translated = opponent_translated
            case 'Z':
                player_translated = translation_part_two[opponent_translated]['L']
        player_score += outcome_scores[player_translated][opponent_translated]
        player_score += move_scores[player_translated]
        
    return player_score

if __name__ == '__main__':
    print(part_one())
    print(part_two())
