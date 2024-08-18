#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
アプリケーションメイン処理

Author: Shimizu
Date: 2024/1/23
"""

from controllers.main_controller import MainController


def main():
    """メイン関数
        NOTE:エントリーポイント
    """
    ### ルート制御インスタンス生成
    controller = MainController()
    # 画面制御処理開始
    controller.run()


if __name__ == "__main__":
    main()
