def play_mini_golf():
    # Prompt the user for their name
    name = input("Welcome to GC mini golf! What is your name?\n")
    print(f"Hi, {name}!")

    # Prompt the user to choose 3 or 6 holes
    holes = int(input("Would you like to play 3 or 6 holes?\n"))

    # Determine the course par based on the number of holes chosen
    course_par = holes * 3

    # Initialize total score for the round
    total_score = 0

    # Prompt the user for the number of putts for each hole
    for i in range(holes):
        hole_number = i + 1
        par = 3
        putts = int(input(f"How many putts for hole {hole_number}? (par: {par})\n"))
        total_score += putts

    # Calculate the user's total par for the round
    user_score = total_score

    # Display the result based on the user's performance relative to par
    if user_score == course_par:
        print(f"Good game, {name}. Your total par was: {course_par - user_score}")
    elif user_score < course_par:
        print(f"Great job, {name}! Your total par was: -{course_par - user_score}")
    else:
        print(f"Nice try, {name}... Your total par was: +{user_score - course_par}")

if __name__ == "__main__":
    play_mini_golf()
