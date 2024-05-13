#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
イベントクラス定義

Author: Shimizu
Date: 2024/2/11
"""

from abc import (ABC, abstractmethod)


class Event(ABC):
    """イベントクラスの抽象クラス
        NOTE: イベントクラスが継承すべき親クラス
    """

    @abstractmethod
    def execute(self) -> None:
        """イベント処理実行
            NOTE: 一度だけ実行するイベント処理を実装する
        """
        raise NotImplementedError('次のメソッドが実装されていません。[execute(Event)]')
