"""
Class:      CSE1321L
Section:    Module 6
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        12B
"""

class Dog:

    def __init__(self, age, weight, name, furColor, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed


    def bark(self):
        print("Woof! Woof!")


    def rename(self, name):
        self.name = name


    def eat(self, food):
        self.weight += food


print("You are about to create a dog.")
dog_age = int(input("How old is the dog: "))
dog_weight = float(input("How much does the dog weigh: "))
dog_name = input("What is the dog's name: ")
dog_color = input("What color is the dog: ")
dog_breed = input("What breed is the dog: ")

dog = Dog(dog_age, dog_weight, dog_name, dog_color, dog_breed)
print(f"{dog.name} is a {dog.age} year old {dog_color} {dog_breed} that weighs {dog.weight} pounds")
dog.bark()

food = float(input(f"{dog.name} is hungry, how much should he eat: "))
new_name = input(f"{dog.name} isn't a very good name. What should they be renamed to: ")

dog.eat(food)
dog.rename(new_name)

print(f"{dog.name} is a {dog.age} year old {dog_color} {dog_breed} that weighs {dog.weight} pounds")
