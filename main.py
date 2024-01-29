import cv2
from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide2.QtGui import QPixmap, QImage, QImageReader
from Interface import *  
import qdarkstyle
from PySide2 import QtCore
import random 
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PySide2.QtGui import QIcon


progress_val = 0

class MainForm(QWidget, Ui_Form):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        #self.widget_0.rpb_setBarStyle('Pizza')
        for i in range(7):  
            self.widget_0.rpb_setBarStyle('Pizza')
            getattr(self, f'widget_{i}').rpb_setBarStyle('Pizza')  # Scale to 0-100


        # ANIMATE THE PROGRESS
        # ADD A TIMER TO CHANGE PROGRESS VALUES
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_prediction)  
        self.timer.timeout.connect(self.update_video_stream)

        # Change all progresses to zero on start
        QtCore.QTimer.singleShot(0, lambda: self.widget_0.rpb_setValue(0))

        # Initialize webcam (not activated immediately)
        self.video_capture = None

        # Set up a timer to update the video stream
        self.webcam_timer = QTimer(self)
        self.webcam_timer.timeout.connect(self.update_video_stream)
        self.webcam_timer.start(60)  

        self.runBtn.clicked.connect(self.start_webcam)
        self.model = tf.keras.models.load_model('C:/Users/21379/Desktop/Master VMI 2024/Interaction Homme Machine/ProjetIhm/ResNet-50.h5')
        self.emotions = ['Angry', 'Disgusted', 'Fearful', 'Happy', 'Sad', 'Surprised', 'Neutral']
        self.cascPath = 'C:/Users/21379/Desktop/Master VMI 2024/Interaction Homme Machine/IHM Project/haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(self.cascPath)
        if self.face_cascade.empty():
            print("Erreur : Impossible de charger le classificateur de visages !")
        else:
            print("Le classificateur de visages a été chargé avec succès !")    

    def start_webcam(self):
        if self.video_capture is None:
            # Initialize webcam when the "Run" button is pressed
            self.video_capture = cv2.VideoCapture(0)  
            print("Webcam activated!")

            # Start the timer for progress bar animation when webcam is activated
            self.timer.start(30)
    def reset_all_progress(self):
        for i in range(7):
            getattr(self, f'widget_{i}').rpb_setValue(0)
    def update_prediction(self):
        if self.video_capture is not None:
            ret, frame = self.video_capture.read()  
            if not ret:
                print("Error reading frame")
                return

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(
                gray_frame,
                scaleFactor=1.1,
                minNeighbors=4,
                minSize=(30, 30)
            )
            if(len(faces)<= 0 ):
                print('No Face Detected !')
                self.reset_all_progress()
            else:
                for (x, y, w, h) in faces:
                    ROI_gray = gray_frame[y:y + h, x:x + w]
                    emotion = self.preprocess_input(ROI_gray)
                    prediction = self.model.predict(emotion)
                    #print(prediction)

                    # Update each progress bar with the respective emotion probability
                    for i in range(7):  # Assuming that we have 7 emotions (Because we are using FER2013 DataSet)
                        probability_prob = prediction[0][i]
                        getattr(self, f'widget_{i}').rpb_setValue(int(probability_prob * 100))  # Scale to 0-100
                        progress_value = int(probability_prob * 100)
                        # Change progress bar color to green if value exceeds 50%
                        if progress_value > 50:
                            getattr(self, f'widget_{i}').rpb_setLineColor((255, 0, 0))
                        else: 
                            getattr(self, f'widget_{i}').rpb_setLineColor((0, 255, 0))

                    

    def preprocess_input(self, image):
        img_width = 197
        img_height = 197
        image = cv2.resize(image, (img_width, img_height))  
        ret = np.empty((img_height, img_width, 3))  
        ret[:, :, 0] = image
        ret[:, :, 1] = image
        ret[:, :, 2] = image

        x = np.expand_dims(ret, axis=0)  
        mean = np.mean(x)
        std = np.std(x)
        x -= mean
        x /= std

        return x

    def update_video_stream(self):
        if self.video_capture is not None:
            
            ret, frame = self.video_capture.read()

            if ret:
                # Convert the frame from BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to QImage
                height, width, channel = rgb_frame.shape
                bytes_per_line = 3 * width
                q_image = QImage(rgb_frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

                
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
    mainWindow.setWindowTitle("Facial Expression Recognition")
    mainWindow.setWindowIcon(QIcon('icon.png'))
    mainWindow.show()
    sys.exit(app.exec_())
