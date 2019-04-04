import codecs

strings = open('files/4.txt', 'r').readlines()
decoded = list()

for a in strings:
    aHex = bytes.fromhex(a)

    results = list()

    for char in range(0, 0xff):
        result = b''
        for byte in aHex:
            result += bytes([byte ^ char])
        try:
            results.append(result.decode('ascii'))
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
        scores[string] = score

    high = 0
    word = ''

    for key in scores:
        if scores[key] >= high:
            word = key
            high = scores[key]

    decoded.append(word)


for string in decoded:
    score = 0
    for char in string:
        if ord(char) > 64 and ord(char) < 91:
            score += 2
        elif ord(char) > 96 and ord(char) < 123:
            score += 5
        elif char is '\'' or char is ' ' or char is ',':
            score += 2
    scores[string] = score

high = 0
word = ''

for key in scores:
    if scores[key] >= high:
        word = key
        high = scores[key]

print(word)
