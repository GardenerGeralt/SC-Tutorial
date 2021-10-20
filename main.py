# Run file for Link Budget Tool

from Calculations import mrgn
import input_parameters as i


def main():
    i.ud = input("Uplink or Downlink? (u/d): ")
    if i.ud == "u":
        _ = i.e_t_t, i.e_t_r
        i.e_t_r, i.e_t_t = _

    it = input("Iterate? (y/n) ")
    if it == "y":
        print("If link does not close, what would you like to change?")
        q = input(
            "For power reply 'p', for receiving antenna diameter - 'dr', for transmitting antenna diameter - 'dt'\n"
            "for other - 'o': ")
        while True:
            snr_rec, margin, tb = round(mrgn()[0], 2), round(mrgn()[1], 2), mrgn()[2]
            if margin >= 3:
                print(f'The S/N received is {round(snr_rec, 2)}dB.')
                print(f'The link margin is {margin}dB.')
                tb = str(tb).split(",")
                for n in range(len(tb)):
                    print(tb[n])
                break
            else:
                if q == "p":
                    i.P += 1
                    print(f"The power is now {round(i.P, 1)} [W]")
                elif q == "dr":
                    i.D_r += 0.1
                    print(f"The D_r is now {round(i.D_r, 1)} [m]")
                elif q == "dt":
                    i.D_t += 0.1
                    print(f"The D_t is now {round(i.D_t, 1)} [m]")
                else:
                    break


if __name__ == '__main__':
    main()
