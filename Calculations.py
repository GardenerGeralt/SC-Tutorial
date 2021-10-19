from math import *
import input_parameters as i


def SNR(P, R, T_s, L_l, L_r, L_a, G_t, G_r, L_s, L_pr):
    k = 228.6       # Boltzmann constant
    snr = P + L_l + G_t + L_a + G_r + L_s + L_pr + L_r + k - R - T_s    # [dB]
    return snr


def dB(value, Xref=1):   # Convert any value to decibels
    X = 10 * log(value / Xref, 10)      # [dB]
    return X


def mid_calc(h, f_d, D_t, D_r, eta, e_t_t, e_t_r):    # intermediate calculations

    # misc values:
    R_E = 6371e3                            # [m] Earth's radius
    S = sqrt((R_E + h) ** 2 - R_E ** 2)     # [m] max s/c <-> ground station distance
    c = 3e8                                 # [m/s] speed of light
    wavelen = c / (f_d * 1e9)               # [m] signal wavelength

    # gains:
    G_t = 20 * log(D_t, 10) + 20 * log(f_d, 10) + 17.8      # [dB] transmitting antenna gain
    G_r = dB(eta * (pi * D_r / wavelen) ** 2)               # [dB] receiving antenna gain

    # half-power angles:
    hpa_t = 21 / (f_d * D_t)    # [deg] transmitting antenna half-power angle
    hpa_r = 21 / (f_d * D_r)    # [deg] receiving antenna half-power angle
    e_t_r = e_t_r * hpa_r       # [deg] ground station pointing offset

    # losses:
    L_s = (wavelen / (4 * pi * S)) ** 2     # [-] space loss
    L_s = dB(L_s)                           # [dB] space loss now in decibels
    L_p_t = - 12 * (e_t_t / hpa_t) ** 2     # [dB] transmitting antenna pointing loss
    L_p_r = - 12 * (e_t_r / hpa_r) ** 2     # [dB] receiving antenna pointing loss
    L_pr = L_p_t + L_p_r                    # [dB] total pointing loss

    return G_t, G_r, L_s, L_pr


def mrgn():
    nums = mid_calc(i.h, i.f, i.D_t, i.D_r, i.eta, i.e_t_t, i.e_t_r)      # perform intermediate calculations
    R = i.R_G * i.D_C / i.T_DL
    snr_rec = SNR(dB(i.P), dB(R), dB(i.T_s), dB(i.L_l), dB(i.L_r), i.L_a,
                  nums[0], nums[1], nums[2], nums[3])
    print(f'The S/N received is {round(snr_rec, 2)}dB.')
    margin = snr_rec - i.snr_req
    return margin
