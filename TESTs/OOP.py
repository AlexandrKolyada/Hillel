class Dog:
    legs = 4
    tail = 1
    ears = 2

    def say(self):
        print("Woof!")

    def go(self):
        for _ in range(self.legs):
            print("Step")


dog1 = Dog()
dog2 = Dog()

print(dog1.legs)
dog1.say()

dog1.legs =3
print('-' * 20)
dog1.go()
print('-' * 20)
dog2.go()

dog1.name = "Bobik"
print(dog1.name)