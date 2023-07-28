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
    gaussian_freq = fr.filterToFrequency(gaussian,s=img.shape)
    gaussian_mag = fr.filterfrequencyToMagnitude(gaussian_freq)
    
    blur_img_freq = img_freq * gaussian_mag
    repaired_img_freq = img_freq / gaussian_mag
    
    blur_img = fr.invertFourierTransform(blur_img_freq)
    repaired_img = fr.invertFourierTransform(repaired_img_freq)
    
    cv.imshow("original",img)
    cv.imshow("blur",blur_img)
    cv.imshow("repaired",repaired_img)
    
    cv.waitKey()
    cv.destroyAllWindows()