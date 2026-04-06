# Lens_Distortion_corrector
Lens distortion correction for video using OpenCV.

# 렌즈 왜곡 보정 프로그램입니다.
OpenCV를 이용해서 영상 왜곡을 보정합니다

사용법
1. 체스판을 출력하여 "수평에 가까운곳"에 부착한뒤 영상을 다양한 각도에서 촬영후 data폴더안에 저장합니다.
   (적어도 영상의 1/3이상은 체스판으로 채우시는것을 권장합니다.)
2. camera_calibration.py 파일의
   VIDEO_FILE(체스보드 파일이름)
   SAMPLE_RATE({SAMPLE_RATE}프레임마다 샘플추출)
   BOARD_ROWS(행방향 내부코너수)
   BOARD_COLS(열방향 내부코너수)를 수정합니다
3. camera_calibration.py 실행
4. 성공적으로 캘리브레이션이 되었다면 K.npy, dist_coeff.npy 파일 생성
5. distortion_correction.py 실행


현재 첨부된 영상의 카메라 캘리브레이션 결과
K = [575.2420, 0.0000, 625.6805], [0.0000, 583.4794, 324.6198], [0.0000, 0.0000, 1.0000]
RMSE = 1.386496
fx = 575.2353,  fy=583.4667,  cx = 625.6735,  cy=324.6171


