import warnings
from typing import Any


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


def advLowMaxHigh(coeffs: dict[str, list[Any]], weight: dict[str, list[float]]) -> list[Any]: #自定义权重融合
    fused_coeffs = []; weight_norm = normalize(weight)

    for i in range(len(coeffs)):
        if i:
            fused_coeffs.append(

            )
    return fused_coeffs