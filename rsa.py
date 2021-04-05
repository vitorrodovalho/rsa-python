import argparse
import math
import random
import sys

########################################################
# Trabalho Matheus Criptografia RSA
########################################################

#cria uma lista de números primos válidos
def lista_primos(n=200):
    nao_primos = set(j for i in range(2, 8) for j in range(i*2, n, i))
    primos = [x for x in range(2, n) if x not in nao_primos]
    return primos

#valida se elemento esta na lista
def e_primo(i):
    primos = lista_primos()
    return i in primos

def mdc(e, x):
    t = 0
    newt = 1
    r = x
    newr = e
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1:
        return None
    if t < 0:
        t += x
    return t

#obtem variveis passadas no argumento
parser = argparse.ArgumentParser()
parser.add_argument('mensagem', type=str, help="Mensagem inválida!")
args = parser.parse_args()

primos = lista_primos()
mensagem = ord(args.mensagem)

d = None

while d is None or encriptar < 33 or encriptar > 255:
    p = random.choice([pr for pr in primos if pr < mensagem])
    q = random.choice([pr for pr in primos if pr < mensagem and pr != p])

    #equacao n
    n = p * q
    phi = (p - 1) * (q - 1)
    dontuse = [p, q]

    #numero primo aleatorio
    e = random.choice([pr for pr in primos if pr < phi and not pr in dontuse])

    #minimo dividor comum menor que n
    d = mdc(e, phi)

    if d is None:
        print("Nenhum MDC menor que n encontrado {}.".format(e))
        #sys.exit(1)
    else:
        encriptar = (pow(mensagem, (e % n))) % n
        decriptar = (pow(encriptar, (d % n))) % n
        
        if(d is not None and encriptar >= 33 and encriptar <= 255):
            print("Algoritimo de criptografia RSA\n")
            print("p = {}".format(p))
            print("q = {}\n".format(q))
            print("n = p * q")
            print("n = {} * {}".format(p, q))
            print("n = {}\n".format(n))
            print("phi(n) = (p - 1) * (q - 1)")
            print("phi(n) = ({} - 1) * ({} - 1)".format(p, q))
            print("phi(n) = ({} * {})".format(p-1, q-1))
            print("phi(n) = {}\n".format(phi))
            print("número primo aleatório menor que phi e diferente de p e q")
            print("e = {}\n".format(e))
            print("d = mdc(e, phi(n)) = 1")
            print("d = mdc({}, {}) = 1".format(e, phi))
            print("d = {}\n".format(d))
            print("Chave Publica  = (n, e) = ({}, {})".format(n, e))
            print("Chave Privada = (n, d) = ({}, {})\n".format(n, d))
            print("mensagem = {}\n".format(mensagem))
            print("Encriptar")
            print("c = m ^ e mod (n)")
            print("c = {} ^ {} mod ({})".format(mensagem, e, n))
            print("c = {}".format(encriptar))
            print("c = {}\n".format(chr(encriptar)))
            print("Decriptar")
            print("m = c ^ d mod (n)")
            print("m = {} ^ {} mod ({})".format(encriptar, d, n))
            print("m = {}".format(decriptar))
            print("m = {}\n".format(chr(decriptar)))