#4.1
pizzas=["tomato","potato","pepperoni"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print("I really love pizza.")
#4.2
animals=["pig","elephant","ant"]
for animal in animals:
    print(animal.title())
    if animal=="pig":
        print(f"A {animal.title()} would make a great pet.")
    else:
        print(f"An {animal.title()} would make a great pet.")
print("Any of these animals would make a great pet.")
#4.3-4.9
for number in range(1,21):
    print(number)
numbers=list(range(1,1000000))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
odds=list(range(1,20,2))
for odd in odds:
    print(odd)
number_3=list(range(3,31,3))
for number in number_3:
    print(number)
numbers=list(range(1,11))
for number in numbers:
    value=number**3
    print(value)
#4.10
print("The first three items in the list are:")
print(numbers[0:3])
print("Three items from the middle of the list are:")
print(numbers[4:7])
print("The last three items in the list are:")
print(numbers[-3:-1])
#4.11
pizzas=["tomato","potato","pepperoni"]
friend_pizzas=pizzas
pizzas.append("cheese")
friend_pizzas.insert(0,"bread")
print(pizzas)
print(friend_pizzas)
#4.13
buffets=("chips","orange","juice","tomato","parrot")
for buffet in buffets:
    print(buffet)
buffets=("chips","apple","cola","tomato","parrot")
for buffet in buffets:
    print(buffet)