#Exercise 1
amount = float(input("How many dollars do you have? "))
rate = 0.95
print("The amount in euro is : ", float(amount*rate))

#Exercise 2 :
ranking = ["John","Sen","Lisa"]
my_index = int(input("Enter rank number:"))
print(ranking[my_index - 1])

#Exercise 3 :
ranking = ["John","Sen","Lisa"]
my_index = input("Enter name:")
name = ranking.index(my_index) + 1
print(name)