#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
画面制御ベースクラス

Author: Shimizu
Date: 2024/5/26
"""

import tkinter as tk


class BaseController:
    """画面制御ベースクラス
        NOTE:ルート画面制御クラス以外の全ての画面制御クラスが継承すべき基底クラス
    """

    def __init__(self, root: tk.Tk) -> None:
        """コンストラクタ
        """
        ### ルートインスタンスを格納
        self.root: tk.Tk = root
