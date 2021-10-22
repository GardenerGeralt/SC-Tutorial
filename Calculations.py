from math import *
import input_parameters as i


def downR(bp, swa, h, psa, RP, MP):     # calculate generated data rate
    ps = 2 * h * tan(radians(psa / 60) / 2)     # [m] pixel size
    G = 6.674e-11       # [m3/kg/s2] gravitational constant
    g = G * MP / ((RP + h) ** 2)    # [m/s^2] gravitational acceleration at orbit
    v = sqrt(g * (RP + h))          # [m/s] orbit velocity, assuming a circular orbit
    sw = 2 * h * tan(radians(swa) / 2)      # [m] swath width (field of view width
    R_G = bp * sw * v / (ps ** 2)       # [bps] generated data rate
    return R_G


def SNR(P, R, T_s, L_l, L_r, L_a, G_t, G_r, L_s, L_pr):
    k = 228.6       # Boltzmann constant
    snr = P + L_l + G_t + L_a + G_r + L_s + L_pr + L_r + k - R - T_s    # [dB]
    return snr


def dB(value, Xref=1):   # Convert any value to decibels
    X = 10 * log(value / Xref, 10)      # [dB]
    return X


def mid_calc(de, f_d, D_t, D_r, eta, e_t_t, e_t_r):    # intermediate calculations

    # misc values:
    S = sqrt((i.RE + de) ** 2 - i.RE ** 2)   # [m] max s/c <-> ground station distance
    c = 3e8                                 # [m/s] speed of light
    wavelen = c / (f_d * 1e9)               # [m] signal wavelength

    # gains:
    G_t = dB(eta * (pi * D_t / wavelen) ** 2)       # [dB] transmitting antenna gain
    G_r = dB(eta * (pi * D_r / wavelen) ** 2)       # [dB] receiving antenna gain

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
    nums = mid_calc(i.de, i.f, i.D_t, i.D_r, i.eta, i.e_t_t, i.e_t_r)      # perform intermediate calculations
    R_G = 8000 #downR(i.bp, i.swa, i.h, i.psa, i.RP, i.MP)        # [bps] generated data rate
    R = R_G * i.D_C / i.T_DL                    # [bps] required data rate
    snr_rec = SNR(dB(i.P), dB(R), dB(i.T_s), dB(i.L_l), dB(i.L_r), i.L_a,
                  nums[0], nums[1], nums[2], nums[3])
    margin = snr_rec - i.snr_req
    table = {"Transmitter Power": round(dB(i.P), 3),
             "Transmitter loss factor": round(dB(i.L_l), 3),
             "Receiver loss factor": round(dB(i.L_r), 3),
             "Transmitting antenna gain": round(nums[0], 3),
             "Receiving antenna gain": round(nums[1], 3),
             "Transmission path loss": round(i.L_a, 3),
             "Space loss": round(nums[2], 3),
             "Total pointing loss": round(nums[3], 3),
             "Required data rate": round(dB(R), 3),
             "System noise temperature": round(dB(i.T_s), 3)
             }
    return snr_rec, margin, table
