name = input("Enter your name: ")
age = int(input("Enter your age: "))
state = input("Enter your state: ")

    # Check if the user is eligible to vote
if age >= 18:
        print("You are eligible to vote.")
        vote = input("Enter the candidate you want to vote for: ")
        print("\nThank you for voting!")
        # Display user information along with their vote
        print("\nVoter Information:")
        print("Name:", name)
        print("Age:", age)
        print("State:", state)
        print("Voted for:", vote)
else:
        print("Sorry, you are not eligible to vote.")
