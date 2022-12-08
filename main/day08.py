from math import prod

def common():
    with open('input/day08.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: list(x.strip()), data))

    return data

def part_one():
    forest = common()
    total_visible = 0
    
    cols = [col for col in zip(*forest)]
    for i in range(len(cols)):
        for j in range(len(forest)):
            left = forest[i][0:j]
            right = forest[i][j+1:len(forest[i])]
            up = cols[j][0:i]
            down = cols[j][i+1:len(cols[i])]

            if all(x < forest[i][j] for x in left) or all(x < forest[i][j] for x in right):
                total_visible += 1
            elif all(x < forest[i][j] for x in up) or all(x < forest[i][j] for x in down):
                total_visible += 1

    return total_visible

def part_two():
    forest = common()
    cols = [col for col in zip(*forest)]
    scenic_scores = list()
    for i, _ in enumerate(cols):
        for j, _ in enumerate(forest):
            left = forest[i][0:j]
            right = forest[i][j+1:len(forest[i])]
            up = cols[j][0:i]
            down = cols[j][i+1:len(cols[i])]

            count = 0
            scores = list()
            current_tree = forest[i][j]
            for direction in [reversed(up), reversed(left), right, down]:
                for tree in direction:
                    if current_tree > tree:
                        count += 1
                    elif tree >= current_tree:
                        count += 1
                        break
                    else:
                        break
                scores.append(count)
                count = 0

            scenic_scores.append(scores)
            
    max_scenic_score = max(list(map(lambda x: prod(x), scenic_scores)))

    return max_scenic_score

if __name__ == '__main__':
    print(part_one())
    print(part_two())
