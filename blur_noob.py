import cv2 as cv
import numpy as np
import fourierssszz as fr


if __name__ == "__main__":
    img = cv.imread("./mushroom.png",cv.IMREAD_GRAYSCALE)
    #filter
    gaussian = np.array([
        [1 , 4 , 1],
        [4 , 16 ,4],
        [1 , 4,  1]
    ])
    # ทำให้ผลรวมออกมาเท่ากับ 1
    s = gaussian.sum()
    gaussian = gaussian / s
    
    img_blur = cv.filter2D(src=img, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    img_blur = cv.filter2D(src=img_blur, ddepth=-1, kernel=gaussian)
    cv.imshow("original", img)
    cv.imshow("brurhh", img_blur)
    cv.waitKey()
    cv.destroyAllWindows()