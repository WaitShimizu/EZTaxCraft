#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ルート画面制御処理

Author: Shimizu
Date: 2024/5/26
"""

import tkinter as tk
from controllers.top_controller import TopController


class RootController:
    """画面制御クラスを制御するクラス
    """

    def __init__(self, width: int = 600, height: int = 400,
                 pos_x: int = 600, pos_y: int = 300) -> None:
        """コンストラクタ

        Args:
            width (int, optional): ウィンドウの横幅 [単位:ピクセル]. Defaults to 500.
            height (int, optional): ウィンドウの高さ [単位:ピクセル]. Defaults to 400.
            pos_x (int, optional): ウィンドウ表示位置のX座標 [単位:ピクセル]. Defaults to 500.
            pos_y (int, optional): ウィンドウ表示位置のY座標 [単位:ピクセル]. Defaults to 300.
        """
        ### 画面のルートインスタンスを生成
        self.root = tk.Tk()
        # NOTE:画面のタイトル文字を削除
        self.root.title("")
        # NOTE:画面のジオメトリを設定
        self.root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
        ### TOP画面インスタンス生成
        # NOTE:画面はTOP画面から始まる
        self.top_controller: TopController = TopController(self.root)

    def start(self) -> None:
        """画面制御を開始する
        """
        self.root.mainloop()
