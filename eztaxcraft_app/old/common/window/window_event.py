#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
画面イベントクラス定義

Author: Shimizu
Date: 2024/2/11
"""

import sys
sys.path.append('../event')
from event.event import Event


class WindowEvent(Event):
    """画面イベントクラス
    """

    def __init__(self) -> None:
        """コンストラクタ
        """
