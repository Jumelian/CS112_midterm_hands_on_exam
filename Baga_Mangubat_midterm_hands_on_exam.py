import random

def generate_question():
    no1 = random.randint(1, 99)
    no2 = random.randint(1, 99)
    sequence = random.choice(['+', '-', '*', '/'])
    if sequence == '+':
        ASMD = f"what is {no1} + {no2}?"
        answer = no1 + no2
    elif sequence == '-':
        ASMD = f"what is {no1} - {no2}?"
        answer = no1 - no2
    elif sequence == '*':
        ASMD = f"what is {no1} x {no2}?"
        answer = no1 * no2
    elif sequence == '/':
        num1, num2 = max(no1, no2), min(no1, no2)
        ASMD = f"what is {no1} / {no2}?"
        answer = no1 // no2
    return ASMD, answer

def main():
    num_questions = 5
    for _ in range(num_questions):
        question, answer = generate_question()
        print(question)
        user_answer = int(input("your answer: "))
        if user_answer == answer:
            print("good work!!! impressive!!!\n")
        else:
            print(f"sorry but that's wrong, the right answer is {answer}.\n")
if __name__ == "__main__":
    main()