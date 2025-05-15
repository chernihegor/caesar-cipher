def encrypt(text: str, shift: int) -> str:
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted
def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)
if name == "__main__":
    action = input("Выберите действие (encrypt/decrypt): ").strip().lower()
    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))
    
    if action == "encrypt":
        result = encrypt(text, shift)
    elif action == "decrypt":
        result = decrypt(text, shift)
    else:
        result = "Неверное действие!"
    
    print(f"Результат: {result}")
