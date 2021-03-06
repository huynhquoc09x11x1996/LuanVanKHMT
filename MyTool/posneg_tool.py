# Written by Huynh Quoc 10/09/2018
# To use this tool you have to install some libs suchas: opencv-contrib-python,
# numpy ,python2x, python3x Following the command line format to use this tool: Type this statement: python
# posneg_tool.py 'source image path' 'pos to save positive image' 'neg to save negative image'
import time
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
    global ix, iy, drawing, index, frame, target_name
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(frame, (ix - 1, iy - 1), (x, y), (255, 0, 0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        index += 1
        cv2.rectangle(frame, (ix - 1, iy - 1), (x, y), (0, 255, 0), 1)
        print("Image:", index)
        cropped = frame[iy:y, ix: x]
        background = np.copy(frame)
        background[iy:y, ix: x] = 0
        target_name = str(int(time.time() * 1000.0))
        cv2.imwrite(positive_path + "IMG_" + target_name + ".jpg".format(index), cropped)
        cv2.imwrite(negative_path + "IMG_" + target_name + ".jpg".format(index), background)
    cv2.imshow(windowName, frame)


cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback(windowName, onMouse)


def getKeyEvent():
    return cv2.waitKey(1) & 0xFF


def isNumber(s):
    realType = int(1)
    if type(s) == type(realType):
        return True
    else:
        return False


try:
    old_index = int(sys.argv[1])
    source_path = sys.argv[2] if sys.argv[2][-1] == "/" else sys.argv[2] + "/"
    positive_path = sys.argv[3] if sys.argv[3][-1] == "/" else sys.argv[3] + "/"
    negative_path = sys.argv[4] if sys.argv[4][-1] == "/" else sys.argv[4] + "/"
    if (len(source_path) and len(positive_path) and len(negative_path)) > 3 and isNumber(
            old_index):  # input params tu command line ok
        index = old_index - 1
        static_source_path = str(source_path).rstrip(
            str(source_path).split('/')[-2])  # rstrip remove object nhap vao => get path not contain folder
        folder_name_source = str(source_path).split('/')[-2]  # get folder name in param
        for _, path in enumerate(os.listdir(static_source_path)):
            list_path.append(static_source_path + path)
        list_path.remove(list_path[0])

        while True:
            key = cv2.waitKey(1) & 0xFF
            path = list_path[index]
            frame = cv2.imread(path, cv2.IMREAD_COLOR)
            cv2.imshow(windowName, frame)
            if key == ord('q'):
                break
            elif key == 32:
                index += 1
            elif key == ord('r'):
                index -= 1
        cv2.destroyAllWindows()

    else:
        print("Kiem tra lai doi so dau vao, co le bi loi~!")
except:
    print("Unexpected error:", sys.exc_info())
