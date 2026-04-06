import cv2 as cv
import numpy as np
import os


VIDEO_FILE  = 'data/chessboard.mp4'       #재생할파일

if os.path.exists("K.npy") and os.path.exists("dist_coeff.npy"): #K.npy and dist_coeff.npy파일이 있으면 불러오고 없으면 기본값사용
    K = np.load("K.npy")                       
    dist_coeff = np.load("dist_coeff.npy")
    print("Calibration files have loaded")
else:
    K = np.array([[575.2420, 0.0000, 625.6805], 
                  [0.0000, 583.4794, 324.6198],
                  [0.0000, 0.0000, 1.0000]])
    dist_coeff = np.array([-0.13892567, 0.09029208, -0.01009389, -0.00294471, 0.01753342])
    print("Calibration file not found. using default values")

video = cv.VideoCapture(VIDEO_FILE)
if not video.isOpened():
    print("Can't open the file")
    exit()

map1, map2 = None, None     #좌표 매핑 테이블 변수 초기화

while True:
    valid, img = video.read()
    if not valid:
        break

    if map1 is None or map2 is None:
        h, w = img.shape[:2]    
        map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (w,h), cv.CV_32FC1) # 왜곡 보정연산속도를 위한 픽셀 이동 맵를 만듦
        
    undistorted = cv.remap(img, map1, map2, interpolation = cv.INTER_LINEAR) # 생성된 맵을 마탕으로 왜곡 보정

    cv.imshow("Original", img)
    cv.imshow("Undistorted", undistorted)

    if cv.waitKey(30) == 27:        #ESC 누르면 종료
        break
video.release()
cv.destroyAllWindows()

