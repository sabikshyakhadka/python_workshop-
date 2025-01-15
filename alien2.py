
def natural_number():
       n = 1
       while True:
              yield n 
              n += 1
gen = natural_number()
for _ in range(10):
       print(next(gen))
def print_result(*args, **kwargs):
 print(args)
 print(kwargs)
 result = 0 
 for number in args:
        result += number
 print(f"my full name is {kwargs['first_name']} {kwargs['last_name']} and total marks = {result}")
print_result(90,90,80,90,70, first_name="sabikshya", last_name="khadka")



treasures = ["gold", "silver", "gems", "antique product"]
upper_treasure = []
for treasure in treasures:
       upper_treasure.append(treasure.upper())
       capitalize_treasure = (treasure.upper())
       print(capitalize_treasure)



def factorial(n):
       if n == 0:
              return 1
       return n*factorial(n - 1)
print (factorial(5))

for letter in "hello":
    print(letter)
