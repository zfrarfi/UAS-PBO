class Furniture:
    def __init__(self, name, price, comfort):
        self.__name = name
        self.__price = price
        self.__comfort = comfort
        self.__level = 1
        self.__upgrade_cost = 200

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_upgrade_cost(self):
        return self.__upgrade_cost

    def get_comfort(self):
        return self.__comfort

    def upgrade(self, money):
        if money >= self.__upgrade_cost:
            money -= self.__upgrade_cost
            self.__level += 1
            self.__comfort += 5
            self.__upgrade_cost += 100
            print(f"{self.__name} berhasil diupgrade")

        else:
            print("Uang tidak cukup")

        return money