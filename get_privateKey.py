from Crypto.Util.number import inverse

'''
This CTf needs u to get the private key from the public key and the ciphertext.
The public key is given as N and e, where e is 65537.  
But the N in this case is easily factored into the two primes p and q. 
p=2
q=N/2

'''

''''
in decrypt.py u have better functions ready to be used
'''
e = 65537
N= 19407625070992492845029991036798862570057493998500944732076633947006273975958317240850396612899614594972882372056927842129312105989371833251520545356884914

p=int(2)
q = int(N // 2)
print("p: ",p,"\nq: " , int(q),)

d = inverse(e, (p-1)*(q-1))   # the private key
print("private key: ", d)