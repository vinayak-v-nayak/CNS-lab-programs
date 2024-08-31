import numpy as np

def matrix_mod_mult(A, B, mod):
    return np.dot(A, B) % mod

def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    )
    return matrix_mod_inv % mod

def text_to_vector(text):
    return [ord(char) - ord('A') for char in text]

def vector_to_text(vector):
    return ''.join(chr(num + ord('A')) for num in vector)

def pad_plaintext(plain_text, block_size):
    padding = (block_size - len(plain_text) % block_size) % block_size
    return plain_text + 'X' * padding

def unpad_plaintext(padded_text):
    return padded_text.rstrip('X')

def encrypt(plain_text, key_matrix):
    n = key_matrix.shape[0]
    padded_text = pad_plaintext(plain_text.upper().replace(' ', ''), n)
    cipher_text = ''
    for i in range(0, len(padded_text), n):
        block = text_to_vector(padded_text[i:i+n])
        block_vector = np.array(block).reshape(n, 1)
        cipher_vector = matrix_mod_mult(key_matrix, block_vector, 26).flatten()
        cipher_text += vector_to_text(cipher_vector)
    return cipher_text

def decrypt(cipher_text, key_matrix):
    n = key_matrix.shape[0]
    inverse_key_matrix = matrix_mod_inverse(key_matrix, 26)
    plain_text = ''
    for i in range(0, len(cipher_text), n):
        block = text_to_vector(cipher_text[i:i+n])
        block_vector = np.array(block).reshape(n, 1)
        plain_vector = matrix_mod_mult(inverse_key_matrix, block_vector, 26).flatten()
        plain_text += vector_to_text(plain_vector)
    return unpad_plaintext(plain_text)

if __name__ == "__main__":
    # Example key matrix (3x3)
    key_matrix = np.array([[6, 24, 1],
                           [13, 16, 10],
                           [20, 17, 15]])

    plain_text = input("Enter the plain text: ")
    print(f"Plain text: {plain_text}")

    # Encryption
    cipher_text = encrypt(plain_text, key_matrix)
    print(f"Cipher text: {cipher_text}")

    # Decryption
    decrypted_text = decrypt(cipher_text, key_matrix)
    print(f"Decrypted text: {decrypted_text}")
