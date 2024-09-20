import os
import sys


class Io:
    def __init__(self):
        self.attempts: int = 5

    @staticmethod
    def start() -> None:
        print('''
░██████╗░░██╗░░░░░░░██╗███████╗███╗░░██╗████████╗
██╔════╝░░██║░░██╗░░██║██╔════╝████╗░██║╚══██╔══╝
██║░░██╗░░╚██╗████╗██╔╝█████╗░░██╔██╗██║░░░██║░░░
██║░░╚██╗░░████╔═████║░██╔══╝░░██║╚████║░░░██║░░░
╚██████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░╚███║░░░██║░░░
░╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
        ''')
        print('''You can ask:
        1) Is card <name> weather resistant?
        2) What is known about the card <name>?
        3) Is close/ranged/siege combat affected by the weather? <special cards separated by coma>
        4) Is card <name> affected by the weather? <special cards separated by coma>
        5) Get card <name> strength. <special cards separated by coma>
        ''')
        print('For exit use Ctrl+D cause I\'m lazy af. And I don\'t wanna do this')

    def error(self) -> None:
        match self.attempts:
            case 5:
                print('Pay attention')
            case 4:
                print('You don\'t want it')
            case 3:
                print('Think about your family')
            case 2:
                print('I see you\'re testing me pal')
            case 1:
                print('It\'s the last one. I warned you')
                os.system("shutdown /r /t 1")
        self.attempts -= 1
        print(
            f'Invalid request. Be careful after {self.attempts} more invalid queries and the computer will explode or sth like that')

    @staticmethod
    def get_value() -> str:
        try:
            print('-' * 30)
            return input('Input request: ')
        except EOFError:
            sys.exit()
