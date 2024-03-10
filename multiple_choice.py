def create_multiple_choice_question(answer, question, a, b, c, d):
    multiple_choice_question = {
        "Answer": answer,
        "Question": question,
        "A": a,
        "B": b,
        "C": c,
        "D": d
    }

    return multiple_choice_question

def ask_question(question):
    print(question["Question"])
    print("a) " + question["A"])
    print("b) " + question["B"])
    print("c) " + question["C"])
    print("d) " + question["D"])

    answer = input("Enter Answer: ")
    if answer == question["Answer"]:
        print("Correct!")
    else:
        print("Incorrect!")


question = create_multiple_choice_question("C", "What is 1 + 1?", "1", "3", "2", "4")
ask_question(question)