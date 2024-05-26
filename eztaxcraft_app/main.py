#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリケーションメイン処理

Author: Shimizu
Date: 2024/1/23
"""

# from dataclasses import dataclass, field
from controllers.root_controller import RootController


def main():
    """メイン関数
        NOTE:エントリーポイント
    """
    ### ルート制御インスタンス生成
    controller: RootController = RootController()
    # 画面制御処理開始
    controller.start()


if __name__ == "__main__":
    main()
