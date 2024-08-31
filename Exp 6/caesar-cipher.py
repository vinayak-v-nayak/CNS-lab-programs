def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))

    encrypted_text = caesar_encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")
