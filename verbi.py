import time
import random

print("Jisimni Ġianni.")
your_name = input("X'jismek? ").capitalize()
print(f"Ħelow, {your_name}!")
start = input("Do you want to start learning Maltese verbs conjugation? ").capitalize()

if start == "No":
    print("Ok, bye!")
    exit()
elif start == "Yes":
    print("Ok, let's start with the verb 'to eat'.")
else:
    print("That was a yes, right?")

print("Do you know that the Maltese verbs don't have the infinitive form?")
time.sleep(3)
print("What you see in the dictionaries is \033[1mmamma - 'he did'\033[0m form. For \033[3m'to eat'\033[0m mamma is \033[1m'kiel'\033[0m.")
time.sleep(5)
print("We will learn how to conjugate the verb 'kiel' one person at a time. You will have to write in Maltese too.")
time.sleep(2)

def countdown():
    for i in range(5, -1, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Let's start with the present tense, affirmative cases")

countdown()
time.sleep(2)

# Verb forms with subject, correct verb, and English translation
verb_forms = [
    ("Jiena", "niekol", "I eat"),
    ("Inti", "tiekol", "You eat (singular)"),
    ("Huwa", "jiekol", "He eats"),
    ("Hija", "tiekol", "She eats"),
    ("Aħna", "nieklu", "We eat"),
    ("Intom", "tieklu", "You eat (plural)"),
    ("Huma", "jieklu", "They eat")
]
# Learning loop
for subject, correct_form, translation in verb_forms:
    print(f"\n{subject}: {correct_form}. {translation}.")  # Show the correct answer first
    time.sleep(2)
    user_input = input(f"{subject} ")  # Ask for it again
    print(f"Your answer was: {subject} {user_input.rstrip('.')}.")
    time.sleep(2)
    if user_input.rstrip('.').strip() == correct_form:
        print(f"Eżatt: {subject} {correct_form}. Prosit!")
    else:
        print(f"Le. {subject} {correct_form}.")
    time.sleep(2)

print("\nYou learned the present tense, affirmative conjugation of the verb 'kiel'. Prosit!")
time.sleep(2)
print("Now, let's practice in again. It's quiz time.")

while True:

    countdown()

# Randomize the order
    random.shuffle(verb_forms)

# Score tracking
    score = 0

# Quiz loop
    for subject, correct_form, translation in verb_forms:
        print(f"\n{subject}:        . {translation}.")
        time.sleep(2)
        answer = input(f"{subject} ")
        print(f"Your answer was: {subject} {answer.rstrip('.')}.")
        time.sleep(2)
        if answer.rstrip('.').strip() == correct_form:
            print(f"Eżatt: {subject} {correct_form}. Prosit!")
            score += 1
        else:
            print(f"Le. {subject} {correct_form}.")
        time.sleep(2)

    print("\nYou learned the present tense, affirmative conjugation of the verb 'kiel'. Prosit!")
    print(f"\nYou got {score} out of {len(verb_forms)} correct.")
    if score == 7:
        print(f"Are you a genius, {your_name}?")
    elif score >= 5:
        print(f"Prosit, {your_name}!")
    else:
        print(f"You need to learn a bit more, {your_name}.");

    time.sleep(2)

    end_input = input("\nType 'exit' to end the program, or press Enter to try again: ").strip().lower()
    if end_input == "exit":
        print("Goodbye!")
        break
    else:
        print("Restarting the quiz...\n")
        time.sleep(1)