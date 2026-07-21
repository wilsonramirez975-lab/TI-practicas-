class Person:
    def __init__(self, initialAge):  # Constructor
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    
    def yearPasses(self):  # Para cumplir años
        self.age += 1


# Código para probar
print("--- Prueba 1 ---")
p1 = Person(-1)
p1.amIOld()

print("\n--- Prueba 2 ---")
p2 = Person(15)
p2.amIOld()
p2.yearPasses()
p2.yearPasses()
p2.yearPasses()
p2.amIOld()