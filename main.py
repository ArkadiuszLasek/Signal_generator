from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow
from SignalGen import SignalGen

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)

        # Setup operations.
        self.pushButton_plot_signal.clicked.connect(self.pushButton_plot_signal_clicked)

        self.show()


    @pyqtSlot()
    def pushButton_plot_signal_clicked(self):
        end_time = float(self.doubleSpinBox_end_time.value())
        amp = float(self.doubleSpinBox_amp.value())
        sampling_rate = int(self.spinBox_sampling_rate.value())
        freq = float(self.doubleSpinBox_freq.value())

        my_signal = SignalGen()
        my_signal.time, my_signal.x = my_signal.create_data(sampling_rate, end_time, amp, freq)

        if self.checkBox_add_noise.isChecked() == True:
            noise_amp = float(self.doubleSpinBox_noise_amp.value())
            std_deviation = float(self.doubleSpinBox_noise_deviation.value())

            my_signal.x_noise = my_signal.create_noise_data(my_signal.x, my_signal.time, noise_amp, std_deviation)
            my_signal.plot_signal(my_signal.time, my_signal.x_noise)
        else:
            my_signal.plot_signal(my_signal.time, my_signal.x)





if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Signal Generator")

    window = MainWindow()
    app.exec_()