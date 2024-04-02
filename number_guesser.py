def number_guesser():
    print("Welcome to the number guesser! Pick a number in your mind and I'll try to guess it!")
    ready = input("Are you ready? (yes or no): ")
    if ready == "yes":
        print("Great! Let's get started")
    else:
        print("Okay, come back when you're ready")
        return

    min_num = 1
    max_num = 100

    while True:
        guess = (min_num + max_num) // 2
        response = input(f"Is it {guess}? (yes or no): ")

        if response == "yes":
            print("YAY! I got it! Thanks for playing")
            break
        elif response == "no":
            response2 = input("Was the guess too high or too low? (too high or too low): ")
            if response2 == "too high":
                max_num = guess - 1
            elif response2 == "too low":
                min_num = guess + 1
            else:
                print("Invalid input! Please enter 'too high' or 'too low'.")

number_guesser()

