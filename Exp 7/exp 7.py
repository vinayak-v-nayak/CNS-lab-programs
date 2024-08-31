from math import gcd

def RSA(p: int, q: int):
    # calculating n
    n = p * q

    # calculating totient, t
    t = (p - 1) * (q - 1)

    # selecting public key, e
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break
    
    # selecting private key, d
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

    # getting message from user
    message = input("Enter the message to encrypt: ")

    # Check if the message is numeric or a string
    if message.isdigit():
        # Process as a number
        message = int(message)
        encrypted_message = (message ** e) % n
        decrypted_message = (encrypted_message ** d) % n
        print(f"Encrypted message is {encrypted_message}")
        print(f"Decrypted message is {decrypted_message}")
    else:
        # Process as a string
        # Convert the message to its ASCII values
        ascii_message = [ord(char) for char in message]

        # Encrypt each ASCII value
        encrypted_message = [(char ** e) % n for char in ascii_message]
        print(f"Encrypted message is {encrypted_message}")

        # Decrypt each ASCII value
        decrypted_message = ''.join([chr((char ** d) % n) for char in encrypted_message])
        print(f"Decrypted message is {decrypted_message}")

# Testcase - 1
print("Testcase - 1")
RSA(p=53, q=59)

# Testcase - 2
print("Testcase - 2")
RSA(p=3, q=7)
