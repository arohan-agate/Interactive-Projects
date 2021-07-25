def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


# -------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# -------------------------

# Credit for the questions goes to: 'historyextra.com/magazine/history-quiz-questions-list/'
questions = {
    "Where was the first British colony in the Americas?: ": "D",
    "Which 19th-century woman became the first qualified medical doctor?: ": "A",
    "The Chinese Exclusion Act was signed into law by which US president in 1882?: ": "C",
    "By what nickname is Edward Teach better known?: ": "B",
    "Which queen had the shortest reign of Henry VIII’s six wives?: ": 'C',
    "In which country is the Bay of Pigs?: ": 'D',
    "Who was the first human to journey into space?: ": 'B',
    "Julius Caesar was assassinated on 15 March 44 BC, a date now often known by what term?: ": 'A',
    'Which American president was in power during the ‘Black Thursday’ Wall Street crash?: ': 'D',
    'During 1963, in Washington DC, Martin Luther King Jr gave his famous ‘I have a dream’ speech on the steps of which famous landmark?: ': 'A '
}

options = [["A. Jamestown", "B. Plymouth", "C. Newfoundland", "D. Roanoke"],
           ["A. Elizabeth Blackwell", "B. Florence Nightingale", "C. Elizabeth Garrett Anderson", "D. Ann Preston"],
           ["A. Andrew Jackson", "B. Theodore Roosevelt", "C. Chester A. Arthur", "D. Grover Cleveland"],
           ["A. Captain Hook", "B. Blackbeard", "C. Calico Jack", "D. Black Bart?"],
           ['A. Catherine of Aragon', 'B. Anne Boleyn', 'C. Anne of Cleves', 'D. Catherine Parr'],
           ['A. the United Kingdom', 'B. Jamaica', 'C. the United States', 'D. Cuba'],
           ['A. Buzz Aldrin', 'B. Yuri Gagarin', 'C. Neil Armstrong', 'D. Alan Shepard'],
           ['A. Ides of March', 'B. April Fools Day', 'C. Christmas', 'D. New Years Eve'],
           ['A. Franklin Roosevelt', 'B. Harry Truman', 'C. Calvin Coolidge', 'D. Herbert Hoover'],
           ['A. the Lincoln Memorial', 'B. the Washington Monument', 'C. U.S. Capitol Building', 'D. the White House']
           ]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")
