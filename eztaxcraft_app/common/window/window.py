#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
画面クラス定義

Author: Shimizu
Date: 2024/2/11
"""

from abc import ABC, abstractmethod


class Base(ABC):
    """画面クラスの基底クラス
        NOTE: 全ての画面クラスが継承すべき基底クラス
    """

    def __init__(self) -> None:
        """コンストラクタ
        """
        # 画面の表示状態情報
        self.__display_state: bool = False

    def set_display_state(self, state: bool) -> None:
        """画面の表示状態を設定する

        Args:
            state (bool): True:画面表示状態/False:画面非表示状態
        """
        if state == self.__display_state:
            return
        self.__display_state = state

    def get_display_state(self) -> bool:
        """画面の表示状態を取得する

        Returns:
            bool: True:画面表示状態/False:画面非表示状態
        """
        return self.__display_state

    @abstractmethod
    def open(self) -> None:
        """画面を開く
        """
        # 継承先で画面を開く処理を実装する
        raise NotImplementedError('次のメソッドが実装されていません。[open]')

    @abstractmethod
    def close(self) -> None:
        """画面を閉じる
        """
        # 継承先で画面を閉じる処理を実装する
        raise NotImplementedError('次のメソッドが実装されていません。[close]')
