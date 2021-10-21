P = 100.        # [W] transmitter power
f = 8.4         # [GHz] signal frequency
L_l = 0.8       # [-] transmitter loss factor
L_r = 0.7       # [-] receiver loss factor
L_a = -0.040    # [dB] transmission path loss
D_t = 2.0       # [m] transmitting antenna diameter
D_r = 35.       # [m] receiving antenna diameter
eta = 0.55      # [-] antenna efficiency
de = 225e9    # [m] s/c distance to Earth
h = 400e3       # [m] s/c orbit altitude
e_t_t = 0.1     # [deg] transmitter pointing offset
e_t_r = 0.1     # [hpa_r] receiver pointing offset as proportion of receiver half power angle
bp = 8          # [bit/p] payload bits per pixel
swa = 10.       # [deg] swath width angle
psa = 0.1      # [arcmin] pixel size angle
D_C = 0.1         # [-] duty cycle
T_DL = 18/24     # [-] link time ratio
T_s = 135.      # [K] system noise temperature
snr_req = 10.5  # [dB] required SNR
RP = 3389.5e3     # [m] planet radius
MP = 6.39e23   # [kg] planet mass
RE = 6371e3     # [m] Earth's radius
ME = 5.972e24   # [kg] Earth's mass
# ignore this:
ud = 0
