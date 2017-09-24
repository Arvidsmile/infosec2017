def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b / a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print "no modular inverse"
    else:
        return x % m

print modinv(int(raw_input("Number1: ")), int(raw_input("Number2: ")))