from typing import Any

import cv2
import pywt
import numpy as np


def _coeffs(imgPath: str, coeffs_name: str, level:int) -> list[Any]: #读取图像并进行小波分解
    coeffs = pywt.wavedec2(cv2.imread(imgPath, 0), str(coeffs_name), level=level)
    return coeffs


def _coeffs_re(coeffs: list[Any], coeffs_name: str) -> np.ndarray: #逆小波分解并还原为图像
    img = np.clip(pywt.waverec2(coeffs, coeffs_name), 0, 255).astype(np.uint8)
    return img