from random import randint

def default_roller():
    return ( randint(1,6), randint(1,6) )


def play_dice(roller=default_roller):
    while True:
        print('Enter r to roll or q to quit')
        choice = input('> ')

        if choice == 'q':
            print('OK, bye')
            break
        
        else:
            roll = roller()
            roller_str = ''
            for num in roll:
                roller_str += str(num) + " "
            print(f'*** {roller_str}***')

if __name__ == '__main__':
    rolls = [(4,),(3,)]

    def mock_roller():
        # return (4,3, 1, 1)
        return rolls.pop(0) if rolls else default_roller()
    
    play_dice(mock_roller)