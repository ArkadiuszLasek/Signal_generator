import numpy as np
import matplotlib.pyplot as plt

class SignalGen():

    def __init__(self):
        self.time = None
        self.x = None
        self.x_noise = None
        self.x_filtered = None

    def smooth(self, y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth

    def create_data(self, sampling_rate, end_time, amp, freq):
        delta_t = 1/sampling_rate
        t = np.arange(0, end_time, delta_t)

        sinus = amp * np.sin(2*np.pi*freq*t)

        x = sinus
        return t, x

    def create_noise_data(self, x, t, noise_amp, std_deviation):
        noise = noise_amp * np.random.normal(0.0, std_deviation, t.size)
        x_noisy = x + noise
        return x_noisy

    def plot_signal(self, t, x):
        plt.figure(figsize=(8,4))
        plt.plot(t, x, 'b', label='generated signal', markersize=3.0)
        plt.grid()
        plt.legend()
        plt.xlabel('time [s]')
        plt.ylabel('displacement [mm]')
        plt.show()

if __name__ == '__main__':
    sampling_rate = 1000
    end_time = 10
    amp = 2.0
    freq = 1.0

    my_signal = SignalGen()
    my_signal.time, my_signal.x = my_signal.create_data(sampling_rate, end_time, amp, freq)
    my_signal.plot_signal(my_signal.time, my_signal.x)

    noise_amp = 0.3
    std_deviation = 0.1
    my_signal.x_noise = my_signal.create_noise_data(my_signal.x, my_signal.time, noise_amp, std_deviation)
    my_signal.plot_signal(my_signal.time, my_signal.x_noise)