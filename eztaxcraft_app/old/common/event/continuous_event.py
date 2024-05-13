#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
イベントクラス定義

Author: Shimizu
Date: 2024/2/11
"""

from abc import (ABC, abstractmethod)


class ContinuousEvent(ABC):
    """継続イベントクラスの抽象クラス
        NOTE: 継続イベントクラスが継承すべき親クラス
              ※継続して実行するイベントを継続イベントとする
    """

    @abstractmethod
    def execute(self) -> None:
        """継続イベント実行
            NOTE: 継続するイベント処理を実装する
        """
        raise NotImplementedError('次のメソッドが実装されていません。[execute(ContinuousEvent)]')

    @abstractmethod
    def terminate(self) -> None:
        """継続イベント終了
        """
        raise NotImplementedError('次のメソッドが実装されていません。[terminate(ContinuousEvent)]')
