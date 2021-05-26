def menu():
    print("[1] Add Dog")
    print("[2] Add Food")
    print("[3] View Dogs")
    print("[4] View Dog Food")
    print("[5] Delete Dog")
    print("[6] Delete Dog Food")
    print("[0] Quit")


class Dog:
    def __init__(self, name):
        self.name = name
        print("Dog created!")


class Food:
    def __init__(self, typ, kg):
        self.type = typ
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
    elif option == 5:
        deleted_dog = (input("Pick dog to delete :"))
        for dog in dog_list:
            print(dog.name)
            if dog.name == deleted_dog:
                dog_list.remove(dog)
                print(dog.name + ":" + "is deleted !")
    elif option == 6:
        delete_food = (input("Pick food to delete :"))
        for food in food_list:
            print(food.type, food.kg + "kg")
            if food.type == delete_food:
                food_list.remove(food)
                print(food.type, food.kg, "kg" ":" + "is deleted !")
            else:
                print("This dog is not in the list !")
    elif option == 0:
        quit()
    else:
        print("Wrong option")
