import cv2
from cv2 import aruco
import matplotlib.pyplot as plt
import time
import threading

def detect_markers(cv2_img):
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    ids = ids if ids is not None else []
    return ids, corners, rejectedImgPoints

def detect_marker_ids(cv2_img):
    ids, _, _ = detect_markers(cv2_img)
    return ids

def mpl_setup_plot_to_draw_detected_markers_over_image(img, ids, corners):
    frame_markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)
    plt.figure()
    plt.imshow(frame_markers)
    for i in range(len(ids)):
        c = corners[i][0]
        plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
    plt.legend()

class TelloVisionMarkerWatcher():
    def __init__(self, tello_object, freq = None, display= False):
        self.t = tello_object
        self.continue_watching = False
        self.freq = freq
        self.last_detected_marker_id = 0
        self.display = display
        self.thread = threading.Thread(target=self._thread_handler)
    
    def get_current_detected_ids(self):
        img = self.t.get_image()
        ids = detect_marker_ids(img)
        if len(ids):
            self.last_detected_marker_id = ids[0]
        return ids

    def get_last_detected_id(self):
        return self.last_detected_marker_id

    def _thread_handler(self):
        while self.continue_watching:
            img = self.t.get_image()
            ids, corners, rejected_image_points = detect_markers(img)
            if len(ids):
                self.last_detected_marker_id = ids[0][0]
            if self.display:
                mpl_setup_plot_to_draw_detected_markers_over_image(img, ids, corners)
                plt.ion()
                plt.pause(0.01)
                plt.show()
            if self.freq is not None:
                time.sleep(1 / self.freq)

    def enable_display(self):
        self.display = True

    def disable_display(self):
        self.display = False

    def start(self):
        self.continue_watching = True
        self.thread = threading.Thread(target=self._thread_handler)
        self.thread.start()

    def stop(self):
        if self.continue_watching:
            self.continue_watching = False
            self.thread.join()