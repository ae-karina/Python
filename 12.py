import hashlib
import string

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

for i in string.ascii_uppercase:
    for j in string.ascii_uppercase:
        for k in string.ascii_uppercase:
            c = 'TASC' + i + 'O3RJMV' + j + 'WDJKX' + k + 'ZM'
            x = md5(c).upper()
            if 'E903' in x and '4DAB' in x and '08' in x and '51' in x and '80' in x and '8A' in x:
                print(c)
                print(x)
                break
