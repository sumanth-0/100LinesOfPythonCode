import sys, time
import numpy as np
import sevseg  # ton module sevseg.py

def tic_tac_signal(freq=1.0, samples=8):
    """Génère un petit signal sinusoïdal (ex : 8 points)."""
    t = np.linspace(0, 1, samples)
    signal = np.sin(2 * np.pi * freq * t)
    return signal

def fourier_matrix(N):
    """Construit la matrice de Fourier NxN."""
    n = np.arange(N)
    k = n.reshape((N, 1))
    omega = np.exp(-2j * np.pi * k * n / N)
    return omega

def dft_matrix(signal):
    """Calcule la DFT en utilisant une multiplication matricielle."""
    N = len(signal)
    F = fourier_matrix(N)
    X = np.dot(F, signal)
    return X

try:
    while True:
        print('\n' * 60)
        currentTime = time.localtime()

        hours = str(currentTime.tm_hour % 12 or 12)
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Affichage des chiffres 7 segments
        hTop, hMid, hBot = sevseg.getSevSegStr(hours, 2).splitlines()
        mTop, mMid, mBot = sevseg.getSevSegStr(minutes, 2).splitlines()
        sTop, sMid, sBot = sevseg.getSevSegStr(seconds, 2).splitlines()

        print(hTop + '   ' + mTop + '   ' + sTop)
        print(hMid + ' * ' + mMid + ' * ' + sMid)
        print(hBot + ' * ' + mBot + ' * ' + sBot)
        print()

        # --- Partie Fourier matricielle ---
        signal = tic_tac_signal(freq=1.0, samples=8)
        X = dft_matrix(signal)

        magnitude = np.round(np.abs(X), 2)
        phase = np.round(np.angle(X), 2)

        print("Signal =", np.round(signal, 2))
        print("Magnitude FFT =", magnitude)
        print("Phase FFT =", phase)
        print('Press Ctrl-C to quit.')

        # Attente d'une nouvelle seconde
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    print('\nDigital Clock (Fourier Matrix Version)')
    sys.exit()
