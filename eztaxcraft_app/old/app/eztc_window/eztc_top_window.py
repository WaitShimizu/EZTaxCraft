#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリのTOP画面クラス定義

Author: Shimizu
Date: 2024/2/11
"""

from eztc_base_windows import BaseWindow
from eztc_window_widget.eztc_widget_notebook import Notebook
from eztc_window_widget.eztc_widget_frame import Frame
from eztc_window_widget.eztc_widget_button import Button
from eztc_window_widget.eztc_widget_style import Style


class TopWindow(BaseWindow):
    """TOP画面クラス

    Args:
        BaseWindow (BaseWindow): ベース画面クラス
    """

    def __init__(self) -> None:
        """コンストラクタ
        """
        ### 親クラスのコンストラクタ呼び出し
        # NOTE: デフォルトのウィンドウ表示位置で設定
        #       ウィンドウ横幅: 600px
        #       ウィンドウ高さ: 400px
        #       ウィンドウX座標:600px
        #       ウィンドウY座標:300px
        super().__init__()

    def initialize(self) -> None:
        """初期化処理
        """
        # #-------- スタイルウィジェット --------
        # # TOP画面用スタイル生成
        # style_name = '.'
        # style = Style(style_name)

        # # TOP画面用スタイルを設定
        # style_font = ('Meiryo', 9)
        # style.config(style_name, font=style_font)

        #-------- タブ画面ウィジェット --------
        # タブ画面生成
        notebook_inst = Notebook(self.root)
        notebook = notebook_inst.get_widget()
        ## タブ画面ウィジェットへタブフレームを登録
        # 登録済みユーザータブ生成
        registered_user_frame = Frame(notebook)
        registered_user_tab = registered_user_frame.get_widget()
        notebook_inst.add_tab(registered_user_tab, "登録済みの方")
        # 未登録ユーザータブ生成
        unregistered_user_frame = Frame(notebook)
        unregistered_user_tab = unregistered_user_frame.get_widget()
        notebook_inst.add_tab(unregistered_user_tab, "未登録の方")
        # 使い方タブ生成
        usage_frame = Frame(notebook)
        usage_tab = usage_frame.get_widget()
        notebook_inst.add_tab(usage_tab, "使い方")

        ### -------- ボタンウィジェット --------
        ## 登録済みユーザータブ用ボタン
        # NOTE:ログインボタン生成
        login_btn_txt = 'ログイン'
        login_btn = Button(registered_user_tab, text=login_btn_txt, command=self.__clicked_login_btn)
        # ログインボタン配置
        login_btn.pack()

        ## 未登録ユーザータブ用ボタン
        # NOTE:ユーザー登録ボタン生成
        register_btn_txt = 'ユーザー登録'
        register_btn = Button(unregistered_user_tab, text=register_btn_txt, command=self.__clicked_register_btn)
        # ユーザー登録ボタンボタン配置
        register_btn.pack()

        ## 使い方タブ用ボタン
        # NOTE:ログインボタン生成
        login_btn = Button(usage_tab, text=login_btn_txt, command=self.__clicked_login_btn)
        # ログインボタン配置
        login_btn.pack()
        # NOTE:ユーザー登録ボタン生成
        register_btn = Button(usage_tab, text=register_btn_txt, command=self.__clicked_register_btn)
        # ユーザー登録ボタンボタン配置
        register_btn.pack()

        # タブ画面配置
        notebook_inst.pack(expand=True, fill="both")

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

    def __clicked_register_btn(self) -> None:
        """ユーザー登録ボタンクリック時の処理実行
        """
        print('[TopWindow: __clicked_register_btn] Clicked.')


if __name__ == '__main__':
    top_window = TopWindow()
    top_window.initialize()
