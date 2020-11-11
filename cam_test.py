# /usr/bin/env python

import cv2

def run_camera():
    #ls /dev | grep video
    #device = "/dev/video2"
    #device = "/dev/v4l/by-id/usb-046d_HD_Pro_Webcam_C920_B180D86F-video-index0"
    #device = "/dev/v4l/by-id/usb-046d_HD_Pro_Webcam_C920_B180D86F-video-index0"

    device = "/dev/video4"

    Cam = cv2.VideoCapture(device)
    Cam.set(cv2.CAP_PROP_BUFFERSIZE, 0)

    print(Cam.isOpened())

    counter = 0
    while 1:
        counter += 1
        ret, image = Cam.read()
        #image = cv2.resize(image, (1280, 720))

        if counter % 1 == 0:
            counter = 0
            if image is not None:
                print(image.shape)
                cv2.imshow("video", image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
            else:
                print("cannot receive img from camera")
                Cam = cv2.VideoCapture(device)
                time.sleep(0.01)
        else:
            continue

def read_img(path_to_img):
    imgage = cv2.imread(path_to_img)
    while 1:
        print(image.shape)
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break


if __name__ == '__main__':
    run_camera()
