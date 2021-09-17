import math

def foil(l):
    r = 4.0
    while l > 0:
        l -= math.pi * r
        r += 0.005
    return r

if __name__ == '__main__':
    print(f'foil(0) -> {foil(0)}')
    print(f'foil(50) -> {foil(50)}')
    print(f'foil(4321) -> {foil(4321)}')
    print(f'foil(10000) -> {foil(10000)}')

