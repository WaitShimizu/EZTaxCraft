#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ノートブッククラス定義

Author: Shimizu
Date: 2024/3/10
"""

import sys
from tkinter import ttk

sys.path.append('.')
from eztc_window_widget.eztc_widget import Widget


class Notebook(Widget):
    """ノートブッククラス
        NOTE: ttkパッケージのNotebookモジュールを利用する
    """
    def __init__(self, parent_widget) -> None:
        """コンストラクタ

        Args:
            parent_widget (tk.Tk): 親ウィジェット
        """
        widget = ttk.Notebook(parent_widget)
        super().__init__(widget)

    def add_tab(self, tab_obj: ttk.Frame, text_str:str='') -> None:
        """タブを追加する

        Args:
            tab_obj (_type_): タブオブジェクト
        """
        self.widget.add(tab_obj, text=text_str)
