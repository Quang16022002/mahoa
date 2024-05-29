def vigenere_decipher(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        decrypted_char = chr((ord(char) - shift) % 256)
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

# Ví dụ giải mã với số bước dịch là 5
ciphertext = "Mjqqt%|twqi&"
shift_amount = 5
decrypted_text = vigenere_decipher(ciphertext, shift_amount)
print("Decrypted text:", decrypted_text)
