import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_numbers=True, use_special=True):
    # Существующие символы для пароля
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase  # Все строчные буквы
    if use_uppercase:
        characters += string.ascii_uppercase  # Все прописные буквы
    if use_numbers:
        characters += string.digits            # Все цифры
    if use_special:
        characters += string.punctuation       # Все специальные символы

    if not characters:
        raise ValueError("Должен быть выбран хотя бы один тип символов.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    while True:
        try:
            password_length = int(input("Введите желаемую длину пароля: "))
            if password_length <= 0:
                print("Длина пароля должна быть положительным числом.")
                continue
            
            include_lowercase = input("Включить строчные буквы? (y/n): ").lower() == 'y'
            include_uppercase = input("Включить прописные буквы? (y/n): ").lower() == 'y'
            include_numbers = input("Включить цифры? (y/n): ").lower() == 'y'
            include_special = input("Включить специальные символы? (y/n): ").lower() == 'y'

            password = generate_password(password_length, include_lowercase, include_uppercase, include_numbers, include_special)
            print(f"Сгенерированный пароль: {password}")
            
            # Предложить создать новый пароль
            another = input("Хотите сгенерировать еще один пароль? (y/n): ").lower()
            if another != 'y':
                break

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
