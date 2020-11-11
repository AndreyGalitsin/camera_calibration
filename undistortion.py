import cv2
import numpy as np


def undistortion(immage, cam_number):
    mtx, dist = get_params(cam_number)
    h, w = immage.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
    dst = cv2.remap(immage, mapx, mapy, cv2.INTER_LINEAR)
    x,y,w,h = roi
    undist_image = dst[y:y+h, x:x+w]

    return undist_image

def get_params(cam_number):
    calibration_params = ['./camera_' +str(cam_number)+ '/cameraMatrix.txt', './camera_' +str(cam_number)+ '/cameraDistortion.txt']
    mtx = np.loadtxt(calibration_params[0], dtype=float, delimiter=',')
    dist = np.loadtxt(calibration_params[1], dtype=float, delimiter=',')
    dist = np.reshape(dist, (1, 5))

    return mtx, dist


if __name__ == '__main__':
    path_to_img = './distorted_img.jpg'
    immage = cv2.imread(path_to_img)
    cam_number = 1
    undist_image = undistortion(immage, cam_number)
    cv2.imwrite("./calibresult.png", undist_image)

    
