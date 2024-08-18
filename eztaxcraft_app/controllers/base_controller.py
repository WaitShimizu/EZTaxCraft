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
    def get_window_size(self) -> tuple[int, int, int, int]:
        """画面のサイズ情報を取得する

        Returns:
            tuple[int, int, int, int]: 画面幅/画面高さ/画面X座標/画面Y座標
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()

    @abstractmethod
    def get_window_title(self) -> str:
        """画面のタイトル情報を取得する

        Returns:
            str: 画面のタイトル情報
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()
