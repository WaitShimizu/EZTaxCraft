#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ベースタブ画面クラス

Author: Shimizu
Date: 2024/6/9
"""

import tkinter as tk
from abc import abstractmethod
from PIL import ImageTk
from tkinter import ttk
from controllers.base_controller import BaseController


class BaseTabView(ttk.Frame):
    """ベースタブ画面クラス
        NOTE:全画面クラスが継承すべき基底クラス
    """

    def __init__(self, master: tk.Tk, style: str, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            style (str): 適応するスタイル名
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(master, style=style)
        ### 画面制御インスタンスを格納
        self.controller = controller
        ### ボディを生成
        self.create_body()

    @abstractmethod
    def create_body(self) -> None:
        """タブ画面のボディを生成する
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()

    def cursor_event_cb(self, event, button: ttk.Button, image: ImageTk.PhotoImage) -> None:
        """カーソルイベント処理(コールバック)
            NOTE: マウスカーソルがボタン上に入ったときのイベント処理

        Args:
            event (_type_): イベントデータ
            button (ttk.Button): ボタンオブジェクト
            image (ImageTk.PhotoImage): 切り替える画像データ
        """
        button.config(image=image)
