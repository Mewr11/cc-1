chd = {}
cmat = []
# m: a list of strings (each string representing a line of the 'maze'
#    the maze must be a rectangle and have at least one row
# d: +1 for rightward transversal, -1 for leftward
# r: current row
# c: current column
def coins_helper(m, d, r, c):
    global chd
    global cmat
    if m != cmat:
        chd = {}
        cmat = m
    
    if (d, r, c) in chd.keys():
        return chd[d, r, c]
    else:
        if c < 0 or r >= len(m) or c >= len(m[0]):
            chd[d, r, c] = 0
            return 0
        p = m[r][c]
        if p == '#':
            chd[d, r, c] = 0
            return 0
        else:
            n = max(coins_helper(m, d, r, c + d), coins_helper(m, -d, r + 1, c))
            if p == 'C':
                chd[d, r, c] = n + 1
                return n + 1
            else:
                chd[d, r, c] = n
                return n

def coins_mat(m):
    return coins_helper(m, 1, 0, 0)

if __name__ == '__main__':
    a = ['EECE#C']
    b = ['CCC', 'CCC']
    c = ['EEC', 'C##', 'C#C']

    for m in a, b, c:
        print('\n'.join(m))
        print(coins_mat(m))
        print()

