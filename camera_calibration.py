import cv2 as cv
import numpy as np


VIDEO_FILE = 'data/chessboard.mp4'            # 파일 이름
SAMPLE_RATE = 30                    # N프레임마다 샘플추출
BOARD_ROWS = 7                      # 체스보드 행방향 내부코너 수
BOARD_COLS = 10                     # 체스보드 열방향 내부코너 수

board_pattern = (BOARD_COLS,BOARD_ROWS)

obj_pts = np.zeros((BOARD_COLS*BOARD_ROWS,3), np.float32)   # 체스보드 코너 개수의 3D 좌표 배열 0으로 초기화
obj_pts[:, :2] = np.mgrid[0:BOARD_COLS, 0:BOARD_ROWS].T.reshape(-1,2)   # X, Y 좌표를 격자 형태로 채움(Z = 0 으로 유지)

obj_points = []                     # 3D 기준점을 쌓아둘 리스트
img_points = []                     # 2D 코너 좌표를 쌓아둘 리스트

video = cv.VideoCapture(VIDEO_FILE)
if not video.isOpened():
    print("Can't open the file")
    exit()

image_size = None                   # 이미지 크기(가로, 세로)
found_count = 0                     # 체스보드 인식에 성공한 프레임의 개수
frame_index = 0                     # 누적 프레임의 개수

while True:
    valid, img = video.read()
    if not valid:
        break
    
    frame_index += 1
    if frame_index % SAMPLE_RATE != 0:  # SAMPLE_RATE의 배수가 아닌 프레임은 건너뜀
        continue
    
    if image_size is None:
        image_size = (img.shape[1], img.shape[0])   #이미지 크기(가로, 세로) 저장

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 흑백으로 변환

    flags = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE   # 이진화, 정규화
    found, corners = cv.findChessboardCorners(gray,board_pattern, flags)    # 체스보드 코너 찾기

    display = img.copy()

    if found:
        
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)    # 최대 30번 반복, 오차 0.001이하면 종료
        corners = cv.cornerSubPix(gray, corners, (11,11), (-1, -1), criteria)   # 코너 위치를 더 정밀하게 다듬기

        obj_points.append(obj_pts)
        img_points.append(corners)
        found_count += 1

        cv.drawChessboardCorners(display, board_pattern, corners, found) # 찾은 코너를 화면에 표시
        print(f"    [{found_count}] frame {frame_index}: success")

    cv.imshow("Calibration", display)
    if cv.waitKey(1) == 27:     # ESC 누르면 종료
        break

video.release()
cv.destroyAllWindows()

if found_count < 5:
    print("At least 6 counts needed.")
    exit()

print(f"\nCalibrating with {found_count} samples")


RMSE, K, dist_coeff, _, _ = cv.calibrateCamera(obj_points, img_points, image_size, None, None)


print("## Camera Calibration Results ##")
print(f" * The number of applied images = {found_count}")
print(f" * RMS error = {RMSE:.6f}")
print(" * Camera matrix(K) =")
for row in K:
    print(f" [{row[0]:.4f}, {row[1]:.4f}, {row[2]:.4f}]")
print(f" * Distortion coefficient (k1, k2, p1, p2, k3, ...) = \n    {dist_coeff.flatten()}")
print(f" * fx = {K[0,0]:.4f},    fy={K[1,1]:.4f}")
print(f" * cx = {K[0,2]:.4f},    cy={K[1,2]:.4f}")


np.save("K.npy", K)
np.save("dist_coeff.npy", dist_coeff)
print("\n## Results saved as K.npy, dist_coeff.npy ##\n")