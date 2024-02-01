class Person:

    def init(self, name):
        self._name = name
        self.bank_account = 25
        self.happiness = 8
        self.hygiene = 8

    @property
    def name(self):
        return self._name


    def is_clean(self):
        if self.hygiene > 7:
            return True
        else:
            return False

    def is_happy(self):
        if self.happiness > 7:
            return True
        else: 
            return False

    def get_paid(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.bank_account += amount
            return("All about the benjamins")

    def take_bath(self):
        self.hygiene += 4
        return("♪ Rub-a-dub just relaxing in the tub ♫")

    def work_out(self):
        self.happiness += 2
        self.hygiene -= 3
        return("♪ another one bites the dust ♫")

    def call_friend(self, friend):
        self.happiness += 3
        friend.happiness += 3
        return(f"Hi {friend.name}! It's {self.name}. How are you?")







jay = Person("Jay")
isaiah = Person("Isaiah")

print(jay.bank_account)
print(jay.get_paid(10))
print(jay.bank_account)

print(isaiah.happiness)
print(jay.happiness)
jay.work_out()
print(jay.call_friend(isaiah))
print(jay.happiness)
print(isaiah.happiness)