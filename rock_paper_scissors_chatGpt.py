import random

choices = ['r', 'p', 's']

while True:
    try:
        # Get user input
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").strip().lower()

        # Check for invalid input using Exception
        if user not in choices:
            raise ValueError("Invalid choice! Please choose 'r', 'p', or 's'.")

        # PC choice
        pc = random.choice(choices)

        print(f"\nUser played : {user}")
        print(f"PC played   : {pc}\n")

        # Game logic
        if user == pc:
            print("It's a tie!")
        elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
            print("You won!")
        else:
            print("You lose!")

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

    except ValueError as err:
     
        print(f"{err}\n")
        continue

    except (KeyboardInterrupt, EOFError):
           
            print("\n\nGame interrupted. Goodbye!")
            break

print("-" * 30 + "\n")   



# import random

# choices = ['r', 'p', 's']

# while True:
#     # Get user input
#     user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").strip().lower()

#     # Check for invalid input
#     if user not in choices:
#         print("Invalid choice! Please choose 'r', 'p', or 's'.\n")
#         continue

#     # PC choice
#     pc = random.choice(choices)

#     print(f"\nUser played : {user}")
#     print(f"PC played   : {pc}\n")

#     # Game logic
#     if user == pc:
#         print("It's a tie!")
#     elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
#         print("You won!")
#     else:
#         print("You lose!")

#     # Ask to play again
#     play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
#     if play_again != 'yes':
#         print("Thanks for playing! Goodbye!")
#         break
      
#     print("-" * 30 + "\n")
    
    
         