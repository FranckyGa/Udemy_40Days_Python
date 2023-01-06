date = input("Enter today's date : ")
mood = input("Rate if your mood today from 1 to 10 :")
thoughts = input("Let your thoughts flow:\n")

with open(f"./../journal/ {date} .txt", "w"):
    file.write(mood)
    file.write(thoughts)