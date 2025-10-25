import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print("Wave Interference Simulator")
print("Provide details for two sine waves.")

try:
    f1 = float(input("Frequency for wave A: "))
    a1 = float(input("Amplitude for wave A: "))
    f2 = float(input("Frequency for wave B: "))
    a2 = float(input("Amplitude for wave B: "))
except ValueError:
    print("Error: Input must be numeric.")
    exit()

plot_window, (wave1_plot, wave2_plot, sum_plot) = plt.subplots(3, 1)
plot_window.suptitle('Interference of Two Waves')
plt.subplots_adjust(hspace=0.6)

x_vals = np.linspace(0, 10, 1000)

wave1_line, = wave1_plot.plot([], [], color='dodgerblue')
wave2_line, = wave2_plot.plot([], [], color='crimson')
sum_line, = sum_plot.plot([], [], color='forestgreen')

wave1_plot.set_xlim(0, 10)
wave1_plot.set_ylim(-2.5, 2.5)
wave1_plot.set_title('Wave A')
wave1_plot.grid(True, linestyle='--')

wave2_plot.set_xlim(0, 10)
wave2_plot.set_ylim(-2.5, 2.5)
wave2_plot.set_title('Wave B')
wave2_plot.grid(True, linestyle='--')

sum_plot.set_xlim(0, 10)
sum_plot.set_ylim(-2.5, 2.5)
sum_plot.set_title('Resultant Wave (A + B)')
sum_plot.grid(True, linestyle='--')
sum_plot.set_xlabel('Distance')

def update_plot(frame_num):
    time_step = frame_num * 0.1
    
    y_vals_1 = a1 * np.sin(f1 * x_vals + time_step)
    y_vals_2 = a2 * np.sin(f2 * x_vals + time_step)
    y_vals_sum = y_vals_1 + y_vals_2
    
    wave1_line.set_data(x_vals, y_vals_1)
    wave2_line.set_data(x_vals, y_vals_2)
    sum_line.set_data(x_vals, y_vals_sum)
    
    return wave1_line, wave2_line, sum_line

ani = animation.FuncAnimation(plot_window, update_plot, interval=25, blit=True)

plt.show()