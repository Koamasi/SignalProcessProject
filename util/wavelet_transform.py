import cv2
import numpy as np
import pywt


def _coeffs(img, coeffs_name, level):
    coeffs = pywt.wavedec2(cv2.imread(img, 0), str(coeffs_name), level=level)
    return coeffs


def _coeffs_re(coeffs, coeffs_name):
    img = pywt.waverec2(coeffs, coeffs_name)
    return img