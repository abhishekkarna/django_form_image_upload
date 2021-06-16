import cv2
import numpy as np

# red   = [0,0,255]
# green = [0,255,0]
# blue  = [255,0,0]
# white = [255,255,255]
# black = [0,0,0]


def proc_image(template, checkprint):
    # template = cv2.imread('left.png')
    # checkprint = cv2.imread('right.png')

    before_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(checkprint, cv2.COLOR_BGR2GRAY)
    before_gray = before_gray.astype(int)
    after_gray = after_gray.astype(int)
    diffimg = before_gray-after_gray
    checkprint = cv2.cvtColor(checkprint, cv2.COLOR_BGR2RGB)
    width, height, chan = checkprint.shape
    for x in range(width):
        for y in range(height):
            if diffimg[x, y] == 0:
                # Make it green because it's unchanged
                if checkprint[x, y][0] != 255 and checkprint[x, y][1] != 255 and checkprint[x, y][2] != 255:
                    checkprint[x, y] = (30, 255, 30)
            else:
                #print(before_gray[x, y] - after_gray[x, y])

                if diffimg[x, y] < 0:
                    checkprint[x, y] = (117, 216, 252)
    return checkprint
    # cv2.imshow('after', checkprint)
    #
    # cv2.waitKey(0)