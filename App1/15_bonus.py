import json

with open("06_files/questions.json","r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    
    user_choice = int(input("Enter your answer : "))
    question["user_choice"] = user_choice               #record answer from user

#print correct answer + user answer
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    
    message = f" {index + 1} {result} Your answer : {question['user_choice']}, "\
             f"Correct answer: {question['correct_answer']}"
    print(message)

#Display score
print(score, "/", len(data))





