#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
エラーデータクラス

Author: Shimizu
Date: 2024/8/17
"""

from tkinter import ttk
from tkinter.font import Font


class StyleManager:
    """スタイル管理クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
        """
        # スタイルインスタンス生成
        self.style = ttk.Style()

    def configure_styles(self) -> None:
        """スタイルを設定する
        """
        # タブタイトルバースタイル設定
        self.__tab_titlebar_style_config()
        # タブボタンスタイル設定
        self.__tab_button_style_config()
        # TOP画面の設定ボタンスタイル設定
        self.__top_setting_button_style_config()

    def bind_hover_events(self, widget, enter_func, leave_func) -> None:
        """マウスカーソルイベントをバインドする

        Args:
            widget (_type_): ウィジェットオブジェクト
            enter_func (_type_): カーソルを乗せたときに実行するコールバック関数
            leave_func (_type_): カーソルが外れたときに実行するコールバック関数
        """
        widget.bind('<Enter>', enter_func)
        widget.bind('<Leave>', leave_func)

    def __tab_titlebar_style_config(self) -> None:
        """タブ画面のスタイル設定を行う [内部処理]
        """
        ### タブ画面タイトルバーのスタイルを設定
        # NOTE: タイトルバーのフォント設定
        expand_font_size = 3
        defalut_font = Font(name="TkDefaultFont", exists=True)
        title_bar_font = defalut_font.copy()
        title_bar_font.config(size=defalut_font.cget("size") + expand_font_size, weight="bold")
        self.style.configure("TNotebook.Tab",
                        padding=(5, 5),
                        width=10,
                        anchor="center",
                        font=title_bar_font,
                        borderwidth=1,
                        borderstyle="solid")

        self.style.map('TNotebook.Tab',
                  background=[("selected", "white"), ("!selected", "#7F7F7F")],
                  foreground=[("selected", "#4472C4"), ("!selected", "white")])

        ### タブ画面のスタイルを設定
        self.style.configure("TFrame", background="white")

    def __tab_button_style_config(self) -> None:
        """タブ画面のボタンスタイル設定を行う [内部処理]
        """
        # タブ画面のボタンのスタイルを設定
        self.style.configure("Flat.TButton",
                        padding=[0, 0, 0, 0],
                        borderwidth=0,
                        relief="flat",
                        background="white")

        # ボタンオブジェクトへのカーソルイベント発生時のスタイル設定
        self.style.map('Flat.TButton',
                  relief=[('active', 'flat'), ('pressed', 'flat')],
                  background=[('active', 'white'), ('pressed', 'white')],
                  highlightcolor=[('focus', 'white')],
                  focuscolor=[('focus', 'white')])

    def __top_setting_button_style_config(self) -> None:
        """TOP画面の設定ボタンスタイル設定を行う [内部処理]
        """
        # 背景色を設定
        background_color = "#D9D9D9"

        # タブ画面の設定ボタンのスタイルを設定
        self.style.configure("Config.TButton",
                        padding=[0, 0, 0, 0],
                        borderwidth=0,
                        relief="flat",
                        background=background_color)

        # ボタンオブジェクトへのカーソルイベント発生時のスタイル設定
        self.style.map('Config.TButton',
                  relief=[('active', 'flat'), ('pressed', 'flat')],
                  background=[('active', background_color), ('pressed', background_color)],
                  highlightcolor=[('focus', background_color)],
                  focuscolor=[('focus', background_color)])
