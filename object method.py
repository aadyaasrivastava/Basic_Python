#WAP to use OBJ METHOD FUNCTION
"""First we make a class
than an obj
then use method function."""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("catherine", 36)
p1.myfunc()
