from Cryptodome.PublicKey import RSA

def main():
    f1 = open("./receiver.pem", "rb")
    public_key = RSA.importKey(f1.read())
    key_bytes = public_key.export_key().hex()
    print(key_bytes)

main()
