import sys

def main():
    name = input('Please Enter your Name: ')
    end_game = 'a'
    while end_game != 'q':
        print(f'{name}, please press q to quit!')
        end_game = input('> ')
    quit_game('Thanks for Playing.')

def quit_game(message):
    sys.exit(message)

if __name__ == "__main__":
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     quit_game('Keyboard Interrup Detected')
    main()