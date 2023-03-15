import random


def play_again():
    response = ''
    while response not in ['y', 'n']:
        response = input('Do you want to play again? (\'y\' / \'n\')')
        if response.lower() == 'n':
            print('Good bye')
            return False
        elif response.lower() == 'y':
            print('Ok. here you go')
            return True


def start_game(start, end):
    generated_number = random.randint(start, end)
    user_input = ''
    count = 0
    while user_input != generated_number:
        if count < 5:
            user_input = input('Guess a number. Chance\'s left {}'.format(5 - count))
            if not user_input.isdigit():
                print('Invalid input. Guess must be an integer')
                continue
            elif int(user_input) > generated_number:
                print('Your guess is too high')
            elif int(user_input) < generated_number:
                print('Your guess is too low')

            elif int(user_input) == generated_number:
                print('Your guess is correct')
                if play_again():
                    break
                else:
                    return
        else:
            print('You have zero chance left. Try later')
            if play_again():
                count = 0
                continue
            else:
                break

        count += 1


start_game(1, 20)
