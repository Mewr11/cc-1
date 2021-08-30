
class Always:
    '''Objects of this class are equal to everything'''
    def __init__(self):
        pass

    def __eq__(self, other):
        return True

def equals():
    return Always()

if __name__ == '__main__':
    print('equals() == 0')
    print(equals() == 0)

    print('equals() == []')
    print(equals() == [])

    print('equals() == (lambda x: 1)')
    print(equals() == (lambda x: 1))

