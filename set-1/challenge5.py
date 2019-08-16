plain = str(input('Plaintext: '))
key = str(input('Key: '))

length = len(plain)
keyPadded = str(key * length)[0:length]

print(keyPadded)
print(plain)

result = b''

plainBytes = plain.encode('ascii')
keyBytes = keyPadded.encode('ascii')

for p, k in zip(plainBytes, keyBytes):
    result += bytes([p ^ k])

print(result.hex())
