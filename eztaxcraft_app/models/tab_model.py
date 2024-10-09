#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
タブ画面データクラス

Author: Shimizu
Date: 2024/9/8
"""

from utils.singleton import SingletonMeta
from utils.utility import load_json


class TabModel(metaclass=SingletonMeta):
    """設定データクラス
    """
    _WINDOW = {
        "window": {
            "width": 600,
            "height": 400,
            "position_x": 600,
            "position_y": 300,
            "title": "かんたん帳簿"
        },
        "font": {
            "font_family": "Arial",
            "font_size": 12
        }
    }

    def __init__(self, setting_file_name: str = '') -> None:
        """コンストラクタ

        Args:
            setting_file_name (str): 設定ファイル名
        """
        self.default_settings = SettingsModel._WINDOW
        self.custom_settings = None
        self.custom_enable = False
        ### 引数チェック
        if setting_file_name != '':
            ### カスタム設定を利用
            path = f'data/setting/{setting_file_name}'
            self.custom_settings = load_json(path)
            self.custom_enable = True

        ### カスタム設定データの存在チェック
        if not self.custom_settings:
            # NOTE: カスタム設定データが無い場合はデフォルト設定を利用する
            self.settings = SettingsModel._WINDOW
            self.custom_enable = False

    def get_window_settings(self) -> tuple[int, int, int, int, str]:
        """画面の設定情報を取得する

        Returns:
            tuple[int, int, int, int, str]: 画面の幅, 高さ, x座標, y座標, タイトル情報
        """
        # NOTE: カスタム情報が存在しなければデフォルト値を応答
        width = self.__get_window_width()
        height = self.__get_window_height()
        pos_x = self.__get_window_position_x()
        pos_y = self.__get_window_position_y()
        title = self.__get_window_title()
        return width, height, pos_x, pos_y, title

    def get_font_settings(self) -> tuple[str, str]:
        """画面のフォント情報を取得する

        Returns:
            tuple[str, str]: フォント, フォントサイズ
        """
        # NOTE: カスタム情報が存在しなければデフォルト値を応答
        font = self.__get_font_family()
        font_size = self.__get_font_size()
        return font, font_size

    def __get_window_width(self) -> int:
        """画面の幅情報を取得する

        Returns:
            int: 画面の幅情報
        """
        ### カスタム設定の有効チェック
        if not self.custom_enable:
            try:
                # NOTE:カスタム設定を応答
                return self.custom_settings['window']['width']
            except KeyError:
                # NOTE:デフォルト設定を応答
                return self.default_settings['window']['width']

        # カスタム設定が無効の場合はデフォルト設定を応答
        return self.default_settings['window']['width']

    def __get_window_height(self) -> int:
        """画面の高さ情報を取得する

        Returns:
            int: 画面の高さ情報
        """
        ### カスタム設定の有効チェック
        if not self.custom_enable:
            try:
                # NOTE:カスタム設定を応答
                return self.custom_settings['window']['height']
            except KeyError:
                # NOTE:デフォルト設定を応答
                return self.default_settings['window']['height']

        # カスタム設定が無効の場合はデフォルト設定を応答
        return self.default_settings['window']['height']

    def __get_window_position_x(self) -> int:
        """画面の位置座標(x座標)を取得する

        Returns:
            int: 画面の位置座標(x座標)
        """
        ### カスタム設定の有効チェック
        if not self.custom_enable:
            try:
                # NOTE:カスタム設定を応答
                return self.custom_settings['window']['position_x']
            except KeyError:
                # NOTE:デフォルト設定を応答
                return self.default_settings['window']['position_x']

        # カスタム設定が無効の場合はデフォルト設定を応答
        return self.default_settings['window']['position_x']

    def __get_window_position_y(self) -> int:
        """画面の位置座標(y座標)を取得する

        Returns:
            int: 画面の位置座標(y座標)
        """
        ### カスタム設定の有効チェック
        if not self.custom_enable:
            try:
                # NOTE:カスタム設定を応答
                return self.custom_settings['window']['position_y']
            except KeyError:
                # NOTE:デフォルト設定を応答
                return self.default_settings['window']['position_y']

        # カスタム設定が無効の場合はデフォルト設定を応答
        return self.default_settings['window']['position_y']

    def __get_window_title(self) -> str:
        """画面のタイトル情報を取得する
            NOTE: カスタム設定の場合も画面タイトルは固定値を応答する

        Returns:
            str: 画面のタイトル情報
        """
        # デフォルト設定を応答
        return self.default_settings['window']['title']

    def __get_font_family(self) -> str:
        """フォントを取得する

        Returns:
            str: フォント
        """
        ### カスタム設定の有効チェック
        if not self.custom_enable:
            try:
                # NOTE:カスタム設定を応答
                return self.custom_settings['font']['font_family']
            except KeyError:
                # NOTE:デフォルト設定を応答
                return self.default_settings['font']['font_family']

        # カスタム設定が無効の場合はデフォルト設定を応答
        return self.default_settings['font']['font_family']

    def __get_font_size(self) -> str:
        """フォントサイズを取得する

        Returns:
            str: フォントサイズ
        """
        ### カスタム設定の有効チェック
        if not self.custom_enable:
            try:
                # NOTE:カスタム設定を応答
                return self.custom_settings['font']['font_size']
            except KeyError:
                # NOTE:デフォルト設定を応答
                return self.default_settings['font']['font_size']

        # カスタム設定が無効の場合はデフォルト設定を応答
        return self.default_settings['font']['font_size']
