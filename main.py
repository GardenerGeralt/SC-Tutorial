# Run file for Link Budget Tool

from Calculations import mrgn


def main():
    print(f'The link margin is {round(mrgn(), 2)}dB.')


if __name__ == '__main__':
    main()
