#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
トップ画面表示処理

Author: Shimizu
Date: 2024/5/23
"""

import tkinter as tk
from tkinter import ttk
from controllers.base_controller import BaseController
from views.base_view import BaseView


class TopView(BaseView):
    """TOP画面クラス

    Args:
        BaseView (_type_): ベース画面クラスを継承
    """
    def __init__(self, master: tk.Tk, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(master, controller)

    def create_widget(self) -> None:
        """ウィジェットを生成する
        """
        ## ノートブックインスタンス NOTE:画面のタブ化
        note_book = ttk.Notebook(self)
        ## タブ画面用フレームインスタンス
        # NOTE:登録済みユーザータブ生成
        self.create_tab(note_book, "登録済みの方")

        # NOTE:未登録ユーザータブ生成
        self.create_tab(note_book, "未登録の方")

        # NOTE:未登録ユーザータブ生成
        self.create_tab(note_book, "使い方")

        # タブ画面配置
        note_book.pack(expand=True, fill="both")

    def create_tab(self, note_book: ttk.Notebook, tab_text: str) -> None:
        """タブメニューを生成する

        Args:
            note_book (ttk.Notebook): ノートブックオブジェクト
            tab_text (str): タブに設定するテキスト文字列
        """
        ### タブフレーム生成
        tab_frame = ttk.Frame(note_book)
        ### ノートブックオブジェクトにタブフレームを追加
        note_book.add(tab_frame, text=tab_text)

