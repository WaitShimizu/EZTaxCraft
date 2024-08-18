#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
設定データクラス

Author: Shimizu
Date: 2024/6/9
"""

from models.error_model import ErrorCode
from utils.singleton import SingletonMeta
from utils.utility import load_json


class DefaultSettingsModel(metaclass=SingletonMeta):
    """デフォルト設定データクラス
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

    def __init__(self) -> None:
        """コンストラクタ
        """
        self.settings = DefaultSettingsModel._WINDOW

    def get_window_width(self) -> tuple[int, ErrorCode]:
        """画面の幅情報を取得する

        Returns:
            tuple[int, ErrorCode]: 画面の幅情報, エラーコード
        """
        ### 応答生成
        data = -1
        try:
            data = self.settings['window']['width']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_WINDOW_WIDTH

    def get_window_height(self) -> tuple[int, ErrorCode]:
        """画面の高さ情報を取得する

        Returns:
            tuple[int, ErrorCode]: 画面の高さ情報, エラーコード
        """
        ### 応答生成
        data = -1
        try:
            data = self.settings['window']['height']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_WINDOW_HEIGHT

    def get_window_position_x(self) -> tuple[int, ErrorCode]:
        """画面の位置座標(x座標)を取得する

        Returns:
            tuple[int, ErrorCode]: 画面の位置座標(x座標), エラーコード
        """
        ### 応答生成
        data = -1
        try:
            data = self.settings['window']['position_x']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_WINDOW_POS_X

    def get_window_position_y(self) -> tuple[int, ErrorCode]:
        """画面の位置座標(y座標)を取得する

        Returns:
            tuple[int, ErrorCode]: 画面の位置座標(y座標), エラーコード
        """
        ### 応答生成
        data = -1
        try:
            data = self.settings['window']['position_y']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_WINDOW_POS_Y

    def get_window_title(self) -> tuple[str, ErrorCode]:
        """画面のタイトル情報を取得する

        Returns:
            tuple[int, ErrorCode]: 画面のタイトル情報, エラーコード
        """
        ### 応答生成
        data = ""
        try:
            data = self.settings['window']['title']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_WINDOW_TITLE

    def get_font_family(self) -> tuple[str, ErrorCode]:
        """フォント情報を取得する

        Returns:
            tuple[str, ErrorCode]: フォント情報, エラーコード
        """
        ### 応答生成
        data = ""
        try:
            data = self.settings['font']['font_family']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_FONT_FAMILY

    def get_font_size(self) -> tuple[str, ErrorCode]:
        """フォントサイズを取得する

        Returns:
            tuple[str, ErrorCode]: フォントサイズ, エラーコード
        """
        ### 応答生成
        data = -1
        try:
            data = self.settings['font']['font_size']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_FONT_SIZE


class CustomSettingsModel(DefaultSettingsModel):
    """カスタム設定データクラス
        NOTE:設定データを保持して変更を通知するためのクラス
    """

    def __init__(self, setting_file_name: str) -> None:
        """コンストラクタ

        Args:
            setting_file_name (str): 設定ファイル名
        """
        ### ファイルパス情報
        path = f'data/setting/{setting_file_name}'
        ### 設定情報をバッファに格納
        self.settings = load_json(path)

    def check_exist_data(self) -> ErrorCode:
        """カスタム設定データの存在チェック
            NOTE: 本クラスを利用する場合は必ず最初に本メソッドを呼び出すこと

        Returns:
            ErrorCode: エラーコード
        """
        ### 設定データの存在チェック
        if not self.settings:
            # NOTE: データなし
            return ErrorCode.NO_DATA
        # NOTE: カスタム設定データ在り
        return ErrorCode.SUCCESS

    def get_window_title(self) -> tuple[str, ErrorCode]:
        """画面のタイトル情報を取得する
            NOTE: カスタム設定の場合も画面タイトルは固定値を応答する

        Returns:
            tuple[int, ErrorCode]: 画面のタイトル情報, エラーコード
        """
        ### 応答生成
        data = ""
        try:
            data = CustomSettingsModel._WINDOW['window']['title']
            return data, ErrorCode.SUCCESS

        except KeyError:
            return data, ErrorCode.NO_DATA_WINDOW_TITLE
