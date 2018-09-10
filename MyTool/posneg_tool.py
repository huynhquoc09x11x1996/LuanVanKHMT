# Written by Huynh Quoc 10/09/2018
# To use this tool you have to install some libs suchas: opencv-contrib-python,
# numpy ,python2x, python3x Following the command line format to use this tool:
#Type this statement: python posneg_tool.py 'source image path' 'pos to save positive image' 'neg to save negative image'

import numpy as np
import cv2
import sys
import os

windowName = "LuanVanKHMT_ObjectMarker"
ix, iy = -1, -1
index = 0
frame = None
drawing = False
list_path = []


def isImagePath(input_path):
    return input_path[len(input_path) - 4:len(input_path)] in ['.png', '.jpg', '.bmp']


def onMouse(event, x, y, flags, param):
    global ix, iy, drawing, index, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(frame, (ix, iy), (x, y), (255, 0, 0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        index += 1
        cv2.rectangle(frame, (ix, iy), (x, y), (0, 255, 0), 1)
        print("Rect", (ix, iy), (x, y))
        cropped = frame[iy:y, ix: x]
        background = np.copy(frame)
        background[iy:y, ix: x] = 0
        # cv2.imshow("ROI", cropped)
        # cv2.imshow("Background", background)
        cv2.imwrite(positive_path + "POS_{:08}_IMG.jpg".format(index), cropped)
        cv2.imwrite(negative_path + "NEG_{:08}_IMG.jpg".format(index), background)
    cv2.imshow(windowName, frame)


cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback(windowName, onMouse)

try:

    source_path = sys.argv[1]
    positive_path = sys.argv[2]

    negative_path = sys.argv[3]

    if (len(source_path) and len(positive_path) and len(negative_path)) > 3:  # input params tu command lin

        static_source_path = str(source_path).rstrip(
            str(source_path).split('/')[-1])  # rstrip remove object nhap vao => get path not contain folder
        folder_name_source = str(source_path).split('/')[-1]  # get folder name in param
        for _, path in enumerate(os.listdir(static_source_path)):
            list_path.append(static_source_path + path)
        list_path.remove(list_path[0])
        while not (cv2.waitKey(1) & 0xFF == ord('q')):
            path = list_path[index]
            frame = cv2.imread(path, cv2.IMREAD_COLOR)
            cv2.imshow(windowName, frame)
        cv2.destroyAllWindows()

    else:
        print("Check your folder path, it maybe is wrong!")
except:
    print "Unexpected error:", sys.exc_info()
