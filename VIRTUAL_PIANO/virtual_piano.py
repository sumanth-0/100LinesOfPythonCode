import pygame
import time

# Initialize pygame mixer for sound playback
pygame.init()
pygame.mixer.init()

# Define piano keys and corresponding sound files
keys = {
    'a': 'notes/c.wav',
    's': 'notes/d.wav',
    'd': 'notes/e.wav',
    'f': 'notes/f.wav',
    'g': 'notes/g.wav',
    'h': 'notes/a.wav',
    'j': 'notes/b.wav',
    'k': 'notes/c_high.wav',
}

def load_sounds():
    sounds = {}
    for key, file in keys.items():
        sounds[key] = pygame.mixer.Sound(file)
    return sounds

def play_piano():
    sounds = load_sounds()
    print("Press keys (A, S, D, F, G, H, J, K) to play notes. Press 'Q' to quit.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key == 'q':
                    print("Exiting virtual piano.")
                    return
                if key in sounds:
                    sounds[key].play()
                    time.sleep(0.3)  # Delay to avoid overlapping sounds

if __name__ == "__main__":
    play_piano()
