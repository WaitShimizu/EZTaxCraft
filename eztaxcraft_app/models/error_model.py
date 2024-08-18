#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
エラーデータクラス

Author: Shimizu
Date: 2024/6/9
"""

from enum import Enum
from dataclasses import dataclass
# from utils.utility import load_json


class ErrorCode(Enum):
    """エラーコードクラス
    """
    ### 成功
    SUCCESS = 0

    ### アプリ画面設定エラー
    NO_DATA                = 1000
    NO_DATA_WINDOW_WIDTH   = 1001
    NO_DATA_WINDOW_HEIGHT  = 1002
    NO_DATA_WINDOW_POS_X   = 1003
    NO_DATA_WINDOW_POS_Y   = 1004
    NO_DATA_WINDOW_TITLE   = 1005
    NO_DATA_FONT_FAMILY    = 1006
    NO_DATA_FONT_SIZE      = 1007


@dataclass
class ErrorModel:
    """エラーデータクラス
    """
    code: ErrorCode
    message: str
    error_messages = {
        ErrorCode.NO_DATA: "Data does not exist.",
        ErrorCode.NO_DATA_WINDOW_WIDTH: "Screen width information is missing.",
        ErrorCode.NO_DATA_WINDOW_HEIGHT: "Screen height information is missing.",
        ErrorCode.NO_DATA_WINDOW_POS_X: "Screen position X information is missing.",
        ErrorCode.NO_DATA_WINDOW_POS_Y: "Screen position Y information is missing.",
        ErrorCode.NO_DATA_WINDOW_TITLE: "Screen title information is missing.",
        ErrorCode.NO_DATA_FONT_FAMILY: "Font family information is missing.",
        ErrorCode.NO_DATA_FONT_SIZE: "Font size information is missing.",
    }
    

    @staticmethod
    def get_error(code: ErrorCode) -> str:
        """エラーコードからエラーメッセージを取得する

        Args:
            code (ErrorCode): エラーコード

        Returns:
            str: エラーメッセージ
        """
        return ErrorModel.error_messages.get(code, 'Unknown error.')


""" テスト """
if __name__ == '__main__':
    # err_msg = ErrorModel.get_error(ErrorCode.NO_DATA_WINDOW_POS_X)
    # print(f'[ErrorModel] -- テスト --  err_msg: {err_msg}')
    error = ErrorModel(code=ErrorCode.NO_DATA_WINDOW_POS_X,
                   message=ErrorModel.get_error(ErrorCode.NO_DATA_WINDOW_POS_X))

    print(f"Error Code: {error.code.value}, Message: {error.message}")
