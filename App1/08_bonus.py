date = input("Enter today's date : ")
mood = input("Rate if your mood today from 1 to 10 :")
thoughts = input("Let your thoughts flow:\n")

with open(f"App1/08_journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)

