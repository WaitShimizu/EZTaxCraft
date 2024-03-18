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
    def __init__(self) -> None:
        """コンストラクタ
        """
        # 親クラスのコンストラクタ呼び出し
        super().__init__()
        # ルートTKインスタンス生成
        self.root = tk.Tk()

    def open(self) -> None:
        """画面を開く
        """
        print('[W]')

    def close(self) -> None:
        """画面を閉じる
        """
        # 継承先で画面を閉じる処理を実装する
        raise NotImplementedError('次のメソッドが実装されていません。[close]')
