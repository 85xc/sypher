from timekey import generate_time_key, is_valid_key
from encryptor import text_to_hex, hex_to_params
from bird_generator import generate_birdsong
from decryptor import fake_decrypt

def encrypt_mode():
    text = input("Введите текст для шифровки: ")
    key = generate_time_key()
    hex_code = text_to_hex(text)
    params = hex_to_params(hex_code)
    file_path = generate_birdsong(params)
    
    print("\n--- Шифрование завершено ---")
    print(f"Hex-код: {hex_code}")
    print(f"Временной ключ (действует 1 час): {key}")
    print(f"Сохранённый файл: {file_path}")

def decrypt_mode():
    input("Укажите путь к .wav файлу (заглушка): ")
    user_key = input("Введите временной ключ: ")
    if is_valid_key(user_key):
        result = fake_decrypt()
        print(f"\nРасшифрованный текст: {result}")
    else:
        print("\n[ОШИБКА] Неверный или просроченный ключ!")

def main():
    print("=== SYPHER: Консольный шифратор птиц ===")
    print("1. Зашифровать текст в трель")
    print("2. Расшифровать трель в текст")
    choice = input("Выберите режим (1/2): ")

    if choice == "1":
        encrypt_mode()
    elif choice == "2":
        decrypt_mode()
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()