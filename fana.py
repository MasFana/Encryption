from genericpath import isdir
import os
    
filename = ".fana"
teks = "aku fana kamu fana kita semua fana aowijfopiwjaoitjowijtw 412987421398569819461829794806958709568=9-06=-908][][p][][.],[.],[].vsjhbdfiuwy59823"

def xor_encrypt_decrypt(data, key):
    extended_key = (key * (len(data) // len(key))) + key[:len(data) % len(key)]
    result = bytearray()
    for d_byte, k_byte in zip(data, extended_key.encode()):
        xor_byte = d_byte ^ k_byte
        result.append(xor_byte)
    return bytes(result)

def enc(key,file):
    try:
        with open(file, 'rb') as f:
            data = f.read()
            encrypted_data = xor_encrypt_decrypt(data, key) 
            with open(file, 'wb') as f:
                f.write(encrypted_data) 
    except:
        pass 
    
def delete():
    os.remove(filename)
    
def decrypt(key):
    for file in os.listdir():
        if "fana." in file:
            continue
        enc(key,file)
        print(f"+ {file} ")
        
    input("\nDecryption complete...")
    
def encrypt(key):
    for file in os.listdir():
        if 'fana.' in file:
            continue
        enc(key,file)
        print(f"- {file} ")
        
    with open(filename, 'wb') as f:
        f.write(xor_encrypt_decrypt(teks.encode(), key))
    input("\nEncryption complete...")

def enwkey(key):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
            test= xor_encrypt_decrypt(data, key).decode()
            isEncrypt = test == teks  
        if isEncrypt:
            print("> Verification successful. Running decryption...\n")
            delete()
            decrypt(key)
            return
        else:
            input("\nDecryption failed...")
            return
    except FileNotFoundError:
        print("> Encryption started...\n")
        encrypt(key)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    teksmenu = r"""
  _____                   _____                             _   
 |  ___|_ _ _ __   __ _  | ____|_ __   ___ _ __ _   _ _ __ | |_ 
 | |_ / _` | '_ \ / _` | |  _| | '_ \ / __| '__| | | | '_ \| __|
 |  _| (_| | | | | (_| | | |___| | | | (__| |  | |_| | |_) | |_ 
 |_|  \__,_|_| |_|\__,_| |_____|_| |_|\___|_|   \__, | .__/ \__|
                                                |___/|_|                                   
"""
    print(teksmenu)
    print("o Current Directory: ", os.getcwd())
    key = input("o Key: ")
    enwkey(key)
    
main()
