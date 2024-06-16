#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
トップ画面制御処理

Author: Shimizu
Date: 2024/5/23
"""

import tkinter as tk
from controllers.base_controller import BaseController
from views.top_view import TopView


class TopController(BaseController):
    """TOP画面制御クラス

    Args:
        BaseController (_type_): 画面制御ベースクラスを継承
    """

    def __init__(self, root: tk.Tk) -> None:
        """コンストラクタ
        """
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(root)
        ### トップ画面インスタンス生成
        self.top_view: TopView = TopView(self.root, self)
        self.show_top_view()
        ### モデルインスタンス生成
        # TODO:モデルクラスを実装後に着手

    def show_top_view(self) -> None:
        """TOP画面を表示する
        """
        self.top_view.pack(expand=True, fill="both", padx=(5,5), pady=(5,5))
