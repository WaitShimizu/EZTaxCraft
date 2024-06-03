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
from views.registered_tab_view import RegisteredTabView
from views.treatment_tab_view import TreatmentTabView
from views.unregistered_tab_view import UnregisteredTabView


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
        #　タブ画面生成
        self.create_tab(note_book)

        # タブ画面配置
        note_book.pack(expand=True, fill="both")

    def create_tab(self, note_book: ttk.Notebook) -> None:
        """タブメニューを生成する

        Args:
            note_book (ttk.Notebook): ノートブックオブジェクト
        """
        ### スタイルの設定
        self.style_setup()

        ### タブフレーム生成
        registered_tab = RegisteredTabView(note_book, self.controller)
        unregistered_tab = UnregisteredTabView(note_book, self.controller)
        treatment_tab = TreatmentTabView(note_book, self.controller)

        ### ノートブックオブジェクトにタブフレームを追加
        note_book.add(registered_tab, text="登録済みの方")
        note_book.add(unregistered_tab, text="未登録の方")
        note_book.add(treatment_tab, text="使い方")

    def style_setup(self) -> None:
        """スタイルの設定を行う
        """
        ### スタイルの設定
        style = ttk.Style()
        style.configure("Flat.TButton", borderwidth=0, relief="flat")
        style.map('Flat.TButton',
                  relief=[('active', 'flat'), ('pressed', 'flat')],
                  background=[('active', 'lightgray'), ('pressed', 'lightgray')],
                  highlightcolor=[('focus', 'lightgray')],
                  focuscolor=[('focus', 'lightgray')])

