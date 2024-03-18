#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ウィジェットクラス定義

Author: Shimizu
Date: 2024/3/10
"""

import tkinter as tk
from typing import Any


class Widget:
    """ウィジェットクラス
        NOTE: 全てのウィジェットクラスが継承すべき親クラス
    """
    def __init__(self, widget: Any) -> None:
        """コンストラクタ
        """
        # ウィジェット用変数を初期化
        self.widget = widget

    def pack(self, **kwargs) -> None:
        """親ウィジェットに配置する
            NOTE:tkinterウィジェットのpackメソッドをラップする
        """
        self.widget.pack(**kwargs)

    def grid(self, **kwargs) -> None:
        """ウィジェットをグリッドレイアウト内に配置する
            NOTE:tkinterウィジェットのgridメソッドをラップする
        """
        self.widget.grid(**kwargs)

    def place(self, **kwargs) -> None:
        """親ウィジェットにピクセル単位で配置する
            NOTE:tkinterウィジェットのplaceメソッドをラップする
        """
        self.widget.place(**kwargs)

    def get_widget(self) -> Any:
        """ウィジェットオブジェクトを取得する

        Returns:
            Any: ウィジェットオブジェクト
        """
        return self.widget
