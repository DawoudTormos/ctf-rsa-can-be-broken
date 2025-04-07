from Crypto.Util.number import bytes_to_long, inverse

flag = "picoCTF{tw0_1$_pr!m3625a858b}"
N = 19407625070992492845029991036798862570057493998500944732076633947006273975958317240850396612899614594972882372056927842129312105989371833251520545356884914
e = 65537


def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

print(encrypt([N,e], flag))