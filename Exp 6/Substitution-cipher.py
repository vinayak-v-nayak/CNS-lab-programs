import string

def generate_substitution_key():
    letters = list(string.ascii_uppercase)
    shuffled_letters = letters[:]
    random.shuffle(shuffled_letters)
    return dict(zip(letters, shuffled_letters))

def substitution_encrypt(text, key):
    result = ""
    for char in text.upper():
        if char in key:
            result += key[char]
        else:
            result += char
    return result

def substitution_decrypt(text, key):
    reversed_key = {v: k for k, v in key.items()}
    result = ""
    for char in text.upper():
        if char in reversed_key:
            result += reversed_key[char]
        else:
            result += char
    return result

if __name__ == "__main__":
    import random
    text = input("Enter text to encrypt: ")

    key = generate_substitution_key()
    print(f"Generated substitution key: {key}")

    encrypted_text = substitution_encrypt(text, key)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = substitution_decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")
