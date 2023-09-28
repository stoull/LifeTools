
import cv2
import time
import numpy as np

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

class USBOpenVCCapture(object):
    def __init__(self):
        pass

    def captureImage(self):
        all_camera_idx_available = []

        for camera_idx in range(4):
            cap = cv2.VideoCapture(camera_idx)
            if cap.isOpened():
                print(f'Camera index available: {camera_idx}')
                all_camera_idx_available.append(camera_idx)
                cap.release()

        cam = cv2.VideoCapture(all_camera_idx_available[0])
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        cam.set(cv2.CAP_PROP_FPS, 25)

        for i in range(1):
            ret, image = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            #cv2.imshow('ImageTest', image)
            #k = cv2.waitKey(1)
            # if k != -1:
            #    break;
        cv2.imwrite('/home/pi/Shared/openCVCaptureImage-1.jpg', image)
        cam.release()
        #cv2.destroyAllWindows()

    def captureVideo(self):
        capture_duration = 60
        all_camera_idx_available = []

        for camera_idx in range(4):
            cap = cv2.VideoCapture(camera_idx)
            if cap.isOpened():
                print(f'Camera index available: {camera_idx}')
                all_camera_idx_available.append(camera_idx)
                cap.release()

        cam = cv2.VideoCapture(all_camera_idx_available[0])
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        cam.set(cv2.CAP_PROP_FPS, 20)

        #width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        width= 1280
        height= 720

        start_time = time.time()
        writer= cv2.VideoWriter('/home/pi/Shared/openCVCaptureImage-1.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 20, (width,height))
        # writer= cv2.VideoWriter('/home/pi/Shared/openCVCaptureImage-1.avi', cv2.VideoWriter_fourcc(*'XVID'), 25, (width,height))
        # 10s长度的视频
        while( int(time.time() - start_time) < capture_duration ):
            ret,frame= cam.read()
            if ret==True:
                writer.write(frame)
        cam.release()
        writer.release()
       #  cv2.destroyAllWindows()


if __name__ == '__main__':
    usbCapture = USBOpenVCCapture()
    usbCapture.captureVideo()
