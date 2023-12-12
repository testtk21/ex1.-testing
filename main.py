user_data = []

while True:
    print("1. Добавить пользователя")
    print("2. Вывести информацию о пользователях")
    print("3. Вычислить средний возраст")
    print("4. Выйти")

    choice = input("Выберите действие (1/2/3/4): ")

    if choice == '1':
        name = input("Введите имя пользователя: ")
        age = input("Введите возраст пользователя: ")

        user_data.append({'name': name, 'age': age})

    elif choice == '2':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {user['name']}, Возраст: {user['age']}")

    elif choice == '4':
        print("Выход из программы.")
        break
