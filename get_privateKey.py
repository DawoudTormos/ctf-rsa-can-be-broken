from Crypto.Util.number import bytes_to_long, inverse

'''
This CTf needs u to get the private key from the public key and the ciphertext.
The public key is given as N and e, where e is 65537.  
But the N is easily factored into the two primes p and q. 
p=2
q=N/2

'''
e = 65537

p=int(2)
q = int(25710065706467575023556628726079138985425832252384427013765989204070117698684094887039084407161180024456250870889233351125421235695621138875015624306863942 / 2)
print("p: ",p,"\nq: " , int(q),)

d = inverse(e, (p-1)*(q-1))   # the private key
print("private key: ", d)