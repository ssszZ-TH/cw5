import cv2 as cv
import numpy as np
import fourierssszz as fr


def getgaussian():
    gaussian = np.array([
        [1, 4, 1],
        [4, 16, 4],
        [1, 4,  1]
    ])
    # ทำให้ผลรวมออกมาเท่ากับ 1
    s = gaussian.sum()
    gaussian = gaussian / s
    return gaussian

## วิธี deconvolution
if __name__ == "__main__":
    img=cv.imread("./mushroom.png",cv.IMREAD_GRAYSCALE)
    gaussian = getgaussian()
    img_freq = fr.imgToFrequency(img)
    gaussian_freq = fr.filterToFrequency(gaussian)
    blur_img = img_freq * gaussian_freq
    repaired_img = img_freq / gaussian_freq
    
    
    
    cv.imshow("original",img)
    cv.imshow("blur",blur_img)
    cv.imshow("repaired",repaired_img)