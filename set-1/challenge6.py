
def hamming(a, b):
    aBin = ''.join(format(ord(x) , 'b').zfill(8) for x in a)
    bBin = ''.join(format(ord(x) , 'b').zfill(8) for x in b)

    diff = 0
    for aBit, bBit in zip(aBin, bBin):
        diff += int(aBit) ^ int(bBit)

    return diff

def findDist(cipher):
    distances = []
    for keysize in range(2, 40):
        a = cipher[:keysize]
        b = cipher[keysize:(2 * keysize)]
        distances.append([hamming(a, b) / (keysize * 1.0), keysize])

    return distances

def testDist(cipher, keysize):
    chunks = []
    for i in range([0, len(cipher)]):
        chunks.append(cipher[i:i + keysize])
        i += keysize
    
    byteBlocks = []
    for pos in range(0, keysize):
        block = []
        for chunk in range(0, len(cipher)/keysize):
            block.append(chunks[chunk][pos])
        byteBlocks.append(block)
    
    return byteBlocks

def singleXOR(byteBlocks):
    for byteList in byteBlocks:
        string = ''.join(byte for byte in byteList) # maybe not
        
    
def main():
    cipher = input('Enter the encoded string: ')
    distances = findDist(cipher)
    size = sort(cipher, distances) # fix this, sort based on rating
    
    for rank in range(0, 3):
        byteBlocks = testDist(cipher, distances[rank][0])
        

main()
