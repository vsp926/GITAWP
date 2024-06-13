from random import randint
import pdb


class InvalidInputException(Exception):
    pass


def GetUserInput():
    try:
        first_number = int(input("Enter the First Number "))
        last_number = int(input("Enter the last Number "))
        if first_number == last_number:
            raise InvalidInputException("First Number should not be same as Last Number ")
        elif first_number > last_number:
            raise InvalidInputException("First Number should not be less than the last Number")
        else:
            user_guess = int(input("What number do you think the system will choose? "))
            if (user_guess >= first_number) and (user_guess <= last_number):
                print("Input Validation passed")
                verify_result(first_number, last_number, user_guess)
            else:
                raise InvalidInputException("Your guess should be between the first number and last number")
    except InvalidInputException as e:
        print(e)
        return None, None, None
    except Exception as e:
        print("Invalid Input, Enter only Whole Number")


def verify_result(first_number, last_number, user_guess):
    system_guess = randint(first_number, last_number)
    if user_guess == system_guess:
        print(f"Your Guess is Correct! The System also predicted {system_guess}")
    else:
        print((f"Your guess is incorrect, the system said {system_guess} "))


def main():
    flag = 1
    while flag == 1:
        GetUserInput()
        user_choice = input("Well Played, Press 'y' to play again, any other key to exit! ")
        if user_choice != 'y':
            flag = 0

if __name__ == "__main__":
    main()
