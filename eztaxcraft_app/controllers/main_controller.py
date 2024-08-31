#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
トップ画面制御処理

Author: Shimizu
Date: 2024/5/23
"""

import tkinter as tk
from controllers.base_controller import BaseController
from views.main_view import MainView
from models.settings_model import SettingsModel
from models.error_model import (ErrorCode, ErrorModel)


class MainController(BaseController):
    """TOP画面制御クラス

    Args:
        BaseController (_type_): 画面制御ベースクラスを継承
    """
    def __init__(self) -> None:
        """コンストラクタ
        """
        ### モデルインスタンス生成
        # TODO:モデルクラスを実装後に着手
        self.error_model = ErrorModel(ErrorCode.SUCCESS, "")
        self.settings_model = SettingsModel("custom.json")
        ### トップ画面インスタンス生成
        self.main_view: MainView = MainView(self)

    def run(self) -> None:
        """TOP画面を表示する
        """
        self.main_view.run()

    def get_window_settings(self) -> tuple[int, int, int, int, str]:
        """画面の設定情報を取得する

        Returns:
            tuple[int, int, int, int, str]: 画面の幅, 高さ, x座標, y座標, タイトル情報
        """
        return self.settings_model.get_window_settings()

    def get_font_settings(self) -> tuple[str, str]:
        """画面の設定情報を取得する

        Returns:
            tuple[str, str]: フォント, フォントサイズ
        """
        return self.settings_model.get_font_settings()
