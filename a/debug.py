from fileinput import filename


def encrypt(data, key):
    extended_key = (key * (len(data) // len(key))) + key[:len(data) % len(key)]
    result = bytearray()
    for d_byte, k_byte in zip(data, extended_key.encode()):
        xor_byte = d_byte ^ k_byte
        result.append(xor_byte)
    return bytes(result)


class Test:
    filename = ".fana"
    teks = "aku fana kamu fana kita semua fana aowijfopiwjaoitjowijtw 412987421398569819461829794806958709568=9-06=-908][][p][][.],[.],[].vsjhbdfiuwy59823"
    def decode(key):
        with open(Test.filename, 'rb') as f:
            data = f.read()
            return encrypt(data, key).decode()
    def encode( key):
        with open(Test.filename, 'wb') as f:
            f.write(encrypt(Test.teks.encode(), key))
            
# Test.encode("key")
print(Test.decode("key"))