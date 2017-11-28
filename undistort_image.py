# You should replace these 3 lines with the output in calibration step
import sys
import cv2
import numpy as np
DIM=(160, 120)
K=np.array([[351.3423711426583, 0.0, 306.0760867449579], [0.0, 328.68909732703247, 240.24349825435272], [0.0, 0.0, 1.0]])
D=np.array([[-0.05461643821913291], [-0.029600365868638304], [0.05454842556489924], [-0.026340680583395275]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)