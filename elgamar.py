import math


def modInverse(b,m):
    g = math.gcd(b, m)
    if (g != 1):
        return -1
    else:
        return pow(b, m - 2, m)
    
def modDivide(a,b,m):
    a = a % m
    inv = modInverse(b,m)
    if(inv == -1):
        raise Exception("division not defined")
    else:
        return (inv*a) % m


def get_n_in_mod_range(n, p):
    if 0 < n < p:
        return n
    elif n > p:
        return n - (n // p) * p
    elif n < 0:
        return n - (n // p) * p
    else:
        return 0
        
def bruteforce_mod(q, d, p):
    x = 0 
    while (d * x - q) % p != 0:
        x += 1
    return x

def ecc_multiplication(x1,y1,k,p, minus=False):
    
    _lambda = modDivide(3 * x1 ** 2 + k, y1 * 2, p) 
    ecc_x3 = (_lambda ** 2 - 2 * x1) 
    ecc_y3 = (_lambda * (x1 - ecc_x3) - y1) 
    
    if minus:
        return (get_n_in_mod_range(ecc_x3, p), get_n_in_mod_range(-ecc_y3, p))
    else:
        
        return (get_n_in_mod_range(ecc_x3, p), get_n_in_mod_range(ecc_y3, p))
    
    
def ecc_addition(x1,x2,y1,y2,p):
    try:
        ecc_lambda = (y2 - y1) / (x2 - x1)
    except Exception:
        ecc_lambda = 0
    
    ecc_x3 = get_n_in_mod_range(ecc_lambda ** 2 - x1 - x2, p)
    ecc_y3 = get_n_in_mod_range(ecc_lambda * (x1 - ecc_x3) - y1, p)
    return (ecc_x3, ecc_y3)


def main(p, b, a, G, M , eq, k):
    init = f"""
    Die Primzahl (p) lautet: {p}
    Die zu verschlüsselnde Nachricht (M) lautet: {M}
    Die Zufallszahl (a) lautet: {a}
    Der geheime Schlüssel (b) lautet: {b}
    """
    print(init)

    # public key
    x1, y1 = G[0], G[1]
    Y = ecc_multiplication(x1, y1, k, p)
    print(f"\n1. Schritt\n Der public Key (p,G,Y) lautet: {p}, {G}, {Y}")


    # ENCRYPTION
    # calculating R
    R = ecc_multiplication(x1, y1, k, p)
    print("\n2. Schritt\n Wir berechnen R = a * G \n \
        R = ", R)

    # intermediate step for calculating S = M + a * Y -> a * Y
    x1, y1 = Y[0], Y[1]
    aY = ecc_multiplication(x1, y1, k, p)
    print(f"\n3. Schritt\n Wir berechnen S = M + a * Y\n\t3.1 Schritt\n\t Wir berechnen a * Y mithilfe der Multiplikation \n\t a * Y = {aY}")

    # addition for M + (a * Y) to finally get S
    x1, y1 = M[0], M[1]
    x2, y2 = aY[0], aY[1]
    S = ecc_addition(x1, x2, y1, y2, p)
    print(f"\t3.2 Schritt\n\t Wir berechnen M + aY mithilfe der Addition \n\t M + aY = {M} + {aY} = {S}\n\t S = {S}")


    # DECRYPTION  
    # calculation to get Z
    x1, y1 = R[0], R[1]
    Z = ecc_multiplication(x1, y1, k, p, True)     
    print(f"\nEntschlüsseln\n-------------------\n1. Schritt\n Wir berechnen das Z mithilfe von\n Z = -b * R = -{b} * {R} = -{Z}")

    # calculation to get the decrypted message
    x1, y1 = Z[0], Z[1]
    x2, y2 = S[0], S[1]
    m = ecc_addition(x1, x2, y1, y2, p)
    print(f"\n2. Schritt\n Wir berechnen das M mithilfe von Z + S \n Fertig! Die entschlüsselte Nachricht lautet: {M}")

    # check if the decrypted message is the same as the plain message
    if M == m:
        print(f"EQUAL: {m} == {M}")
    else:
        print(f"ERROR! not the same {m} != {M}")


# Übungbeispiel 1
main(5,2,2,(1,1),(2,2),"",-4) 

# Übungsbeispiel 2
#main(11,2,2,(8, 3),(3,1),"",-3)

# Folienbeispiel 
#main(7,2,2,(5,2),(4,2),"",2)

# Hausübung
#main(7,2,2,(5,3),(2,1),"",-1)