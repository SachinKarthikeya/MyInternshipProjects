def ask_question(question, options, correct_answer, user_score):
    print(question)
    for option in options:
        print(option)

    user_choice = input("Choose Your option: ")
    if user_choice.lower() == correct_answer:
        print("You are Correct!")
        return user_score + 1
    else:
        print("You are Incorrect!")
        return user_score

def play_quiz():
    print("Welcome to the General Knowledge Quiz Game!!")

    user_decision = input("Do you want to play?: ")

    if user_decision.lower() == 'yes':
        print("Let us start the quiz!")

        user_score = 0
        total_score = 8

        user_score = ask_question("1. What is the capital city of India?", ["a. Mumbai", "b. Hyderabad", "c. New Delhi", "d. Chennai"], "c", user_score)
        user_score = ask_question("2. Who is known as the 'Megastar' in Telugu cinema?", ["a. Balakrishna", "b. Chiranjeevi", "c. Venkatesh", "d. Nagarjuna"], "b", user_score)
        user_score = ask_question("3. What is the national currency of India?", ["a. Rupee", "b. Dollar", "c. Euro", "d. Yen"], "a", user_score)
        user_score = ask_question("4. Which planet is known as the 'Red Planet'?", ["a. Mars", "b. Earth", "c. Saturn", "d. Jupiter"], "a", user_score)
        user_score = ask_question("5. In which year did the Titanic sink?", ["a. 1905", "b. 1912", "c. 1920", "d. 1931"], "b", user_score)
        user_score = ask_question("6. Who painted the Mona Lisa?", ["a. Vincent van Gogh", "b. Michalangelo", "c. Pablo Picasso", "d. Leonardo da Vinci"], "d", user_score)
        user_score = ask_question("7. Which element has the elemental symbol 'O'?", ["a. Oxygen", "b. Nitrogen", "c. Hydrogen", "d. Carbon"], "a", user_score)
        user_score = ask_question("8. What is the largest desert in the world?", ["a. Atacama", "b. Gobi", "c. Sahara", "d. Thar"], "c", user_score)

        print(f"Your final score for this quiz is {user_score} out of {total_score}.")
        print("Thank You for playing the Quiz. See you next time.")

    elif user_decision.lower() == 'no':
        print("You Quit the game.")
        quit()
    else:
        print("Invalid choice.")
        quit()

play_quiz()