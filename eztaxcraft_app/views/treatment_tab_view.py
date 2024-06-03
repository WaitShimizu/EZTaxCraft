#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[使い方]タブ画面表示処理

Author: Shimizu
Date: 2024/5/23
"""

import tkinter as tk
from tkinter import ttk
from controllers.base_controller import BaseController
from views.base_view import BaseView
from utils.utility import get_icon


class TreatmentTabView(BaseView):
    """[使い方]タブクラス

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

    def create_header(self) -> None:
        """タブ画面のヘッダーを生成する
        """
        icon = get_icon("logo.png")
        app_icon_button = ttk.Button(self, text="",
                                    image=icon,
                                    compound="left",
                                    command=self.clicked_cb,
                                    style="Flat.TButton")
        app_icon_button.pack()
        ## ログインボタンインスタンス生成
        login_button = ttk.Button(self, text="ログイン", command=self.clicked_cb)
        login_button.pack()
        ## ユーザー登録ボタンインスタンス生成
        regist_button = ttk.Button(self, text="ユーザー登録", command=self.clicked_cb)
        regist_button.pack()

    def create_widget(self) -> None:
        """ウィジェットを生成する
        """
        ## ヘッダー生成
        self.create_header()

        

    def clicked_cb(self) -> None:
        """ログインボタンクリック処理(コールバック)
        """
        print("[TreatmentTabView-clicked_login] Clicked.")
