#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリのTOP画面クラス定義

Author: Shimizu
Date: 2024/2/11
"""

from tkinter import ttk


class Button:
    """ボタンクラス
        NOTE: ttkパッケージのButtonモジュールを利用する
    """
    def __init__(self, name: str, parent_widget, text: str, style: str) -> None:
        self.name = name
        # 配置する親ウィジェットオブジェクト
        self.parent_widget = parent_widget
        # ボタンウィジェットに設定するテキスト文字列
        self.text = text
        # 利用するスタイル
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

if __name__ == '__main__':
    top_window = TopWindow()
    top_window.initialize()
