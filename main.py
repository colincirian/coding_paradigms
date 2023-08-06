class Car:
    def __init__(self, make, model, year, driver, name):
        self.make = make
        self.model = model
        self.year = year
        self.driver = driver
        self.name = name
        
    def car_stats(self):
        print(f"Make:{self.make}, Model:{self.model}, Year:{self.year}")

    def talk(self):
        print(f"Hello, {self.driver}, my name is {self.name}")

car1 = Car("Honda", "Accord", 2022, "Colin", "Rachel")
car2 = Car("Honda", "Civic Type R", 2023, "Jonathan", "Johann")

car1.talk()
car2.talk()

#car stats
car3 = Car("Honda", "Civic", 2020)
car4 = Car("Acura", "Integra Type S", 2024)

car3.car_stats()
car4.car_stats()