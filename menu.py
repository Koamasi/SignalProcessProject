import warnings
from tkinter import Tk, filedialog
from typing import Any
from goto import with_goto

import pywt
from util import menu_tool as mt


# TODO 弃用类 需要获取多图路径 分解方案 小波名称 分解层数 融合方案 若自定义融合需获取权重
# TODO 可视化进度 存在确认阶段 预设（未完成
menu_control = mt.menu_questions


@with_goto
def menu_start() -> list[Any]:
    result = []

    label .decomposition
    decomposition = menu_control.decomposition_select.get_choice()

    match int(decomposition[1]):
        case 1:
            wavelet = menu_control.wavelet_select.get_choice()
        case 2:
            print('尚未完成'); goto .decomposition

    return result


if __name__ == '__main__':
    menu_start()