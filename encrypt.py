import sys
from itertools import cycle
import base64




password = sys.argv[1]
in_file = sys.argv[2]
out_file = sys.argv[3]

f = open(in_file)
z = open (out_file, "wb")

inputString = f.read()


def encryptDecrypt(sir_input):   
  
    xoring = ''.join(chr(ord(x)^ord(y)) for (x,y) in zip (inputString, cycle(password)))        

    return base64.encodebytes(xoring.encode()).strip()



inputString = encryptDecrypt(inputString)
inputString = inputString.decode('utf-8')

z.write(inputString.encode())
f.close()
z.close()