#Жаныбаев Бекмамат

from re import U


user_data = []
x = 0 
while True:
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("3. Вывести информацию о пользователях")
    print("4. Вычислить средний возраст")
    print("5. Выйти")
    # ЧТОТОТОТЧОЧТОЧТОЧ
    choice = input("Выберите действие (1/2/3/4/5): ")

    if choice == '1':
        name = input("Введите имя пользователя : ")
        for i in name :
            if i.isdigit():
                print("Имя не должо содержать цифр")
        age = input("Введите возраст пользователя: ")
        if not age.isdigit() :
            print("Возраст должен быть написан цифрами")
        age =int(age)
        user_data.append({'name': name, 'age': age})
    elif choice == '2':
        h = input("Ввелите имя удаляемого пользователя:")
        for i in user_data:
            if h == i["name"]:
                user_data.remove(i)
    elif choice == '3':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {user['name']}, Возраст: {user['age']}")
    elif choice =='4':
        for i in user_data:
            x+=i['age']
        sred=(x/len(user_data))
        print("Средний возраст пользователей:", sred)
    elif choice == '5':
        print("Выход из программы.")
    
        
    
        break
