bva = []
def visualizeBinaryPattern(text):
    for c in text:
        bv = bin(ord(c))[2:]
        bva.append(bv)
    for s in bva:
        print(s)

def main():
    print('Sample Text: "Hello this text will become binary"')
    print('--- Sample Text Converted to binary ⬇️ ---')
    print('==============================')
    visualizeBinaryPattern("Hello this text will become binary");

if __name__ == '__main__':
    main();