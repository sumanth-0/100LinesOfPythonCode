import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os
import keyboard

def load_audio(file_path):
    """Load audio file and return sample rate and data."""
    data, sample_rate = sf.read(file_path)
    return data, sample_rate

def generate_ascii_visualizer(data, sample_rate):
    """Generate ASCII art based on audio data."""
    # Normalizing the audio data
    data = data / np.max(np.abs(data))
    
    # ASCII characters used for visualization
    ascii_chars = '@%#*+=-:. '
    ascii_len = len(ascii_chars)

    # Create a figure for plotting
    plt.ion()
    fig, ax = plt.subplots()

    # Create a continuous loop to visualize the audio
    for i in range(0, len(data), sample_rate // 10):  # Update every 0.1 seconds
        # Get a segment of audio data
        segment = data[i:i + sample_rate // 10]
        if len(segment) < sample_rate // 10:
            break
        
        # Create a list to hold the ASCII representation
        ascii_output = []
        
        # Convert segment to ASCII
        for sample in segment:
            idx = int((sample + 1) / 2 * (ascii_len - 1))  # Normalize sample to ASCII index
            ascii_output.append(ascii_chars[idx])
        
        # Clear the axis
        ax.clear()
        
        # Create a string representation for the current frame
        visual_frame = ''.join(ascii_output)
        ax.text(0.5, 0.5, visual_frame, fontsize=8, ha='center', va='center')
        ax.axis('off')  # Turn off axes
        
        # Update the display
        plt.pause(0.1)
        
        # Break if 'q' is pressed
        if keyboard.is_pressed('q'):
            break

    plt.ioff()
    plt.show()

def main():
    """Main function to run the ASCII Music Visualizer."""
    audio_file = input("Enter the path to the audio file: ")
    if not os.path.exists(audio_file):
        print("File not found. Please enter a valid path.")
        return
    
    data, sample_rate = load_audio(audio_file)
    generate_ascii_visualizer(data, sample_rate)

if __name__ == "__main__":
    main()
