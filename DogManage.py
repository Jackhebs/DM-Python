def menu():
    print("[1] Add Dog")
    print("[2] Add Food")
    print("[3] View Dogs")
    print("[4] View dog food")
    print("[0] Quit")


class Dog:
    def __init__(self, name):
        self.name = name
        print("Dog created!")


class Food:
    def __init__(self, type, kg):
        self.type = type
        self.kg = kg
        print("Food created!")


print("***MENU***")

food_list = []
dog_list = []
option = -1
while option != 0:
    menu()
    option = int(input("pick an option : "))
    if option == 1:
        my_dog = Dog(input(" Dog Name : "))
        dog_list.append(my_dog)
    elif option == 2:
        my_food = Food(input("type :"), input("kg :"))
        food_list.append(my_food)
    elif option == 3:
        for dog in dog_list:
            print(dog.name)
    elif option == 4:
        for food in food_list:
            print(food.type + " : " + food.kg + "kg")
    else:
        print("Wrong option")
