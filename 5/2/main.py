# Базовий клас Приміщення
class Room:
    def __init__(self, room_type, functionality):
        self.__room_type = room_type  # Тип приміщення
        self.__functionality = functionality  # Функціональність

    def set_room_type(self, type):
        self.__room_type = type

    def set_functionality(self, func):
        self.__functionality = func

    # Метод для виведення інформації про приміщення
    def display_info(self):
        print(f"Тип приміщення: {self.__room_type}\nФункціональність: {self.__functionality}\n", end = '')


# Клас Вітальня
class LivingRoom(Room):
    def __init__(self, room_type, functionality, furniture):
        super().__init__(room_type, functionality)
        self.__furniture = furniture  # Меблі

    def add_furniture(self, *items):
        self.__furniture.extend(items)
        print("Меблі успішно додано!")

    # Перевизначений метод для виведення інформації про житлове приміщення
    def display_info(self):
        super().display_info()
        print(f"Меблі: {', '.join(self.__furniture)}\n", end = '')


# Клас Робоче приміщення
class Workspace(Room):
    def __init__(self, room_type, functionality, equipment):
        super().__init__(room_type, functionality)
        self.__equipment = equipment  # Обладнання для роботи

    def add_equipment(self, *items):
        self.__equipment.extend(items)
        print("Обладнання успішно додано!")

    # Перевизначений метод для виведення інформації про робоче приміщення
    def display_info(self):
        super().display_info()
        print(f"Обладнання: {', '.join(self.__equipment)}\n", end = '')


# Клас Кухня
class Kitchen(LivingRoom):
    def __init__(self, room_type, functionality, furniture, appliances):
        super().__init__(room_type, functionality, furniture)
        self.__appliances = appliances  # Побутова техніка

    def add_appliances(self, *items):
        self.__appliances.extend(items)
        print("Побутова техніка успішно додана!")

    # Перевизначений метод для виведення інформації про кухню
    def display_info(self):
        super().display_info()
        print(f"Побутова техніка: {', '.join(self.__appliances)}\n")


# Клас Спальня
class Bedroom(LivingRoom):
    def __init__(self, room_type, functionality, furniture, bed_size):
        super().__init__(room_type, functionality, furniture)
        self.__bed_size = bed_size  # Розмір ліжка

    # Перевизначений метод для виведення інформації про спальню
    def display_info(self):
        super().display_info()
        print(f"Розмір ліжка: {self.__bed_size}\n")


# Клас Аудиторія
class Auditorium(Workspace):
    def __init__(self, room_type, functionality, equipment, capacity):
        super().__init__(room_type, functionality, equipment)
        self.__capacity = capacity  # Ємність (кількість місць)

    # Перевизначений метод для виведення інформації про аудиторію
    def display_info(self):
        super().display_info()
        print(f"Ємність: {self.__capacity}\n")


# Клас Офіс
class Office(Workspace):
    def __init__(self, room_type, functionality, equipment, desks):
        super().__init__(room_type, functionality, equipment)
        self.__desks = desks  # Кількість робочих столів

    # Перевизначений метод для виведення інформації про офіс
    def display_info(self):
        super().display_info()
        print(f"Кількість робочих столів: {self.__desks}\n")

# Клас Ванна кімната
class Bathroom(LivingRoom):
    def __init__(self, room_type, functionality, furniture, fixtures):
        super().__init__(room_type, functionality, furniture)
        self.__fixtures = fixtures  # Сантехніка

    def add_fixtures(self, *items):
        self.__fixtures.extend(items)
        print("Сантехніка успішно додана!")

    # Перевизначений метод для виведення інформації про ванну кімнату
    def display_info(self):
        super().display_info()
        print(f"Сантехніка: {', '.join(self.__fixtures)}\n")


# Клас Гараж
class Garage(Room):
    def __init__(self, room_type, functionality, vehicles):
        super().__init__(room_type, functionality)
        self.__vehicles = vehicles  # Транспортні засоби

    def add_vehicles(self, *items):
        self.__vehicles.extend(items)
        print("Транспортні засоби успішно додані!")

    # Перевизначений метод для виведення інформації про гараж
    def display_info(self):
        super().display_info()
        print(f"Транспортні засоби: {', '.join(self.__vehicles)}\n")


# Клас Спортивний зал
class Gym(Workspace):
    def __init__(self, room_type, functionality, equipment, machines):
        super().__init__(room_type, functionality, equipment)
        self.__machines = machines  # Тренажери та обладнання для фітнесу

    def add_machines(self, *items):
        self.__machines.extend(items)
        print("Тренажери та обладнання для фітнесу успішно додані!")

    # Перевизначений метод для виведення інформації про спортивний зал
    def display_info(self):
        super().display_info()
        print(f"Тренажери та обладнання для фітнесу: {', '.join(self.__machines)}\n")



# Створення об'єктів
kitchen = Kitchen("Kitchen", "Житлове", ["Стіл", "Стільці", "Плита"], ["Холодильник", "Мікрохвильовка"])
bedroom = Bedroom("Bedroom", "Житлове", ["Ліжко", "Шафа", "Тумбочка"], "King Size")
auditorium = Auditorium("Auditorium", "Робоче", ["Проектор", "Стільці", "Столи"], 100)
office = Office("Office", "Робоче", ["Комп'ютер", "Столи", "Стільці"], 10)
bathroom = Bathroom("Bathroom", "Санітарний", ["Диван", "Стіл", "Лампа"], ["Умивальник", "Туалет", "Душ"])
garage = Garage("Garage", "Зберігання", ["Автомобіль", "Велосипед", "Інструменти"])
gym = Gym("Gym", "Фітнес", ["Гантелі", "Мати для вправ"], ["Бігова доріжка", "Статичний велосипед"])

# Виведення інформації про об'єкти
kitchen.display_info()
bedroom.display_info()
auditorium.display_info()
office.display_info()
bathroom.display_info()
garage.display_info()
gym.display_info()

gym.add_machines("Штанга")
gym.display_info()