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
from style.style_manager import StyleManager
from utils.utility import get_icon


class MainView(BaseView):
    """TOP画面クラス

    Args:
        BaseView (_type_): ベース画面クラスを継承
    """
    def __init__(self, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### 設定ボタンアイコン用変数定義
        self.config_img = None
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(controller)

    def run(self) -> None:
        """画面処理を開始する
        """
        self.pack(expand=True, fill="both", padx=(5,5), pady=(5,5))
        self.root.mainloop()

    def create_widget(self) -> None:
        """ウィジェットを生成する
        """
        # タブ画面生成
        self.create_tab()
        # 設定画面用ボタン生成
        self.create_config()

    def create_tab(self) -> None:
        """タブメニューを生成する
        """
        ## ノートブックインスタンス NOTE:画面のタブ化
        note_book = ttk.Notebook(self)

        ### スタイルの設定
        self.style_setup()

        ### タブフレーム生成
        registered_tab = RegisteredTabView(note_book, "TFrame", self.controller)
        unregistered_tab = UnregisteredTabView(note_book, "TFrame", self.controller)
        treatment_tab = TreatmentTabView(note_book, "TFrame", self.controller)

        ### ノートブックオブジェクトにタブフレームを追加
        note_book.add(registered_tab, text="登録済みの方")
        note_book.add(unregistered_tab, text="未登録の方")
        note_book.add(treatment_tab, text="使い方")

        # タブ画面配置
        note_book.pack(expand=True, fill="both")

    def create_config(self) -> None:
        """設定ボタンを生成する
        """
        ### 設定ボタンアイコン取得
        self.config_img = get_icon("global_setting.png", 25, 25)        
        ### ボタンの生成
        home_button = ttk.Button(self, text="",
                                 image=self.config_img,
                                 command=lambda: print("Clicked Config button"),
                                 style="Config.TButton")
        home_button.place(relx=1.0, rely=0.0, anchor='ne')

    def style_setup(self) -> None:
        """スタイルの設定を行う
        """
        ### スタイルマネージャ生成
        style_manager = StyleManager()
        style_manager.configure_styles()
