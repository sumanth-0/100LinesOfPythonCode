import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io import wavfile
from scipy import signal
from pathlib import Path


# ---------- (1) Optional test WAV generator ----------
def generate_test_wav(path='test.wav', sr=44100, duration=3.0):
    """Generate a short test tone WAV (sine + harmonics)"""
    t = np.linspace(0, duration, int(sr*duration), endpoint=False)
    audio = 0.6*np.sin(2*np.pi*220*t) + 0.25*np.sin(2*np.pi*440*t) + 0.1*np.sin(2*np.pi*880*t)
    audio *= (0.5 + 0.5*np.sin(2*np.pi*1.5*t))  # slow amplitude modulation
    audio = audio / np.max(np.abs(audio)) * 0.9
    wav = (audio * 32767).astype(np.int16)
    wavfile.write(path, sr, wav)
    print(f"✅ Generated test WAV at {path}")
    return path


# ---------- (2) Convert audio → bar magnitudes ----------
def audio_to_bar_envelope(wav_path, n_bars=64, n_fft=2048, hop_length=512):
    """Compute a time–frequency envelope reduced to n_bars bands."""
    sr, data = wavfile.read(wav_path)

    # convert to mono float32 [-1,1]
    if data.ndim > 1:
        data = data.mean(axis=1)
    data = data.astype(np.float32)
    data /= np.max(np.abs(data)) + 1e-9

    # STFT
    f, t, Zxx = signal.stft(data, fs=sr, nperseg=n_fft, noverlap=n_fft-hop_length, padded=False)
    mag = np.abs(Zxx)

    # guard: no STFT frames
    if mag.size == 0 or mag.shape[1] == 0:
        raise ValueError("STFT produced no frames — audio too short or STFT parameters incompatible with input length")

    mag_db = 20 * np.log10(mag + 1e-10)

    # normalize 0..1
    mag_db -= mag_db.min()
    mag_db /= mag_db.max() + 1e-9

    # group into n_bars (log spacing) — make lower bound robust
    freqs = f
    # choose a safe positive lower bound (avoid zero and handle tiny arrays)
    if freqs.shape[0] > 1:
        start_freq = max(freqs[1], 20.0)
    else:
        start_freq = max(freqs[0], 20.0)
    end_freq = max(freqs[-1], start_freq * 2.0)
    band_edges = np.geomspace(start_freq, end_freq, n_bars + 1)
    bars = np.zeros((n_bars, mag_db.shape[1]))

    for i in range(n_bars):
        low, high = band_edges[i], band_edges[i+1]
        idx = np.where((freqs >= low) & (freqs < high))[0]
        if len(idx) == 0:
            idx = [np.argmin(np.abs(freqs - (low+high)/2))]
        bars[i] = mag_db[idx].mean(axis=0)

    # smooth over time
    alpha = 0.3
    for i in range(1, bars.shape[1]):
        bars[:, i] = alpha * bars[:, i] + (1 - alpha) * bars[:, i-1]

    return sr, t, bars


# ---------- (3) Make animation ----------
def make_audio_bars_animation(wav_path, out_path='audio_bars.mp4', n_bars=64, fps=30):
    """Create and save bar animation reacting to sound amplitude."""
    sr, times, bars = audio_to_bar_envelope(wav_path, n_bars)
    n_frames = bars.shape[1]

    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.arange(n_bars)
    bar_container = ax.bar(x, bars[:, 0], width=0.8)

    ax.set_ylim(0, 1)
    ax.set_xlim(-0.5, n_bars - 0.5)
    ax.set_xlabel("Frequency band →")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Audio Reactive Bars: {Path(wav_path).name}")
    ax.set_xticks([])

    def update(frame):
        for rect, h in zip(bar_container, bars[:, frame]):
            rect.set_height(h)
        return bar_container

    interval = 1000 * (times[1] - times[0]) if len(times) > 1 else 1000 / fps
    ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=interval, blit=False)

    try:
        ani.save(out_path, writer="ffmpeg", fps=fps, bitrate=2000)
    except Exception:
        gif_path = str(Path(out_path).with_suffix('.gif'))
        ani.save(gif_path, writer='pillow', fps=fps)
        out_path = gif_path

    plt.close(fig)
    print(f"🎬 Saved animation to {out_path}")
    return out_path


# ---------- (4) Run example ----------
if __name__ == "__main__":
    # If you already have a WAV file, replace this line:
    wav_file = generate_test_wav("test.wav")

    # Create animation
    make_audio_bars_animation(wav_file, out_path="audio_bars.mp4", n_bars=64, fps=30)