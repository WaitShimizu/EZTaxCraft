#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
共通利用する関数群を定義

Author: Shimizu
Date: 2024/5/23
"""

import json
import os
from PIL import Image, ImageTk


def get_icon(file_name: str, width: int = 100, height: int = 50) -> ImageTk.PhotoImage:
    """アイコン画像を取得する
        NOTE:取得先のパスは「eztaxcraft_app」ディレクトリ直下の「/data/icon」固定

    Args:
        file_name (str): 取得するアイコン画像ファイル名
        width (int, optional): 画像横幅サイズ. Defaults to 100.
        height (int, optional): 画像高さサイズ. Defaults to 50.

    Returns:
        ImageTk.PhotoImage: 画像データ
    """
    ### 画像データを取得してバッファに格納する
    file_path = f"data/icon/{file_name}"
    image = Image.open(file_path)
    resized_image = image.resize((width, height))
    logo_image = ImageTk.PhotoImage(resized_image)
    return logo_image

def load_json(file_path: str) -> dict:
    """Jsonデータ取得
        NOTE:Jsonファイルを読み込んで辞書型データを応答する

    Args:
        file_path (str): 読み込み対象のJsonファイルパス

    Returns:
        dict: 読み込みデータ
    """
    ### 読み込み設定
    MODE = 'r'
    ENCODING = 'utf-8'

    ### ファイルの存在チェック
    if not os.path.exists(file_path):
        # NOTE: ファイルが存在しない場合：空データを応答
        return {}

    try:
        with open(file_path, MODE, encoding=ENCODING) as file:
            # 結果応答
            return json.load(file)
    except json.JSONDecodeError:
        # NOTE: JSONデータのでコード失敗
        return {}
