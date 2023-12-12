user_data = []

while True:
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("2. Вывести информацию о пользователях")
    print("4. Вычислить средний возраст")
    print("5. Выйти")
    # ЧТОТОТОТЧОЧТОЧТОЧ
    choice = input("Выберите действие (1/2/3/4/5): ")

    if choice == '1':
        name = input("Введите имя пользователя: ")
        age = input("Введите возраст пользователя: ")

        user_data.append({'name': name, 'age': age})

    elif choice == '3':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {user['name']}, Возраст: {user['age']}")

    elif choice == '5':
        print("Выход из программы.")
        break
