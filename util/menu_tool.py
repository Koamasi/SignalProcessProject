from typing import AnyStr

import pywt
from terminal_layout.extensions.choice import Choice, StringStyle
from terminal_layout import Fore, LayoutCtl, TableRow, TextView
from terminal_layout.extensions.input import InputEx


class data:
    wave_name = pywt.families()


def add_index(lst: list[AnyStr]) -> list[AnyStr]:
    return ['['+str(i)+']'+lst[i] for i in range(len(lst))]


def Choice_init(title: str, choices: list[str]) -> Choice:
    return Choice(
        title,
        choices,
        icon_style=StringStyle(Fore.lightblue),
        selected_style=StringStyle(Fore.lightblue)
    )


def Input_init(info: str, id: str) -> LayoutCtl:
    return LayoutCtl.quick(
        TableRow,
        TextView('', info),
        TextView(id, '')
    )


def confirm_text(
        decomposition: str,
        fusion: str,
        wavelet: str=None,
        level: int=None,
        weight: list[int]=None
) -> list[str | None]:
    return [decomposition, fusion, wavelet, level, weight]


def confirm_choice(lst: list[str | None]) -> Choice:
    return Choice_init(
        '请进行最后的确认',
        lst + ['一切就绪']
    )


class menu_questions:
    decomposition_select = Choice_init(
        '请选择分解策略',
        [
            '[1]小波分解',
            '[2]拉普拉斯金字塔分解(NYI)'
        ]
    )

    wavelet_select = Choice_init(
        '请选择小波',
        add_index(data.wave_name)
    )

    level_input = Input_init('请输入分解层数', 'level')

    input_decomposition_level = InputEx(level_input)

    fusion_select = Choice_init(
        '请选择融合策略',
        [
            '[1]绝对值取大',
            '[2]自定义加权平均',
            '[3]区域能量取大(NYI)',
            '[4]区域方差取大(NYI)'
        ]
    )

    weight_input = Input_init('请输入融合权重 支持非归一化权重输入', 'weight')

    input_fusion_weight = InputEx(weight_input)