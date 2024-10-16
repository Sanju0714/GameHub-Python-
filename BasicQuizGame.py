def check_ans(que, answer):
    global score
    still_answering = True
    attempt = 0
    while still_answering and attempt < 3:
        if que.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_answering = False
        else:
            if attempt < 2:
                que = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess Correct Answer")
que1 = input(" Who developed the Python language? ")
check_ans(que1, "Guido van Rossum")
que2 = input(" What is the correct extension of the Python file? ")
check_ans(que2, ".py")
que3 = input("What do we use to define a block of code in Python language? ")
check_ans(que3, "Indentation")
print("Your total score is "+ str(score))
