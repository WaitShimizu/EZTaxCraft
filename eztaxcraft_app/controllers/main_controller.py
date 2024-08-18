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
from models.settings_model import (DefaultSettingsModel, CustomSettingsModel)
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
        self.custom_settings_model = CustomSettingsModel("custom.json")
        self.default_settings_model = DefaultSettingsModel()
        ### トップ画面インスタンス生成
        self.main_view: MainView = MainView(self)

    def run(self) -> None:
        """TOP画面を表示する
        """
        self.main_view.run()

    def get_window_width(self) -> tuple[int, ErrorCode]:
        """画面の幅情報を取得する

        Returns:
            int: 画面の幅情報, エラーコード
        """
        ### カスタム設定チェック
        if self.custom_settings_model.check_exist_data() != ErrorCode.SUCCESS:
            # NOTE: カスタム情報が存在しなければデフォルト値を応答
            return self.default_settings_model.get_window_width()

        # NOTE: カスタム情報があればカスタム値を応答
        return self.custom_settings_model.get_window_width()

    def get_window_height(self) -> tuple[int, ErrorCode]:
        """画面の高さ情報を取得する

        Returns:
            int: 画面の高さ情報, エラーコード
        """
        ### カスタム設定チェック
        if self.custom_settings_model.check_exist_data() != ErrorCode.SUCCESS:
            # NOTE: カスタム情報が存在しなければデフォルト値を応答
            return self.default_settings_model.get_window_height()

        # NOTE: カスタム情報があればカスタム値を応答
        return self.custom_settings_model.get_window_height()

    def get_window_position_x(self) -> tuple[int, ErrorCode]:
        """画面の位置座標(x座標)を取得する

        Returns:
            int: 画面の位置座標(x座標), エラーコード
        """
        ### カスタム設定チェック
        if self.custom_settings_model.check_exist_data() != ErrorCode.SUCCESS:
            # NOTE: カスタム情報が存在しなければデフォルト値を応答
            return self.default_settings_model.get_window_position_x()

        # NOTE: カスタム情報があればカスタム値を応答
        return self.custom_settings_model.get_window_position_x()

    def get_window_position_y(self) -> tuple[int, ErrorCode]:
        """画面の位置座標(y座標)を取得する

        Returns:
            int: 画面の位置座標(y座標), エラーコード
        """
        ### カスタム設定チェック
        if self.custom_settings_model.check_exist_data() != ErrorCode.SUCCESS:
            # NOTE: カスタム情報が存在しなければデフォルト値を応答
            return self.default_settings_model.get_window_position_y()

        # NOTE: カスタム情報があればカスタム値を応答
        return self.custom_settings_model.get_window_position_y()

    def get_window_title(self) -> tuple[str, ErrorCode]:
        """画面のタイトル情報を取得する

        Returns:
            tuple[str, ErrorCode]: 画面のタイトル情報, エラーコード
        """
        ### カスタム設定チェック
        if self.custom_settings_model.check_exist_data() != ErrorCode.SUCCESS:
            # NOTE: カスタム情報が存在しなければデフォルト値を応答
            return self.default_settings_model.get_window_title()

        # NOTE: カスタム情報があればカスタム値を応答
        return self.custom_settings_model.get_window_title()

    def get_font_family(self) -> tuple[str, ErrorCode]:
        """フォント情報を取得する

        Returns:
            tuple[str, ErrorCode]: フォント情報, エラーコード
        """
        ### カスタム設定チェック
        if self.custom_settings_model.check_exist_data() != ErrorCode.SUCCESS:
            # NOTE: カスタム情報が存在しなければデフォルト値を応答
            return self.default_settings_model.get_font_family()

        # NOTE: カスタム情報があればカスタム値を応答
        return self.custom_settings_model.get_font_family()

    def get_font_size(self) -> tuple[str, ErrorCode]:
        """フォントサイズを取得する

        Returns:
            tuple[str, ErrorCode]: フォントサイズ, エラーコード
        """
        ### カスタム設定チェック
        if self.custom_settings_model.check_exist_data() != ErrorCode.SUCCESS:
            # NOTE: カスタム情報が存在しなければデフォルト値を応答
            return self.default_settings_model.get_font_size()

        # NOTE: カスタム情報があればカスタム値を応答
        return self.custom_settings_model.get_font_size()
