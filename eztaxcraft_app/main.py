#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリケーションメイン処理

Author: Shimizu
Date: 2024/1/23
"""

import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass, field


def main():
    """メイン関数
    """
    ## テスト処理追加
    print("EZTaxCraft")
    top = TopWindow()


class TopWindow:
    """TOP画面クラス

    Args:
        BaseWindow (BaseWindow): ベース画面クラス
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
        ### インスタンス変数定義
        ## rootインスタンス NOTE:メイン画面オブジェクト生成
        self.root = tk.Tk()
        self.root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
        ## ノートブックインスタンス NOTE:画面のタブ化
        self.note_book = ttk.Notebook(self.root)
        ## タブ画面用フレームインスタンス
        # NOTE:登録済みユーザータブ生成
        self.registered_user_frame = ttk.Frame(self.note_book)
        self.note_book.add(self.registered_user_frame, text="登録済みの方")
        # NOTE:未登録ユーザータブ生成
        self.unregistered_user_frame = ttk.Frame(self.note_book)
        self.note_book.add(self.unregistered_user_frame, text="未登録の方")
        # NOTE:未登録ユーザータブ生成
        self.usage_frame = ttk.Frame(self.note_book)
        self.note_book.add(self.usage_frame, text="使い方")
        # タブ画面配置
        self.note_book.pack(expand=True, fill="both")
        #-------- ウィンドウ表示 --------
        self.root.mainloop()


    def open(self) -> None:
        """画面を開く
        """
        print('[TopWindow: open] Called.')

    def close(self) -> None:
        """画面を閉じる
        """
        # 継承先で画面を閉じる処理を実装する
        print('[TopWindow: close] Called.')

    def __clicked_login_btn(self) -> None:
        """ログインボタンクリック時の処理実行
        """
        print('[TopWindow: __clicked_login_btn] Clicked.')


if __name__ == "__main__":
    main()
