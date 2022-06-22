from Crypto.Cipher import ARC4 as rc4cipher
import base64


def rc4_algorithm(encrypt_or_decrypt, data):
    key1="af156arg3a"
    if encrypt_or_decrypt == "encrypt":
        key = bytes(key1, encoding='utf-8')
        enc = rc4cipher.new(key)
        res = enc.encrypt(data.encode('utf-8'))
        res=base64.b64encode(res)
        res = str(res,'utf8')
        return res
    elif encrypt_or_decrypt == "decrypt":
        data = base64.b64decode(data)
        key = bytes(key1, encoding='utf-8')
        enc = rc4cipher.new(key)
        res = enc.decrypt(data)
        res = str(res,'utf8')
        return res

def RSA(x):
    x=int(x[1:])
    e = 65537
    n = 1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413
    p = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489
    g = 36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917
    phi = (p-1) * (g-1)
    #CRT
    yp = x % p
    yg = x % g

    dp = e % (p-1)
    dg = e % (g-1)

    xp = pow(yp , dp ,p)
    xg = pow(yg , dg ,g)

    cp = pow(g , -1 ,p)
    cg = pow(p , -1 ,g)

    x = ((g*cp)*xp + (p*cg)*xg) % n

    return x 

