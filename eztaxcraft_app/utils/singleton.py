#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
シングルトンメタクラス

Author: Shimizu
Date: 2024/8/17
"""

from dataclasses import dataclass
from typing import Any

class SingletonMeta(type):
    """シングルトンメタクラス
        NOTE: シングルトンクラスを実装する場合は本クラスを継承する

    Args:
        type (_type_): メタクラスを継承(__call__メソッドカスタマイズ用)
    """
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]
