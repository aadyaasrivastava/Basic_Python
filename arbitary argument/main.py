#arbitary argument

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Lopez", "Beth")

"""
keyword argument
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
"""