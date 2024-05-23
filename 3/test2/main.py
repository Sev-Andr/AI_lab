# Словник для зберігання даних про транспортні компанії
companies = {
    "Нова Пошта": {
        "vehicles": 1000,
        "cost_per_km": 1.5,
        "address": "вул. Київська, 12",
        "max_weight": 30,
    },
    "Укрпошта": {
        "vehicles": 500,
        "cost_per_km": 1.2,
        "address": "вул. Шевченка, 24",
        "max_weight": 20,
    },
    "Делівері": {
        "vehicles": 300,
        "cost_per_km": 1.8,
        "address": "вул. Франка, 36",
        "max_weight": 50,
    },
}

# Валідація
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Невірний формат. Введіть число.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Невірний формат. Введіть число з плаваючою комою.")

# Функція для додавання нової компанії
def add_company():
    name = input("Введіть назву компанії: ")
    vehicles = get_int_input("Введіть кількість автомобілів: ")
    cost_per_km = get_float_input("Введіть вартість 1 км перевезення: ")
    address = input("Введіть адресу: ")
    max_weight = get_int_input("Введіть максимальну допустиму вагу: ")

    companies[name] = {
        "vehicles": vehicles,
        "cost_per_km": cost_per_km,
        "address": address,
        "max_weight": max_weight,
    }

# Функція для видалення компанії
def remove_company():
    name = input("Введіть назву компанії для видалення: ")

    if name in companies:
        del companies[name]
        print(f"Компанія {name} успішно видалена.")
    else:
        print(f"Компанія {name} не знайдена.")

# Функція для редагування інформації про компанію
def edit_company():
    while True:
        name = input("Введіть назву компанії для редагування: ")
        if name in companies:
            company = companies[name]

            vehicles = get_int_input("Введіть нову кількість автомобілів (або Enter для пропуску): ")
            if vehicles:
                company["vehicles"] = vehicles

            cost_per_km = get_float_input("Введіть нову вартість 1 км перевезення (або Enter для пропуску): ")
            if cost_per_km:
                company["cost_per_km"] = cost_per_km

            address = input("Введіть нову адресу (або Enter для пропуску): ")
            if address:
                company["address"] = address

            max_weight = get_int_input("Введіть нову максимальну допустиму вагу (або Enter для пропуску): ")
            if max_weight:
                company["max_weight"] = max_weight

            print(f"Інформація про компанію {name} успішно оновлена.")
            break
        else:
            print(f"Компанія {name} не знайдена.")


# Функція для демонстрації всіх компаній
def show_companies():
    for name, company in companies.items():
        print(f"--- {name} ---")
        print(f"Кількість автомобілів: {company['vehicles']}")
        print(f"Вартість 1 км перевезення: {company['cost_per_km']}")
        print(f"Адреса: {company['address']}")
        print(f"Максимальна допустима вага: {company['max_weight']}")

# Функція для пошуку компаній з максимальною допустимою вагою більше N
def find_companies_by_max_weight():
    while True:
        try:
            n = get_int_input("Введіть мінімальну допустиму вагу: ")
            break
        except ValueError:
            print("Невірний формат. Введіть ціле число більше 0.")

    filtered_companies = []
    for name, company in companies.items():
        if company["max_weight"] >= n:
            filtered_companies.append((name, company))

    if filtered_companies:
        print(f"Знайдено {len(filtered_companies)} компаній з максимальною допустимою вагою більше {n}:")
        for name, company in filtered_companies:
            print(f"- {name}")
    else:
        print(f"Компаній з максимальною допустимою вагою більше {n} не знайдено.")


# Меню для роботи з довідником
while True:
    print("-" * 20)
    print("Меню довідника \"Транспортні компанії\"")
    print("-" * 20)
    print("1. Додати нову компанію")
    print("2. Видалити компанію")
    print("3. Редагувати інформацію про компанію")
    print("4. Переглянути всі компанії")
    print("5. Знайти компанії за максимальною допустимою вагою")
    print("0. Вихід")
    print("-" * 20)

    choice = input("Введіть номер пункту меню: ")

    if choice == "1":
        add_company()
    elif choice == "2":
        remove_company()
    elif choice == "3":
        edit_company()
    elif choice == "4":
        show_companies()
    elif choice == "5":
        find_companies_by_max_weight()
    elif choice == "0":
        print("Дякуємо за використання довідника!")
        break
    else:
        print("Невірний номер пункту меню.")