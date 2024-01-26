# -*- coding: utf-8 -*-

import cv2
from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide2.QtGui import QPixmap, QImage, QImageReader
from Interface import *  # Replace 'your_ui_module_name' with the actual name of your UI module
import qdarkstyle

class MainForm(QWidget, Ui_Form):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.widget.rpb_setBarStyle('Pizza')


        # Initialize webcam (not activated immediately)
        self.video_capture = None

        # Set up a timer to update the video stream
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_video_stream)
        self.timer.start(30)  # Update every 30 milliseconds (adjust as needed)

        self.runBtn.clicked.connect(self.start_webcam)

    def start_webcam(self):
        if self.video_capture is None:
            # Initialize webcam when the "Run" button is pressed
            self.video_capture = cv2.VideoCapture(0)  # Use the default camera (index 0)
            print("Webcam activated!")

    def update_video_stream(self):
        if self.video_capture is not None:
            # Read a frame from the webcam
            ret, frame = self.video_capture.read()

            if ret:
                # Convert the frame from BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to QImage
                height, width, channel = rgb_frame.shape
                bytes_per_line = 3 * width
                q_image = QImage(rgb_frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

                # Convert QImage to QPixmap and set it as the label's pixmap
                pixmap = QPixmap.fromImage(q_image)
                self.videoLabel.setPixmap(pixmap)

    def closeEvent(self, event):
        # Release the webcam when the application is closed
        if self.video_capture is not None:
            self.video_capture.release()
        event.accept()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainForm()
    mainWindow.show()
    sys.exit(app.exec_())
