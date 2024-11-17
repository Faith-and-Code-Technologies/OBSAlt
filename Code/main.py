import cv2, mss, time
import numpy as np
from threading import Thread
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from ui_main import Ui_MainWindow as main_ui

FPS = 60.0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_ui()
        self.ui.setupUi(self)

        self.recording = False
        self.preview_running = True
        self.thread = None
        self.out = None

        # Connect buttons
        self.ui.startrec.clicked.connect(self.start_recording)
        self.ui.stoprec.clicked.connect(self.stop_recording)

        # Start live preview
        self.start_preview()

    def start_preview(self):
        # Start the preview in a separate thread.
        self.preview_running = True
        self.thread = Thread(target=self.update_preview, daemon=True)
        self.thread.start()

    def start_recording(self):
        # Begin recording frames.
        if not self.recording:
            self.recording = True
            # Set up the video writer
            sct = mss.mss()
            monitor = sct.monitors[1]
            width, height = monitor["width"], monitor["height"]
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.out = cv2.VideoWriter('screen_recording.mp4', fourcc, FPS, (width, height))

    def stop_recording(self):
        # Stop recording frames.
        self.recording = False
        if self.out:
            self.out.release()
            self.out = None

    def update_preview(self):
        # Continuously update the screen preview and record frames if recording.
        sct = mss.mss()
        monitor = sct.monitors[1]
        while self.preview_running:
            start_time = time.time()
            
            # Capture screen
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            # Always update preview
            self.display_preview(frame)

            # Save frames if recording
            if self.recording and self.out:
                self.out.write(frame)

            # Maintain frame rate (60 FPS)
            time.sleep(max(0, (1 / FPS) - (time.time() - start_time)))  # 1/60 = 0.016 seconds per frame

    def display_preview(self, frame):
        # Display the captured frame in the GUI.
        h, w, _ = frame.shape
        if h > 0 and w > 0:
            qt_image = QImage(frame.data, w, h, w * 3, QImage.Format_BGR888)
            self.ui.preview.setPixmap(QPixmap.fromImage(qt_image).scaled(1280, 720, Qt.KeepAspectRatio))

    def closeEvent(self, event):
        # Stop threads and release resources on application close.
        self.preview_running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
        if self.out:
            self.out.release()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


#Double Speed Recordings!#