#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリのTOP画面クラス定義

Author: Shimizu
Date: 2024/2/11
"""

import tkinter as tk
from tkinter import ttk

class TopWindow:
    """TOP画面クラス
    """

    def __init__(self, ) -> None:
        """コンストラクタ
        """
        # TOP画面のルートインスタンス生成
        self.root = tk.Tk()
        self.font = ("Meiryo", 9)
        # スタイルを定義
        self.style = ttk.Style()
        self.button1_style = 'button1.TButton'
        self.style.configure(self.button1_style, font=self.font)

    def initialize(self) -> None:
        """初期化処理
        """
        test1_button_text = 'テストボタン1'
        # 'テストボタン1'というスタイルにフォントを設定
        button1_instance = Button(test1_button_text, self.root,
                                  test1_button_text, self.button1_style)
        button1 = button1_instance.create_widget()
        button1.pack(side='top')
        self.root.mainloop()

    def __create_button(self, parent_widget, text_str: str, callback) -> ttk.Button:
        """ボタン生成

        Args:
            parent_widget (obj): 生成する親ウィジェットオブジェクト
            text_str (str): ボタンに設定するテキスト文字列
            callback (obj): ボタン押下時に呼び出されるコールバック関数(メソッド)

        Returns:
            ttk.Button: ボタンウィジェットオブジェクト
        """
        return ttk.Button(parent_widget, text=text_str, command=callback)

    def __cb_clicked(self) -> None:
        """ボタン押下時の処理用コールバック
        """
        print('[TOP Window][Test Button] Clicked.')

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
