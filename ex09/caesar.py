import sys

def caesar():
    if ( len(sys.argv) == 4 ):
        mode, line, shift = sys.argv[1], sys.argv[2], int(sys.argv[3]) % 26
        if (mode == "decode" ):
            shift = -shift
        result = ""
        for i in range(len(line)):
            if ( (ord(line[i]) >= 65 and ord(line[i]) <= 90) ):
                result += chr( ( ord(line[i]) - 65 + shift) % 26 + 65)
            elif (ord(line[i]) >= 97 and ord(line[i]) <= 122):
                result += chr( ( ord(line[i]) - 97 + shift) % 26 + 97)
            elif ( ord(line[i]) >= 0 and ord(line[i]) <= 127):
                result += chr(ord(line[i]))
            else:
                result = "The script does not support your language yet."
                break
        print(result)


    else:
        raise ValueError("Wrong number of arguments")
if __name__ == '__main__':
    caesar()