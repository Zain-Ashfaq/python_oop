# Object-Oriented Programming (OOP) Notes

## Classes

In object-oriented programming (OOP), a class is a blueprint for creating objects (instances) that encapsulate data (attributes) and behavior (methods) related to a specific concept or entity. It defines the structure and behavior of objects of that class.

To create a class in Python, you typically use the `class` keyword followed by the name of the class. Here's an example of a `Dog` class:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def describe(self):
        print(f"I am {self.name}, a {self.age}-year-old dog.")
```
In the above example, the Dog class has attributes (name and age) and methods (bark and describe). The __init__ method is a special method called the constructor, which is executed when a new instance of the class is created.
## Four Pillars of OOP

The four pillars of OOP are the fundamental principles that guide the design and implementation of object-oriented systems. They are:
## Encapsulation

Encapsulation is the bundling of data (attributes) and the methods that operate on that data within a class. It hides the internal implementation details of an object and provides access to the object's behavior through well-defined interfaces.

Example: Encapsulating the Dog class:

```python

dog = Dog("Max", 3)
dog.describe()  # Output: I am Max, a 3-year-old dog.
```
In the example, the Dog class encapsulates the data (name and age) and methods (bark and describe) within the class. The describe method provides an interface to access the internal attributes and behavior of the Dog object.
## Inheritance

Inheritance allows classes to inherit attributes and methods from other classes, forming a hierarchy of classes. A subclass (child class) inherits the characteristics of its superclass (parent class), enabling code reuse and promoting the concept of "is-a" relationships.

Example: Inheriting from the Animal class to create a Reptile class:

```python

class Animal:
    def eat(self):
        print("Eating...")

class Reptile(Animal):
    def crawl(self):
        print("Crawling...")

reptile = Reptile()
reptile.eat()   # Output: Eating...
reptile.crawl() # Output: Crawling...
```
In the example, the Reptile class inherits the eat method from the Animal class. The Reptile class can access and use the methods of its superclass.
## Polymorphism

Polymorphism allows objects of different classes to be treated as interchangeable, as long as they share a common interface or superclass. It allows different classes to implement their own versions of methods, providing flexibility and extensibility.

Example: Implementing a Snake class that overrides a method inherited from its superclass Reptile:

```python

class Snake(Reptile):
    def crawl(self):
        print("Slithering...")

snake = Snake()
snake.crawl()  # Output: Slithering...
```
In the example, the Snake class inherits the crawl method from the Reptile class but overrides it with its own implementation. This demonstrates polymorphism, where the same method name is used across different classes but exhibits different behaviors.

## Abstraction

Abstraction is a principle in object-oriented programming that focuses on hiding unnecessary implementation details and exposing only the essential features or functionalities to the user.

Example: Implementing abstraction with an Animal class and its subclasses (Reptile, Snake, and Python):

```python

class Animal:
    def make_sound(self):
        pass

class Reptile(Animal):
    def make_sound(self):
        print("Making reptile sound...")

class Snake(Reptile):
    def make_sound(self):
        print("Hissing...")

class Python(Snake):
    def make_sound(self):
        print("Sssss...")

python = Python()
python.make_sound()  # Output: Sssss...
```
In the example, the Animal class defines an abstract method make_sound() without any implementation. The subclasses (Reptile, Snake, and Python) inherit from the Animal class and provide their own implementations of the make_sound() method.

By using abstraction, we can define a common interface (make_sound()) in the superclass Animal and allow each subclass to implement it according to its specific behavior. This allows for flexibility and modularity in the design of our code.

Object-oriented programming (OOP) employs classes to encapsulate data and behavior, and the four pillars of OOP (encapsulation, inheritance, polymorphism, and abstraction) provide guiding principles for designing robust and flexible systems. By utilizing these principles, we can create well-structured, reusable, and maintainable code.