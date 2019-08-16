import codecs

a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

aHex = bytes.fromhex(a)

results = list()

for char in range(0, 0xff):
    result = b''
    for byte in aHex:
        result += bytes([byte ^ char])
    try:
        results.append(result.decode('utf-8'))
    except:
        pass

scores = dict()

for string in results:
    score = 0
    for char in string:
        if ord(char) > 64 and ord(char) < 91:
            score += 2
        elif ord(char) > 96 and ord(char) < 123:
            score += 5
        elif char is '\'' or char is ' ' or char is ',':
            score += 2
        else:
            score -= 1
    scores[string] = score

high = 0
word = ''

for key in scores:
    if scores[key] > high:
        word = key
        high = scores[key]

print(word)
#print(results)
