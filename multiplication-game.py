from random import randint

count = 0
for i in range(10):
    num1 = randint(1, 100) % 9 + 1
    num2 = randint(1, 100) % 9 + 1
    print(f"Question:{i+1} --> ", end=" ")
    print(f"{num1} X {num2} = ", end="")
    answer = int(input())
    if answer == (num1 * num2):
        count += 1
print(f"correct = {count} , wrong= {10-count}")
