#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリのTOP画面クラス定義

Author: Shimizu
Date: 2024/2/11
"""

from eztc_base_windows import BaseWindow
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
        # 親クラスのコンストラクタ呼び出し
        super().__init__()

        # # スタイルウィジェットインスタンス生成
        # self.style_name = '.'
        # self.style = Style(self.style_name)
        # # ボタンウィジェットインスタンス生成
        # login_btn_txt = 'ログイン'
        # command = self.__clicked_login_btn
        # self.login_btn = Button(self.root, style='.', text=login_btn_txt, command=command)

    def initialize(self) -> None:
        """初期化処理
        """
        #-------- スタイルウィジェット --------
        # TOP画面用スタイル生成
        style_name = '.'
        style = Style(style_name)

        # TOP画面用スタイルを設定
        style_font = ('Meiryo', 9)
        style.config(style_name, font=style_font)

        #-------- ボタンウィジェット --------
        # ログインボタン生成
        login_btn_txt = 'ログイン'
        command = self.__clicked_login_btn
        login_btn = Button(self.root, text=login_btn_txt, command=command)
        # ログインボタン配置
        login_btn.pack()

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


if __name__ == '__main__':
    top_window = TopWindow()
    top_window.initialize()
