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
    def __init__(self, parent_widget: tk.Tk, **kwargs) -> None:
        """コンストラクタ
            NOTE:tkinterのButtonクラスをラップする

        Args:
            parent_widget (tk.Tk): 配置する親ウィジェットオブジェクト
            **kwargs (dict): キーワード引数 (※NOTE: 以下を設定可能)
                            command: _ButtonCommand = ...,
                            compound: _TtkCompound = ...,
                            cursor: _Cursor = ...,
                            default: Literal['normal', 'active', 'disabled'] = ...,
                            image: _ImageSpec = ...,
                            name: str = ...,
                            padding: ... = ...,
                            state: str = ...,
                            style: str = ...,
                            takefocus: _TakeFocusValue = ...,
                            text: float | str = ...,
                            textvariable: Variable = ...,
                            underline: int = ...,
                            width: int | Literal[''] = ...
        """
        self.widget = ttk.Button(parent_widget, **kwargs)

    def pack(self, **kwargs) -> None:
        """親ウィジェットに配置する
            NOTE:tkinterウィジェットのpackメソッドをラップする
        """
        self.widget.pack(**kwargs)

    def grid(self, **kwargs) -> None:
        """ウィジェットをグリッドレイアウト内に配置する
            NOTE:tkinterウィジェットのgridメソッドをラップする
        """
        self.widget.grid(**kwargs)

    def place(self, **kwargs) -> None:
        """親ウィジェットにピクセル単位で配置する
            NOTE:tkinterウィジェットのplaceメソッドをラップする
        """
        self.widget.place(**kwargs)
