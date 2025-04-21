import json
import random
import os

FLASHCARDS_FILE = 'FlashCards.json'


def load_flashcards():
    if not os.path.exists(FLASHCARDS_FILE):
        return {}
    with open(FLASHCARDS_FILE, 'r') as file:
        return json.load(file)


def save_flashcards(data):
    with open(FLASHCARDS_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def teacher_mode():
    flashcards = load_flashcards()
    print("\n--- Teacher Mode ---")
    while True:
        key = input("Enter question (or type 'exit' to stop): ")
        if key.lower() == 'exit':
            break
        value = input("Enter answer: ")
        flashcards[key] = value
        print("Flashcard added.\n")
    save_flashcards(flashcards)
    print("All flashcards saved!")


def student_mode():
    flashcards = load_flashcards()
    if not flashcards:
        print("No flashcards found. Add some in Teacher Mode first.")
        return

    print("\n--- Student Mode ---")
    keys = list(flashcards.keys())
    random.shuffle(keys)
    score = 0
    streak = 0

    for key in keys:
        print(f"Question: {key}")
        answer = input("Your answer: ").strip()
        if answer.lower() == flashcards[key].lower():
            print("Correct!")
            streak += 1
            bonus = streak - 1  # 1 point per streak after the first correct answer
            score += 1 + bonus
            if bonus:
                print(f"Streak bonus! +{bonus} point(s)")
        else:
            print(f"Incorrect! The correct answer was: {flashcards[key]}")
            streak = 0
        print(f"Current Score: {score}\n")

    print(f"Final Score: {score}")


def main():
    while True:
        print("\n--- Flash Card App ---")
        mode = input("Choose mode: (1) Teacher, (2) Student, (3) Exit: ")
        if mode == '1':
            teacher_mode()
        elif mode == '2':
            student_mode()
        elif mode == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == '__main__':
    main()
