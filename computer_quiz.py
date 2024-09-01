# .lower() is the variables turn into a lower case string

score = int()

print("Are u ready to play a computer quiz?")

user_start = str(input("Yes or no?\n")).lower()


if user_start == "yes" or user_start == "y":
    ans_one = input("What does GPU stand for?\n").lower()
    if ans_one == 'graphic processing unit':
        score += 1

    else:
        print("incorrect")

    ans_two = input("What does CPU stand for?\n").lower()
    if ans_two == 'central processing unit':
        print("correct\n")
        score += 1
    else:
        print("incorrect")

else:
 quit()


print(f"\nYour score is: {score} , you got {score} of 2 max points.")
print("Thanks for playing!")
