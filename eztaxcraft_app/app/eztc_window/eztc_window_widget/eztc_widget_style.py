#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
画面ウィジェット用のスタイルクラス定義

Author: Shimizu
Date: 2024/2/12
"""

from tkinter import ttk
from dataclasses import dataclass, field

class Singleton:
    """シングルトンメタクラス
    """
    _instance = None

    def __new__(cls, _):
        """ニューオペレータ

        Returns:
            any: 継承先クラスのインスタンス
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Style(Singleton):
    """スタイルクラス
        NOTE: ttkパッケージのStyleモジュールを利用する
              シングルトンで実装する
    """
    # シングルトン用
    _instance = None
    _inisialize = False

    def __init__(self, name: str) -> None:
        """コンストラクタ
        """
        if Style._inisialize is False:
            # スタイルデータインスタンス生成
            self.style_data: StyleData = StyleData()
            # 初期化済みに設定
            Style._inisialize = True

        ## スタイル登録済みチェック
        if not name in self.style_data.info:
            # バッファにスタイル情報を作成して登録する
            self.style_data.info[name] = ttk.Style()

        else:
            # 既にスタイル情報がバッファに登録されていればログ出力
            print(f'[ERROR] 既に同じ名前のStyleが登録されています。Style名:[{name}]')

    def config(self, style_name: str, **kwargs) -> None:
        """スタイルを設定する

        Args:
            style_name (str): 設定対象のスタイル名
            font_str (str): 設定するフォント文字列
            font_size (float): フォントサイズ_
        """
        ## スタイル登録済みチェック
        if not style_name in self.style_data.info:
            # スタイル情報がバッファに登録されてなければログ出力
            print(f'[ERROR] Styleが登録されていません。Style名:[{style_name}]')
            return

        # スタイルを設定
        self.style_data.info[style_name].configure(style_name, **kwargs)

@dataclass
class StyleData:
    """スタイルデータクラス
    """
    info: dict = field(default_factory=dict)
