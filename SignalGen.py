import numpy as np
import matplotlib.pyplot as plt

class SignalGen():

    def __init__(self):
        self.time = None
        self.x = None
        self.x_filtered = None

    def smooth(self, y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth

    def create_data(self, end_time, amp):
        t = np.arange(0, end_time, 0.001)

        sinus = amp * np.sin(2*np.pi*2*t)
        noise = np.random.normal(0.0, 0.05, t.size)

        x = sinus + noise

        return t, x

    def plot_signal(self, t, x, x_filtered):
        plt.figure(figsize=(8,4))
        plt.plot(t, x, 'bo-', label='sinus', markersize=3.0)
        plt.plot(t, x_filtered, 'k', label='smoothed')
        plt.grid()
        plt.legend()
        plt.xlabel('time [s]')
        plt.ylabel('displacement [mm]')
        plt.show()

if __name__ == '__main__':
    end_time = 10
    amp = 2.0

    my_signal = SignalGen()
    my_signal.time, my_signal.x = my_signal.create_data(end_time, amp)
    my_signal.x_filtered = my_signal.smooth(my_signal.x, 9)
    my_signal.x_filtered = my_signal.smooth(my_signal.x_filtered, 5)
    my_signal.plot_signal(my_signal.time, my_signal.x, my_signal.x_filtered)