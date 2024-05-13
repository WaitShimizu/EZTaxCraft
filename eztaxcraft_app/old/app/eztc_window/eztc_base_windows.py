#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリ画面の基底クラス定義

Author: Shimizu
Date: 2024/2/11
"""

import sys
import tkinter as tk
from tkinter import ttk

sys.path.append('../../common')
from window.window import Window


class BaseWindow(Window):
    """ベース画面クラス
        NOTE: 画面クラスが継承すべき親クラス

    Args:
        Window (Window): 継承元の画面クラス
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
        # 親クラスのコンストラクタ呼び出し
        super().__init__()
        # ルートTKインスタンス生成
        self.root = tk.Tk()
        self.root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')

    def open(self) -> None:
        """画面を開く
        """
        print('[W]')

    def close(self) -> None:
        """画面を閉じる
        """
        # 継承先で画面を閉じる処理を実装する
        raise NotImplementedError('次のメソッドが実装されていません。[close]')
