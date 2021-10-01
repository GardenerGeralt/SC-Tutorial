import math
from input_parameters import P, L_l, L_a, L_r, T_s

def SNR():
    k = 228.6       # Boltzmann constant
    snr = P + L_l + G_t + L_a + G_r + L_s + L_pr + L_r + k - R - T_s
    return snr

def decibel_converter(value, Xref):   #  Convert any value to decibels
    X = math.log(value/Xref, 10)
    return X