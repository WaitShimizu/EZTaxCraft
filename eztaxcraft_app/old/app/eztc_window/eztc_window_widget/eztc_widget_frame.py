#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
フレームクラス定義

Author: Shimizu
Date: 2024/3/12
"""

import sys
from tkinter import ttk

sys.path.append('.')
from eztc_window_widget.eztc_widget import Widget


class Frame(Widget):
    """フレームクラス
        NOTE: ttkパッケージのFrameモジュールを利用する
    """
    def __init__(self, parent_widget) -> None:
        """コンストラクタ

        Args:
            parent_widget (tk.Tk): 親ウィジェット
        """
        widget = ttk.Frame(parent_widget)
        super().__init__(widget)
