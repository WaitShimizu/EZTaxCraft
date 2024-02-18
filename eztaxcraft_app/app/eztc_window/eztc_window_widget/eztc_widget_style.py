#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
画面ウィジェット用のスタイルクラス定義

Author: Shimizu
Date: 2024/2/12
"""

from tkinter import ttk


class Style:
    """スタイルクラス
        NOTE: ttkパッケージのButtonモジュールを利用する
    """
    def __init__(self, widget_name: str) -> None:
        self.widget_name = widget_name
        self.style = ttk.Style()

    def set_style(self, style_name: str, font: tuple) -> None:
        """スタイルを設定する

        Args:
            style_name (str): スタイル名
            font (tuple): 設定するフォント情報
        """
        self.style.configure(style_name, font=font)
