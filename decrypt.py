import sys
from itertools import cycle
import base64




password = sys.argv[2]
in_file = sys.argv[1]
out_file = sys.argv[3]

f = open(in_file,"rb")
z = open (out_file, "w+")

inputString = f.read()
inputString = base64.b64decode(inputString)
inputString = inputString.decode('utf-8')


# inputString = base64.b64decode(inputString)
#inputString = inputString.encode()

def encryptDecrypt(sir_input):   
    
    xoring = ''.join(chr(ord(x)^ord(y)) for (x,y) in zip (sir_input, cycle(password)))        

    return xoring



inputString = encryptDecrypt(inputString)
#inputString = inputString.decode('utf-8')

z.write(inputString)

f.close()
z.close()