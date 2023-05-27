import cv2
import numpy as np
import argparse
import os

import time

def fileExists(filename):
    """Judge wether the file exists!
    """
    if filename in ('', None):
        raise ValueError("The input file can't be '' or None.")
    return os.path.isfile(filename)

def buildPyramid(image, maxleval):
    """Build image pyramid for level [0,...,maxlevel]
    """
    imgpyr = [image]
    aux = image
    for i in range(0,maxleval):
        aux = cv2.pyrDown(aux)
        imgpyr.append(aux)

    imgpyr.reverse()
    return imgpyr


def fastTemplateMatchPyramid(src_refimg, src_tplimg, maxleval):
    """Do fast template matching using matchTemplate plus an approximation
    through pyramid construction to improve it's performance on large images.
    """
    results = []

    ## Change BGR to Grayscale
    gray_refimg = cv2.cvtColor(src_refimg, cv2.COLOR_BGR2GRAY)
    gray_tplimg = cv2.cvtColor(src_tplimg, cv2.COLOR_BGR2GRAY)

    ## Build image pyramid
    refimgs = buildPyramid(gray_refimg, maxleval)
    tplimgs = buildPyramid(gray_tplimg, maxleval)

    ## Do template match
    for idx in range(0, maxleval+1):
        refimg = refimgs[idx]
        tplimg = tplimgs[idx]

        # On the first level performs regular template matching.
        # On every other level, perform pyramid transformation and template matching
        # on the predefined ROI areas, obtained using the result of the previous level.
        # Uses contours to define the region of interest and perform TM on the areas.
        if idx == 0:
            result = cv2.matchTemplate(refimg, tplimg, cv2.TM_CCORR_NORMED)
        else:
            mask = cv2.pyrUp(threshed)
            mask8u = cv2.inRange(mask, 0, 255)
            contours = cv2.findContours(mask8u, cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_NONE)[-2]

            tH, tW = tplimg.shape[:2]
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                src = refimg[y:y+h+tH, x:x+w+tW]
                result = cv2.matchTemplate(src, tplimg, cv2.TM_CCORR_NORMED)

        T, threshed = cv2.threshold(result, 0.90, 1., cv2.THRESH_TOZERO)
        results.append(threshed)

    return threshed
    #return results


def fastTemplateMatch(refname, tplname, maxleval = 5):
    """Fast template match.
    """
    ## Read the image pairs.
    if fileExists(refname) == False:
        raise IOError("Input file not found.")
    if fileExists(tplname) == False:
        raise IOError("Input file not found.")

    refimg = cv2.imread(refname)
    tplimg = cv2.imread(tplname)
    cv2.imwrite("cat.png",refimg)

    ## Call fastTemplateMatchInPyramid()
    start = time.time()
    result = fastTemplateMatchPyramid(refimg, tplimg, maxleval)
    print(time.time()-start)
    ## Analysis the result
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)
    if maxval > 0.9:
        pt1 = maxloc
        pt2 = (maxloc[0] + tplimg.shape[1], maxloc[1] + tplimg.shape[0])
        print("Found the template region: {} => {}".format(pt1,pt2))
        dst = refimg.copy()
        cv2.rectangle(dst, pt1, pt2, (0,255,0), 2)
        #cv2.imshow("Result", dst)
        #cv2.imwrite("template_matching_result.png",dst)
        #cv2.waitKey()
    else:
        print("Cannot find the template in the origin image!")


if __name__ == '__main__':

    refname = "./data/Text_flipped.bmp"
    tplname = "./data/text_pattern.bmp"
    maxlevel = 5

    ## call the function

    fastTemplateMatch(refname, tplname, maxlevel)
