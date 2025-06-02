from typing import Any


def ensureLowHigh(level: int) -> dict[str, list[Any]]: #确定并拆分低频与高频部分
    result = {'Low':[], 'High':[]}
    return result


def advLowMaxHigh(coeffs: dict[str, list[Any]]) -> list[Any]: #低频平均高频取大策略
    fused_coeffs = []

    for i in range(len(coeffs)):
        if i:
            fused_coeffs.append([np.maximum(coeffs[i][j], coeffs[i][j]) for j in range(len(coeffs[i]))])
    return fused_coeffs