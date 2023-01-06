#Exercise 1:
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

#Exercise 2:
usernames = ["john 1990", "alberta1970", "magnola2000"]
username = [len(username) for username in usernames]
print(username)

#Exercise 3:
user_entries = ['10', '19.1', '20']
user_entries = [float(number) for number in user_entries]
print(user_entries)

#Exercise 4 :
user_entries = ['10', '19.1', '20']
my_sum =[float(number) for number in user_entries]
print(sum(my_sum))
