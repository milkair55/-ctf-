import string
import hashlib
payloads = string.ascii_letters+string.digits
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'+'0123456789'
for a in payloads:
    for b in payloads:
        for c in payloads:
            s = "TASC"+a+"O3RJMV"+b+"WDJKX"+c+"ZM"
            flag = hashlib.md5(s.encode("utf8")).hexdigest()
            if flag[:5] == 'e9032':
                print(s)
                print(flag)