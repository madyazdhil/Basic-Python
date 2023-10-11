def vol_balok(p, l, t1):
    n = p*l*t1
    return n

def vol_tabung(r, t2):
    phi = 3.14
    z = phi * r * r * t2
    return z

def bol_kubus(s):
    m = s * s * s
    print(m)

wew = vol_tabung(7, 14)
print(wew)
vol_tabung(14, 56)

bol_kubus(4)