from random import randint, choice

numBerOfQuestion = int(input("Number of Question to answer "))
operation = [1, 2, 3]
# print(operation)
correct = 0
for i in range(numBerOfQuestion):
    temp = choice(operation)
    if temp == 1:
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        answer = num1 * num2
        user = int(input(f"Question number-{i+1} ->> {num1} X {num2} = "))
        if user == answer:
            correct = correct + 1
    elif temp == 2:
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        answer = num1 + num2
        user = int(input(f"Question number-{i+1} ->> {num1} + {num2} = "))
        if user == answer:
            correct = correct + 1
    elif temp == 3:
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        answer = num1 - num2
        user = int(input(f"Question number-{i+1} ->> {num1} - {num2} = "))
        if user == answer:
            correct = correct + 1

print(f"correct = {correct} wrong = {numBerOfQuestion-correct}")
