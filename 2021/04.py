with open('input04', 'r', encoding='utf-8') as f:
    xs = f.read().strip().split('\n\n')
    nums = [int(x) for x in xs[0].split(',')]
    boards, markeds = [], []
    for b in xs[1:]:
        boards.append(list(map(lambda x: [int(n) for n in x.split()], b.split('\n'))))
        markeds.append(list(map(lambda x: [False for n in x.split()], b.split('\n'))))

def bingo(board, marked):
    _sum, _bingo = 0, False
    for i,row in enumerate(board):
        m_row = marked[i]
        _sum += sum([x for _i,x in enumerate(row) if not m_row[_i]])
        if all(m_row):
            _bingo = True
    for i,col in enumerate(board):
        m_col = [marked[j][i] for j in range(len(col))]
        if all(m_col):
            _bingo = True
    return _sum if _bingo else -1

def mark(board, marked, num):
    for i,row in enumerate(board):
        if num in row:
            j = row.index(num)
            marked[i][j] = True
            break
    return marked

def game(nums, boards, markeds, first_win=True):
    wins = [False] * len(boards)
    for num in nums:
        for i,board in enumerate(boards):
            markeds[i] = mark(board, markeds[i], num)
            _sum = bingo(board, markeds[i])
            if _sum != -1:
                wins[i] = True
                if first_win and any(wins):
                    return num * _sum
                if all(wins):
                    return num * _sum

print(f'part1: {game(nums, boards, markeds, first_win=True)}')

print(f'part2: {game(nums, boards, markeds, first_win=False)}')
