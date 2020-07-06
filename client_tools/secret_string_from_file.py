from Cryptodome.PublicKey import RSA

secret = open('private.pem', 'rb')
secret_key = RSA.importKey(secret.read())
print(secret_key.export_key())

