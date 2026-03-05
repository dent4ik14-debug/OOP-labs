class Carriage:
    def __init__(self, number_of_passengers, amount_of_luggage):
        self.number_of_passengers = number_of_passengers
        self.amount_of_luggage = amount_of_luggage
        if number_of_passengers < 0 or amount_of_luggage < 0:
            raise ValueError("Кількість пасажирів або багажу не може бути від'ємною.")
    def __repr__(self):
        return self.__str__()


class Suit(Carriage):
    def __init__(self, number_of_passengers, amount_of_luggage):
        Carriage.__init__(self, number_of_passengers, amount_of_luggage)
        self.comfort_level = 5
    def __str__(self):
        return (f"Suit Carriage: \n"
                f"Number of passengers: {self.number_of_passengers}; \n"
                f"Amount of luggage: {self.amount_of_luggage}; \n"
                f"Comfort level: {self.comfort_level} \n")



class IntercityPlus(Carriage):
    def __init__(self, number_of_passengers, amount_of_luggage):
        Carriage.__init__(self, number_of_passengers, amount_of_luggage)
        self.comfort_level = 4

    def __str__(self):
        return (f"IntercityPlus Carriage: \n"
                f"Number of passengers: {self.number_of_passengers}; \n"
                f"Amount of luggage: {self.amount_of_luggage}; \n"
                f"Comfort level: {self.comfort_level}. \n")


class Compartment(Carriage):
    def __init__(self, number_of_passengers, amount_of_luggage):
        Carriage.__init__(self, number_of_passengers, amount_of_luggage)
        self.comfort_level = 3
    def __str__(self):
        return (f"Compartment Carriage: \n"
                f"Number of passengers: {self.number_of_passengers}; \n"
                f"Amount of luggage: {self.amount_of_luggage}; \n"
                f"Comfort level: {self.comfort_level}. \n")


class Intercity(Carriage):
    def __init__(self, number_of_passengers, amount_of_luggage):
        Carriage.__init__(self, number_of_passengers, amount_of_luggage)
        self.comfort_level = 2
    def __str__(self):
        return (f"Intercity Carriage: \n"
                f"Number of passengers: {self.number_of_passengers}; \n"
                f"Amount of luggage: {self.amount_of_luggage}; \n"
                f"Comfort level: {self.comfort_level}. \n")


class Berth(Carriage):
    def __init__(self, number_of_passengers, amount_of_luggage):
        Carriage.__init__(self, number_of_passengers, amount_of_luggage)
        self.comfort_level = 1
    def __str__(self):
        return (f"Berth Carriage: \n"
                f"Number of passengers: {self.number_of_passengers}; \n"
                f"Amount of luggage: {self.amount_of_luggage}; \n"
                f"Comfort level: {self.comfort_level}. \n")


class Train():
    def __init__(self):
        self.carriages = []

    def add_carriage(self, carriage):
        if isinstance(carriage, list):
            for i in carriage:
                self.add_carriage(i)
        elif isinstance(carriage, Carriage):
            self.carriages.append(carriage)
        else:
            print("Це не вагон!")

    def print_carriages(self):
        for carriage in self.carriages:
            print(carriage)

    def counting_number_of_passengers(self):
        total = 0
        for carriage in self.carriages:
            total += carriage.number_of_passengers
        return f"Number of passengers:{total}"

    def get_total_luggage(self):
        total = 0
        for carriage in self.carriages:
            total += carriage.amount_of_luggage
        return f"Number of luggage:{total}"

    def find_carriages_by_passengers(self, min_p, max_p):
        found = [c for c in self.carriages if min_p <= c.number_of_passengers <= max_p]
        return found

    def sort_carriages(self):
        self.carriages.sort(key=lambda c: c.comfort_level, reverse=True)


def main():
    try:
        # 1. Створення вагонів (можна додати перевірку на від'ємні значення)
        carriage_list = [
            Suit(15, 75),
            IntercityPlus(20, 70),
            Compartment(25, 60),
            Intercity(30, 50),
            Berth(50, 25)
        ]

        train = Train()
        train.add_carriage(carriage_list)

        print(f"Загальна кількість пасажирів: {train.counting_number_of_passengers()}")
        print(f"Загальна кількість багажу: {train.get_total_luggage()}")

        train.sort_carriages()
        print("\nВагони після сортування за комфортом:")
        train.print_carriages()

        min_p, max_p = 20, 30
        results = train.find_carriages_by_passengers(min_p, max_p)
        print(f"\nВагони з кількістю пасажирів від {min_p} до {max_p}:")
        if results:
            for r in results: print(r)
        else:
            print("Нічого не знайдено.")
    except Exception as e:
        print(f"Виникла помилка під час виконання програми: {e}")

if __name__ == '__main__':
    main()