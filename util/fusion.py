import warnings
from idlelib.debugger_r import restart_subprocess_debugger
from typing import Any, Tuple, TypeVar

import cv2
import numpy as np
from numpy import ndarray

T = TypeVar('T', list[ndarray], list[list[ndarray]])


def ensureLowHigh(level: int) -> dict[str, list[Any]]: #确定并拆分低频与高频部分
    warnings.warn('', DeprecationWarning)
    result = {'Low':[], 'High':[]}
    return result

def weight_normalize(weight: dict[str, list[float]]) -> dict[str, list[float]]: #权重归一化
    result = {'Low': [], 'High': []}

    if sum(weight['Low']) == 1:
        result['Low'] = result['Low'] + weight['Low']
    else:
        weight_sum_Low = sum(weight['Low'])
        for i in weight['Low']:
            result['Low'].append(i/weight_sum_Low)

    if sum(weight['High']) == 1:
        result['High'] = result['High'] + weight['High']
    else:
        weight_sum_High = sum(weight['High'])
        for i in weight['High']:
            result['High'].append(i/weight_sum_High)

    return result


def custom_weight_fuse(coeffs: list[list[Any]], weight: dict[str, list[float]], level: int) -> list[Any]: #自定义权重融合
    fused_coeffs = []; weight_norm = weight_normalize(weight)

    for i in range(len(coeffs)):
        fused_coeffs.append(
            [
            weight_norm['Low'][i] * coeffs[i][0],
            (
                (weight_norm['High'][i] * coeffs[i][j][k]) for k in range(3)
            )
        ] for j in range(min(1, level), level)
        )
    return fused_coeffs


def max_abs(data: T, is_low: bool) -> T:
    result = []

    if is_low:
        stacked = np.stack(data, axis=1)
        abs_value = np.abs(stacked)
        max_index = np.argmax(abs_value, axis=0)
        result = np.choose(max_index, stacked)
    else:
        for i in range(3):
            prestack = [j[i] for j in data]
            stacked = np.stack(prestack)
            abs_value = np.abs(stacked)
            max_index = np.argmax(abs_value, axis=0)
            result.append(np.choose(max_index, stacked))

    return result

# TODO  写你妈
# FIXME
def max_energy(data: T, is_low: bool, window: int = 5) -> T:
    result = []

    if is_low:
        result.append(np.maximum(data))
    else:
        H = _fuse_subband([j[i] for j in data])
        V = _fuse_subband([j[i] for j in data])
        D = _fuse_subband([j[i] for j in data])

        for i in zip(data):
            for j in range(3):
                H = _fuse_subband()
                result.append()
    return result


def _fuse_subband(subband: list[ndarray], window_size: int) -> ndarray:
    result = np.zeros_like(subband[0]); height, width = subband[0].shape
    radius = window_size // 2
    pad_sb = [cv2.copyMakeBorder(i, radius, radius, radius, radius, cv2.BORDER_REFLECT) for i in subband]
    roi = []

    for y in range(radius, height+radius):
        for x in range(radius, width+radius):
            for i in range(len(subband)):
                roi = [pad_sb[i][y-radius:y-radius+1, x-radius:x+radius+1]]

            energy = [np.sum(np.abs(i)) for i in roi]

            result[x-radius, y-radius] = subband[np.argmax(energy)][y-radius, x-radius]

    return result


[
    array(
        [
            [1, 2, 3],
            [1, 2, 3]
        ]
    )
]

[
    array(
        [
            [3., 6.]
        ]
    ),
    (
        array([[0., 0.]]),
        array([[-1.,  0.]]),
        array([[0., 0.]])
    )
]

[
    array(
        [
            [9.]
        ]
    ),
    (
        array(
            [
                [0.]
            ]
        ),
        array(
            [
                [-3.]
            ]
        ),
        array(
            [
                [0.]
            ]
        )
    ),
    (
        array(
            [
                [0., 0.]
            ]
        ),
        array(
            [
                [-1.,  0.]
            ]
        ),
        array(
            [
                [0., 0.]
            ]
        )
    )
]

[
    array([[18.]]),
    (array([[0.]]), array([[0.]]), array([[0.]])),
    (array([[0.]]), array([[-3.]]), array([[0.]])),
    (array([[0., 0.]]), array([[-1.,  0.]]), array([[0., 0.]]))
]