a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

aBin = bin(int(a, 16))[2:]
bBin = bin(int(b, 16))[2:]

c = int(aBin, 2) ^ int(bBin, 2)

print(hex(c))
