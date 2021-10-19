# Run file for Link Budget Tool

from Calculations import mrgn
import input_parameters as i


def main():
    print("If link does not close, what would you like to change?")
    q = input("For power reply 'p', for receiving antenna diameter - 'dr', for transmitting antenna diameter - 'dt'\n"
              "for other - 'o': ")
    while True:
        snr_rec, margin = round(mrgn()[0], 2), round(mrgn()[1], 2)
        if margin >= 3:
            print(f'The S/N received is {round(snr_rec, 2)}dB.')
            print(f'The link margin is {margin}dB.')
            break
        else:
            if q == "p":
                i.P += 1
                print(f"The power is now {i.P} [W]")
            elif q == "dr":
                i.D_r += 0.1
                print(f"The D_r is now {i.D_r} [m]")
            elif q == "dt":
                i.D_t += 0.1
                print(f"The D_t is now {i.D_t} [m]")
            else:
                break


if __name__ == '__main__':
    main()
