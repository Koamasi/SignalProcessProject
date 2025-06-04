import warnings
from typing import Any, Tuple

from numpy import ndarray


def ensureLowHigh(level: int) -> dict[str, list[Any]]: #确定并拆分低频与高频部分
    warnings.warn('', DeprecationWarning)
    result = {'Low':[], 'High':[]}
    return result

def normalize(weight: dict[str, list[float]]) -> dict[str, list[float]]: #权重归一化
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


# TODO 融合部分需要重写
def custom_weight_fuse(coeffs: list[list[Any]], weight: dict[str, list[float]]) -> list[Any]: #自定义权重融合
    fused_coeffs = []; weight_norm = normalize(weight)

    for i in range(len(coeffs)):
        if i:
            fused_coeffs.append(

            )
        else:
            fused_coeffs.append(
                sum([weight_norm['Low'][j] * coeffs[j][0] for j in range(len(coeffs))])
            )
    return fused_coeffs

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