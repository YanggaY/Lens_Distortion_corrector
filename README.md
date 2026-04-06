# Lens_Distortion_corrector

Lens distortion correction for video using OpenCV.<br>
---
*필요 환경*


*Numpy, openCV가 설치되어있지 않다면 아래 명령어를 통해 설치*


*pip install opencv-python numpy*

# 렌즈 왜곡 보정 프로그램입니다.
OpenCV를 이용해서 영상 왜곡을 보정합니다.

사용법
1. 체스판을 출력하여 "수평에 가까운 곳"에 부착한뒤 영상을 다양한 각도에서 촬영후 data폴더안에 저장합니다.<br>
   (적어도 영상의 1/3이상은 체스판으로 채우시고, AF는 고정으로 촬영합니다.)

   
2. camera_calibration.py 파일의<br>
   VIDEO_FILE    (체스보드 파일이름)<br>
   SAMPLE_RATE   (N프레임마다 샘플추출)<br>
   BOARD_ROWS    (행방향 내부코너수)<br>
   BOARD_COLS    (열방향 내부코너수)를 수정합니다.

   
3. camera_calibration.py 실행

   
4. 성공적으로 캘리브레이션이 되었다면 K.npy, dist_coeff.npy 파일 생성

   
5. distortion_correction.py 실행 (실행 중 ESC 키를 누르면 종료됨)

<br><br><br>
---
**현재 첨부된 영상의 카메라 캘리브레이션 결과**<br>(아이폰15pro 광각 + 안경렌즈(-2.5D)2개 중첩)


K = [575.2420, 0.0000, 625.6805], [0.0000, 583.4794, 324.6198], [0.0000, 0.0000, 1.0000]
RMSE = 1.386496


dist_coeff = [-0.13892567, 0.09029208, -0.01009389, -0.00294471, 0.01753342]


fx = 575.2353,  fy = 583.4667,  cx = 625.6735,  cy = 324.6171

<br><br><br>

---


**Requirements**

If Numpy and OpenCV are not installed, run the command below.

pip install opencv-python numpy

---
# Results
![Original](data/Orginal.png)
## Usage

1. Print a chessboard pattern, attach it to a nearly flat surface, and record a video from various angles. Save the video in the `data` folder.
   (Fill at least 1/3 of the frame with the chessboard, and keep AF fixed while recording.)

2. Edit the following variables in `camera_calibration.py`
   - `VIDEO_FILE`  — Video file name
   - `SAMPLE_RATE` — Sample every N frames
   - `BOARD_ROWS`  — Inner corners (rows)
   - `BOARD_COLS`  — Inner corners (cols)

3. Run `camera_calibration.py`

4. If calibration is successful, `K.npy` and `dist_coeff.npy` will be generated.

5. Run `distortion_correction.py` — Press `ESC` to exit.

---

## Calibration Results
(iPhone 15 Pro wide + 2x glasses lens (-2.5D))
