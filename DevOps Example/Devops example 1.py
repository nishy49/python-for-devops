#print("Hello World")

#name="Nishy"
#age=25
#height=5.7
#is_dev=True
#print(f"Name:{name},AGE:{age},Height:{height},Developer:{is_dev}")

"""
Taking user input
name=input("Enter your name:")
print(f"Hello, {name}  !")
"""
"""
#ifElse statment
num=int(input("Enter a number:"))#Converts input to integer

if num%2==0:
    print("evennumber")
else:
    print("odd number")
"""

#def greet(name):
    #return f"Hello,{name}"
#print(greet('Nishy'))

"""
fruits =["Apple","Banana","Mango"]
fruits.append("Orange")
fruits.remove("Banana")
print(fruits)
"""

coordinates=('nisy',10,20)
print(coordinates[0])

person={"name":"Nischal","age":25,"city":"Mumbai"}
print(person)

squares =[x**2 for x in range(50)]
print(squares)



try:
    num=int(input("Enter a number :"))
    print(10/num)
except ZeroDivisionError:
    print("Cannotdivide by zero!")
except ValueError:
    print("invalid input!" "ENTER A NUMBER")

class Car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model

        def details(self):
            return f"Car:{self,brand}{self.model}"

        my_car =Car("Tesla", "Model S")
        print(my_car.details())
