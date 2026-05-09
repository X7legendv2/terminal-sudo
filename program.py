import random
import time

print("Добро пожаловать!")

plasma = random.randint(1, 10)
name = None 
list_command = ("register", "sudo", "plasma", "whoami", "help", "winget", "exit", "calc")

while True:
    command = input("Choose the command: ").lower().strip()
    
    if command == "register":
        name = input("Создайте аккаунт: ")
        password = int(input("Создайте пароль: "))
        print(f"Пользователь {name} создан!")
        print(f"DEBUG: {name}, {command}, {password}")

    elif command == "sudo":
        if name is None:
            print("Сначала регистрация!")
        else:
            print("sudo -h | -K | -k | -V")
           
    elif command == "plasma":
        if name is None:
            print("Сначала регистрация!")
        else:
            print(plasma)

    elif command == "whoami":
        if name is None:
            print("Сначала регистрация!")
        else:
            print(name)
            
    elif command == "help":
        if name is None:
            print("Сначала регистрация!")
        else:
            print(list_command)
    
    elif command == "calc":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        print("1. Операция +")
        print("2. Операция -")
        print("3. Операция *")
        print("4. Операция /")
        
        op = input("Выберите операцию (1-4): ")
        
        if op == "1":
            print(num1 + num2)
        elif op == "2":
            print(num1 - num2)
        elif op == "3":
            print(num1 * num2)
        elif op == "4":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Ошибка: деление на ноль!")
        else:
            print("Неверная операция")

    elif command == "winget":
        print("Необходимо выбрать класс:")
        print("1. Установка софта")
        print("2. Проверка winget")
        print("3. Выход")
        print("4. Показать лист приложений")
    
        winget_soft = input("Выберите 1, 2, 3, 4: ")
    
        if winget_soft == "1":
            list_app = ("Open Shell","Powershell","Libreoffice")
            print(list_app)
            app = input("Выберите программу: ").lower().strip()
            
            if app == "open shell":
                print("Загрузка начинается..")
                time.sleep(1)
                print("загрузка 20%")
                time.sleep(1)
                print("Распаковка Файлов 30%")
                time.sleep(1)
                print("Загрузка важных компонентов 70%")
                time.sleep(1)
                print("Завершено, программа Open Shell установлена")
            
            elif app == "powershell":
                print("Загрузка начинается..")
                time.sleep(1)
                print("загрузка 20%")
                time.sleep(1)
                print("Распаковка Файлов 30%")
                time.sleep(1)
                print("Загрузка важных компонентов 70%")
                time.sleep(1)
                print("Завершено, программа PowerShell установлена")
            
            elif app == "libreoffice":
                print("Загрузка начинается..")
                time.sleep(1)
                print("загрузка 20%")
                time.sleep(1)
                print("Распаковка Файлов 30%")
                time.sleep(1)
                print("Загрузка важных компонентов 70%")
                time.sleep(1)
                print("Завершено, программа Libreoffice установлена")
            else:
                print("Программа не найдена")
        
        elif winget_soft == "2":
            print("Проверка winget...")
        
        elif winget_soft == "3":
            print("Выход из winget")
            
        elif winget_soft == "4":
            list_app = ("Open Shell","Powershell","Libreoffice")
            print(list_app)

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Неизвестная команда. Доступно: register, sudo, plasma, whoami, help, winget, exit, calc")