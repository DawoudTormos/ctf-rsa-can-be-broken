from Crypto.Util.number import long_to_bytes,bytes_to_long
from time import sleep


N = 24695962559492772392173955004148011564966953285674042322650180013677376451019230458925648944755892992729220383218061425839604135134715691854099635304467494
remainder = 19842722240978446808319190740748647757528465076516068629292305792545387596848271654857191730107075299885703231034311519512269804062473525709456619784264257
x=0

m="hello"
print(long_to_bytes(bytes_to_long(m.encode('utf-8'))).decode('utf-8'))

while True:

    remainder += N
    x+=1
    print(x)

    original_bytes = long_to_bytes(remainder)
    #original_string=""
    try:
        original_string = long_to_bytes(pow(remainder, (1/65537))).decode('utf-8')
        print(original_string)
        #break
    except UnicodeDecodeError:
        continue

    print(original_string)
    #sleep(0.01)
    

