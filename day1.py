#day1
"""a = 3
b = "3.0"
ans = a + int(float(b))
print(ans)

a=3
A=4
print(a+3+7)

a35=6
35a=7
35_a=8
_a=9
a$=1
print(a35+35a)
print(35_a+_a)
print(a$)"""

"""
name=input("Enter your name: ")
age=input("Enter your age: ")
print("My name is ",name, "and my age is ",age)

name=input("Enter your name: ")
age=input("Enter your age: ")
if name=="Namita":
 print("My name is ",name, "and my age is ",age)
else:
 print("Your name is invalid")
 """

"""
name1=input("Enter your name: ")
age1=input("Enter your age: ")
name2=input("Enter your name: ")
age2=input("Enter your age: ")
#print("My name is ",name1, "and my age is ",age1 if age1>=age2 else "My name is ",name2, "and my age is ",age2 )
if age1>=age2:
     print("My name is ",name1, "and my age is ",age1)
else:
     print("My name is ",name2, "and my age is ",age2)

"""

"""
def calc():
 a=int(input("Enter value for a: "))
 b=int(input("Enter value for b: "))
 flag=True;
 while flag:
  choice=int(input("Enter choice: 1.SUM 2.SUBTRACT 3.MULTIPLY 4.DIVISION 5.EXIT :"))
  if choice==1:
      print(a+b)
  elif choice==2:
      print(a-b)
  elif choice==3:
      print(a*b)
  elif choice==4:
      print(a/b)
  elif choice==5:
      print("Exit")
      flag=False
  else:
      print("Invalid try again")
calc()
"""
"""
def findmax(l):
    max=l[0]   
    for x in l:
        if x>max:
            max=x
    print(f"The largest number is: {max}")
l=[2,3,4,5,1,7,3,9]
findmax(l)
"""
"""
l=[]
n=int(input("Enter limit: "))
for i in range(n):
    num=int(input("Enter the value: "))
    l.append(num)
avg=0
sum=0
for i in l:
    sum+=i;
print(f"Sum={sum} and average={sum/n}")
"""

#hw


"""

dictionary = {
    "apple": "A fruit that is typically red, green, or yellow, and has a crisp texture and a sweet or sour taste.",
    "banana": "A long, curved fruit that has a soft, yellow flesh and is often eaten as a snack.",
    "carrot": "A long, orange root vegetable that is often used in cooking and is a good source of vitamins.",

}

def find_definition(word):
    return dictionary.get(word, "Word not found in the dictionary.")

while True:
    user_input = input("Enter a word to look up (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    definition = find_definition(user_input.lower())
    
    print(definition)
"""
"""num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    ans = num * i
    print(f"{num} x {i} = {ans}")"""


"""def countvc(word):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vcount = sum(1 for char in word if char in vowels)
    ccount = sum(1 for char in word if char in consonants)
    tc = len(word)
    return {
        "Vowels": vcount,
        "Consonants": ccount,
        "Total Characters": tc,
    }
word = input("Enter a string: ")
result = countvc(word)
print("Answer:")
for key, value in result.items():
    print(f"{key}: {value}")"""


"""class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Division by zero is not allowed"
        return x / y

calculator = Calculator()

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            print("Result:", calculator.add(num1, num2))
        elif user_input == "subtract":
            print("Result:", calculator.subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", calculator.multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", calculator.divide(num1, num2))
    else:
        print("Invalid input. Please try again.")"""
