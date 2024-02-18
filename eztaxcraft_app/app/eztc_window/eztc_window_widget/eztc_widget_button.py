#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリのTOP画面クラス定義

Author: Shimizu
Date: 2024/2/11
"""

import tkinter as tk
from tkinter import ttk


class Button:
    """ボタンクラス
        NOTE: ttkパッケージのButtonモジュールを利用する
    """
    def __init__(self, widget_name: str, parent_widget: tk.Tk, text: str, style: str) -> None:
        """コンストラクタ

        Args:
            name (str): ウィジェット名
            parent_widget (tk.Tk): 配置する親ウィジェットオブジェクト
            text (str): ウィジェットに表示するテキスト
            style (str): ウィジェットに適用するスタイル名
        """
        self.widget_name = widget_name
        self.parent_widget = parent_widget
        self.text = text
        self.style = style

    def create_widget(self) -> ttk.Button:
        """ボタンウィジェット生成

        Returns:
            ttk.Button: 生成されたボタンウィジェット
        """
        return ttk.Button(self.parent_widget, text=self.text,
                          style= self.style, command=self.clicked)

    def clicked(self) -> None:
        """ボタンクリック時の処理実行
        """
        print(f'[{self.name}] Clicked.')
