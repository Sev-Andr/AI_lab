# Створіть клас planet, який містить інформацію про планету сонячної
# системи, що включає наступні атрибути: назва, діаметр, масу і відстань
# від Сонця в тисячах кілометрів у закритій частині класу. В класі
# повинна бути відкрита функція, яка повертає відстань від Сонця в
# милях і відкрита функцію, яка виводить усю інформацію про планету
# на екран.

class Planet:
    def __init__(self, name, diameter, mass, distance_from_sun):
        self.__name = name
        self.__diameter = diameter
        self.__mass = mass
        self.__distance_from_sun = distance_from_sun

    def __str__(self):
        return f"Назва планети: {self.__name}\nДіаметр планети: {self.__diameter} км\nМаса планети: {self.__mass} кг\nВідстань від Сонця: {self.__distance_from_sun} тис. км\nВідстань від Сонця в милях: {self.distance_from_sun_in_miles()} миль\n"

    def distance_from_sun_in_miles(self):
        return self.__distance_from_sun * 0.621371192  # переведення кілометрів в милі

    def display_info(self):
        print(self)

    def get_name(self):
        return self.__name

    def get_diameter(self):
        return self.__diameter

    def get_mass(self):
        return self.__mass

    def get_distance_from_sun(self):
        return self.__distance_from_sun

# Створення об'єктів класу Planet
mercury = Planet("Меркурій", 4879, 3.3011e23, 57909)
venus = Planet("Венера", 12104, 4.8675e24, 108160)
earth = Planet("Земля", 12742, 5.972e24, 149600)
mars = Planet("Марс", 6792, 6.4171e23, 227936)

# Демонстрація роботи методів класу
mercury.display_info()
print(mercury.get_name())
venus.display_info()
earth.display_info()
mars.display_info()
