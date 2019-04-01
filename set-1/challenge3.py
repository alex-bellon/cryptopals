import codecs

a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

aBin = bin(int(a, 16))[2:]

results = list()

for char in range(0, 16):
    temp = codecs.decode(hex(int(aBin, 2) ^ char), 'hex')
    print(temp)
    results.append(temp)

print(results)
