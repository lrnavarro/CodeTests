import base64

print("Enter hexadecimal string to translate to Base64")
hex = input()
bytes = bytearray.fromhex(hex)
encoded = base64.encodebytes(bytes).decode()
print("Base64 translation is " + (encoded))
