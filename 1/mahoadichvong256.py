def vigenere_cipher(text, shift):
    encrypted_text = []
    for char in text:
        encrypted_char = chr((ord(char) + shift) % 256)
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

# Ví dụ mã hóa với dịch số bước là 5
plaintext = "Hello World!"
shift_amount = 5
ciphertext = vigenere_cipher(plaintext, shift_amount)
print("Ciphertext:", ciphertext)
