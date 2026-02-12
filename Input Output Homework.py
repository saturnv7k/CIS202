#input
import math

family = 4
pizzaslices=8

mom = (int(input ("How many pieces of pizza does mom eat? ")))
dad = (int(input ("How many pieces of pizza does dad eat? ")))
son = (int(input ("How many pieces of pizza does the son eat? ")))
daughter = (int(input ("How many pieces of pizza does the daughter eat? ")))

#processing
totalslices = (mom + dad + son + daughter)
wholepizzas = math.ceil (totalslices/pizzaslices)
print("We need to order these many pizzas: ", wholepizzas)
leftover = wholepizzas*pizzaslices - totalslices
print("The leftover amount of slices will be: ", leftover)

leftoverbymodulo = totalslices%pizzaslices
print(leftoverbymodulo)