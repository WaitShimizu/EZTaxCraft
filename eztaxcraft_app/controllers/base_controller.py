#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
画面制御ベースクラス

Author: Shimizu
Date: 2024/5/26
"""

import tkinter as tk
from abc import abstractmethod


class BaseController:
    """画面制御ベースクラス
        NOTE:ルート画面制御クラス以外の全ての画面制御クラスが継承すべき基底クラス
    """
    @abstractmethod
    def get_window_settings(self) -> tuple[int, int, int, int, str]:
        """画面の設定情報を取得する

        Returns:
            tuple[int, int, int, int, str]: 画面の幅, 高さ, x座標, y座標, タイトル情報
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()

    @abstractmethod
    def get_font_settings(self) -> tuple[str, str]:
        """画面の設定情報を取得する

        Returns:
            tuple[str, str]: フォント, フォントサイズ
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()
