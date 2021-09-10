
def doesBrickFit(x, y, z, w, h):
    d1, d2, d3 = sorted((x, y, z))
    a, b = sorted((w, h))

    return d1 <= a and d2 <= b

if __name__ == '__main__':
    print(f'(1 x 1 x 1) into (1 x 1): {doesBrickFit(1, 1, 1, 1, 1)}')
    print(f'(1 x 2 x 1) into (1 x 1): {doesBrickFit(1, 2, 1, 1, 1)}')
    print(f'(1 x 2 x 2) into (1 x 1): {doesBrickFit(1, 2, 2, 1, 1)}')

