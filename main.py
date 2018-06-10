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
        self.pushButton_plot.clicked.connect(self.pushButton_plot_clicked)

        self.show()


    @pyqtSlot()
    def pushButton_plot_clicked(self):
        end_time = float(self.lineEdit_time.text())
        amp = float(self.lineEdit_amp.text())

        my_signal = SignalGen()
        my_signal.time, my_signal.x = my_signal.create_data(end_time, amp)
        my_signal.x_filtered = my_signal.smooth(my_signal.x, 9)
        my_signal.x_filtered = my_signal.smooth(my_signal.x_filtered, 5)
        my_signal.plot_signal(my_signal.time, my_signal.x, my_signal.x_filtered)





if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Hello")

    window = MainWindow()
    app.exec_()