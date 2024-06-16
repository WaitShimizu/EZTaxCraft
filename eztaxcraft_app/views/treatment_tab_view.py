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
from views.base_tab_view import BaseTabView
from utils.utility import get_icon


class TreatmentTabView(BaseTabView):
    """[使い方]タブクラス

    Args:
        BaseTabView (_type_): ベースタブ画面クラスを継承
    """

    def __init__(self, master: tk.Tk, style: str, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            style (str): 適応するスタイル名
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### ボタン用画像データ取得
        self.home_logo_img = get_icon("app_logo.png", 210, 45)
        self.login_leave_img = get_icon("login_leave.png", 150, 45)
        self.login_enter_img = get_icon("login_enter.png", 150, 45)
        self.user_regist_leave_img = get_icon("user_regist_leave.png", 150, 45)
        self.user_regist_enter_img = get_icon("user_regist_enter.png", 150, 45)
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(master, style, controller)

    def create_body_header(self) -> None:
        """タブ画面のボディヘッダーを生成する
        """
        ### ヘッダーのボタンウィジェット生成
        # ホームボタン
        home_button = ttk.Button(self,
                                 image=self.home_logo_img,
                                 command=self.clicked_cb,
                                 style="Flat.TButton")
        home_button.pack(side=tk.LEFT, anchor=tk.N, padx=(15,0), pady=(15,0))

        # ユーザー登録ボタン
        user_regist_button = ttk.Button(self,
                                        image=self.user_regist_leave_img,
                                        command=self.clicked_cb,
                                        style="Flat.TButton")
        user_regist_button.pack(side=tk.RIGHT, anchor=tk.N, padx=(0,20), pady=(20,0))

        # ログインボタン
        login_button = ttk.Button(self, text="",
                                  image=self.login_leave_img,
                                  compound="center",
                                  command=self.clicked_cb,
                                  style="Flat.TButton")
        login_button.pack(side=tk.RIGHT, anchor=tk.N, padx=(0,0), pady=(20,0))

        # マウスカーソルイベント登録
        user_regist_button.bind("<Enter>", lambda event: self.cursor_event_cb(event, user_regist_button, self.user_regist_enter_img))
        user_regist_button.bind("<Leave>", lambda event: self.cursor_event_cb(event, user_regist_button, self.user_regist_leave_img))
        login_button.bind("<Enter>", lambda event: self.cursor_event_cb(event, login_button, self.login_enter_img))
        login_button.bind("<Leave>", lambda event: self.cursor_event_cb(event, login_button, self.login_leave_img))

    def create_body(self) -> None:
        """タブ画面のボディを生成する
        """
        ## ヘッダー生成
        self.create_body_header()

    def clicked_cb(self) -> None:
        """ログインボタンクリック処理(コールバック)
        """
        print("[TreatmentTabView-clicked_cb] Clicked.")
