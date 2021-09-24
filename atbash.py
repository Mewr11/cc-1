def chr_atbash(c):
    i = ord(c)
    if i >= 97 and i <= 122:
        return chr(219 - i)
    elif i >= 65 and i <= 90:
        return chr(155 - i)
    else:
        return c

def atbash(s):
    return ''.join(map(chr_atbash, s))

if __name__ == '__main__':
    print(f'atbash("apple") -> "{atbash("apple")}"')
    print(f'atbash("Hello world!") -> "{atbash("Hello world!")}"')

