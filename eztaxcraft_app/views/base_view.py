#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ベース画面クラス

Author: Shimizu
Date: 2024/5/26
"""

import tkinter as tk
from abc import abstractmethod
from tkinter import ttk
from controllers.base_controller import BaseController


class BaseView(ttk.Frame):
    """ベース画面クラス
        NOTE:全画面クラスが継承すべき基底クラス
    """

    def __init__(self, master: tk.Tk, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(master)
        ### 画面制御インスタンスを格納
        self.controller = controller
        ### ウィジェットを生成
        self.create_widget()

    @abstractmethod
    def create_widget(self) -> None:
        """ウィジェットを生成する
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()
